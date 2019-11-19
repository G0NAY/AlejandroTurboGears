# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1572884039.645152
_enable_loop = True
_template_filename = '/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/jqgrid.mak'
_template_uri = '/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/jqgrid.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'local:templates.master', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n<html lang="en">\n<head>\n<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>\n  <script src="//cdn.jsdelivr.net/free-jqgrid/4.8.0/js/i18n/grid.locale-es.js"></script>\n  <script src="//cdn.jsdelivr.net/free-jqgrid/4.8.0/js/jquery.jqgrid.min.js"></script>\n  <link rel="stylesheet" href="//cdn.jsdelivr.net/free-jqgrid/4.8.0/css/ui.jqgrid.css">\n\n  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">\n  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">\n  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>\n\n  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>\n  <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/themes/redmond/jquery-ui.css" type="text/css"/>\n    <meta charset="utf-8" />\n    <title>jqGrid Loading Data - Million Rows from a REST service</title>\n</head>\n<body>\n    <table style="width:100%;overflow:auto;">\n    <table id="jqGridTable" class="scroll" cellpadding="0" cellspacing="0"></table>\n    <div id="listPagerTables" class="scroll" style="text-align:center;"></div>\n    <div id="listPsetcols" class="scroll" style="text-align:center;"></div>\n    </table>\n<script type="text/javascript">\n        $(document).ready(\n        function () {\n            var grid_name = \'#jqGridTable\';\n            var grid_pager= \'#listPagerTables\';\n            var update_url=\'/updateTest2\';\n            var load_url=\'/loadTest2/\';\n            var header_container=\'Test 2\';\n            var addParams = {left: 0,width: window.innerWidth-600,top: 20,height: 200,url: update_url, closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}\n            var editParams = {left: 0,width: window.innerWidth-400,top: 20,height: 200,url: update_url,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,\n                    width: "500",\n                    editfunc: function (rowid) {\n                    alert(\'The "Edit" button was clicked with rowid=\' + rowid);\n                    }\n                };\n            var deleteParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}\n            var viewParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}\n            var searchParams = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url,modal: true, };\n            var grid = jQuery(grid_name);\n            grid.jqGrid({\n                url: load_url,\n                datatype: \'json\',\n                mtype: \'GET\',\n                colNames: [\'id\', \'imei\',\'ticket\',\'nombre\'],\n                colModel: [\n                    {name: \'id\',index: \'id\', width: 5,align: \'left\',key:true,hidden: true, editable: true,edittype: \'text\',editrules: {required: false}},\n                    {name: \'imei\',index: \'imei\', width: 30, align: \'right\',hidden: false,editable: true, edittype: \'text\',editrules: {required: false}},\n                    {name: \'ticket\',index: \'ticket\', width: 30, align: \'right\',hidden: false,editable: true, edittype: \'text\',editrules: {required: false}},\n                    {name: \'name\',index: \'name\', width: 30, align: \'right\',hidden: false,editable: true, edittype: \'text\',editrules: {required: false}},\n                ],\n                pager: jQuery(grid_pager),\n                rowNum: 10,\n                rowList: [10, 50, 100],\n                sortname: \'imei\',\n                sortorder: "desc",\n                autowidth: true,\n                shrinkToFit: true,\n                viewrecords: true,\n                height: 250,\n                caption: header_container,\n\n            });\n            grid.jqGrid(\'navGrid\',grid_pager,{edit:true,add:true,del:true, search:true},\n                            editParams,\n                            addParams,\n                            deleteParams,\n                            searchParams,\n                            viewParams);\n        });\n        $.extend($.jgrid.nav,{alerttop:1});\n    </script>\n\n\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/jqgrid.mak", "uri": "/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/jqgrid.mak", "source_encoding": "utf-8", "line_map": {"28": 0, "33": 1, "39": 33}}
__M_END_METADATA
"""
