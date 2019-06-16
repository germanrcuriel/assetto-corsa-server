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

# args:
#   seasons : [{'id':,'name':}]
#   cs_id
#   events  : [{'id':,'name':,'sessions'}]
#   event_id
#   players : [{'name':, 'guid':, 'cum_points':}]
#
championshipTemplate = SimpleTemplate("""
% from ptracker_lib.helpers import format_datetime, unixtime2datetime

<script type="text/javascript">
% if features['admin']:
function validateNewSeason(asn)
{
    var valid = (/^[\w-+@ ]+$/.test(asn))
% for s in seasons:
                && asn != '{{!s['name']}}'
% end
                ;
    if( valid )
    {
        $("#add_season_name")[0].parentElement.classList.add("has-success");
        $("#add_season_label")[0].parentElement.classList.add("has-success");
        $("#add_season_name")[0].parentElement.classList.remove("has-error");
        $("#add_season_label")[0].parentElement.classList.remove("has-error");
        $("#btnNewSeason")[0].classList.remove("disabled");
        return true;
    } else
    {
        $("#add_season_name")[0].parentElement.classList.add("has-error");
        $("#add_season_label")[0].parentElement.classList.add("has-error");
        $("#add_season_name")[0].parentElement.classList.remove("has-success");
        $("#add_season_label")[0].parentElement.classList.remove("has-success");
        $("#btnNewSeason")[0].classList.add("disabled");
        return false;
    }
};
function addNewSeason()
{
    var asn = document.getElementById("add_season_name").value;
    if( validateNewSeason(asn) )
    {
        window.location.href = "modify_cs?add_season="+asn;
    }
    return false;
};
function delSeason()
{
    var sel = document.getElementById('dseason');
    if( sel.selectedIndex >= 0 )
    {
        var csid = sel.value;
        var sname = sel.options[sel.selectedIndex].text;
        if( confirm("Do you really want to delete the season '" + sname + "' and all related entries?") )
        {
            window.location.href = "modify_cs?del_season="+csid;
        }
    }
    return false;
};
% end
function showSeason()
{
    var csid = document.getElementById("cs_selector").value;
    window.location.href = "championship?cs_id="+csid;
    return false;
};
function showSeasonTeam()
{
    var csid = document.getElementById("cs_selector").value;
    window.location.href = "championship?team_score=1&cs_id="+csid;
    return false;
};
</script>

% if not events is None:
<script type="text/javascript">
% if features['admin']:
function validateNewEvent(aen)
{
    var valid = (/^[\w-+@ ]+$/.test(aen))
% for e in events:
                && aen != '{{!e['name']}}'
% end
                ;
    if( valid )
    {
        $("#add_event_name")[0].parentElement.classList.add("has-success");
        $("#add_event_label")[0].parentElement.classList.add("has-success");
        $("#add_event_name")[0].parentElement.classList.remove("has-error");
        $("#add_event_label")[0].parentElement.classList.remove("has-error");
        $("#btnNewEvent")[0].classList.remove("disabled");
        return true;
    } else
    {
        $("#add_event_name")[0].parentElement.classList.add("has-error");
        $("#add_event_label")[0].parentElement.classList.add("has-error");
        $("#add_event_name")[0].parentElement.classList.remove("has-success");
        $("#add_event_label")[0].parentElement.classList.remove("has-success");
        $("#btnNewEvent")[0].classList.add("disabled");
        return false;
    }
};
function addNewEvent()
{
    var aen = document.getElementById("add_event_name").value;
    if( validateNewEvent(aen) )
    {
        window.location.href = "modify_cs?cs_id={{!cs_id}}&add_event="+aen;
    }
    return false;
};
function delEvent()
{
    var sel = document.getElementById('devent');
    if( sel.selectedIndex >= 0 )
    {
        var eid = sel.value;
        var ename = sel.options[sel.selectedIndex].text;
        if( confirm("Do you really want to delete the event '" + ename + "' and all related entries?") )
        {
            window.location.href = "modify_cs?cs_id={{!cs_id}}&del_event="+eid;
        }
    }
    return false;
};
function validateNewTeamName(pid, value)
{
    var valid = (/^[\w-+@ ]+$/.test(value))
                || (value == "")
                ;

    var label = $("#teamNameLabelPid_" + pid.toString())[0];
    var input = $("#teamNameInputPid_" + pid.toString())[0];
    var btn = $("#teamNameSubmitBtn_" + pid.toString())[0];
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
};
function submitTeamName(pid)
{
    var tn = $("#teamNameInputPid_" + pid.toString())[0].value;
    if( validateNewTeamName(pid, tn) )
    {
        window.location.href = "championship_setteam?cs_id={{!cs_id}}&team_name="+tn+"&pid="+pid.toString();
    }
    return false;
};
% end
</script>
% end

<div class="container">
    <div class="row page-header">
        <div class="col-md-6"><img src="/img/banner.png" title="Logo Track" class="ACimg">
        </div>

        <div class="col-md-6">
            <div class="row">
                <form id="displaySeason" name="displaySeason" onsubmit="return showSeason();">
                    <div class="row">
                        <div class="col-md-3">
                            <label for="cs_selector" class="control-label">Championship</label>
                        </div>
                        <div class="col-md-5">
                            <select id="cs_selector" name="cs_selector" class="form-control multiselect">
                                  % for s in seasons:
                                  %   if s['id'] == cs_id:
                                  %     sel = "selected"
                                  %   else:
                                  %     sel = ""
                                  %   end
                                    <option {{!sel}} value="{{s['id']}}">{{s['name']}}</option>
                                  % end
                            </select>
                        </div>
                        <div class="col-md-2">
                            <button type="submit" name="btnShowSeason" id="btnShowSeason" class="form-control btn btn-primary">Individual</button>
                        </div>
                        <div class="col-md-2">
                            <button type="button" name="btnShowSeason" id="btnShowSeasonTeam" class="form-control btn btn-primary" onclick="showSeasonTeam()">Team</button>
                        </div>
                    </div>
                </form>
            </div>
% if features['admin']:
            <br>
            <div class="row">
                <form id="formNewSeason" name="formNewSeason" onsubmit="return addNewSeason();">
                    <div class="row">
                        <div class="form-group">
                            <div class="col-md-4" for="groups">
                                <label name="add_season_label" id="add_season_label" for="add_season_name" class="control-label">
                                    New Championship
                                </label>
                            </div>
                            <div class="col-md-5">
                                <input type="text" name="add_season_name" id="add_season_name" class="form-control" placeholder="Championship Name" onchange="validateNewSeason(this.value)"/>
                            </div>
                            <div class="col-md-3">
                                <button type="submit" name="btnNewSeason" id="btnNewSeason" class="form-control btn btn-primary disabled">
                                    Add
                                </button>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
            <div class="row">
                <form id="formDelSeason" name="formDelSeason" onsubmit="return delSeason();">
                    <div class="row">
                        <div class="form-group">
                            <div class="col-md-4" for="groups">
                                <label for="dseason" class="control-label">Remove</label>
                            </div>
                            <div class="col-md-5">
                                <select id="dseason" name="dseason" class="form-control multiselect">
                                  % for s in seasons:
                                  %   if s['id'] == cs_id:
                                  %     sel = "selected"
                                  %   else:
                                  %     sel = ""
                                  %   end
                                    <option {{!sel}} value="{{s['id']}}">{{s['name']}}</option>
                                  % end
                                </select>
                            </div>
                            <div class="col-md-3">
                                <button type="submit" name="btnDelSeason" id="btnDelSeason" class="form-control btn btn-danger">
                                    Del
                                </button>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
% end
% if not events is None:
            <br>
% if features['admin']:
            <div class="row">
                <form id="formNewEvent" name="formNewEvent" onsubmit="return addNewEvent();">
                    <div class="row">
                        <div class="form-group">
                            <div class="col-md-4" for="groups">
                                <label name="add_event_label" id="add_event_label" for="add_event_name" class="control-label">
                                    New Event
                                </label>
                            </div>
                            <div class="col-md-5">
                                <input type="text" name="add_event_name" id="add_event_name" class="form-control" placeholder="Event Name" onchange="validateNewEvent(this.value)"/>
                            </div>
                            <div class="col-md-3">
                                <button type="submit" name="btnNewEvent" id="btnNewEvent" class="form-control btn btn-primary disabled">
                                    Add
                                </button>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
            <div class="row">
                <form id="formDelEvent" name="formDelEvent" onsubmit="return delEvent();">
                    <div class="row">
                        <div class="form-group">
                            <div class="col-md-4" for="groups">
                                <label for="devent" class="control-label">Remove</label>
                            </div>
                            <div class="col-md-5">
                                <select id="devent" name="devent" class="form-control multiselect">
                                      % for e in events:
                                      %   if e['id'] == event_id:
                                      %     sel = "selected"
                                      %   else:
                                      %     sel = ""
                                      %   end
                                        <option {{!sel}} value="{{e['id']}}">{{e['name']}}</option>
                                      % end
                                </select>
                            </div>
                            <div class="col-md-3">
                                <button type="submit" name="btnDelEvent" id="btnDelEvent" class="form-control btn btn-danger">
                                    Del
                                </button>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
% end
% end
% if features['admin']:
            <br>
            <div class="row">
                <div class="row">
                    <div class="col-md-5 col-md-offset-4">
                        <a class="btn btn-primary" href="point_schemata" role="button">
                            Manage championship point schemata
                        </a>
                    </div>
                </div>
            </div>
% end
        </div>
    </div>
    <div class="row">
% if not players is None and not events is None:
% cntCols = 0
% for e in events:
%   cntCols += max(1, len(e['sessions']))
% end
% requiredSpace = 3 + cntCols // 4
% requiredSpace = ((min(12, max(4, requiredSpace))+1)//2)*2
% colOffset = (12-requiredSpace)//2
% if not team_score:
%    allTeamsNone = all([p['teams'] == set(["(none)"]) for p in players])
% end
        <div class="col-md-offset-{{colOffset}} col-md-{{requiredSpace}}">
            <table class="table table-striped table-condensed table-bordered table-hover">
                <thead>
                    <tr>
                        <th rowspan="2" class="vert-align">Rank</th>
% if not team_score:
                        <th rowspan="2" class="vert-align">Name</th>
%if not allTeamsNone:
                        <th rowspan="2" class="vert-align">Team</th>
%end
% if features['admin']:
                        <th rowspan="2" class="vert-align">Team Admin</th>
% end
% else:
                        <th rowspan="2" class="vert-align">Team</th>
% end
                        <th rowspan="2" class="vert-align">Total Points</th>
%   for e in events:
%     s = e['sessions']
                        <th class="text-center" colspan="{{max(1,len(s))}}">
                            <span data-toggle="tooltip" title="{{e['name']}}" class="glyphicon glyphicon-info-sign text-info" aria-hidden="true">
                            </span>
                        </th>
%   end
                    </tr>
                    <tr>
%   for e in events:
                        {{!"<th></th>" if len(e['sessions']) == 0 else ""}}
%     for s in e['sessions']:
                        <th class="text-center">
                            <a href="sessiondetails?sessionid={{s['sessionId']}}" data-toggle="tooltip" title="{{s['sessionName']}}"><i class="glyphicon glyphicon-info-sign"></i></a>
                        </th>
%     end
%   end
                    </tr>
                </thead>
                <tbody>
%   format_points = lambda x: "%d" % x if round(x) == x else str(x)
%   lastPoints = None
%   table = teams if team_score else players
%   for i,p in enumerate(table):
%     pid = p['pid']
%     pos = i+1 if lastPoints != p['cum_points'] else lastPos
%     lastPoints = p['cum_points']
%     lastPos = pos
                    <tr>
                        <td class="text-center">{{"%d." % lastPos if lastPos == i+1 else ""}}</td>
                        <td>{{p['name']}}</td>
%     if not team_score:
%         if not allTeamsNone:
                        <td>{{",".join(p['teams'])}}</td>
%          end
%       if features['admin']:
                        <td class="noclick">
% btnId = "dropdownMenu%d" % p['pid']
                            <div class="dropdown">
                                <button type="button" class="btn btn-primary btn-xs dropdown-toggle" id="{{btnId}}" data-toggle="dropdown" aria-expanded="true">
                                    Manage <span class="caret"></span>
                                </button>
                                <div style="width:100%;min-width:400px" class="dropdown-menu">
% formId = "formPid_%d" % p['pid']
% teamNameLabelId = "teamNameLabelPid_%d" % p['pid']
% teamNameInputId = "teamNameInputPid_%d" % p['pid']
% buttonName = "teamNameSubmitBtn_%d" % p['pid']
                                    <form class="form-horizontal" role="form" id="{{!formId}}" name="{{!formId}}" onsubmit="return submitTeamName({{p['pid']}});">
                                        <fieldset>
                                          <div class="form-group">
                                            <label name="{{!teamNameLabelId}}"
                                                   id="{{!teamNameLabelId}}"
                                                   class="col-md-5 control-label">Set team name (for all events)</label>
                                            <div class="col-md-6">
                                                <input type="text"
                                                       name="{{!teamNameInputId}}"
                                                       id="{{!teamNameInputId}}"
                                                       class="form-control"
                                                       placeholder="(Team Name)"
                                                       onchange="validateNewTeamName({{p['pid']}},this.value)"
                                                       value=""
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
                        </td>

%       end
%     end

                        <td class="text-center">{{format_points(p['cum_points'])}}</td>
%     for e in events:
                        {{!"<td></td>" if len(e['sessions']) == 0 else ""}}
%       for s in e['sessions']:
%         cm = s['classment'] if not team_score else s['teamClassment']
%         p = list(filter(lambda x: x[0] == pid, cm))
%         if len(p) == 0:
                        <td class="text-center">-</td>
%         else:
%           pos = p[0][1]
%           points = p[0][2]
                        <td class="text-center">{{format_points(points)}}</td>
%         end
%       end
%     end
                    </tr>
%   end
                </tbody>
        </div>
% end
    </div>
</div>
<script>
$('[data-toggle="tooltip"]').tooltip({
    'placement': 'top'
});
</script>
""")

