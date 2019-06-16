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

generalAdminTemplate = SimpleTemplate("""
% from http_templates.tmpl_helpers import car_tmpl
<script>
function general_admin_remove(column, item)
{
    if( confirm("Do you really want to remove this item?") )
    {
        window.location = "general_admin_remove?"+column+"="+item;
    }
    return false;
}
</script>
<div class="container">
    <div class="row page-header">
        <div class="col-md-6"><img src="/img/banner.png" title="Logo Track" class="ACimg"></div>
        <div class="col-md-6">
            <div class="row">
                <div class="col-md-4 col-md-offset-8">
                    <button class="form-control btn btn-sm btn-primary" onClick="window.history.back()">
                        Back
                    </button>
                </div>
            </div>
            <br>
            <div class="row">
                <div class="col-md-12 panel panel-info">
                    <div class="panel-heading">Note</div>
                    <div class="panel-body">
                        You can add user interface data from your Assetto Corsa
                        game installation folder. This data can be used to have
                        a nicer display for cars and tracks. You have to execute
                        stracker-packager.exe on a computer with Assetto Corsa
                        installed. The output of this process is a .zip
                        file called stracker-package.zip. With the button below,
                        you can send this file to the server where the information
                        will be stored in the database.<br>
                        The process will not overwrite UI data already stored.
                        If you want data to be overwritten, remove it before
                        uploading stracker-package.zip.
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-8 col-md-offset-4">
                    <input id="syncFileUpload" type="file" class="file" data-upload-url="upload_sync_file">
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-md-6">
            <table class="table table-striped table-condensed table-bordered table-hover">
                <caption>Tracks stored in database</caption>
                <thead>
                    <tr>
                        <th>Internal name</th>
                        <th>UI name</th>
                        <th>Length</th>
                        <th>Map data</th>
                    </tr>
                </thead>
                <tbody>
% for t in res['tracks']:
                    <tr>
                        <td>
% tag = "disabled" if t['uiname'] is None and t['length'] is None and t['mapdata'] is None else "active"
                            <button type="button" class="btn btn-danger btn-xs {{!tag}}" onclick="general_admin_remove('allTrackData','{{!t['acname']}}')">
                                <span class="glyphicon glyphicon-remove"
                                      data-toggle="tooltip"
                                      title="Remove all additional UI data for this track.">
                                </span>
                            </button>
                            {{t['acname']}}
                        </td>
                        <td class="{{!"success" if t['uiname'] else "warning"}}">
% if t['uiname']:
                            {{t['uiname']}}
% else:
                            <span class="glyphicon glyphicon-minus"></span>
% end
                        </td>
                        <td class="{{!"success" if t['length'] else "warning"}}">
% if t['length']:
                            {{"%.3f km"%(t['length']*0.001)}}
% else:
                            <span class="glyphicon glyphicon-minus"></span>
% end
                        </td>
                        <td class="{{!"success" if t['mapdata'] else "warning"}}">
                            <span class="glyphicon {{!"glyphicon-ok" if t['mapdata'] else "glyphicon-minus"}}"></span>
                        </td>
                    </tr>
% end
                </tbody>
            </table>
        </div>
        <div class="col-md-6">
            <table class="table table-striped table-condensed table-bordered table-hover">
                <caption>Cars stored in database</caption>
                <thead>
                    <tr>
                        <th>Internal name</th>
                        <th>UI name</th>
                        <th>Brand</th>
                        <th>Badge</th>
                    </tr>
                </thead>
                <tbody>
% for c in res['cars']:
                    <tr>
                        <td>
% tag = "disabled" if c['uiname'] is None and c['brand'] is None and c['badge'] is None else "active"
                            <button type="button" class="btn btn-danger btn-xs {{!tag}}" onclick="general_admin_remove('allCarData','{{!c['acname']}}')">
                                <span class="glyphicon glyphicon-remove"
                                      data-toggle="tooltip"
                                      title="Remove all additional UI data for this car.">
                                </span>
                            </button>
                            {{c['acname']}}
                        </td>
                        <td class="{{!"success" if c['uiname'] else "warning"}}">
% if c['uiname']:
                            {{!car_tmpl.render(car=c['acname'], uicar=c['uiname'])}}
% else:
                            <span class="glyphicon glyphicon-minus"></span>
% end
                        </td>
                        <td class="{{!"success" if c['brand'] else "warning"}}">
% if c['brand']:
                            {{c['brand']}}
% else:
                            <span class="glyphicon glyphicon-minus"></span>
% end
                        </td>
                        <td class="{{!"success" if c['badge'] else "warning"}}">
                            <span class="glyphicon {{!"glyphicon-ok" if c['badge'] else "glyphicon-minus"}}"></span>
                        </td>
                    </tr>
% end
                </tbody>
            </table>
        </div>
    </div>
</div>
<script type="text/javascript">
$("#syncFileUpload").fileinput({'uploadUrl': 'upload_sync_file',
                                allowedFileExtensions:['zip'],
                                dropZoneEnabled:false,
                                maxFileCount:1});
$('#syncFileUpload').on('fileuploaded', function(event, data, previewId, index) {
    var form = data.form, files = data.files, extra = data.extra,
        response = data.response, reader = data.reader;
    window.location="general_admin";
});
</script>
""")

