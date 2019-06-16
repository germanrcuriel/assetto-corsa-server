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
# lap statistics template
# ----------------------------------------------

lapStatTableTemplate = SimpleTemplate("""
%from http_templates.tmpl_helpers import car_tmpl
%from stracker_lib import config
%from ptracker_lib.helpers import *
%
% alltyres = [("(SS)","Slicks Supersoft"),
%             ("(S)" ,"Slicks Soft"),
%             ("(M)" ,"Slicks Medium"),
%             ("(H)" ,"Slicks Hard"),
%             ("(SH)","Slicks Superhard"),
%             ("(ST)","Street"),
%             ("(SV)","Street Vintage"),
%             ("(SM)","Semislicks"),
%             ("(HR)","Hypercar Road"),
%             ("(I)" ,"Intermediate"),
%             ("(V)" ,"Vintage"),
%             ("(E)" ,"Eco")]
%
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

function ms_to_string(ms)
{
    res = '';
    for(var i=0; i < ms.length; i++) {
        if (ms.options[i].selected) {
            if (res != '') {
                res = res + ",";
            }
            res = res + ms.options[i].value
        }
    }
    return res;
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

function applySelections() {
    var track = document.getElementById("trackname").value;
    var ranking = document.getElementById("ranking").value;
    var ms_cars = document.getElementById("cars");
    var ms_valid = document.getElementById("valid");
    var ms_tyres = document.getElementById("tyres");
    var ms_servers = document.getElementById("servers");
    var ms_groups = document.getElementById("groups");
    var server = "";
% if len(servers) > 1:
    if( (ms_count(ms_servers) < {{!len(servers)}}) && (ms_servers.length > 0) )
    {
        server = "&currservers=" + ms_to_string(ms_servers);
    }
% end
    var valid = ms_to_string(ms_valid);
    var cars = ms_to_string(ms_cars);
    var date_from = document.getElementById("dateStart").value;
    var date_to = document.getElementById("dateStop").value;
    var tyres = ms_to_string(ms_tyres);
    var groups = ms_to_string(ms_groups);
    if (ms_count(ms_tyres) < {{len(alltyres)}} ) {
        tyres = '&tyres='+tyres;
    } else
    {
        tyres = '';
    }
    if (ms_count(ms_groups) > 0) {
        groups = '&groups='+groups;
    } else
    {
        groups = '';
    }
    if (ranking != '0')
    {
        ranking = '&ranking='+ranking;
    } else
    {
        ranking = '';
    }
    window.location='lapstat?track='+track+'&cars='+cars+'&valid='+valid+'&date_from='+date_from+'&date_to='+date_to+tyres+server+groups+ranking;
}
</script>

<div class="container">
  <div class="page-header">
    <div class="row">
        <div class="col-md-6">
            <img src="/img/banner.png" title="Logo Track" class="ACimg">
        </div>
        <div class="col-md-6">
            <form class="form-horizontal collapse-group" role="form">
                <!-- *********** standard filters ************* -->
                <div class="form-group">
                    <label for="trackname" class="col-md-2 control-label">Track</label>
                    <div class="col-md-10">
                        <select id="trackname" name="trackname" class="multiselect form-control">
% for d in tracks:
%   t = d['track']
%   tui = d['uitrack']
%   if t == currtrack:
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
%   if c in currcars:
%     s = "selected"
%   else:
%     s = ""
%   end
                            <option {{!s}} value="{{c}}">{{uic}}</option>
% end
                        </select>
                    </div>
                </div>
            </form>
        </div>
    </div>
    <div class="row">
        <!-- *********** detailed filters ************* -->
        <div class="col-md-12 collapse-group" id="filterCollapse">
            <div class="col-md-6">
                <form class="form-horizontal" role="form">
%options_detailed = not date_from[0] is None or not date_to[0] is None or valid != set([1,2]) or (not tyres is None and len(tyres) < len(alltyres)) or ranking != 0 or currgroups != []
                    <div class="form-group collapse {{!"in" if options_detailed else ""}}">
                        <div class="row">
                            <label for="valid" class="col-md-2 control-label">Valid</label>
                            <div class="col-md-10">
                                <select id="valid" name="valid" class="form-control multiselect" multiple="multiple">
                                    <option {{!"selected" if 1 in valid else ""}} value="1">valid</option>
                                    <option {{!"selected" if 2 in valid else ""}} value="2">unknown</option>
                                    <option {{!"selected" if 0 in valid else ""}} value="0">invalid</option>
                                </select>
                            </div>
                        </div>
                        <div class="row">
                            <label for="tyres" class="col-md-2 control-label">Tyres</label>
                            <div class="col-md-10">
                                <select id="tyres" name="tyres" class="form-control multiselect" multiple="multiple">
% for t in alltyres:
                                    <option {{!"selected" if tyres is None or t[0] in tyres else ""}} value="{{!t[0]}}">{{t[1]}}</option>
% end
                                </select>
                            </div>
                        </div>
                        <div class="row">
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
                        </div>
                    </div>
                </form>
            </div>
            <div class="col-md-6">
                <form class="form-horizontal" role="form">
                    <div class="form-group collapse {{!"in" if options_detailed else ""}}">
% if len(servers) > 1:
                        <div class="row">
                            <label for="servers" class="col-md-2 control-label">Servers</label>
                            <div class="col-md-10">
                                <select id="servers" name="servers" class="form-control multiselect" multiple="multiple">
% for s in servers:
                                    <option {{!"selected" if currservers is None or s in currservers else ""}} value="{{!s}}">{{s}}</option>
% end
                                </select>
                            </div>
                        </div>
% end
                        <div class="row">
                            <label for="ranking" class="col-md-2 control-label">Ranking</label>
                            <div class="col-md-10">
                                <select id="ranking" name="ranking" class="form-control multiselect">
                                    <option {{!"selected" if not ranking else ""}} value="0">Multiple cars and multiple drivers</option>
                                    <option {{!"selected" if ranking in [1,True] else ""}} value="1">One entry per driver</option>
                                    <option {{!"selected" if ranking == 2 else ""}} value="2">One entry per car</option>
                                </select>
                            </div>
                        </div>
                        <div class="row">
                            <label for="groups" class="col-md-2 control-label">Groups</label>
                            <div class="col-md-10">
                                <select id="groups" name="groups" class="form-control multiselect" multiple="multiple">
% for s in sorted(groups, key=lambda x: x['groupid']):
                                    <option {{!"selected" if not currgroups is None and s['groupid'] in currgroups else ""}} value="{{s['groupid']}}">{{s['name']}}</option>
% end
                                </select>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-md-6 col-md-offset-6">
            <form class="form-horizontal collapse-group" role="form">
                <!-- *********** buttons ************* -->
                <div class="form-group form-group">
                    <div class="col-md-offset-0 col-md-2">
                        <a class="form-control btn btn-info"
                           role="button"
                           onclick="toggleCollapse(getElementById('filterCollapse'), this)"
                           href="#">{{!"-" if options_detailed else "+"}}</a>
                    </div>
                    <div class="col-md-offset-0 col-md-5">
                        <a class="form-control btn btn-primary"
                           role="button"
                           onclick="applySelections()"
                           href="#">Show selected</a>
                    </div>
                    <div class="col-md-offset-0 col-md-5">
% if len(servers) <= 1:
                        <a class="form-control btn btn-primary" href="lapstat" role="button">Show last combo</a>
% else:
%   import urllib.parse
                        <div class="btn-group">
                            <button type="button" class="form-control btn btn-primary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                Show last combo <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu">
%   for s in servers:
                                <li><a href="lapstat?currservers={{!urllib.parse.quote(s)}}" role="button">Server {{s}}</a>
%   end
                            </ul>
                        </div>
% end
                    </div>
                </div>
            </form>
        </div>
    </div>
    </div>
    <div class="row"><div class="col-md-12">
        <table class="table table-striped table-condensed table-bordered table-hover">
            <thead>
            <tr>
                <th>Pos</th>
                <th>Driver</th>
                <th>Car</th>
                <th>Best lap</th>
                <th>Gap to 1st</th>
% from ptracker_lib.helpers import isProMode, format_time_ms, format_datetime, unixtime2datetime, format_vel, format_temp
% for i in range(count):
                <th>{{'S%d' % (i+1)}}</th>
% end
%
% def collisions(r):
%     cEnv = r.get('collenv', None)
%     cCar = r.get('collcar', None)
%     if cEnv is None or cCar is None: res = '-'
%     else: res = str(cEnv+cCar)
%     end
%     res = res + "("
%     if cCar is None: res += "-"
%     else: res += str(cCar)
%     end
%     res += ")"
%     return res
% end
%
% def temps(r):
%     tAmb = r.get('tempAmbient', None)
%     tTrack = r.get('tempTrack', None)
%     res = '-' if tAmb is None else (format_temp(tAmb))
%     res += "/"
%     res += '-' if tTrack is None else (format_temp(tTrack))
%     return res
% end
%
% def format_tyre(r):
%     if r is None:
%        return "-"
%     end
%     import re
%     s = re.sub(r'.*\((.*)\)', r'\\1', r)
%     s = '?' if s == r else s
%     return s
% end
%
% add_columns = config.config.HTTP_CONFIG.lap_times_add_columns.split("+")
% add_columns_disp = {
%   'valid' : ('Valid', lambda r: ['no','yes','-'][r['valid']]),
%   'aids' : ('Aids', None),
%   'laps' : ('Laps', lambda r: r['numLaps']),
%   'date' : ('Date', lambda r: '-' if r.get('timeStamp', None) is None else format_datetime(unixtime2datetime(r.get('timeStamp', None)))),
%   'grip' : ('Grip', lambda r: '-' if r.get('grip', None) is None else "%.1f%%" % (r['grip']*100.)),
%   'cuts' : ('Cuts', lambda r: '-' if r.get('cuts', None) is None else r['cuts']),
%   'collisions' : ('Crashes (car/car)', lambda r: collisions(r)),
%   'tyres' : ('Tyres', lambda r: format_tyre(r.get('tyres', None))),
%   'temps' : ('Amb./Track', lambda r: temps(r)),
%   'ballast': ('Ballast', lambda r: "-" if r.get('ballast', None) is None else "%.1f kg" % r['ballast'] ),
%   'vmax': ('vMax', lambda r: "-" if r.get('maxSpeed', None) is None else format_vel(r['maxSpeed'])),
% }
% for c in add_columns:
                <th>{{add_columns_disp[c][0]}}</th>
% end
            </tr>
            </thead>
            <tbody>
% for i,r in enumerate(lapStatRes):
%   if r['bestServerLap']:
%       c = 'class="bestLap" '
%   else:
%       c = ''
%   end
            <tr class='clickableRow' href="lapdetails?lapid={{"%d" % r['id']}}#">
                <td {{!c}}>{{"%d." % r['pos']}}</td>
                <td {{!c}}>{{r['name']}}</td>
                <td {{!c}}>
                    {{!car_tmpl.render(car=r['car'], uicar=r['uicar'])}}
                </td>
                <td {{!c}}>{{format_time_ms(r['lapTime'], False)}}</td>
                <td {{!c}}>{{format_time_ms(r['gapToBest'], True)}}</td>
% for si in range(count):
    % if r['sectors'][si] == bestSectors[si]:
    %   c = 'class="bestSector" '
    % else:
    %   c = ''
    % end
    % if r['sectors'][si] is None:
    %   s = "-"
    % else:
    %   s = format_time_ms(r['sectors'][si], False)
    % end
                <td {{!c}}>{{s}}</td>
% end
%
% def adaptClassBool(x, r, hasFacSetting=False):
%     v = r.get(x, None)
%     if v is None:
%          v = "unknown"
%     else:
%          if hasFacSetting:
%              v = ["off", "factory", "on", "unknown"][v+1]
%          else:
%              v = ["off", "on", "unknown"][v]
%          end
%     end
%     return v
% end
%
% for c in add_columns:
%   if add_columns_disp[c][1]:
                <td>{{add_columns_disp[c][1](r)}}</td>
%   else:
                <td><div>
                    <a class="aids autoclutch {{adaptClassBool('autoClutch', r)}}" title="Automatic clutch {{adaptClassBool('autoClutch', r)}}"></a>
                    <a class="aids abs {{adaptClassBool('abs', r, True)}}" title="ABS {{adaptClassBool('abs', r, True)}}"></a>
                    <a class="aids autobrake {{adaptClassBool('autoBrake', r)}}" title="Automatic brake {{adaptClassBool('autoBrake', r)}}"></a>
                    <a class="aids autogearbox {{adaptClassBool('autoShift', r)}}" title="Automatic gearbox {{adaptClassBool('autoShift', r)}}"></a>
                    <a class="aids blip {{adaptClassBool('autoBlib', r)}}" title="Automatic throttle blip {{adaptClassBool('autoBlib', r)}}"></a>
                    <a class="aids idealline {{adaptClassBool('idealLine', r)}}" title="Ideal racing line {{adaptClassBool('idealLine', r)}}"></a>
                    <a class="aids tc {{adaptClassBool('tractionControl', r, True)}}" title="Traction control {{adaptClassBool('tractionControl', r, True)}}"></a>
                </div></td>
%   end
% end
            </tr>
% end
            </tbody>
        </table>
    </div></div>
</div>
""")