# args:
#   - point_schemata : [{'pointSchemaId':,'psName':,'schema':{pos:points}]
#   - ps_id
pointSchemaTemplate = SimpleTemplate("""
% if features['admin']:
% from ptracker_lib.helpers import format_datetime, unixtime2datetime

<script type="text/javascript">
function validateNewPS(asn)
{
    var valid = (/^[\w-+@ ]+$/.test(asn))
% for ps in point_schemata:
                && asn != '{{!ps['psName']}}'
% end
                ;
    if( valid )
    {
        $("#add_ps_name")[0].parentElement.classList.add("has-success");
        $("#add_ps_label")[0].parentElement.classList.add("has-success");
        $("#add_ps_name")[0].parentElement.classList.remove("has-error");
        $("#add_ps_label")[0].parentElement.classList.remove("has-error");
        $("#btnNewPS")[0].classList.remove("disabled");
        return true;
    } else
    {
        $("#add_ps_name")[0].parentElement.classList.add("has-error");
        $("#add_ps_label")[0].parentElement.classList.add("has-error");
        $("#add_ps_name")[0].parentElement.classList.remove("has-success");
        $("#add_ps_label")[0].parentElement.classList.remove("has-success");
        $("#btnNewPS")[0].classList.add("disabled");
        return false;
    }
};
function addNewPS()
{
    var asn = document.getElementById("add_ps_name").value;
    if( validateNewPS(asn) )
    {
        window.location.href = "modify_point_schema?add_schema="+asn;
    }
    return false;
};
function showPS()
{
    var psid = document.getElementById("ps_selector").value;
    window.location.href = "point_schemata?ps_id="+psid;
    return false;
};
function delPS()
{
    var sel = document.getElementById('dps');
    if( sel.selectedIndex >= 0 )
    {
        var psid = sel.value;
        var psname = sel.options[sel.selectedIndex].text;
        if( confirm("Do you really want to delete the season '" + psname + "' and all related entries?") )
        {
            window.location.href = "modify_point_schema?del_schema="+psid;
        }
    }
    return false;
};
function validateNewPoints(pos, value)
{
    var valid = (/^\d+(\.\d+)?$/.test(value));
    if( valid )
    {
        $("#pointInput_"+pos.toString())[0].parentElement.classList.add("has-success");
        $("#pointInput_"+pos.toString())[0].parentElement.classList.remove("has-error");
        $("#saveInput_"+pos.toString())[0].classList.remove("disabled");
        return true;
    } else
    {
        $("#pointInput_"+pos.toString())[0].parentElement.classList.add("has-error");
        $("#pointInput_"+pos.toString())[0].parentElement.classList.remove("has-success");
        $("#saveInput_"+pos.toString())[0].classList.add("disabled");
        return false;
    }
};
function newPointsFor(pos)
{
    var i = document.getElementById("pointInput_" + pos.toString());
    window.location.href = "modify_point_schema?pos="+pos.toString()+"&points="+i.value+"&ps_id={{ps_id}}";
    return false;
};
function delPointsFor(pos)
{
    window.location.href = "modify_point_schema?delpos="+pos.toString()+"&ps_id={{ps_id}}";
    return false;
};
</script>
<div class="container">
    <div class="row page-header">
        <div class="col-md-6"><img src="/img/banner.png" title="Logo Track" class="ACimg">
        </div>
        <div class="col-md-6">
            <div class="row">
                <form id="displayPS" name="displayPS" onsubmit="return showPS();">
                    <div class="row">
                        <div class="col-md-4">
                            <label for="ps_selector" class="control-label">Point Schema</label>
                        </div>
                        <div class="col-md-5">
                            <select id="ps_selector" name="ps_selector" class="form-control multiselect">
                                  % for s in point_schemata:
                                  %   if s['pointSchemaId'] == ps_id:
                                  %     sel = "selected"
                                  %   else:
                                  %     sel = ""
                                  %   end
                                    <option {{!sel}} value="{{s['pointSchemaId']}}">{{s['psName']}}</option>
                                  % end
                            </select>
                        </div>
                        <div class="col-md-3">
                            <button type="submit" name="btnShowPS" id="btnShowPS" class="form-control btn btn-primary">Show</button>
                        </div>
                    </div>
                </form>
            </div>
            <div class="row">
                <form id="formNewPS" name="formNewPS" onsubmit="return addNewPS();">
                    <div class="row">
                        <div class="form-group">
                            <div class="col-md-4">
                                <label name="add_ps_label" id="add_ps_label" for="add_ps_name" class="control-label">
                                    New point schema
                                </label>
                            </div>
                            <div class="col-md-5">
                                <input type="text" name="add_ps_name" id="add_ps_name" class="form-control" placeholder="Schema Name" onchange="validateNewPS(this.value)"/>
                            </div>
                            <div class="col-md-3">
                                <button type="submit" name="btnNewPS" id="btnNewPS" class="form-control btn btn-primary disabled">
                                    Add
                                </button>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
            <div class="row">
                <form id="formDelPS" name="formDelPS" onsubmit="return delPS();">
                    <div class="row">
                        <div class="form-group">
                            <div class="col-md-4">
                                <label for="dps" class="control-label">Remove</label>
                            </div>
                            <div class="col-md-5">
                                <select id="dps" name="dps" class="form-control multiselect">
                                  % for s in point_schemata:
                                  %   if s['pointSchemaId'] == ps_id:
                                  %     sel = "selected"
                                  %   else:
                                  %     sel = ""
                                  %   end
                                  %   if s['removable']:
                                    <option {{!sel}} value="{{s['pointSchemaId']}}">{{s['psName']}}</option>
                                  %   end
                                  % end
                                </select>
                            </div>
                            <div class="col-md-3">
                                <button type="submit" name="btnDelPS" id="btnDelPS" class="form-control btn btn-danger">
                                    Del
                                </button>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-md-4">
% ps = None
% for r in point_schemata:
%   if r['pointSchemaId'] == ps_id:
%     ps = r
%     break
%   end
% end
% if not ps is None:
            <table class="table">
                <thead>
                    <tr>
                        <th>Position</th>
                        <th>Points</th>
                        <th></th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
% pos = 0
% for pos in sorted(ps['schema'].keys()):
                    <tr>
                        <td>{{pos}}</td>
                        <td><input type="text" name="pointInput_{{pos}}" id="pointInput_{{pos}}" placeholder="Points" value="{{ps['schema'][pos]}}" onchange="validateNewPoints({{pos}},this.value)"/></td>
                        <td>
                            <a name="saveInput_{{pos}}" id="saveInput_{{pos}}" class="btn btn-primary btn-xs" href="#" role="button" onclick="newPointsFor({{pos}});">
                                Save
                            </a>
                        </td>
% if pos == len(ps['schema']):
                        <td>
                            <a name="saveInput_{{pos}}" id="saveInput_{{pos}}" class="btn btn-primary btn-xs" href="#" role="button" onclick="delPointsFor({{pos}});">
                                Remove
                            </a>
                        </td>
% end
                    </tr>
% end
% pos += 1
                    <tr>
                        <td>{{pos}}</td>
                        <td><div><input type="text" name="pointInput_{{pos}}" id="pointInput_{{pos}}" placeholder="Points" value="" onchange="validateNewPoints({{pos}},this.value)"/></div></td>
                        <td><div>
                            <a name="saveInput_{{pos}}" id="saveInput_{{pos}}" class="btn btn-primary btn-xs" href="#" role="button" onclick="newPointsFor({{pos}});">
                                Save
                            </a>
                        </div></td>
                    </tr>
                </tbody>
            </table>
% else:
            <div class="panel panel-info">
                <div class="panel-heading">Note</div>
                <div class="panel-body">
                    No point schema selected - select a point schema to be displayed
                    with the controls in the upper right.
                </div>
            </div>
% end
        </div>
% if not ps is None and not ps['removable']:
        <div class="col-md-4">
            <div class="panel panel-warning">
                <div class="panel-heading">Warning</div>
                <div class="panel-body">
                    You are modifying a point schema already used to assign points
                    in a championship event. Modifying the schema has effects on
                    the championship. If this is not intended, create a new point
                    schema and do not alter the existing one.
                </div>
            </div>
        </div>
% end
    </div>
</div>
% end
""")
