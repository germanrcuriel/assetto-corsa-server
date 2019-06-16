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

livemapTemplate = SimpleTemplate("""
% goodWidth = 1024
% goodHeight = 640
% gscale = min(goodWidth/width, goodHeight/height)
% svgW = round(width*gscale)
% svgH = round(height*gscale)
% vbX = round((goodWidth - svgW)/2)
% vbY = round((goodHeight - svgH)/2)

<script>
$(function() {

  function update() {
    $.getJSON('livemap_stream?key={{!key}}{{!("&server="+server if not server is None else "") + "&global_scale=%.5f"%(gscale*scale)}}', {}, function(data) {
      if (data.state != 'done') {
        if ('svg_data' in data) {
            $('#livemap_contents')[0].innerHTML = data.svg_data;
        }
        if ('session_data' in data) {
            $('#session_display')[0].innerHTML = data.session_data;
        }
        if ('class_data' in data) {
            $('#class_display')[0].innerHTML = data.class_data;
        }
        if ('alive_data' in data) {
            $('#alive_ticker')[0].innerHTML = data.alive_data;
        }
        if ('chat_data' in data) {
            $('#chat_contents')[0].innerHTML = data.chat_data;
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
                </div>
                <div class="form-group">
% if len(servers) > 1:
                    <div class="col-md-4 col-md-offset-2">
                        <button class="form-control btn btn-sm btn-primary">
                            Submit
                        </button>
                    </div>
                    <div class="col-md-4 col-md-offset-2">
% else:
                    <div class="col-md-4 col-md-offset-8">
% end
                        <button class="form-control btn btn-sm btn-primary" onClick="window.history.back()">
                            Back
                        </button>
                    </div>
                </div>
            </form>
        </div>
    </div>
% if features['admin']:
    <div class="row page-header">
%   cserver = "" if server is None else server
            <form action="broadcastchat" class="form-horizontal" role="form">
                <div class="form-group">
                    <input type="hidden" name="server" value="{{!cserver}}" />
                    <label for="bcastchat" class="col-md-1 control-label">Chat</label>
                    <div class="col-md-8">
                        <input id="bcastchat" name="message" class="form-control">
                    </div>
                    <div class="col-md-offset-1 col-md-2"><button type="submit" class="form-control btn btn-primary">Chat</button></div>
                </div>
            </form>
            <form action="manage_session" class="form-horizontal" role="form">
                <div class="form-group">
                    <input type="hidden" name="server" value="{{!cserver}}" />
                    <label for="ptime" class="col-md-1 control-label">Pract. Minutes</label>
                    <div class="col-md-2">
                        <input type="number" min="1" max="300" value="" id="ptime" name="ptime" class="form-control">
                    </div>
                    <label for="ptime" class="col-md-1 control-label">Quali Minutes</label>
                    <div class="col-md-2">
                        <input type="number" min="1" max="300" id="qtime" name="qtime" class="form-control">
                    </div>
                    <label for="ptime" class="col-md-1 control-label">Race Laps</label>
                    <div class="col-md-2">
                        <input type="number" min="1" max="999" id="rlaps" name="rlaps" class="form-control">
                    </div>
                    <div class="col-md-offset-1 col-md-2"><button type="submit" class="form-control btn btn-primary">Set</button></div>
                </div>
            </form>
            <form class="form-horizontal" role="form">
                <div class="form-group">
                    <input type="hidden" name="server" value="{{!cserver}}" />
                    <div class="col-md-offset-7 col-md-2"><a href="manage_session?restart=1&server={{cserver}}" class="form-control btn btn-primary">Restart Session</a></div>
                    <div class="col-md-offset-1 col-md-2"><a href="manage_session?skip=1&server={{cserver}}" class="form-control btn btn-primary">Skip Session</a></div>
                </div>
            </form>
    </div>
% end
    <div class="row page-header">
        <div class="col-md-6">
            <div>

                <svg id="stracker_liveview" viewBox="0 0 {{svgW}} {{svgH}}" xmlns="http://www.w3.org/2000/svg" style="max-height:{{!goodHeight}}px">
                    <g transform="scale({{!gscale}})">
                        <image width="{{!width}}" height="{{!height}}" preserveAspectRatio="none" xlink:href="{{!track_image}}"></image>
                        <g id="alive_ticker">
                        </g>
                        <g id="chat_contents">
                        </g>
                        <g id="livemap_contents" class="plot_overlay" transform="translate({{!'%.1f,%.1f' % (offsetx*scale,offsety*scale)}}) scale({{!'%f' % scale}})">
                        </g>
                    </g>
                </g>
                </svg>

            </div>
        </div>
        <div class="col-md-6">
            <div>
                <table class="table table-striped table-condensed table-bordered table-hover">
                    <thead>
                    <tr>
                        <th>Track</th>
                        <th>Session</th>
                        <th>Duration</th>
                    </tr>
                    </thead>
                    <tbody id="session_display">
                    </tbody>
                </table>
            </div>
            <div>
                <table class="table table-striped table-condensed table-bordered table-hover">
                    <thead>
                    <tr>
                        <th>Rank</th>
                        <th>Car</th>
                        <th>Driver</th>
% if features['admin']:
                        <th>Admin</th>
% end
                        <th>Best Lap</th>
                        <th>Laps</th>
                        <th>Finish Time</th>
                    </tr>
                    </thead>
                    <tbody id="class_display">
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
""")

