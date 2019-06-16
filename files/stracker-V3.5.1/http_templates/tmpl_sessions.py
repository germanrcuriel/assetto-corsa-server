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
# session statistics template
# ----------------------------------------------

sesStatTableTemplate = SimpleTemplate("""
% from ptracker_lib.helpers import format_datetime, unixtime2datetime
<div class="container">
    <div class="row page-header">
        <div class="col-md-6"><img src="/img/banner.png" title="Logo Track" class="ACimg">
        </div>
        <div class="col-md-6">
            <form class="form-horizontal collapse-group" role="form">
                <div class="form-group">
                    <label for="trackname" class="col-md-4 control-label">Track</label>
                    <div class="col-md-8">
                        <select id="trackname" name="trackname" class="multiselect form-control">
                              % for d in tracks:
                              %   t = d['track']
                              %   uit = d['uitrack']
                              %   if t == currtrack:
                              %     s = "selected"
                              %   else:
                              %     s = ""
                              %   end
                                <option {{!s}} value="{{t}}">{{uit}}</option>
                              % end
                        </select>
                    </div>
                    <label for="session_type" class="col-md-4 control-label">Type</label>
                    <div class="col-md-8">
                        <select id="session_type" name="session_type" class="form-control multiselect" multiple="multiple">
                            <option {{"selected" if "Practice" in session_types else ""}} value="Practice">Practice</option>
                            <option {{"selected" if "Qualify" in session_types else ""}} value="Qualify">Qualify</option>
                            <option {{"selected" if "Race" in session_types else ""}} value="Race">Race</option>
                        </select>
                    </div>
                </div>
%options_detailed = num_players > 0 or num_laps > 0 or datespan[0] != "" or datespan[1] != ""
                <div class="form-group collapse {{!"in" if options_detailed else ""}}" id="filterCollapse">
                    <div class="row">
                        <label for="num_players" class="col-md-4 control-label">Number of Players</label>
                        <div class="col-md-8">
                            <select id="num_players" name="num_players" class="form-control multiselect">
                                <option {{"selected" if num_players == 0 else ""}} value="0">any</option>
% for i in range(1,25):
                                <option {{"selected" if num_players == i else ""}} value="{{i}}">{{"%d or more" % i}}</option>
% end
                            </select>
                        </div>
                    </div>
                    <div class="row">
                        <label for="num_laps" class="col-md-4 control-label">Number of Laps</label>
                        <div class="col-md-8">
                            <select id="num_laps" name="num_laps" class="form-control multiselect">
                                <option {{"selected" if num_laps == 0 else ""}} value="0">any</option>
% for i in range(1,50):
                                <option {{"selected" if num_laps == i else ""}} value="{{i}}">{{"%d or more" % i}}</option>
% end
                            </select>
                        </div>
                    </div>
                    <div class="row">
                        <label for="datespan" class="col-md-4 control-label">Date</label>
                        <div id="datespan" class="col-md-8">
                            <div class="form-group row">
                                <label for="dateStart" class="col-md-2 control-label">From</label>
                                <div class="col-md-4">
                                    <input id="dateStart" class="datepicker form-control" data-date-format="yyyy-mm-dd" value="{{!datespan[0]}}" />
                                </div>
                                <label for="dateStop" class="col-md-2 control-label">To</label>
                                <div class="col-md-4">
                                    <input id="dateStop" class="datepicker form-control" data-date-format="yyyy-mm-dd" value="{{!datespan[1]}}" />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="form-group">
<script>
function toggleCollapse(e, self) {
    var $e = $(e);
    var $collapse = $e.closest('.collapse-group').find('.collapse');
    var $self = $(self);
    console.log("toggleCollapse: " + $($self[0]).text());
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
</script>
                    <div class="col-md-offset-2 col-md-2">
                        <a class="form-control btn btn-info"
                           role="button"
                           onclick="toggleCollapse(getElementById('filterCollapse'), this)"
                           href="#">{{!"-" if options_detailed else "+"}}</a>
                    </div>
                    <div class="col-md-offset-0 col-md-4">
<script>
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
function applySelections() {
    var track = document.getElementById("trackname").value;
    var startDate = document.getElementById("dateStart").value;
    var stopDate = document.getElementById("dateStop").value;
    var session_types = ms_to_string(document.getElementById("session_type"));
    var num_players = document.getElementById("num_players").value
    var num_laps = document.getElementById("num_laps").value
    window.location='sessionstat?track='+track+'&start='+startDate+'&stop='+stopDate+'&session_types='+session_types+'&num_players='+num_players+'&num_laps='+num_laps;
}
</script>
                        <a class="form-control btn btn-primary"
                           role="button"
                           onclick="applySelections()"
                           href="#">Show selected</a>
                    </div>
                    <div class="col-md-offset-0 col-md-4">
                        <a class="form-control btn btn-primary" href="sessionstat" role="button">Show all</a>
                    </div>
                </div>
            </form>
        </div>
    </div>
    <div class="row"><div class="col-md-12">
        <table class="table table-striped table-condensed table-bordered table-hover">
            <thead>
            <tr>
                <th>Track</th>
                <th>Type</th>
                <th>First</th>
                <th>Second</th>
                <th>Third</th>
                <th>Number of drivers</th>
                <th>Date</th>
            </tr>
            </thead>
            <tbody>
% for i,r in enumerate(sesStatRes):
            <tr class="clickableRow" href="sessiondetails?sessionid={{"%d" % r['id']}}#">
                <td>{{r['uitrack']}}</td>
                <td>{{r['type']}}</td>
                <td>{{"" if r['podium'][0] is None else r['podium'][0]}}</td>
                <td>{{"" if r['podium'][1] is None else r['podium'][1]}}</td>
                <td>{{"" if r['podium'][2] is None else r['podium'][2]}}</td>
                <td>{{r['numPlayers']}}</td>
                <td>
% ts = r.get('timeStamp', None)
% if ts is None:
%     ts = "-"
% else:
%     ts = format_datetime(unixtime2datetime(ts))
% end
                    {{ts}}
                </td>
            </tr>
% end
            </tbody>
        </table>
    </div></div>
</div>
""")

