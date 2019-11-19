# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1573258265.683106
_enable_loop = True
_template_filename = '/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/prestamostemplate.mak'
_template_uri = '/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/prestamostemplate.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<script>\nfunction  displayUsuarios() {\n                var winHeight=Math.round(window.innerHeight*.75)\n                var winWidth=Math.round(window.innerWidth*.86)\n                // Create Dialog\n                var Dialog02 = $( "#dialoForm02" ).dialog({\n                        autoOpen: false,\n                        height: winHeight-100,\n                        width: winWidth-200,\n                        modal: true,\n                        close: function() {\n                        }\n                 });\n                $.ajax({\n                    type: "GET",\n                    url: "')
        __M_writer(escape(tg.url('/libreria/displayUsuarios')))
        __M_writer('",\n                    contentType: "application/json; charset=utf-8",\n                    data: { \'param\':\'gaugeParameters\'},\n                    success: function(parameterdata) {\n                        //Insert HTML code\n                        $( "#dialoForm02" ).html(parameterdata.displayusuarios);\n                        Dialog02.data(\'rowId\',1);\n                        Dialog02.dialog( "open" );\n                    },\n                    error: function() {\n                        alert("Error accessing server /libreria/displayusuarios")\n                    },\n                    complete: function() {\n                    }\n                 });\n\n        }\n\nfunction displayLibros() {\n  alert("Hemos Hecho Clic x2 n_0")\n}\n</script>\n<form id="prestamoForm">\n  <div class="form-group">\n    <label for="usuario">Nombre de usuario</label>\n    <input type="text" onclick="displayUsuarios()" class="form-control" id="usuario" name="usuario">\n    <div id="dialoForm02"  title="Display Usuarios">\n  </div>\n    <div class="form-group">\n    <label for="libro">Nombre de Libro</label>\n    <input type="text" onclick="ClicMeAgain()" class="form-control" id="libro" name="libro">\n  </div>\n</form>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/prestamostemplate.mak", "uri": "/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/prestamostemplate.mak", "source_encoding": "utf-8", "line_map": {"17": 0, "23": 1, "24": 16, "25": 16, "31": 25}}
__M_END_METADATA
"""
