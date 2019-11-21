# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1574208777.635705
_enable_loop = True
_template_filename = '/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/prestamostemplate.mak'
_template_uri = '/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/prestamostemplate.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _ = context.get('_', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<script>\n    function agregaUsuario() {\n\n                    var rowId =$("#jqGridTableUsuarios").jqGrid(\'getGridParam\',\'selrow\');\n                    var rowData = jQuery("#jqGridTableUsuarios").getRowData(rowId);\n                    var rowNameUser = rowData[\'name\'];\n                    var usuario_id= rowData[\'usuario_id\'];\n\n                    if (!rowId){\n                      alert("Select a row")\n                    }\n                      else {\n                      <!--alert(\'{\' + \'usuario_id:\' + usuario_id +\',\'+\'name:\' + rowName +\'}\');-->\n                      document.getElementById("usuarios").value = rowNameUser;\n                      document.getElementById("usuarios_id").value = usuario_id;\n                    }\n\n    }\n    function agregaLibro() {\n                    var rowId = $("#jqGridTableBooks").jqGrid(\'getGridParam\', \'selrow\');\n                    var rowData = jQuery("#jqGridTableBooks").getRowData(rowId);\n                    var rowNameBook = rowData[\'book_name\'];\n                    var book_id = rowData[\'book_id\'];\n\n                    if (!rowId){\n                      alert("Select a row")\n                    }\n                      else {\n                      <!--alert(\'book_id:\'+book_id +\',\'+\'book_name:\' + rowName);-->\n\n                      document.getElementById("libros").value = rowNameBook;\n                      document.getElementById("libros_id").value = book_id;\n                    }\n\n    }\n\nfunction  displayUsuarios() {\n                var winHeight=Math.round(window.innerHeight*.75)\n                var winWidth=Math.round(window.innerWidth*.86)\n                // Create Dialog\n                var Dialog02 = $( "#dialoForm02" ).dialog({\n                        autoOpen: false,\n                        height: winHeight-100,\n                        width: winWidth-200,\n                        modal: true,\n                        title: "')
        __M_writer(escape(_('Agregar Usuario')))
        __M_writer('",\n                        buttons: {\n                            "')
        __M_writer(escape(_('Agregar')))
        __M_writer('": function () {\n                              agregaUsuario();\n                              $(\'#dialogActivityVenus4\').html("");\n                                Dialog02.dialog( "close" );\n                            },\n                        },\n                        close: function() {\n                        }\n                 });\n                $.ajax({\n                    type: "GET",\n                    url: "')
        __M_writer(escape(tg.url('/libreria/displayUsuarios')))
        __M_writer('",\n                    contentType: "application/json; charset=utf-8",\n                    data: { \'param\':\'gaugeParameters\'},\n                    success: function(parameterdata) {\n                        //Insert HTML code\n                        $( "#dialoForm02" ).html(parameterdata.displayusuarios);\n                        Dialog02.data(\'rowId\',1);\n                        Dialog02.dialog( "open" );\n                    },\n                    error: function() {\n                        alert("Error accessing server /libreria/displayusuarios")\n                    },\n                    complete: function() {\n                    }\n                 });\n        }\n\nfunction displayLibros() {\n                var winHeight=Math.round(window.innerHeight*.75)\n                var winWidth=Math.round(window.innerWidth*.86)\n                // Create Dialog\n                var Dialog03 = $( "#dialoForm03" ).dialog({\n                        autoOpen: false,\n                        height: winHeight-100,\n                        width: winWidth-200,\n                        modal: true,\n                        title: "')
        __M_writer(escape(_('Agregar Libro')))
        __M_writer('",\n                        dialogClass: "noclose",\n                        closeOnEscape: false,\n                        close: function() {\n                        },\n                        buttons: {\n                            "')
        __M_writer(escape(_('Agregar')))
        __M_writer('": function () {\n                                agregaLibro();\n                                $(\'#dialogActivityVenus4\').html("");\n                                Dialog03.dialog( "close" );\n                            },\n                        },\n                 });\n                $.ajax({\n                    type: "GET",\n                    url: "')
        __M_writer(escape(tg.url('/libreria/displayBooks')))
        __M_writer('",\n                    contentType: "application/json; charset=utf-8",\n                    data: { \'param\':\'gaugeParameters\'},\n                    success: function(parameterdata) {\n                        //Insert HTML code\n                        $( "#dialoForm03" ).html(parameterdata.displaybooks);\n                        Dialog03.data(\'rowId\',1);\n                        Dialog03.dialog( "open" );\n                    },\n                    error: function() {\n                        alert("Error accessing server /libreria/displayBooks")\n                    },\n                    complete: function() {\n                    }\n                 });\n}\n</script>\n\n<form id="prestamoForm">\n  <div class="form-group">\n    <label for="usuarios">Nombre de usuario</label>\n    <input id="usuarios" type="text" onclick="displayUsuarios()" class="form-control" name="usuario">\n    <input id="usuarios_id" type="text" name="usuarios" hidden >\n    <div id="dialoForm02"  title="Display Usuarios"></div>\n  </div>\n    <br>\n  <div class="form-group">\n    <label for="libros">Nombre de Libro</label>\n    <input id="libros" type="text" onclick="displayLibros()" class="form-control" name="libro">\n    <input id="libros_id" type="text" name="libros" hidden >\n    <div id="dialoForm03"  title="Display Libros"></div>\n  </div>\n</form>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/prestamostemplate.mak", "uri": "/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/prestamostemplate.mak", "source_encoding": "utf-8", "line_map": {"17": 0, "24": 1, "25": 46, "26": 46, "27": 48, "28": 48, "29": 59, "30": 59, "31": 85, "32": 85, "33": 91, "34": 91, "35": 100, "36": 100, "42": 36}}
__M_END_METADATA
"""
