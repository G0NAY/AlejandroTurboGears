# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1574284846.8666492
_enable_loop = True
_template_filename = '/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/makoconnection/test.mak'
_template_uri = '/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/makoconnection/test.mak'
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
        __M_writer('\n<html lang="en">\n<head>\n<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>\n  <script src="//cdn.jsdelivr.net/free-jqgrid/4.8.0/js/i18n/grid.locale-es.js"></script>\n  <script src="//cdn.jsdelivr.net/free-jqgrid/4.8.0/js/jquery.jqgrid.min.js"></script>\n  <link rel="stylesheet" href="//cdn.jsdelivr.net/free-jqgrid/4.8.0/css/ui.jqgrid.css">\n\n  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">\n  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">\n  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>\n\n  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>\n  <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/themes/redmond/jquery-ui.css" type="text/css"/>\n    <meta charset="utf-8" />\n    <title>jqGrid Loading Data - Million Rows from a REST service</title>\n</head>\n<body>\n<div style="margin-left:20px">\n    <table id="jqGrid"></table>\n    <div id="jqGridPager"></div>\n</div>\n    <script type="text/javascript">\n        $(document).ready(\n            function () {\n\n                var direccion = \'liga/carpeta\';\n\n            $("#jqGrid").jqGrid({\n                url: "http://trirand.com/blog/phpjqgrid/examples/jsonp/getjsonp.php?callback=?&qwery=longorders",\n                mtype: "GET",\n\t\t\t\tstyleUI : \'Bootstrap\',\n                datatype: "jsonp",\n                colModel: [\n                    { label: \'OrderID\', name: \'OrderID\', key: true, width: 75 },\n                    { label: \'Customer ID\', name: \'CustomerID\', width: 150 },\n                    { label: \'Order Date\', name: \'OrderDate\', width: 150 },\n                    { label: \'Freight\', name: \'Freight\', width: 150 },\n                    { label:\'Ship Name\', name: \'ShipName\', width: 150 }\n                ],\n\t\t\t\tviewrecords: true,\n                height: 250,\n                rowNum: 20,\n                pager: "#jqGridPager"\n            });\n        });\n\n   </script>\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/makoconnection/test.mak", "uri": "/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/makoconnection/test.mak", "source_encoding": "utf-8", "line_map": {"28": 0, "33": 1, "39": 33}}
__M_END_METADATA
"""
