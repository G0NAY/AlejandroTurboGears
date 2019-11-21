# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1574363967.43617
_enable_loop = True
_template_filename = '/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/courses/courses.mak'
_template_uri = '/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/courses/courses.mak'
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
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<html lang="en">\n<head>\n<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>\n  <script src="//cdn.jsdelivr.net/free-jqgrid/4.8.0/js/i18n/grid.locale-es.js"></script>\n  <script src="//cdn.jsdelivr.net/free-jqgrid/4.8.0/js/jquery.jqgrid.min.js"></script>\n  <link rel="stylesheet" href="//cdn.jsdelivr.net/free-jqgrid/4.8.0/css/ui.jqgrid.css">\n\n  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">\n  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">\n  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>\n\n  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>\n  <link rel="stylesheet" type="text/css" media="screen" href="')
        __M_writer(escape(tg.url('/css/dot-luv/jquery-ui.css')))
        __M_writer('" />\n    <meta charset="utf-8" />\n    <title>jqGrid Loading Data - Million Rows from a REST service</title>\n</head>\n<body>\n\n<table style="width:100%;overflow:auto;">\n    <table id="jqGridTableCourses" class="scroll" cellpadding="0" cellspacing="0"></table>\n    <div id="listPagerTablesCourses" class="scroll" style="text-align:center;"></div>\n    <div id="listPsetcolsCourses" class="scroll" style="text-align:center;"></div>\n</table>\n<script type="text/javascript">\n        $(document).ready(\n        function () {\n            var grid_name_course= \'#jqGridTableCourses\';\n            var grid_pager_course= \'#listPagerTablesCourses\';\n            var update_url_course=\'/courses/updateCourses\';\n            var load_url_course=\'/courses/loadCourses/\';\n            var header_container_course=\'Registro de Cursos\';\n            var addParams_course = {left: 0,width: window.innerWidth-400,top: 20,height: 250,url: update_url_course, closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}\n            var editParams_course = {left: 0,width: window.innerWidth-400,top: 20,height: 250,url: update_url_course,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,\n                    width: "500",\n                    editfunc: function (rowid) {\n                    alert(\'The "Edit" button was clicked with rowid=\' + rowid);\n                    }\n                };\n            var deleteParams_course = {left: 0,width: window.innerWidth-500,top: 20,height: 130,url: update_url_course,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}\n            var viewParams_course = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url_course,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}\n            var searchParams_course = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url_course,modal: true, };\n            var grid_course = jQuery(grid_name_course);\n            grid_course.jqGrid({\n                url: load_url_course,\n                datatype: \'json\',\n                mtype: \'GET\',\n                colNames: [\'ID de Curso\', \'Registro\',\'Nombre\'],\n                colModel: [\n                    {name: \'course_id\',index: \'course_id\', width: 5,align: \'left\',key:true,hidden: true, editable: true,edittype: \'text\',editrules: {required: false}},\n                    {name: \'code\',index: \'code\', width: 30, align: \'right\',hidden: false,editable: true, edittype: \'text\',editrules: {required: false}},\n                    {name: \'name\',index: \'name\', width: 30, align: \'right\',hidden: false,editable: true, edittype: \'text\',editrules: {required: false}},\n\n                ],\n                pager: jQuery(grid_pager_course),\n                rowNum: 10,\n                rowList: [10, 50, 100],\n                sortname: \'course_id\',\n                sortorder: "desc",\n                autowidth: true,\n                shrinkToFit: true,\n                viewrecords: true,\n                height: 150,\n                caption: header_container_course,\n                ondblClickRow: function(rowId) {\n                    closeVenusActivity(rowId);\n                }\n            });\n            grid_course.jqGrid(\'navGrid\',grid_pager_course,{edit:true,add:true,del:true, search:true},\n                            editParams_course,\n                            addParams_course,\n                            deleteParams_course,\n                            searchParams_course,\n                            viewParams_course);\n\n\n\n        });\n        $.extend($.jgrid.nav,{alerttop:1});\n</script>\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/courses/courses.mak", "uri": "/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/courses/courses.mak", "source_encoding": "utf-8", "line_map": {"28": 0, "34": 1, "35": 14, "36": 14, "42": 36}}
__M_END_METADATA
"""
