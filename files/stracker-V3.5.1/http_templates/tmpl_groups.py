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

groupsTemplate = SimpleTemplate("""
% from ptracker_lib.helpers import isProMode, format_time_s, format_time_ms, format_datetime, unixtime2datetime
<script type="text/javascript">
function validateNewGroup(agn)
{
    if( /^\w+$/.test(agn) )
    {
        $("#add_group_name")[0].parentElement.classList.add("has-success");
        $("#add_group_label")[0].parentElement.classList.add("has-success");
        $("#add_group_name")[0].parentElement.classList.remove("has-error");
        $("#add_group_label")[0].parentElement.classList.remove("has-error");

        $("#btnNewGroup")[0].classList.remove("disabled");
        return true;
    } else
    {
        $("#add_group_name")[0].parentElement.classList.add("has-error");
        $("#add_group_label")[0].parentElement.classList.add("has-error");
        $("#add_group_name")[0].parentElement.classList.remove("has-success");
        $("#add_group_label")[0].parentElement.classList.remove("has-success");
        $("#btnNewGroup")[0].classList.add("disabled");
        return false;
    }
};
function addNewGroup()
{
    var agn = document.getElementById("add_group_name").value;
    if( validateNewGroup(agn) )
    {
        window.location.href = "modify_groups?add_group="+agn;
    }
    return false;
};
function showGroup()
{
    var gid = document.getElementById("groups").value;
    window.location.href = "groups?group_id="+gid;
    return false;
};
function delGroup()
{
    var gid = document.getElementById("dgroups").value;
    var gname = document.getElementById('dgroups').options[document.getElementById('dgroups').selectedIndex].text;
    if( confirm("Do you really want to delete the group '" + gname + "'?") )
    {
        window.location.href = "modify_groups?del_group="+gid;
    }
    return false;
};
</script>
<div class="container">
    <div class="row page-header">
        <div class="col-md-6"><img src="/img/banner.png" title="Logo Track" class="ACimg"></div>
        <div class="col-md-6">
            <div class="row">
                <form id="displayGroup" name="displayGroup" onsubmit="return showGroup();">
                    <div class="row">
                        <div class="col-md-2">
                            <label for="groups" class="control-label">Display</label>
                        </div>
                        <div class="col-md-6">
                            <select id="groups" name="groups" class="form-control multiselect">
% for g in res['groups']:
                                <option value="{{!g['groupid']}}" {{!"selected" if g['groupid'] == group_id else ""}}>{{g['name']}}</option>
% end
                            </select>
                        </div>
                        <div class="col-md-4">
                            <button type="submit" name="btnShowGroup" id="btnShowGroup" class="form-control btn btn-primary">Show</button>
                        </div>
                    </div>
                </form>
            </div>
            <br>
            <div class="row">
                <form id="formNewGroup" name="formNewGroup" onsubmit="return addNewGroup();">
                    <div class="row"><div class="form-group">
                        <div class="col-md-2" for="groups">
                            <label name="add_group_label" id="add_group_label" for="add_group_name" class="control-label">Add group</label>
                        </div>
                        <div class="col-md-6">
                            <input type="text" name="add_group_name" id="add_group_name" class="form-control" placeholder="Group Name" onchange="validateNewGroup(this.value)"/>
                        </div>
                        <div class="col-md-4">
                            <button type="submit" name="btnNewGroup" id="btnNewGroup" class="form-control btn btn-primary disabled">Add new group</button>
                        </div>
                    </div></div>
                </form>
            </div>
            <br>
            <div class="row">
                <form id="formDelGroup" name="formDelGroup" onsubmit="return delGroup();">
                    <div class="row"><div class="form-group">
                        <div class="col-md-2" for="groups">
                            <label for="dgroups" class="control-label">Remove group</label>
                        </div>
                        <div class="col-md-6">
                            <select id="dgroups" name="dgroups" class="form-control multiselect">
% for g in res['groups']:
%   if g['groupid'] == 0:
%     continue
%   end
                                <option value="{{!g['groupid']}}" {{!"selected" if g['groupid'] == group_id else ""}}>{{g['name']}}</option>
% end
                            </select>
                        </div>
                        <div class="col-md-4">
                            <button type="submit" name="btnDelGroup" id="btnDelGroup" class="form-control btn btn-danger">Remove group</button>
                        </div>
                    </div></div>
                </form>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-md-12">
% if len(res['players']) == 0:
            <div class="panel panel-info">
                <div class="panel-heading">Note</div>
                <div class="panel-body">
                    There are no drivers in this group. To assign drivers to groups, go to the <a href="players">Drivers</a> section,
                    click on a driver, and add him to the group.
                </div>
            </div>
% else:
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
% end
                        <td>{{format_datetime(unixtime2datetime(r['lastSeen'])) if not r['lastSeen'] is None else '-'}}</td>
                    </tr>
% end
                </tbody>
            </table>
% end
        </div>
    </div>
</div>
""")
