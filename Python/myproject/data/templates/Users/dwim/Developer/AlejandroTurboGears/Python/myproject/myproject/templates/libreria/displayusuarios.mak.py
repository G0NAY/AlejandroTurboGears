# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1574208778.544718
_enable_loop = True
_template_filename = '/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/displayusuarios.mak'
_template_uri = '/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/displayusuarios.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<html lang="en">\n<head>\n<body>\n    <table style="width:100%;overflow:auto;">\n    <table id="jqGridTableUsuarios" class="scroll" cellpadding="0" cellspacing="0"></table>\n    <div id="listPagerTablesUsuarios" class="scroll" style="text-align:center;"></div>\n    <div id="listPsetcolsUsuarios" class="scroll" style="text-align:center;"></div>\n    </table>\n<script type="text/javascript">\n        $(document).ready(\n        function () {\n            var grid_name_usuarios= \'#jqGridTableUsuarios\';\n            var grid_pager_usuarios= \'#listPagerTablesUsuarios\';\n            var update_url_usuarios=\'/libreria/updateUsuarios\';\n            var load_url_usuarios=\'/libreria/loadUsuario/\';\n            var header_container_usuarios=\'Registro de Usuarios\';\n            var addParams_usuarios = {left: 0,width: window.innerWidth-400,top: 20,height: 250,url: update_url_usuarios, closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}\n            var editParams_usuarios = {left: 0,width: window.innerWidth-400,top: 20,height: 250,url: update_url_usuarios,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,\n                    width: "500",\n                    editfunc: function (rowid) {\n                    alert(\'The "Edit" button was clicked with rowid=\' + rowid);\n                    }\n                };\n            var deleteParams_usuarios = {left: 0,width: window.innerWidth-500,top: 20,height: 130,url: update_url_usuarios,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}\n            var viewParams_usuarios = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url_usuarios,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}\n            var searchParams_usuarios = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url_usuarios,modal: true, };\n            var grid_usuarios = jQuery(grid_name_usuarios);\n            grid_usuarios.jqGrid({\n                url: load_url_usuarios,\n                datatype: \'json\',\n                mtype: \'GET\',\n                colNames: [\'Num_Usuario\', \'Nombre\',\'Edad\',\'Telefono\',\'Email\',\'Fecha de ingreso\'],\n                colModel: [\n                    {name: \'usuario_id\',index: \'usuario_id\', width: 5,align: \'left\',key:true,hidden: true, editable: true,edittype: \'text\',editrules: {required: false}},\n                    {name: \'name\',index: \'name\', width: 30, align: \'right\',hidden: false,editable: true, edittype: \'text\',editrules: {required: false}},\n                    {name: \'age\',index: \'age\', width: 30, align: \'right\',hidden: false,editable: true, edittype: \'text\',editrules: {required: false}},\n                    {name: \'phone\',index: \'phone\', width: 30, align: \'right\',hidden: false,editable: true, edittype: \'text\',editrules: {required: false}},\n                    {name: \'email_address\',index: \'email_address\', width: 30, align: \'right\',hidden: false,editable: true, edittype: \'text\',editrules: {required: false}},\n                    {name: \'created\',index: \'created\', width: 30, align: \'right\',hidden: false,editable: true, edittype: \'text\',editrules: {required: false}},\n\n                ],\n                pager: jQuery(grid_pager_usuarios),\n                rowNum: 10,\n                rowList: [10, 50, 100],\n                sortname: \'name\',\n                sortorder: "desc",\n                autowidth: true,\n                shrinkToFit: true,\n                viewrecords: true,\n                height: 150,\n                caption: header_container_usuarios,\n            });\n            grid_usuarios.jqGrid(\'navGrid\',grid_pager_usuarios,{edit:false,add:false,del:false, search:false},\n                            editParams_usuarios,\n                            addParams_usuarios,\n                            deleteParams_usuarios,\n                            searchParams_usuarios,\n                            viewParams_usuarios);\n        });\n        $.extend($.jgrid.nav,{alerttop:1});\n\n    </script>\n</body>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/displayusuarios.mak", "uri": "/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/displayusuarios.mak", "source_encoding": "utf-8", "line_map": {"17": 0, "22": 1, "28": 22}}
__M_END_METADATA
"""
