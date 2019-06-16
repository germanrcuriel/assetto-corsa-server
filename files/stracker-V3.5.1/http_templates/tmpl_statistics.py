# -*- coding: utf-8 -*-

# Copyright 2015-2016 NEYS
# This file is part of sptracker.
#
#    sptracker is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    sptracker is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.


from bottle import SimpleTemplate

# ----------------------------------------------
# statistics template
# ----------------------------------------------

statisticsTemplate = SimpleTemplate("""
% from ptracker_lib.helpers import isProMode, format_time_ms, format_datetime, unixtime2datetime
% from http_templates.tmpl_helpers import car_tmpl

<script>
function toggleCollapse(e, self) {
    var $e = $(e);
    var $collapse = $e.closest('.collapse-group').find('.collapse');
    var $self = $(self);
    if( $($self[0]).text() == "+" )
    {
        $($self[0]).text("-");
        $collapse.collapse('show');
    } else
    {
        $($self[0]).text("+");
        $collapse.collapse('hide');
    }
}

function ms_count(ms)
{
    res = 0;
    for(var i=0; i < ms.length; i++) {
        if (ms.options[i].selected) {
            res = res + 1;
        }
    }
    return res;
}

function ms_to_string(old_o, name, ms)
{
    res = '';
    allSelected = 1;
    for(var i=0; i < ms.length; i++) {
        if (ms.options[i].selected) {
            if (res != '') {
                res = res + ",";
            }
            res = res + ms.options[i].value
        } else
        {
            allSelected = 0;
        }
    }
    if(allSelected)
    {
        return old_o;
    }
    if (old_o == "")
    {
        c = '?';
    } else
    {
        c = '&';
    }
    return old_o + c + name + "=" + res;
}

function getLocation() {
    var ms_tracks = document.getElementById("tracks");
    var ms_cars = document.getElementById("cars");
    var ms_servers = document.getElementById("servers");
    options =           '?date_from=' + document.getElementById("dateStart").value;
    options = options + '&date_to='   + document.getElementById("dateStop").value;
    options = ms_to_string(options, "tracks", ms_tracks);
    options = ms_to_string(options, "cars", ms_cars);
% if len(servers) > 1:
    options = ms_to_string(options, "servers", ms_servers);
% end
    return options;
}

function applySelections() {
    window.location='statistics' + getLocation();
}

function invalidateLaps() {
    var sl = getLocation();
%    curr_url = curr_url.split("/")[-1]
    var curr_url = '{{!curr_url}}';
    if( curr_url != 'statistics' + sl ) {
        alert("The currently set filters do not match the display. Display will be reloaded now (click again to invalidate the laps).");
        window.location = sl;
    } else
    {
        if( confirm("Do you really want to invalidate the selected {{!stats['numLaps']}} laps?") == true )
        {
            window.location = 'invalidate_laps' + sl;
        }
    }
}
</script>

<div class="container">
    <div class="row page-header">
        <div class="col-md-6"><img src="/img/banner.png" title="Logo Track" class="ACimg"></div>
        <div class="col-md-6">

            <form class="form-horizontal collapse-group" role="form">
                <div class="form-group">
                    <label for="trackname" class="col-md-2 control-label">Track</label>
                    <div class="col-md-10">
                        <select id="tracks" name="tracks" class="form-control multiselect" multiple="multiple">
                              % for d in tracks:
                              %   t = d['track']
                              %   tui = d['uitrack']
                              %   if currtracks is None or t in currtracks:
                              %     s = "selected"
                              %   else:
                              %     s = ""
                              %   end
                                <option {{!s}} value="{{t}}">{{tui}}</option>
                              % end
                        </select>
                    </div>
                    <label for="cars" class="col-md-2 control-label">Cars</label>
                    <div class="col-md-10">
                        <select id="cars" name="cars" class="form-control multiselect" multiple="multiple">
                                  % for d in cars:
                                  %   c = d['car']
                                  %   uic = d['uicar']
                                  %   if currcars is None or c in currcars:
                                  %     s = "selected"
                                  %   else:
                                  %     s = ""
                                  %   end
                                    <option {{!s}} value="{{c}}">{{uic}}</option>
                                  % end
                        </select>
                    </div>
                </div>
%options_detailed = not date_from[0] is None or not date_to[0] is None or not currservers is None
                <div class="form-group collapse {{!"in" if options_detailed else ""}}" id="filterCollapse">
                    <label for="datespan" class="col-md-2 control-label">Date</label>
                    <div id="datespan" class="col-md-10">
                        <div class="form-group row">
                            <label for="dateStart" class="col-md-2 control-label">From</label>
                            <div class="col-md-3">
                                <input id="dateStart" class="datepicker form-control" data-date-format="yyyy-mm-dd" value="{{date_from[1]}}" />
                            </div>
                            <label for="dateStop" class="col-md-2 control-label">To</label>
                            <div class="col-md-3">
                                <input id="dateStop" class="datepicker form-control" data-date-format="yyyy-mm-dd" value="{{date_to[1]}}" />
                            </div>
                        </div>
                    </div>
% if len(servers) > 1:
                    <label for="servers" class="col-md-2 control-label">Servers</label>
                    <div class="col-md-10">
                        <select id="servers" name="servers" class="form-control multiselect" multiple="multiple">
% for s in servers:
                            <option {{!"selected" if currservers is None or s in currservers else ""}} value="{{!s}}">{{s}}</option>
% end
                        </select>
                    </div>
% end
                </div>
                <div class="form-group form-group">
                    <div class="col-md-offset-0 col-md-2">
                        <a class="form-control btn btn-info"
                           role="button"
                           onclick="toggleCollapse(getElementById('filterCollapse'), this)"
                           href="#">{{!"-" if options_detailed else "+"}}</a>
                    </div>
% if features['admin']:
                    <div class="col-md-offset-0 col-md-5">

                        <a class="form-control btn btn-danger"
                           role="button"
                           onclick="invalidateLaps()"
                           href="#">Set laps invalid</a>
                    </div>

                    <div class="col-md-offset-0 col-md-5">
% else:
                    <div class="col-md-offset-5 col-md-5">
% end

                        <a class="form-control btn btn-primary"
                           role="button"
                           onclick="applySelections()"
                           href="#">Show selected</a>
                    </div>
                </div>
            </form>
        </div>
    </div>
    <div class="row">
        <div class="col-md-6">
            <div>
                {{!http_server.serverstats_svg()}}
            </div>
            <div>
                {{!http_server.lapspertrack_svg()}}
            </div>
            <div>
                {{!http_server.lapspercar_svg()}}
            </div>
            <div>
                {{!http_server.lapspercombo_svg()}}
            </div>
        </div>
        <div class="col-md-6">
% def entry(key, conv=str):
%    v = lapdetails.get(key, None)
%    if v is None:
%        v = '-'
%    else:
%        v = conv(v)
%    end
%    return v
% end
            <table class="table table-striped table-condensed table-bordered table-hover">
                <caption>Overall Statistics</caption>
                <tbody>
                    <tr><td>Total number of drivers seen</td><td>{{stats['numPlayers']}}</td></tr>
% if features['banlist']:
                    <tr><td>Number of drivers banned</td><td>{{stats['bannedPlayers']}}</td></tr>
% end
                    <tr><td>Number of laps</td><td>{{stats['numLaps']}}</td></tr>
% if not stats['kmDriven'] is None:
                    <tr><td>Distance driven</td><td>{{"%.0f" % stats['kmDriven']}} km</td></tr>
% end
                </tbody>
            </table>
            <table class="table table-striped table-condensed table-bordered table-hover">
                <caption>Track / car combinations</caption>
                <thead>
                    <tr><th>Track</th><th>Cars</th><th>Date</th></tr>
                </thead>
% for comboId,date in stats['recentCombos']:
    <tr>
        <td>
            {{stats['lapsPerCombo'][comboId]['uitrack']}}
        </td>
        <td>
% for i,car in enumerate(stats['lapsPerCombo'][comboId]['cars']):
%   uicar = stats['lapsPerCombo'][comboId]['uicars'][i]
            {{! car_tmpl.render(car=car, uicar=uicar, tooltip=True) }}
% end
        </td>
        <td>
            {{str(unixtime2datetime(date).date())}}
        </td>
    </tr>
% end
            </table>
        </div>
    </div>
</div>
""")