# ----------------------------------------------
# lap details template
# ----------------------------------------------

lapDetailsTableTemplate = SimpleTemplate("""
% from ptracker_lib.helpers import *
% from http_templates.tmpl_helpers import car_tmpl
<div class="container">
    <div class="row page-header">
        <div class="col-md-6"><img src="/img/banner.png" title="Logo Track" class="ACimg"></div>
        <div class="col-md-6">
            <div class="row">
% if features['pts']:
                <div class="col-md-4">
% remote = 0 if 'local' in curr_url else 1
                    <script>
                    function setCompareLapId()
                    {
                        var lapId = {{!lapdetails['lapid']}};
                        var remote = {{!remote}};
                        var track = "{{!lapdetails['track']}}";
                        console.log("track=" + track);
                        ptracker.setCompareLapId(lapId, remote, track);
                    }
                    </script>
                    <button class="form-control btn btn-sm btn-primary" onclick="setCompareLapId()">
                        Set Comparison Lap
                    </button>
                </div>
                <div class="col-md-4">
                    <button class="form-control btn btn-sm btn-primary" onclick="ptracker.resetCompareLap()">
                        Reset Comparison Lap
                    </button>
                </div>
                <div class="col-md-4">
                    <button class="form-control btn btn-sm btn-primary" onclick="window.history.back()">
                        Back
                    </button>
                </div>
% else:
                <div class="col-md-4 col-md-offset-8">
                    <button class="form-control btn btn-sm btn-primary" onclick="window.history.back()">
                        Back
                    </button>
                </div>
% end
            </div>
% if features['admin']:
<script>
function confirmDBChangeBeforeLink(l, msg)
{
    if( confirm("Do you really want to " + msg) )
    {
        window.location.href = l;
    }
}
</script>
            <br>
            <div class="row">
                <div class="col-md-4">
                    <button class="form-control btn btn-sm btn-danger"
                            onclick="confirmDBChangeBeforeLink('{{!"modify_lap?lapid=%d&valid=0" % lapdetails['lapid']}}', 'invalidate the lap?');"
                            role="button">
                        Set lap invalid
                    </button>
                </div>
                <div class="col-md-4">
                    <button class="form-control btn btn-sm btn-danger"
                            onclick="confirmDBChangeBeforeLink('{{!"modify_lap?lapid=%d&valid=1" % lapdetails['lapid']}}', 'set the lap valid?');"
                            role="button">
                        Set lap valid
                    </button>
                </div>
                <div class="col-md-4">
                    <button class="form-control btn btn-sm btn-danger"
                            onclick="confirmDBChangeBeforeLink('{{!"modify_lap?lapid=%d&valid=2" % lapdetails['lapid']}}', 'set the lap to unknown?');"
                            role="button">
                        Set lap unknown
                    </button>
                </div>
            </div>
% if features['checksum_tests']:
            <br>
            <div class="row">
                <div class="col-md-6">
                    <button class="form-control btn btn-sm btn-warning"
                            onclick="confirmDBChangeBeforeLink('{{!"modify_reqchecksum?lapid=%d&track=%s&track_checksum=%s" % (lapdetails['lapid'], lapdetails['track'], lapdetails['trackChecksum'])}}', 'set the required track checksum to this lap\\'s checksum?');"
                            role="button">
                        Set required track checksum
                    </button>
                </div>
                <div class="col-md-6">
                    <button class="form-control btn btn-sm btn-warning"
                            onclick="confirmDBChangeBeforeLink('{{!"modify_reqchecksum?lapid=%d&car=%s&car_checksum=%s" % (lapdetails['lapid'], lapdetails['car'], lapdetails['carChecksum'])}}', 'set the required car checksum to this lap\\'s checksum?');"
                            role="button">
                        Set required car checksum
                    </button>
                </div>
            </div>
            <br>
            <div class="row">
                <div class="col-md-6">
                    <button class="form-control btn btn-sm btn-warning"
                            onclick="confirmDBChangeBeforeLink('{{!"modify_reqchecksum?lapid=%d&track=%s" % (lapdetails['lapid'], lapdetails['track'])}}', 'remove the required checksum for this track?');"
                            role="button">
                        Remove required track checksum
                    </button>
                </div>
                <div class="col-md-6">
                    <button class="form-control btn btn-sm btn-warning"
                            onclick="confirmDBChangeBeforeLink('{{!"modify_reqchecksum?lapid=%d&car=%s" % (lapdetails['lapid'], lapdetails['car'])}}', 'remove the required checksum for this car?');"
                            role="button">
                        Remove required car checksum
                    </button>
                </div>
            </div>
% end
% end
        </div>
    </div>
    <div class="row">
        <div class="col-md-3">
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
                <caption>Driver/combo information</caption>
                <tbody>
                    <tr><td>Name</td><td>{{lapdetails['name']}}</td></tr>
                    <tr><td>Driver type</td><td>{{['human driver', 'artificial intelligence'][lapdetails['artint']]}}</td></tr>
% if features['admin']:
                    <tr><td>Steam GUID Hash</td><td>{{"..." + lapdetails['steamguid'][-10:]}}</td></tr>
% end
                    <tr><td>Track</td><td>{{lapdetails['uitrack']}}</td></tr>
                    <tr><td>Car</td><td>{{!car_tmpl.render(car=lapdetails['car'], uicar=lapdetails['uicar'])}}</td></tr>
                    <tr><td>Laps (total)</td><td>{{lapdetails['numlaps_invalid']+lapdetails['numlaps_valid']+lapdetails['numlaps_unknown']}}</td></tr>
                    <tr><td>Laps (valid)</td><td>{{lapdetails['numlaps_valid']}}</td></tr>
                    <tr><td>Laps (unknown)</td><td>{{lapdetails['numlaps_unknown']}}</td></tr>
                    <tr><td>Best lap time</td><td>{{entry('pb', lambda x: format_time_ms(x, False))}}</td></tr>
                    <tr><td>Theoretical best</td><td>{{entry('tb', lambda x: format_time_ms(x, False))}}</td></tr>
                </tbody>
            </table>
        </div>
        <div class="col-md-3">
             <table class="table table-striped table-condensed table-bordered table-hover">
              <caption>Lap information</caption>
                <tbody>
                    <tr><td>Lap time</td><td>{{format_time_ms(lapdetails['laptime'], False)}}</td></tr>
                    <tr><td>Achieved on</td><td>{{format_datetime(unixtime2datetime(lapdetails['timestamp']))}}</td></tr>
                    <tr><td>Valid</td><td>{{["no","yes","unknown"][lapdetails['valid']]}}</td></tr>
                    <tr><td>Cuts</td><td>{{entry('cuts')}}</td></tr>
                    <tr><td>Maximum Speed</td><td>{{entry("maxspeed_kmh", format_vel)}}</td></tr>
                    <tr><td>Pit Lane Time</td><td>{{format_time_ms(lapdetails['timeinpitlane'], False) if lapdetails['timeinpitlane'] != None and lapdetails['timeinpitlane'] > 0 else '-'}}</td></tr>
                    <tr><td>Pit Time</td><td>{{format_time_ms(lapdetails['timeinpit'], False) if lapdetails['timeinpit'] != None and lapdetails['timeinpit'] > 0 else '-'}}</td></tr>
                    <tr><td>Tyres used</td><td>{{entry('tyrecompound')}}</td></tr>
                    <tr><td>Grip level</td><td>{{entry('griplevel', lambda x: "%.1f %%"%(x*100.))}}</td></tr>
                    <tr><td>Fuel load</td><td>{{entry('fuelratio', lambda x: "%.1f %%"%(x*100.) if not x is None and x >= 0.0 else '-')}}</td></tr>
                    <tr><td>Car collisions</td><td>{{entry('collisionscar')}}</td></tr>
                    <tr><td>Env collisions</td><td>{{entry('collisionsenv')}}</td></tr>
                    <tr><td>Ballast</td><td>{{entry('ballast',lambda x: '%.1f kg'%x)}}</td></tr>
% bestSectors = lapdetails.get('bestSectors', [])
% for s in range(10):
%    st = lapdetails.get('sectortime%d'%s, None)
%    bs = bestSectors[s] if s < len(bestSectors) else None
%    if st is None:
%        break
%    end
%    if not st is None and not bs is None:
%        delta = st-bs
%    else:
%        delta = None
%    end
%    st = entry('sectortime%d'%s, lambda x: format_time_ms(x, False))
%    delta = " (%s)" % format_time_ms(delta,True)
                    <tr><td>{{"Sector %d" % (s+1)}}</td><td>{{st + delta}}</td></tr>
% end
                </tbody>
            </table>
        </div>
        <div class="col-md-3">
            <table class="table table-striped table-condensed table-bordered table-hover">
                <caption>Session information</caption>
                <tbody>
                    <tr><td>Penalties</td><td>{{entry("penaltiesenabled", lambda x: ["no", "yes"][x])}}</td></tr>
                    <tr><td>Limit on tyres out</td><td>{{entry("allowedtyresout", lambda x: [str(x), '(no limit)'][x == -1])}}</td></tr>
                    <tr><td>Tyre wear factor</td><td>{{entry("tyrewearfactor", lambda x: "%.1f x" % x)}}</td></tr>
                    <tr><td>Fuel rate</td><td>{{entry('fuelrate', lambda x: "%.1f x" % x)}}</td></tr>
                    <tr><td>Mechanical damage</td><td>{{entry('damage', lambda x: "%3d %%" % int(x*100))}}</td></tr>
                    <tr><td>Ambient temperature</td><td>{{entry('temperatureambient', format_temp)}}</td></tr>
                    <tr><td>Track temperature</td><td>{{entry('temperaturetrack', format_temp)}}</td></tr>
                    <tr><td>Input method</td><td>{{entry('inputmethod')}}</td></tr>
                    <tr><td>Shifter used</td><td>{{entry('inputshifter', lambda x: ["paddles", "H shifter", "other"][x])}}</td></tr>
                    <tr><td>AC version</td><td>{{entry('acVersion')}}</td></tr>
                    <tr><td>ptracker version</td><td>{{entry('ptVersion')}}</td></tr>
                    <tr><td>stracker version</td><td>{{entry('stVersion')}}</td></tr>
                    <tr><td>Server name</td><td>{{entry('server')}}</td></tr>
% if features['admin']:
%  v = lapdetails['trackChecksumCheck']
%  spanClass = "label label-danger" if v == False else "label label-success" if v == True else "label label-default"
%  tdClass = '' #'text-danger' if v == False else 'text-success' if v == True else 'text-muted'
%  d = entry('trackChecksum')
%  d = d[:4] + "..." + d[-4:] if len(d) > 8 else d
                    <tr><td>Track checksum</td><td class="{{!tdClass}}"><span class="{{!spanClass}}">{{!d}}</span></td></tr>
%  v = lapdetails['carChecksumCheck']
%  spanClass = "label label-danger" if v == False else "label label-success" if v == True else "label label-default"
%  tdClass = '' #'text-danger' if v == False else 'text-success' if v == True else 'text-muted'
%  d = entry('carChecksum')
%  d = d[:4] + "..." + d[-4:] if len(d) > 8 else d
                    <tr><td>Car checksum</td><td class="{{!tdClass}}"><span class="{{!spanClass}}">{{!d}}</span></td></tr>
% end
                </tbody>
            </table>
        </div>
        <div class="col-md-3">
            <table class="table table-striped table-condensed table-bordered table-hover">
                <caption>Aid information</caption>
                <tbody>
% def levelAidToStr(enabledKey, usedKey):
%    aidEnabled = lapdetails.get(enabledKey, None)
%    if not aidEnabled is None:
%       aid = ["Off", "Factory", "On"][aidEnabled+1]
%    else:
%       aid = "?"
%    end
%    level = lapdetails.get(usedKey, None)
%    if not level is None:
%       level = "%.2f" % level
%    else:
%       level = "?"
%    end
%    return "%s [level: %s]" % (aid, level)
% end
                    <tr><td>ABS</td><td>{{levelAidToStr('aidabs', 'lapmaxabs')}}</td></tr>
                    <tr><td>Traction control</td><td>{{levelAidToStr('aidtractioncontrol', 'lapmaxtc')}}</td></tr>
                    <tr><td>Automatic heeltoe</td><td>{{entry("aidautoblib", lambda x: ["Off", "On"][x])}}</td></tr>
                    <tr><td>Automatic brake</td><td>{{entry("aidautobrake", lambda x: ["Off", "On"][x])}}</td></tr>
                    <tr><td>Automatic clutch</td><td>{{entry("aidautoclutch", lambda x: ["Off", "On"][x])}}</td></tr>
                    <tr><td>Automatic gearbox</td><td>{{entry("aidautoshift", lambda x: ["Off", "On"][x])}}</td></tr>
                    <tr><td>Ideal line</td><td>{{entry("aididealline", lambda x: ["Off", "On"][x])}}</td></tr>
                    <tr><td>Stability control</td><td>{{entry("aidstabilitycontrol", lambda x: "%3d %%" % int(x*100))}}</td></tr>
                    <tr><td>Slip stream</td><td>{{entry("aidslipstream", lambda x: "%.1f x" % x)}}</td></tr>
                    <tr><td>Tyre blankets</td><td>{{entry("aidtyreblankets", lambda x: ["Off", "On"][x])}}</td></tr>
                </tbody>
            </table>
        </div>
    </div>
% if lapdetails['historyinfo'] is None:
    <div class="row">
        <div class="col-md-12 panel panel-info">
            <div class="panel-heading">Info</div>
            <div class="panel-body">
                This lap has no history information stored, because it was incomplete (e.g. out lap).
            </div>
        </div>
    </div>
% else:
%   lapIds = [lapdetails['lapid']]
%   legends = ["C"]
%   if cmpbits is None:
%     if not cmp_lapid is None and cmp_lapid != lapdetails['lapid']:
%        cmpbits=16
%     else:
%        cmpbits=4|8
%     end
%   end
%   if lapdetails["driversBestValidSessionLapId"] and cmpbits & 1:
%     lapIds.append(lapdetails["driversBestValidSessionLapId"])
%     legends.append("PSB")
%   end
%   if lapdetails["bestValidSessionLapId"] and cmpbits & 2:
%     lapIds.append(lapdetails["bestValidSessionLapId"])
%     legends.append("SB")
%   end
%   if lapdetails["driversBestValidServerLapId"] and cmpbits & 4:
%     lapIds.append(lapdetails["driversBestValidServerLapId"])
%     legends.append("PB")
%   end
%   if lapdetails["bestValidServerLapId"] and cmpbits & 8:
%     lapIds.append(lapdetails["bestValidServerLapId"])
%     legends.append("B")
%   end
%   if not cmp_lapid is None and cmpbits & 16:
%     lapIds.append(cmp_lapid)
%     legends.append("M")
%   end
    <script>
function updateComparison() {
    var cbPSB = document.getElementById("cbPSB").checked;
    var cbSB = document.getElementById("cbSB").checked;
    var cbPB = document.getElementById("cbPB").checked;
    var cbB = document.getElementById("cbB").checked;
    var cbM = document.getElementById("cbM").checked;
%   import re
%     nocmpbits_url = re.sub(r"([?&])cmpbits=\d+([?&])?", r"\g<1>", curr_url)
%     if not '?' in nocmpbits_url:
%        nocmpbits_url += "?"
%     elif not nocmpbits_url[-1] in ['?', '&']:
%        nocmpbits_url += "&"
%     end
    var url = '{{!nocmpbits_url}}cmpbits=' + (cbPSB | (cbSB << 1) | (cbPB << 2) | (cbB << 3) | (cbM << 4)).toString();
    window.location=url;
    return false;
}
    </script>
    <div class="row">
        <hr>
        <div class="col-md-8 col-md-offset-0">
            <div>
                {{!http_server.ltcomparison_svg(lapIds=",".join(map(str, lapIds)), labels=",".join(legends), curr_url=curr_url) }}
            </div>
            <div>
                {{!http_server.ltcomparisonmap_svg(lapIds=",".join(map(str, lapIds)), labels=",".join(legends), curr_url=curr_url) }}
            </div>
        </div>
        <div class="col-md-4">
            <div class="col-md-12 panel panel-info">
                <div class="panel-heading">Select comparison laps</div>
                    <div class="panel-body">
                        <form>
                            <div class="checkbox">
                                <label>
                                    <input type="checkbox" {{!"checked" if cmpbits & 1 else ""}} id="cbPSB">
                                    Personal Session Best (PSB)
                                </label>
                            </div>
                            <div class="checkbox">
                                <label>
                                    <input type="checkbox" {{!"checked" if cmpbits & 2 else ""}} id="cbSB">
                                    Session Best (SB)
                                </label>
                            </div>
                            <div class="checkbox">
                                <label>
                                    <input type="checkbox" {{!"checked" if cmpbits & 4 else ""}} id="cbPB">
                                    Personal Best (PB)
                                </label>
                            </div>
                            <div class="checkbox">
                                <label>
                                    <input type="checkbox" {{!"checked" if cmpbits & 8 else ""}} id="cbB">
                                    Server Best (B)
                                </label>
                            </div>
                            <div class="checkbox {{!'disabled' if cmp_lapid is None or cmp_lapid == lapdetails['lapid'] else ''}}">
                                <label>
                                    <input {{!'disabled' if cmp_lapid is None or cmp_lapid == lapdetails['lapid'] else ''}} type="checkbox" {{!"checked" if cmpbits & 16 else ""}} id="cbM">
                                    Manual Selection (M)
                                </label>
                            </div>
                            <div class="btn-group btn-group-justified" role="group">
                                <a class="btn btn-default" onclick="updateComparison()" role="button">Submit</button>
                                <a data-toggle="tooltip" title="Save this lap for manual comparison. When visiting another lap's detail page, you get the comparison to this lap. Cookies have to be enabled for this."
                                   class="btn btn-default" href="lapdetails_store_lapid?lapid={{!("%d" % lapdetails['lapid']) + ('&cmpbits=%d'%cmpbits if not cmpbits is None else'')}}"
                                   role="button">
                                    Manual compare
                                </a>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
% end
</div>
<script>
$('[data-toggle="tooltip"]').tooltip({
    'placement': 'top',
    'container': 'body'
});
</script>
""")