sesDetailsTemplate = SimpleTemplate("""
% from ptracker_lib.helpers import isProMode, format_time_s, format_time_ms, format_datetime, unixtime2datetime
% from http_templates.tmpl_helpers import car_tmpl
<div class="container">
    <div class="row page-header">
        <div class="col-md-6"><img src="/img/banner.png" title="Logo Track" class="ACimg"></div>
        <div class="col-md-6">
<script type="text/javascript">
% si = s['sessionInfo']
% if features['admin']:
function validateNewSessionName(aen)
{
% if not 'csName' in si:
    var valid = (/^[\w-+@ ]+$/.test(aen))
% else:
    var valid = 0
% end
                ;
    if( valid )
    {
        $("#session_name_input")[0].parentElement.classList.add("has-success");
        $("#session_name_label")[0].parentElement.classList.add("has-success");
        $("#session_name_input")[0].parentElement.classList.remove("has-error");
        $("#session_name_label")[0].parentElement.classList.remove("has-error");
        $("#addSessionBtn")[0].classList.remove("disabled");
        return true;
    } else
    {
        $("#session_name_input")[0].parentElement.classList.add("has-error");
        $("#session_name_label")[0].parentElement.classList.add("has-error");
        $("#session_name_input")[0].parentElement.classList.remove("has-success");
        $("#session_name_label")[0].parentElement.classList.remove("has-success");
        $("#addSessionBtn")[0].classList.add("disabled");
        return false;
    }
};
function addToEvent()
{
    var name = document.getElementById("session_name_input").value;
    var eventId = document.getElementById("event_selector").value;
    var psId = document.getElementById("ps_selector").value;
    if( validateNewSessionName(name) )
    {
        window.location.href = "modify_cs?event_id="+eventId+"&ps_id="+psId+"&session_name="+name+"&session_id={{session_id}}";
    }
    return false;
};
% if 'csName' in si:
function removeFromEvent()
{
    if( confirm('Do you really want to remove the session from the event?') )
    {
        window.location.href = "modify_cs?remove_event_session_id={{si['csEventSessionId']}}&session_id={{session_id}}";
    }
    return false;
};
% end
function validateNewDeltaTime(pisId, value)
{
    var valid = (/^[+-]?\s*(\d+:)?\d+\.\d+$/.test(value))
                || (value == "")
                ;
    var label = $("#dtLabelPis_" + pisId.toString())[0];
    var input = $("#dtInputPis_" + pisId.toString())[0];
    var btn = $("#penSubmitBtn_" + pisId.toString())[0];
    if(valid)
    {
        label.parentElement.classList.add("has-success");
        input.parentElement.classList.add("has-success");
        label.parentElement.classList.remove("has-error");
        input.parentElement.classList.remove("has-error");
        btn.classList.remove("disabled");
    } else
    {
        label.parentElement.classList.remove("has-success");
        input.parentElement.classList.remove("has-success");
        label.parentElement.classList.add("has-error");
        input.parentElement.classList.add("has-error");
        btn.classList.add("disabled");
    }
    return valid;
}
function validateNewDeltaPoints(pisId, value)
{
    var valid = (/^[+-]?\s*\d+(\.\d+)?$/.test(value))
                || (value == "")
                ;
    var label = $("#dpLabelPis_" + pisId.toString())[0];
    var input = $("#dpInputPis_" + pisId.toString())[0];
    var btn = $("#penSubmitBtn_" + pisId.toString())[0];
    if(valid)
    {
        label.parentElement.classList.add("has-success");
        input.parentElement.classList.add("has-success");
        label.parentElement.classList.remove("has-error");
        input.parentElement.classList.remove("has-error");
        btn.classList.remove("disabled");
    } else
    {
        label.parentElement.classList.remove("has-success");
        input.parentElement.classList.remove("has-success");
        label.parentElement.classList.add("has-error");
        input.parentElement.classList.add("has-error");
        btn.classList.add("disabled");
    }
    return valid;
}
function validateNewDeltaLaps(pisId, value)
{
    var valid = (/^[+-]?\s*\d+$/.test(value))
                || (value == "")
                ;
    var label = $("#dlLabelPis_" + pisId.toString())[0];
    var input = $("#dlInputPis_" + pisId.toString())[0];
    var btn = $("#penSubmitBtn_" + pisId.toString())[0];
    if(valid)
    {
        label.parentElement.classList.add("has-success");
        input.parentElement.classList.add("has-success");
        label.parentElement.classList.remove("has-error");
        input.parentElement.classList.remove("has-error");
        btn.classList.remove("disabled");
    } else
    {
        label.parentElement.classList.remove("has-success");
        input.parentElement.classList.remove("has-success");
        label.parentElement.classList.add("has-error");
        input.parentElement.classList.add("has-error");
        btn.classList.add("disabled");
    }
    return valid;
}
function validateNewPenaltyComment(pisId, value)
{
    var valid = (/^[\w +-@_]*$/.test(value))
                ;
    var label = $("#pcLabelPis_" + pisId.toString())[0];
    var input = $("#pcInputPis_" + pisId.toString())[0];
    var btn = $("#penSubmitBtn_" + pisId.toString())[0];
    if(valid)
    {
        label.parentElement.classList.add("has-success");
        input.parentElement.classList.add("has-success");
        label.parentElement.classList.remove("has-error");
        input.parentElement.classList.remove("has-error");
        btn.classList.remove("disabled");
    } else
    {
        label.parentElement.classList.remove("has-success");
        input.parentElement.classList.remove("has-success");
        label.parentElement.classList.add("has-error");
        input.parentElement.classList.add("has-error");
        btn.classList.add("disabled");
    }
    return valid;
}
function submitPenalties(pisId)
{
    var dt = $("#dtInputPis_" + pisId.toString())[0].value;
    var dp = $("#dpInputPis_" + pisId.toString())[0].value;
    var dl = $("#dlInputPis_" + pisId.toString())[0].value;
    var pc = $("#pcInputPis_" + pisId.toString())[0].value;
    if( validateNewDeltaTime(pisId, dt) &&
        validateNewDeltaPoints(pisId, dp) &&
        validateNewDeltaLaps(pisId, dl) &&
        validateNewPenaltyComment(pisId, pc))
    {
        window.location.href = "modify_session_penalties?dt="+dt+"&dp="+dp+"&dl="+dl+"&pc="+pc+"&pisId="+pisId.toString()+"&session_id={{session_id}}";
    }
    return false;
}
% end
</script>
% if features['admin']:
% if 'csName' in si:
            <div class="row">
                <form id="pointSchemaToAdd" name="pointSchemaToAdd" onsubmit="return removeFromEvent();">
                    <div class="row">
                        <div class="col-md-9">
                            <label for="delSessionBtn" class="control-label">Remove session from event <i>{{si['csEventName']}}</i> of <i>{{si['csName']}}</i></label>
                        </div>
                        <div class="col-md-3">
                            <button id="delSessionBtn" name="delSessionBtn" type="submit" class="form-control btn btn-danger">
                                Remove
                            </button>
                        </div>
                    </div>
                </form>
            </div>
            <br>
% else:
            <div class="row">
                <form id="eventToAdd" name="eventToAdd" onsubmit="return false;">
                    <div class="row">
                        <div class="col-md-4">
                            <label for="event_selector" class="control-label">Add to event</label>
                        </div>
                        <div class="col-md-5">
                            <select id="event_selector" name="event_selector" class="form-control multiselect">
                                  % for e in events:
                                    <option value="{{e['id']}}">{{e['name']}}</option>
                                  % end
                            </select>
                        </div>
                    </div>
                </form>
            </div>
            <div class="row">
                <form id="sessionName" name="sessionName" onsubmit="return false;">
                    <div class="row">
                        <div class="col-md-4">
                            <label name="session_name_label" id="session_name_label" for="session_name_input" class="control-label">Session Name</label>
                        </div>
                        <div class="col-md-5">
                            <input type="text" name="session_name_input" id="session_name_input" class="form-control" placeholder="Session Name" onchange="validateNewSessionName(this.value)"/>
                        </div>
                    </div>
                </form>
            </div>
            <div class="row">
                <form id="pointSchemaToAdd" name="pointSchemaToAdd" onsubmit="return addToEvent();">
                    <div class="row">
                        <div class="col-md-4">
                            <label for="ps_selector" class="control-label">Using point schema</label>
                        </div>
                        <div class="col-md-5">
                            <select id="ps_selector" name="ps_selector" class="form-control multiselect">
                                  % for ps in point_schemata:
                                    <option value="{{ps['pointSchemaId']}}">{{ps['psName']}}</option>
                                  % end
                            </select>
                        </div>
                        <div class="col-md-3">
                            <button id="addSessionBtn" name="addSessionBtn" type="submit" class="form-control btn btn-primary disabled">
                                Add
                            </button>
                        </div>
                    </div>
                </form>
            </div>
            <br>
% end
% end
            <div class="row">
                <form onsubmit="return false;">
                    <div class="row">
% if 'csName' in si:
                        <div class="col-md-9 panel panel-info">
                            <div class="panel-heading">Note</div>
                            <div class="panel-body">
                                This session is part of the event
                                <a href="championship?event_id={{si['csEventId']}}">{{si['csEventName']}}</a>
                                of the championship <a href="championship?cs_id={{si['csId']}}">{{si['csName']}}</a>.
                                The session name is {{"'%s'"%si['csSessionName']}}.
                            </div>
                        </div>
% else:
% if features['admin']:
                        <div class="col-md-4"></div>
                        <div class="col-md-5">
                            <button class="form-control btn btn-primary" onClick="window.location.href='entry_list?sessionid={{!session_id}}';">
                                Generate entry_list.ini
                            </button>
                        </div>
% else:
                        <div class="col-md-9"></div>
% end
% end
                        <div class="col-md-3">
                            <button class="form-control btn btn-primary" onClick="window.history.back();">
                                Back
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-md-12">
            <table class="table table-striped table-condensed table-bordered table-hover">
                <tr>
                    <th>Track</th>
                    <th>Session</th>
% displayNumLaps = not si['numLaps'] in [None,0]
% displayDuration = not si['duration'] in [None,0]
% if displayNumLaps:
                    <th>Number of laps</th>
% end
% if displayDuration:
                    <th>Duration</th>
% end
                    <th>Date and time</th>
                    <th>Penalties and Corrections</th>
                </tr>

                <tr>
                    <td>{{si['uitrack'] if not si['uitrack'] is None else si['track']}}</td>
                    <td>{{si['sessionType']}}</td>
% if displayNumLaps:
                    <td>{{si['numLaps']}}</td>
% end
% if displayDuration:
                    <td>{{format_time_s(si['duration']*1000)}}</td>
% end
% ts = si['timestamp'][0]
% if ts is None:
%     ts = "-"
% else:
%     ts = format_datetime(unixtime2datetime(ts))
% end
                    <td>{{ts}}</td>
                    <td>{{'yes' if si['corrected'] else 'no'}}</td>
                </tr>
            </table>
        </div>
    </div>
    <div class="row">
        <div class="col-md-12">
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
                <caption>Classification</caption>
                <thead>
                <tr>
                    <th>Rank</th>
                    <th>Driver</th>
                    <th>Car</th>
% if si['sessionType'] == 'Race':
                    <th>Total time</th>
                    <th>Gap to 1st</th>
                    <th>Fastest lap</th>
                    <th>Pit stops</th>
                    <th>Drive through</th>
                    <th>Pit lane time</th>
% else:
                    <th>Fastest lap</th>
                    <th>Gap to 1st</th>
% end
                    <th>Laps (valid)</th>
                    <th>Cuts</th>
                    <th>Crashes (car/car)</th>
% if si['corrected']:
                    <th>Penalties</th>
                    <th>Original Rank</th>
% end
% if features['admin']:
                    <th>Penalty Admin</th>
% end
                </tr>
                </thead>
                <tbody>
% timeWinner = s['classification'][0]['finishTime'] if si['sessionType'] == "Race" else s['classification'][0]['fastestLap']
% lapsWinner = s['classification'][0]['numLaps']
% fastestLap = min(s['classification'], key=lambda x: x['fastestLap'] if not x['fastestLap'] is None else 1000*60*60*24*5)['fastestLap']
% for i,r in enumerate(s['classification']):
%   timeCurr = r['finishTime'] if si['sessionType'] == "Race" else r['fastestLap']
                    <tr class="clickableRow" href="sessiondetails?playerInSessionId={{"%d" % r['pisId']}}#">
%   pos = str(r['pos'])
                        <td>{{pos}}</td>
                        <td>{{r['name']}}</td>
                        <td>{{!car_tmpl.render(car=r['car'], uicar=r['uicar'])}}</td>
% c = 'class="bestLap" ' if r['fastestLap'] == fastestLap else ''
% if si['sessionType'] == 'Race':
                        <td>{{format_time_ms(r['finishTime'],False)}}</td>
% if r['numLaps'] == lapsWinner or timeCurr is None:
                        <td>{{"" if i == 0 or timeWinner is None or timeCurr is None else format_time_ms(timeCurr - timeWinner, True)}}</td>
% else:
%   d = lapsWinner - r['numLaps']
                        <td>{{"+%d lap%s" % (d, "s"*(d > 1))}}</td>
% end
                        <td {{!c}}>{{format_time_ms(r['fastestLap'],False)}}</td>
% if r['pitInfoAvailable'] or 1:
                        <td>{{r['numPitStops']}}</td>
                        <td>{{r['numDriveThroughs']}}</td>
                        <td>{{format_time_ms(r['totalTimePitLane'],False)}}</td>
% else:
                        <td>-</td>
                        <td>-</td>
                        <td>-</td>
% end
% else:
                        <td {{!c}}>{{format_time_ms(r['fastestLap'],False)}}</td>
                        <td>{{"" if i == 0 or timeWinner is None or timeCurr is None else format_time_ms(timeCurr - timeWinner, True)}}</td>
% end
                        <td>{{r['numLaps']}} ({{r['numLapsValid']}})</td>
                        <td>{{r['numCuts']}}</td>
                        <td>{{r['numCollisions']}} ({{r['numCollisionsC2C']}})</td>
%   penTime = ""
%   penLaps = ""
%   penPoints = ""
%   penComment = r['corrComment'] if not r['corrComment'] is None else ""
% if si['corrected']:
%   pen = []
%   if not r['deltaTime'] is None:
%      penTime = format_time_ms(r['deltaTime'],True)
%      pen.append(penTime)
%   end
%   if not r['deltaLaps'] is None:
%      penLaps = "%+d" % r['deltaLaps']
%      pen.append(penLaps + " laps")
%   end
%   format_points = lambda x: ("+" if x > 0 else "") + ("%d" % x if round(x) == x else str(x))
%   if not r['deltaPoints'] is None:
%      penPoints = format_points(r['deltaPoints'])
%      pen.append(penPoints + " points")
%   end
%   pen = "; ".join(pen)
%   comment = r['corrComment']
                        <td>
%   if not comment is None:
                            <span data-toggle="tooltip" title="{{comment}}" class="text-info" aria-hidden="true">{{pen}}</span>
%   else:
                            {{pen}}
%   end
                        </td>
                        <td>{{r['finishPositionOrig']}}</td>
% end
% if features['admin']:
                        <td class="noclick">
% btnId = "dropdownMenu%d" % r['pisId']
                            <div class="dropdown">
                                <button type="button" class="btn btn-primary btn-xs dropdown-toggle" id="{{btnId}}" data-toggle="dropdown" aria-expanded="true">
                                    Manage <span class="caret"></span>
                                </button>
                                <div style="width:100%;min-width:400px" class="dropdown-menu">
% formId = "formPis_%d" % r['pisId']
% timeDeltaLabelId = "dtLabelPis_%d" % r['pisId']
% timeDeltaInputId = "dtInputPis_%d" % r['pisId']
% pointDeltaLabelId = "dpLabelPis_%d" % r['pisId']
% pointDeltaInputId = "dpInputPis_%d" % r['pisId']
% lapDeltaLabelId = "dlLabelPis_%d" % r['pisId']
% lapDeltaInputId = "dlInputPis_%d" % r['pisId']
% pCommentLabelId = "pcLabelPis_%d" % r['pisId']
% pCommentInputId = "pcInputPis_%d" % r['pisId']
% buttonName = "penSubmitBtn_%d" % r['pisId']
                                    <form class="form-horizontal" role="form" id="{{!formId}}" name="{{!formId}}" onsubmit="return submitPenalties({{r['pisId']}});">
                                        <fieldset>
                                          <div class="form-group">
                                            <label name="{{!timeDeltaLabelId}}"
                                                   id="{{!timeDeltaLabelId}}"
                                                   class="col-md-5 control-label">Correction Time</label>
                                            <div class="col-md-6">
                                                <input type="text"
                                                       name="{{!timeDeltaInputId}}"
                                                       id="{{!timeDeltaInputId}}"
                                                       class="form-control"
                                                       placeholder="[+-] mm:ss.MMM"
                                                       onchange="validateNewDeltaTime({{r['pisId']}},this.value)"
                                                       value="{{penTime}}"
                                                       />
                                            </div>
                                          </div>
                                          <div class="form-group">
                                            <label name="{{!pointDeltaLabelId}}"
                                                   id="{{!pointDeltaLabelId}}"
                                                   class="col-md-5 control-label">Correction Points</label>
                                            <div class="col-md-6">
                                                <input type="text"
                                                       name="{{!pointDeltaInputId}}"
                                                       id="{{!pointDeltaInputId}}"
                                                       class="form-control"
                                                       placeholder="[+-] <number>"
                                                       onchange="validateNewDeltaPoints({{r['pisId']}},this.value)"
                                                       value="{{penPoints}}"
                                                       />
                                            </div>
                                          </div>
                                          <div class="form-group">
                                            <label name="{{!lapDeltaLabelId}}"
                                                   id="{{!lapDeltaLabelId}}"
                                                   class="col-md-5 control-label">Correction Laps</label>
                                            <div class="col-md-6">
                                                <input type="text"
                                                       name="{{!lapDeltaInputId}}"
                                                       id="{{!lapDeltaInputId}}"
                                                       class="form-control"
                                                       placeholder="[+-] <number>"
                                                       onchange="validateNewDeltaLaps({{r['pisId']}},this.value)"
                                                       value="{{penLaps}}"
                                                       />
                                            </div>
                                          </div>
                                          <div class="form-group">
                                            <label name="{{!pCommentLabelId}}"
                                                   id="{{!pCommentLabelId}}"
                                                   class="col-md-5 control-label">Comment</label>
                                            <div class="col-md-6">
                                                <input type="text"
                                                       name="{{!pCommentInputId}}"
                                                       id="{{!pCommentInputId}}"
                                                       class="form-control"
                                                       placeholder="Comment"
                                                       onchange="validateNewPenaltyComment({{r['pisId']}},this.value)"
                                                       value="{{penComment}}"
                                                       />
                                            </div>
                                          </div>
                                          <div class="form-group">
                                            <div class="col-sm-offset-5 col-sm-6">
                                                <button type="submit" name="{{!buttonName}}" id="{{!buttonName}}" class="btn btn-default">Submit</button>
                                            </div>
                                          </div>
                                        </fieldset>
                                    </form>
                                </div>
                                </div>
                            </div>
                        </td>
% end
                    </tr>
% end
                </tbody>
            </table>
        </div>
    </div>
</div>
<script>
$('[data-toggle="tooltip"]').tooltip({
    'placement': 'top'
});
</script>
""")

