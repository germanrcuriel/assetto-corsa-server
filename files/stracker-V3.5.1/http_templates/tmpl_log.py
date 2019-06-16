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

logTemplate = SimpleTemplate("""
<script>
$(function() {

  function update() {
%if not server is None:
%   serverStr = "&server="+server
%else:
%   serverStr = ""
%end
%serverStr += "&level="+level
    $.getJSON('log_stream?key={{!key}}&limit={{!str(limit) + serverStr}}', {}, function(data) {
      if (data.state != 'done') {
        if(data.content != '') {
            $('#log_contents').append(data.content);
            window.scrollTo(0,document.body.scrollHeight);
        }
        setTimeout(update, 0);
      }
    });
  }

  update();
});
</script>
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
                    <label for="limit" class="col-md-2 control-label">Lines</label>
                    <div class="col-md-10">
                        <select id="limit" name="limit" class="form-control multiselect">
% limits = set([10,20,50,100,200,1000] + [limit])
% for l in sorted(list(limits)):
                            <option {{!"selected" if l == limit else ""}} value="{{l}}">{{l}}</option>
% end
                        </select>
                    </div>

                    <label for="level" class="col-md-2 control-label">Level</label>
                    <div class="col-md-10">
                        <select id="level" name="level" class="form-control multiselect">
% levels = ["error", "warning", "info", "debug", "unclassified"]
% for l in levels:
                            <option {{!"selected" if l == level else ""}} value="{{l}}">{{l}}</option>
% end
                        </select>
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
            <table class="table table-condensed">
                <tbody id="log_contents">
                </tbody>
            </table>
        </div>
    </div>
</div>
""")

