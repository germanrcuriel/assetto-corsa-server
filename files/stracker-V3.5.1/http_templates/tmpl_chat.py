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

chatlogTemplate = SimpleTemplate("""
<div class="container">
    <div class="row page-header">
        <div class="col-md-6"><img src="/img/banner.png" title="Logo Track" class="ACimg"></div>
        <div class="col-md-6">
            <form class="form-horizontal collapse-group" role="form">
                <div class="form-group">
% if len(servers) > 1:
                    <label for="servers" class="col-md-2 control-label">Server</label>
                    <div class="col-md-10">
                        <select id="server" name="server" class="form-control multiselect">
%   for s in servers:
                            <option {{!"selected" if s == server else ""}} value="{{s}}">{{s}}</option>
%   end
                        </select>
                    </div>
% end
                    <label for="date_from" class="col-md-2 control-label">From</label>
                    <div class="col-md-3">
                        <input name="date_from" id="date_from" class="datepicker form-control" data-date-format="yyyy-mm-dd" value="{{date_from if not date_from is None else ''}}" />
                    </div>
                    <label for="date_to" class="col-md-2 control-label">To</label>
                    <div class="col-md-3">
                        <input name="date_to" id="date_to" class="datepicker form-control" data-date-format="yyyy-mm-dd" value="{{date_to if not date_to is None else ''}}" />
                    </div>
                </div>
                <div class="form-group">
                    <div class="col-md-4 col-md-offset-2">
                        <button class="form-control btn btn-sm btn-primary">
                            Submit
                        </button>
                    </div>
                    <div class="col-md-4 col-md-offset-2">
                        <button class="form-control btn btn-sm btn-primary" onClick="window.history.back()">
                            Back
                        </button>
                    </div>
                </div>
            </form>
        </div>
    </div>
    <div class="row">
        <div class="col-md-12">
            <table class="table table-responsive table-hover table-striped table-condensed">
                <thead>
                    <tr><th class="col-sm-2 text-right">Timestamp</th><th class="col-sm-2 text-center">Name</th><th class="col-sm-8">Chat message</th></tr>
                </thead>
                <tbody">
% from ptracker_lib.helpers import *
% for msg in messages:
%    ts = unixtime2datetime(msg['timestamp'])
%    ts = format_datetime(ts)
                    <tr><td class="text-right">{{ts}}</td><td class="text-right"><a href="playerdetails?pid={{"%d" % msg['playerid']}}#">{{msg['name']}}:</a></td><td>{{msg['content']}}</td></tr>
% end
                </tbody>
            </table>
        </div>
    </div>
</div>
""")

