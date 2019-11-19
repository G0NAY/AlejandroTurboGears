# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1573250391.608309
_enable_loop = True
_template_filename = '/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/displayusuarios.mak'
_template_uri = '/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/displayusuarios.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<html lang="en">\n<head>\n<body>\n    <table style="width:100%;overflow:auto;">\n    <table id="jqGridTableUsuario" class="scroll" cellpadding="0" cellspacing="0"></table>\n    <div id="listPagerTablesUsuario" class="scroll" style="text-align:center;"></div>\n    <div id="listPsetcolsUsuario" class="scroll" style="text-align:center;"></div>\n    </table>\n    <script type="text/javascript">\n        $(document).ready(\n        function () {\n            var grid_name_usuario= \'#jqGridTableUsuario\';\n            var grid_pager_usuario= \'#listPagerTablesUsuario\';\n            var load_url_usuario=\'/loadUsuario/\';\n            var header_container_usuario=\'Usuarios\';\n            var grid_usuario = jQuery(grid_name_usuario);\n            grid_usuario.jqGrid({\n                url: load_url_usuario,\n                datatype: \'json\',\n                mtype: \'GET\',\n                colNames: [\'Num_Usuario\', \'Nombre\',\'Edad\',\'Telefono\',\'Email\',\'Fecha de ingreso\'],\n                colModel: [\n                    {name: \'usuario_id\',index: \'usuario_id\', width: 5,align: \'left\',key:true,hidden: true, editable: true,edittype: \'text\',editrules: {required: false}},\n                    {name: \'name\',index: \'name\', width: 30, align: \'right\',hidden: false,editable: true, edittype: \'text\',editrules: {required: false}},\n                    {name: \'age\',index: \'age\', width: 30, align: \'right\',hidden: false,editable: true, edittype: \'text\',editrules: {required: false}},\n                    {name: \'phone\',index: \'phone\', width: 30, align: \'right\',hidden: false,editable: true, edittype: \'text\',editrules: {required: false}},\n                    {name: \'email_address\',index: \'email_address\', width: 30, align: \'right\',hidden: false,editable: true, edittype: \'text\',editrules: {required: false}},\n                    {name: \'created\',index: \'created\', width: 30, align: \'right\',hidden: false,editable: true, edittype: \'text\',editrules: {required: false}},\n\n                ],\n                pager: jQuery(grid_pager_usuario),\n                rowNum: 10,\n                rowList: [10, 50, 100],\n                sortname: \'name\',\n                sortorder: "desc",\n                autowidth: true,\n                shrinkToFit: true,\n                viewrecords: true,\n                height: 150,\n                caption: header_container_usuario,\n\n            });\n        });\n        $.extend($.jgrid.nav,{alerttop:1});\n\n    </script>\n</body>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/displayusuarios.mak", "uri": "/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/displayusuarios.mak", "source_encoding": "utf-8", "line_map": {"17": 0, "22": 1, "28": 22}}
__M_END_METADATA
"""
