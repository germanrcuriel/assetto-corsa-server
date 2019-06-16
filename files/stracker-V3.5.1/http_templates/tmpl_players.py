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

playersTemplate = SimpleTemplate("""
% from ptracker_lib.helpers import isProMode, format_time_s, format_time_ms, format_datetime, unixtime2datetime
<div class="container">
    <div class="row page-header">
        <div class="col-md-6"><img src="/img/banner.png" title="Logo Track" class="ACimg"></div>
        <div class="col-md-6">
% if features['banlist'] and features['admin'] and caller == "banlist":
            <div class="panel panel-info">
                <div class="panel-heading">Note</div>
                <div class="panel-body">
                    To add a driver to the banlist, go to the <a href="players">Drivers</a> section,
                    click on the driver to ban and choose the ban duration.
                </div>
            </div>
            <br>
% end
            <form class="form-inline" role="form" onsubmit="applySelections(); return false;">
                <div class="form-group">
                    <label for="search_pattern" class="col-md-2 control-label"><span class="glyphicon glyphicon-search"></span></label>
                    <input type="search" id="search_pattern" class="col-md-2 form-control" placeholder="Search" {{!'value="%s"' % search_pattern if not search_pattern in [None,""] else ""}}/>
<script>
function applySelections() {
    var sp = document.getElementById("search_pattern").value;
    var address = 'players?search_pattern='+sp;
    console.log(address);
    window.location.href = address;
}
</script>
                    <div class="col-md-2">
                        <button type="button" class="form-control btn btn-primary" onclick="applySelections()">Show</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
    <div class="row">
        <div class="col-md-12">
            <table class="table table-striped table-condensed table-bordered table-hover">
                <thead>
                    <tr>
                        <th>Driver name</th>
                        <th>Online</th>
% if features['admin']:
                        <th>Steam GUID Hash</th>
%    if features['banlist']:
                        <th>Ban count</th>
                        <th>Banned until</th>
%    end
                        <th>Whitelisted</th>
% end
                        <th>Last seen</th>
                    </tr>
                </thead>
                <tbody>
% for i,r in enumerate(res['players']):
                    <tr class='clickableRow' href="playerdetails?pid={{"%d" % r['playerId']}}#">
                        <td>{{r['name']}}</td>
                        <td>{{'@' + r['isOnline'] if not r['isOnline'] is None else '-'}}</td>
% if features['admin']:
                        <td>{{"..." + r['guid'][-10:]}}</td>
%    if features['banlist']:
                        <td>{{r['banCount'] if not r['banCount'] is None else '-'}}</td>
                        <td>{{format_datetime(unixtime2datetime(r['bannedUntil']),onlyDate=True) if not r['bannedUntil'] is None else '-'}}</td>
%    end
                        <td>{{"yes" if r['whitelisted'] else "no"}}</td>
% end
                        <td>{{format_datetime(unixtime2datetime(r['lastSeen'])) if not r['lastSeen'] is None else '-'}}</td>
                    </tr>
% end
                </tbody>
            </table>
        </div>
    </div>
</div>
""")

