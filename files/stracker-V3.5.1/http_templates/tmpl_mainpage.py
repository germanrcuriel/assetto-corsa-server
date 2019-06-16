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

mainPageTemplate = SimpleTemplate("""
<div class="container">
    <div class="row page-header">
        <div class="col-md-6"><img src="/img/banner.png" title="Logo Track" class="ACimg">
        </div>
        <div class="col-md-6">
        </div>
    </div>
    <div class="row">
        <div class="col-md-12">
            <h1>Welcome to the stracker statistics query</h1>
            <h2>What is stracker</h2>
            <p><i>stracker</i> is a service supporting Assetto Corsa servers with automatically
               generated statistics.</p>
            <h2>Prerequisites</h2>
            <p>While <i>stracker</i> works as a standalone server-side application,
            Assetto Corsa drivers are encouraged to use the app <i>ptracker</i> which
               offers the following benefits:
                <ul>
                    <li>in-game access to the most important statistics pages</li>
                    <li>sending setups between drivers</li>
                    <li>automaticall save personal best setups</li>
                    <li>optional leaderboard display with various delta methods</li>
                    <li>optional live delta display to your fastest lap or any stored lap in the server</li>
                    <li>optional display of <i>stracker</i> messages</li>
                    <li>send detailed lap information to <i>stracker</i></li>
                </ul>
            </p>
            <h2>Project homepages</h2>
            <p><a href="http://n-e-y-s.de">ptracker and stracker homepage</a><br>
               <a href="http://n-e-y-s.de/ptracker_doc">ptracker documentation and FAQ</a><br>
               <a href="http://n-e-y-s.de/stracker_doc">stracker documentation and FAQ</a></p>
        </div>
    </div>
</div>
""")