pisDetailsTemplate = SimpleTemplate("""
% from ptracker_lib.helpers import isProMode, format_time_s, format_time_ms, format_datetime, unixtime2datetime
<div class="container">
    <div class="row page-header">
        <div class="col-md-6"><img src="/img/banner.png" title="Logo Track" class="ACimg"></div>
        <div class="col-md-2 col-md-offset-4">
            <button class="form-control btn btn-primary" onClick="window.history.back()">
                Back
            </button>
        </div>
    </div>
    <div class="row">
        <div class="col-md-12">
% def entry(key, d, conv=str):
%    v = d.get(key, None)
%    if v is None:
%        v = '-'
%    else:
%        v = conv(v)
%    end
%    return v
% end
% pis = res['playerInSessioInfo']
% count = res['sectorCount']
% laps = res['laps']
            <table class="table table-striped table-condensed table-bordered table-hover">
                <caption>Laps of driver {{pis['name']}}</caption>
                <thead>
                <tr>
                <th>Lap number</th>
                <th>Lap time</th>
% from ptracker_lib.helpers import isProMode, format_time_ms, format_datetime, unixtime2datetime
% for i in range(count):
                <th>{{'S%d' % (i+1)}}</th>
% end
                <th>Pit lane time</th>
                <th>Pit time</th>
                <th>Valid</th>
                <th>Cuts</th>
                <th>Collisions (car-to-car)</th>
                <th>Fuel</th>
                <th>Aids</th>
            </tr>
            </thead>
            <tbody>
% for i,r in enumerate(laps):
            <tr class='clickableRow' href="lapdetails?lapid={{"%d" % r['id']}}#">
                <td>{{"%d." % (r['lapCount']) if not r['lapCount'] is None else '-'}}</td>
                <td>{{format_time_ms(r['lapTime'], False)}}</td>
% for si in range(count):
    % if r['sectors'][si] is None:
    %   s = "-"
    % else:
    %   s = format_time_ms(r['sectors'][si], False)
    % end
                <td>{{s}}</td>
% end
                <td>{{format_time_ms(r['timeInPitLane'], False) if not r['timeInPitLane'] is None and r['timeInPitLane'] > 0 else '-'}}</td>
                <td>{{format_time_ms(r['timeInPit'], False) if not r['timeInPit'] is None and r['timeInPit'] > 0 else '-'}}</td>
                <td>{{['no','yes','-'][r['valid']] + (" (ESC used)" if r['escKeyPressed'] else "")}}</td>
                <td>{{r['cuts']}}</td>
                <td>{{r['collisions']}} ({{r['collisionsCar']}})</td>
                <td>{{entry('fuelRatio', d=r, conv=lambda x: ("%.1f%%" % (x*100.) if x > 0 else '-'))}}</td>
                <td><div>
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
                    <a class="aids autoclutch {{adaptClassBool('autoClutch', r)}}" title="Automatic clutch {{adaptClassBool('autoClutch', r)}}"></a>
                    <a class="aids abs {{adaptClassBool('abs', r, True)}}" title="ABS {{adaptClassBool('abs', r, True)}}"></a>
                    <a class="aids autobrake {{adaptClassBool('autoBrake', r)}}" title="Automatic brake {{adaptClassBool('autoBrake', r)}}"></a>
                    <a class="aids autogearbox {{adaptClassBool('autoShift', r)}}" title="Automatic gearbox {{adaptClassBool('autoShift', r)}}"></a>
                    <a class="aids blip {{adaptClassBool('autoBlib', r)}}" title="Automatic throttle blip {{adaptClassBool('autoBlib', r)}}"></a>
                    <a class="aids idealline {{adaptClassBool('idealLine', r)}}" title="Ideal racing line {{adaptClassBool('idealLine', r)}}"></a>
                    <a class="aids tc {{adaptClassBool('tractionControl', r, True)}}" title="Traction control {{adaptClassBool('tractionControl', r, True)}}"></a>
                </div></td>
            </tr>
% end
            </tbody>
        </table>
        </div>
    </div>
</div>
""")