livemapClassification = SimpleTemplate("""
%   from ptracker_lib.helpers import *
%   from stracker_lib import config
%   from http_templates import tmpl_helpers
%   connected = {}
%   for ci in carClassEntries:
%       guid = ci.guid
%       pos = ci.pos
%       name = ci.name
%       bestLapTime = format_time_ms(ci.bestLapTime, False) if ci.bestLapTime > 0 else "-"
%       laps = ci.lapCount
%       color = color_map[ci.guid]
%       style = ""
%       if not ci.connected:
%           color = "gray"
%           style = ' style="color:gray"'
%       end
%       finishTime = format_time_ms(ci.sumLapTimes, False) if ci.finished and sessionInfo.session_type == ac_server_protocol.SESST_RACE else "-"
%       car = tmpl_helpers.car_tmpl.render(car=ci.car, tooltip=True)
%       btnId = "dropdown_%s" % ci.guid
%       formId = "form_%s" % ci.guid
%       labelId = "label_%s" % ci.guid
%       inputId = "input_%s" % ci.guid
%       cserver = server if not server is None else config.config.STRACKER_CONFIG.server_name
            <tr>
                <td style="color:{{!color}}"><b>&bull;</b> {{pos}}.</td>
                <td{{!style}}>{{!car}}</td>
                <td{{!style}}>{{name}}</td>
%       if features['admin']:
%           if not ci.connected:
                <td></td>
%           else:
                <td class="noclick">
                    <div class="dropdown">
                        <button type="button" class="btn btn-primary btn-xs dropdown-toggle" id="{{!btnId}}" data-toggle="dropdown" aria-expanded="true">
                            Manage <span class="caret"></span>
                        </button>
                        <div style="width:100%%;min-width:400px" class="dropdown-menu">
                            <div class="form-horizontal">
                                <form action="whisper" role="form">
                                      <input type="hidden" name="guid" value="{{!guid}}" />
                                      <input type="hidden" name="server" value="{{!cserver}}" />
                                      <div class="form-group form-group-sm">
                                        <label class="col-sm-3 control-label input-sm" for="whisper_{{!guid}}">Whisper</label>
                                        <div class="col-sm-6"><input class="form-control input-sm" type="text" name="text" id="whisper_{{!guid}}" value="" /></div>
                                        <div class="col-sm-3"><button type="submit" class="btn btn-primary btn-sm">Whisper</button></div>
                                      </div>
                                </form>
                                <form action="kick?guid={{!guid}}" role="form" onsubmit="return confirm('Do you really want to kick {{!name}} ?');">
                                      <input type="hidden" name="guid" value="{{!guid}}" />
                                      <input type="hidden" name="server" value="{{!cserver}}" />
                                      <div class="form-group form-group-sm">
                                          <div class="col-sm-offset-9 col-sm-3"><button type="submit" class="btn btn-warning btn-sm">Kick</button></div>
                                      </div>
                                </form>
                                <form action="ban?guid={{!guid}}" role="form" onsubmit="return confirm('Do you really want to ban {{!name}} ?');">
                                      <input type="hidden" name="guid" value="{{!guid}}" />
                                      <input type="hidden" name="server" value="{{!cserver}}" />
                                      <div class="form-group form-group-sm">
                                        <label class="col-sm-3 control-label input-sm" for="ban_{{!guid}}">Ban days</label>
                                        <div class="col-sm-6"><input class="form-control input-sm" type="number" name="days" value="30" min="1" max="999"></div>
                                        <div class="col-sm-3"><button type="submit" class="btn btn-danger btn-sm">Ban</button></div>
                                      </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </td>

%           end
%       end
                <td{{!style}}>{{bestLapTime}}</td>
                <td{{!style}}>{{laps}}</td>
                <td{{!style}}>{{finishTime}}</td>
            </tr>
%   end
""")