plyDetailsTemplate = SimpleTemplate("""
% from ptracker_lib.helpers import *
% import datetime
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
        <div class="col-md-4">
% def entry(v, conv=str):
%    if v is None:
%        v = '-'
%    else:
%        v = conv(v)
%    end
%    return v
% end
            <table class="table table-striped table-condensed table-bordered table-hover">
                <caption>Driver informations</caption>
                <tbody>
                    <tr><td>Name</td><td>{{entry(ply['info']['name'])}}</td></tr>
                    <tr><td>Driver type</td><td>{{['human driver', 'artificial intelligence'][ply['info']['artint']]}}</td></tr>
% if features['admin']:
                    <tr><td>Steam GUID Hash</td><td>{{"..." + ply['info']['steamguid'][-10:]}}</td></tr>
                    <tr><td>Whitelisted</td><td>{{entry(ply['info']['whitelisted'])}}</td></tr>
% end
                </tbody>
            </table>
            <table class="table table-striped table-condensed table-bordered table-hover">
                <caption>Statistics (total) </caption>
                <tbody>
                    <tr><td>Number of server laps</td><td>{{entry(ply['numLaps'])}}</td></tr>
%#                    <tr><td>Number of km</td><td>{{round(ply['km']) if not ply['km'] is None else '-'}}</td></tr>
                    <tr><td>Number of cuts</td><td>{{entry(ply['numCuts'])}}</td></tr>
                    <tr><td>Number of car/car collisions</td><td>{{entry(ply['numCollisionsCar'])}}</td></tr>
                    <tr><td>Number of env collisions</td><td>{{entry(ply['numCollisionsEnv'])}}</td></tr>
                    <tr><td>Number of races</td><td>{{entry(ply['numRaces'])}}</td></tr>
                    <tr><td>Number of races finished first</td><td>{{ply['numPodiums'][0]}}</td></tr>
                    <tr><td>Number of races finished second</td><td>{{ply['numPodiums'][1]}}</td></tr>
                    <tr><td>Number of races finished third</td><td>{{ply['numPodiums'][2]}}</td></tr>
                </tbody>
            </table>
            <table class="table table-striped table-condensed table-bordered table-hover">
                <caption>Statistics (last 30 days) </caption>
                <tbody>
                    <tr><td>Number of server laps</td><td>{{entry(ply['numLaps30days'])}}</td></tr>
                    <tr><td>Number of km</td><td>{{round(ply['km30days']) if not ply['km30days'] is None else '-'}}</td></tr>
                    <tr><td>Number of cuts</td><td>{{entry(ply['numCuts30days'])}}</td></tr>
                    <tr><td>Number of car/car collisions</td><td>{{entry(ply['numCollisionsCar30days'])}}</td></tr>
                    <tr><td>Number of env collisions</td><td>{{entry(ply['numCollisionsEnv30days'])}}</td></tr>
                    <tr><td>Number of races</td><td>{{entry(ply['numRaces30days'])}}</td></tr>
                    <tr><td>Number of races finished first</td><td>{{ply['numPodiums30days'][0]}}</td></tr>
                    <tr><td>Number of races finished second</td><td>{{ply['numPodiums30days'][1]}}</td></tr>
                    <tr><td>Number of races finished third</td><td>{{ply['numPodiums30days'][2]}}</td></tr>
                </tbody>
            </table>
        </div>
% if features['admin'] and features['banlist']:
        <div class="col-md-4">
% banActive = False
% if len(ply['bans']) > 0:
             <table class="table table-striped table-condensed table-bordered table-hover">
             <caption>Banlist information</caption>
                <tbody>
                    <tr>
                        <th>Active</th>
                        <th>Start date</th>
                        <th>End date</th>
                    </tr>
% now = unixtime_now()
% for b in ply['bans']:
%   active = now <= b['dateadded']+b['duration']
%   banActive = banActive or active
                    <tr>
                        <td>{{'yes' if active else 'no'}}</td>
                        <td>{{format_datetime(unixtime2datetime(b['dateadded']),onlyDate=True)}}</td>
                        <td>{{format_datetime(unixtime2datetime(b['dateadded']+b['duration']),onlyDate=True)}}</td>
                    </tr>
% end
                </tbody>
            </table>
% else:
            <div class="panel panel-info">
                <div class="panel-heading">Note</div>
                <div class="panel-body">
                    This driver has not been banned until now.
                </div>
            </div>
% end
        </div>
% end
% if features['admin']:
        <div class="col-md-4">
<script>
function extendBanPeriod() {
    var period = document.getElementById("banperiod").value;
    if (confirm("Do you really want to change the ban period of this driver?") == true)
    {
        window.location = 'ban?pid={{!ply["info"]["playerid"]}}&extendPeriod='+period;
    }
}
function unban() {
    if (confirm("Do you really want to remove the ban from this driver?") == true)
    {
        window.location = 'ban?pid={{!ply["info"]["playerid"]}}&unban=1';
    }
}
function ban() {
    var period = document.getElementById("banperiod").value;
    if (confirm("Do you really want to ban this driver?") == true)
    {
        window.location = 'ban?pid={{!ply["info"]["playerid"]}}&period='+period;
    }
}
function addToGroup() {
    var groupId = document.getElementById("addGroupSelect").value;
    window.location.href = "modify_groups?add_player_id="+{{!ply["info"]["playerid"]}}+"&group_id="+groupId;
}
function delFromGroup() {
    var groupId = document.getElementById("delGroupSelect").value;
    var groupName = document.getElementById('delGroupSelect').options[document.getElementById('delGroupSelect').selectedIndex].text;
    if (confirm("Do you really want to remove this driver from the group '"+groupName+"'?") == true)
    {
        window.location.href = "modify_groups?del_player_id="+{{!ply["info"]["playerid"]}}+"&group_id="+groupId;
    }
}
function whitelist() {
    if (confirm("Do you really want to whitelist this driver?") == true)
    {
        window.location.href = "modify_whitelist?whitelist_player_id={{!ply["info"]["playerid"]}}";
    }
}
function unwhitelist() {
    if (confirm("Do you really want to un-whitelist this driver?") == true)
    {
        window.location.href = "modify_whitelist?unwhitelist_player_id={{!ply["info"]["playerid"]}}";
    }
}
</script>
            <form class="form-horizontal" role="form" onsubmit="return false">
% if features['banlist']:
              <div class="form-group">
                <label for="banperiod" class="col-sm-5 control-label">Period from now</label>
                <div class="col-sm-7">
                    <select id="banperiod" name="banperiod" class="form-control multiselect">
                            <option value="{{60*60*24}}">1 day</option>
                            <option value="{{60*60*24*7}}">1 week</option>
                            <option value="{{60*60*24*7*4}}">4 weeks</option>
                            <option selected value="{{60*60*24*7*12}}">12 weeks</option>
                            <option value="{{60*60*24*365}}">1 year</option>
                            <option value="{{60*60*24*365*3}}">3 years</option>
                            <option value="{{60*60*24*365*10}}">10 years</option>
                    </select>
                </div>
              </div>
              <div class="form-group">
% if banActive:
                <div class="col-sm-offset-5 col-sm-7">
                    <button type="button" class="form-control btn btn-danger" disabled="disabled">Ban this driver</button>
                </div>
                <div class="col-sm-offset-5 col-sm-7">
                    <button type="button" class="form-control btn btn-danger" onClick="extendBanPeriod()">Change ban period</button>
                </div>
                <div class="col-sm-offset-5 col-sm-7">
                    <button type="button" class="form-control btn btn-success" onClick="unban()">Remove ban</button>
                </div>
% else:
                <div class="col-sm-offset-5 col-sm-7">
                    <button type="button" class="form-control btn btn-danger" onClick="ban()">Ban this driver</button>
                </div>
                <div class="col-sm-offset-5 col-sm-7">
                    <button type="button" class="form-control btn btn-danger" disabled="disabled">Change ban period</button>
                </div>
                <div class="col-sm-offset-5 col-sm-7">
                    <button type="button" class="form-control btn btn-success" disabled="disabled">Remove ban</button>
                </div>
% end
              </div>
% end
              <div class="form-group">
                <label for="addGroupSelect" class="col-sm-5 control-label">Add to group</label>
                <div class="col-sm-4">
                    <select id="addGroupSelect" name="addGroupSelect" class="form-control multiselect">
% groupNames = {}
% countAddGroups = 0
% for g in ply['groups']:
    % groupNames[g['groupid']] = g['name']
    % if g['groupid'] > 0 and not g['groupid'] in ply['memberOfGroup']:
        % countAddGroups += 1
                        <option value="{{!g['groupid']}}">{{g['name']}}</option>
    % end
% end
                    </select>
                </div>
                <div class="col-sm-3">
                    <button type="button"
                            class="form-control btn btn-success"
                             {{!'disabled="disabled"' if countAddGroups == 0 else ''}}
                             onclick="addToGroup()">Add</button>
                </div>
              </div>
              <div class="form-group">
                <label for="delGroupSelect" class="col-sm-5 control-label">Remove from group</label>
                <div class="col-sm-4">
                    <select id="delGroupSelect" name="delGroupSelect" class="form-control multiselect">
% for gid in ply['memberOfGroup']:
                        <option value="{{!gid}}">{{groupNames[gid]}}</option>
% end
                    </select>
                </div>
                <div class="col-sm-3">
                    <button type="button"
                            class="form-control btn btn-danger"
                            {{!'disabled="disabled"' if len(ply['memberOfGroup']) == 0 else ''}}
                            onclick="delFromGroup()">Remove</button>
                </div>
              </div>
              <div class="form-group">
% if ply["info"]['whitelisted']:
                <div class="col-sm-offset-5 col-sm-7">
                    <button type="button" class="form-control btn btn-success" disabled="disabled">Add to whitelist</button>
                </div>
                <div class="col-sm-offset-5 col-sm-7">
                    <button type="button" class="form-control btn btn-danger" onClick="unwhitelist()">Remove from whitelist</button>
                </div>
% else:
                <div class="col-sm-offset-5 col-sm-7">
                    <button type="button" class="form-control btn btn-success" onClick="whitelist()">Add to whitelist</button>
                </div>
                <div class="col-sm-offset-5 col-sm-7">
                    <button type="button" class="form-control btn btn-danger" disabled="disabled">Remove from whitelist</button>
                </div>
% end
              </div>
            </form>
        </div>
% end # admin area
    </div>
</div>
""")

