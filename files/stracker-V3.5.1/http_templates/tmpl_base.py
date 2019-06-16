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
# basic template for bootstrap
# ----------------------------------------------

baseTemplate = SimpleTemplate("""
%from ptracker_lib.helpers import acdebug
%acdebug("Rendering %s", curr_url)
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">

% if src != "main":
    <meta name="robots" content="noindex, nofollow">
    <meta name="googlebot" content="noindex, nofollow">
% end

    <!-- Include Twitter Bootstrap and jQuery: -->

    <link rel="stylesheet" href="/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="/bootstrap/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="/bootstrap/css/bootstrap-multiselect.css" type="text/css"/>
    <link rel="stylesheet" href="/bootstrap/css/bootstrap-datepicker.css" type="text/css"/>
    <link rel="stylesheet" href="/bootstrap/css/sticky-footer.css" type="text/css"/>
    <link rel="stylesheet" href="/bootstrap/css/fileinput.min.css" media="all" type="text/css" />

    <script src="/jquery/jquery.min.js"></script>
    <script src="/bootstrap/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="/bootstrap/js/bootstrap-multiselect.js"></script>
    <script type="text/javascript" src="/bootstrap/js/bootstrap-datepicker.js"></script>
    <script src="/bootstrap/js/fileinput.min.js" type="text/javascript"></script>
% if pygal:
    <script type="text/javascript" src="/pygal/svg.jquery.js"></script>
    <script type="text/javascript" src="/pygal/pygal-tooltips.min.js"></script>
% end

    % title_texts = dict(lapstat="Laps", sesstat="Sessions", players="Drivers", cs="Championships", stats="Statistics", livemap="Live Map", banlist="Ban List", groups="Groups", admin="General Admin", log="Log")
    % title = title_texts.get(src, "stracker")
    <title>{{title}}</title>
    <link rel="shortcut icon" type="image/x-icon" href="/img/brand_icon_small_wob.png">

    <style>

        .aids {
            width:16px;
            height:16px;
            background:none left top no-repeat;
            display:inline-block;
            background-size:cover;
            margin-right:-3px;
            margin-left:-3px;
            margin-top:-3px;
            margin-bottom:-3px;
        }

        .aids.autoclutch.off { background-image:url(/img/icn_stability_off.png) }
        .aids.autoclutch.on  { background-image:url(/img/icn_stability_on.png) }
        .aids.autoclutch.unknown { background-image:url(/img/icn_stability_unknown.png) }

        .aids.abs.off { background-image:url(/img/icn_abs_off.png) }
        .aids.abs.factory { background-image:url(/img/icn_abs_factory.png) }
        .aids.abs.on { background-image:url(/img/icn_abs_on.png) }
        .aids.abs.unknown { background-image:url(/img/icn_abs_unknown.png) }

        .aids.autobrake.off { background-image:url(/img/icn_automaticbraking_off.png) }
        .aids.autobrake.on { background-image:url(/img/icn_automaticbraking_on.png) }
        .aids.autobrake.unknown { background-image:url(/img/icn_automaticbraking_unknown.png) }

        .aids.autogearbox.off { background-image:url(/img/icn_gearbox_off.png) }
        .aids.autogearbox.on { background-image:url(/img/icn_gearbox_on.png) }
        .aids.autogearbox.unknown { background-image:url(/img/icn_gearbox_unknown.png) }

        .aids.blip.off { background-image:url(/img/icn_heeltoe_off.png) }
        .aids.blip.on { background-image:url(/img/icn_heeltoe_on.png) }
        .aids.blip.unknown { background-image:url(/img/icn_heeltoe_unknown.png) }

        .aids.idealline.off { background-image:url(/img/icn_idealline_off.png) }
        .aids.idealline.on { background-image:url(/img/icn_idealline_on.png) }
        .aids.idealline.unknown { background-image:url(/img/icn_idealline_unknown.png) }

        .aids.tc.off { background-image:url(/img/icn_tractioncontrol_off.png) }
        .aids.tc.factory { background-image:url(/img/icn_tractioncontrol_factory.png) }
        .aids.tc.on { background-image:url(/img/icn_tractioncontrol_on.png) }
        .aids.tc.unknown { background-image:url(/img/icn_tractioncontrol_unknown.png) }

        .aids.damage.off { background-image:url(/img/icn_stability_off.png) }
        .aids.damage.on { background-image:url(/img/icn_stability_on.png) }
        .aids.damage.unknown { background-image:url(/img/icn_stability_unknown.png) }

        .bestLap { color:#ff00ff }
        .bestSector { color:#00c000 }

        .multiselect {
            text-align: left;
        }
        .multiselect b.caret {
            position: absolute;
            top: 14px;
            right: 8px;
        }
        .multiselect-container>li>a>label>input[type=checkbox]{margin-bottom:0px}

        .table-condensed>thead>tr>th,
        .table-condensed>tbody>tr>th,
        .table-condensed>tfoot>tr>th,
        .table-condensed>thead>tr>td,
        .table-condensed>tbody>tr>td,
        .table-condensed>tfoot>tr>td {
            padding: 2px;
        }
        .clickableRow td {
            cursor: pointer;
            cursor: hand;
        }
        .clickableRow td.noclick {
            cursor: auto;
        }
        .table tbody>tr>td.vert-align {
            vertical-align: middle;
        }
        .table thead>tr>th.vert-align {
            vertical-align: middle;
        }
        .navbar-fixed-bottom {
            z-index: 900;
        }
% if features['pts']:
        html body {
            background: rgba(255,255,255,0.6);
        }
        .table-striped > tbody > tr:nth-child(2n+1) > td, .table-striped > tbody > tr:nth-child(2n+1) > th {
            background-color: rgba(249,249,249,0.6);
        }
        .navbar-default {
            background: rgba(255,255,255,0.6);
            background: -moz-linear-gradient(top, rgba(255,255,255,0.6) 0%, rgba(248,248,248,0.6) 100%);
            background: -webkit-gradient(left top, left bottom, color-stop(0%, rgba(255,255,255,0.6)), color-stop(100%, rgba(248,248,248,0.6)));
            background: -webkit-linear-gradient(top, rgba(255,255,255,0.6) 0%, rgba(248,248,248,0.6) 100%);
            background: -o-linear-gradient(top, rgba(255,255,255,0.6) 0%, rgba(248,248,248,0.6) 100%);
            background: -ms-linear-gradient(top, rgba(255,255,255,0.6) 0%, rgba(248,248,248,0.6) 100%);
            background: linear-gradient(to bottom, rgba(255,255,255,0.6) 0%, rgba(248,248,248,0.6) 100%);
            filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#ffffff', endColorstr='#f8f8f8', GradientType=0 );
        }
        .navbar-default .navbar-nav > .active > a {
            background: rgba(235,235,235,0.6);
            background: -moz-linear-gradient(top, rgba(235,235,235,0.6) 0%, rgba(248,248,248,0.6) 100%);
            background: -webkit-gradient(left top, left bottom, color-stop(0%, rgba(235,235,235,0.6)), color-stop(100%, rgba(248,248,248,0.6)));
            background: -webkit-linear-gradient(top, rgba(235,235,235,0.6) 0%, rgba(248,248,248,0.6) 100%);
            background: -o-linear-gradient(top, rgba(235,235,235,0.6) 0%, rgba(248,248,248,0.6) 100%);
            background: -ms-linear-gradient(top, rgba(235,235,235,0.6) 0%, rgba(248,248,248,0.6) 100%);
            background: linear-gradient(to bottom, rgba(235,235,235,0.6) 0%, rgba(248,248,248,0.6) 100%);
            filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#ebebeb', endColorstr='#f8f8f8', GradientType=0 );
        }
% end
    </style>
    <link rel="stylesheet" href="/bootstrap/css/custom.css" media="all" type="text/css" />
</head>
<body>

% from stracker_lib import config
% navbar_style = "inverse" if config.config.HTTP_CONFIG.inverse_navbar else "default"

<nav class="navbar navbar-{{!navbar_style}}" role="navigation">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="{{!rootpage}}"><img class="img-responsive" alt="stracker" src="/img/brand_icon_large_wob.png" /></a>
    </div>
    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li {{!'class="active"' if src == "lapstat" else ""}}><a href="{{!rootpage}}lapstat">Lap Times</a></li>
        <li {{!'class="active"' if src == "sesstat" else ""}}><a href="{{!rootpage}}sessionstat">Sessions</a></li>
        <li {{!'class="active"' if src == "players" else ""}}><a href="{{!rootpage}}players">Drivers</a></li>
% if not features['pts'] or 'server' in curr_url:
        <li {{!'class="active"' if src == "cs"      else ""}}><a href="{{!rootpage}}championship">Championships</a></li>
% end
        <li {{!'class="active"' if src == "stats"   else ""}}><a href="{{!rootpage}}statistics">Statistics</a></li>
% if not features['pts']:
        <li {{!'class="active"' if src == "livemap" else ""}}><a href="{{!rootpage}}livemap">Live Map</a></li>
% end
% admin = features['admin']
% banlist = features['banlist']
% if not admin is None and admin:
%   if banlist:
        <li {{!'class="active"' if src == "banlist" else ""}}><a href="{{!rootpage}}banlist">Banlist</a></li>
%   end
        <li {{!'class="active"' if src == "groups" else ""}}><a href="{{!rootpage}}groups">Groups</a></li>
        <li {{!'class="active"' if src == "admin"  else ""}}><a href="{{!rootpage}}general_admin">General Admin</a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Logs <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="{{!rootpage}}log">Stracker log</a></li>
            <li><a href="{{!rootpage}}chatlog">Chat log</a></li>
          </ul>
        </li>
% end
      </ul>
      <ul class="nav navbar-nav navbar-right">
% if not admin is None and admin:
%       user_url = curr_url
%       if user_url.startswith("/admin"):
%          user_url = user_url[len("/admin"):]
%       end
        <li><a href="{{!user_url}}">User Area</a></li>
% elif not admin is None and not admin:
        <li><a href="{{!"/admin%s" % curr_url}}">Admin Area</a></li>
% end
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>




  {{!base}}




<nav class="navbar navbar-{{!navbar_style}} navbar-fixed-bottom">
    <div class="container-fluid">
       <div class="col-sm-3">
       </div>

        <div style="text-align:center" class="col-sm-6">
% if not pagination is None:
%    page = pagination[0]
%    totalPages = pagination[1]
% import re
% def link_to_page(p):
%    nopage_url = re.sub(r"([?&])page=[^?&]*([?&])?", r"\g<1>", curr_url)
%    if not '?' in nopage_url:
%        nopage_url += "?"
%    elif not nopage_url[-1] in ['?', '&']:
%        nopage_url += "&"
%    end
%    res = nopage_url + ("page=%d" % p)
%    return res
% end
% def class_of_page(p, cp):
%    if p < 0 or p >= totalPages:
%        return 'class="disabled"'
%    elif p == cp:
%        return 'class="active"'
%    else:
%        return ''
%    end
% end
% def displayed_pages(cp):
%    minp = max(0,cp-2)
%    maxp = min(minp+4,totalPages-1)
%    minp = max(0,maxp-4)
%    return range(minp, maxp+1)
% end
                <ul class="pagination pagination-sm">
                    <li><a href="{{!link_to_page(0)}}"><span class="glyphicon glyphicon-fast-backward"></span></a></li>
                    <li {{!class_of_page(page-1,page)}}><a href="{{!link_to_page(page-1)}}"><span class="glyphicon glyphicon-backward"></span></a></li>
% for p in displayed_pages(page):
                    <li {{!class_of_page(p,page)}}><a href="{{!link_to_page(p)}}">{{"%d" % (p+1)}}</a></li>
% end
                    <li {{!class_of_page(page+1,page)}}><a href="{{!link_to_page(page+1)}}"><span class="glyphicon glyphicon-forward"></span></a></li>
                    <li><a href="{{!link_to_page(totalPages-1)}}"><span class="glyphicon glyphicon-fast-forward"></span></a></li>
                </ul>
% end
        </div>
        <div class="col-sm-3">
                <p class="navbar-text navbar-right">
                   {{"v"+features['version']}} provided by <b>Neys</b>
                </p>
        </ul>
    </div>
</nav>
<!--</div>-->
</body>

<!-- Initialize the multiselect plugin: -->
<script type="text/javascript">
$(document).ready(function() {
    $('.multiselect').multiselect({
        buttonWidth: '100%',
        includeSelectAllOption: true,
        enableFiltering: true,
        enableCaseInsensitiveFiltering: true,
        maxHeight: 350
    });
});
</script>

<!-- Support clickable table rows -->
<script type="text/javascript">
jQuery(document).ready(function($) {
      $(".clickableRow td:not(.noclick)").click(function() {
            var tr = $(this).context.parentElement;
            window.document.location = $(tr).attr("href");
      });
});
</script>

<!-- Initialize the datepicker plugin -->
<script type="text/javascript">
$('.datepicker').datepicker()
</script>
</html>
""")
