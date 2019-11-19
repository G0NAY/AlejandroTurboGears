# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1573851129.3786151
_enable_loop = True
_template_filename = '/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/libreria/testbasededatos.mak'
_template_uri = '/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/libreria/testbasededatos.mak'
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
        h = context.get('h', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<html lang="en">\n<head>\n<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>\n  <script src="//cdn.jsdelivr.net/free-jqgrid/4.8.0/js/i18n/grid.locale-es.js"></script>\n  <script src="//cdn.jsdelivr.net/free-jqgrid/4.8.0/js/jquery.jqgrid.min.js"></script>\n  <link rel="stylesheet" href="//cdn.jsdelivr.net/free-jqgrid/4.8.0/css/ui.jqgrid.css">\n\n  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">\n  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">\n  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>\n\n  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>\n  <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/themes/redmond/jquery-ui.css" type="text/css"/>\n    <meta charset="utf-8" />\n    <title>jqGrid Loading Data - Million Rows from a REST service</title>\n</head>\n<body>\n\n<div class="h"></div>\n<div>\n\t<input type="checkbox" id="autosearch" onclick="enableAutosubmit(this.checked)"> Autobuscador <br/><br/>\n\tNombre<br />\n\t<input type="text" id="search_cd" onkeydown="doSearch(arguments[0]||event)" />\n</div>\n<div>\n\tId<br>\n\t<input type="text" id="item" onkeydown="doSearch(arguments[0]||event)" />\n\t<button onclick="gridReload()" id="submitButton" style="margin-left:30px;">Search</button>\n</div>\n\n<br />\n\n\n    <table style="width:100%;overflow:auto;">\n    <table id="jqGrid"></table>\n    <div id="jqGridPager"></div>\n    <div id="dialogForm01"  title="Agregar Prestamos"></div>\n    </table>\n\n <script type="text/javascript">\n\nvar timeoutHnd;\nvar flAuto = false;\n\nfunction doSearch(ev){\n\tif(!flAuto)\n\t\treturn;\n//\tvar elem = ev.target||ev.srcElement;\n\tif(timeoutHnd)\n\t\tclearTimeout(timeoutHnd)\n\ttimeoutHnd = setTimeout(gridReload,500)\n}\n\nfunction gridReload(){\n\tvar nm_mask = jQuery("#item_nm").val();\n\tvar cd_mask = jQuery("#search_cd").val();\n\tjQuery("#bigset").jqGrid(\'setGridParam\',{url:"bigset.php?nm_mask="+nm_mask+"&cd_mask="+cd_mask,page:1}).trigger("reloadGrid");\n}\nfunction enableAutosubmit(state){\n\tflAuto = state;\n\tjQuery("#submitButton").attr("disabled",state);\n}\n\n        $(document).ready(\n            function () {\n\n            $("#jqGrid").jqGrid({\n                url: "')
        __M_writer(escape(tg.url('/libreria/tablaBaseConec')))
        __M_writer('",\n                datatype: "json",\n                colNames: [\'Usuario\', \'Libro\'],\n                colModel: [\n                    { name: \'usuario_id\', index :\'usuario_id\', width: 250 },\n                    { name: \'book_id\', index :\'book_id\',width: 250 },\n                ],\n\t\t\t\tviewrecords: true,\n                height: 250,\n                rowNum: 20,\n                pager: "#jqGridPager",\n                caption: "Prestamos"\n            });\n            jQuery("#jqGrid").jqGrid(\'navGrid\',\'#jqGridPager\',{edit:false,add:false,del:false});\n\n\n            jQuery("#jqGrid").navButtonAdd(\'#jqGridPager\',\n                {\n                    buttonicon: "ui-icon-circle-plus",\n                    title: "')
        __M_writer(escape(_('Plus')))
        __M_writer('",\n                    caption: "')
        __M_writer(escape(_('Plus')))
        __M_writer('",\n                    position: "first",\n                    onClickButton: function(){\n                        displayPrestamo();\n                    }\n                });\n        });\n\nfunction alertaPrestamo() {\n\n                var libro = $(\'#libros\').val();\n                var libro_id = $(\'#libros_id\').val();\n                var usuario = $(\'#usuarios\').val();\n                var usuario_id = $(\'#usuarios_id\').val();\n\n                if (!libro_id || !usuario_id){\n                      alert("Llene ambos campos")\n                    }\n                else {\n                    <!--alert(usuario+usuario_id+\'\\n\'+libro + libro_id)-->\n\n                    var formData = new FormData();\n                    formData.append("usuario_id", usuario_id);\n                    formData.append("book_id", libro_id);\n\n                    var request = new XMLHttpRequest();\n                    request.open("POST", \'')
        __M_writer(escape(h.url()))
        __M_writer('/libreria/alertPrestamo\');\n                    request.send(formData);\n                }\n\n}\n\nfunction  displayPrestamo() {\n    // Create Dialog\n                 var winHeight=Math.round(window.innerHeight*.75)\n                 var winWidth=Math.round(window.innerWidth*.86)\n                 var Dialog01 = $( "#dialogForm01" ).dialog({\n                        autoOpen: false,\n                        height: winHeight-100,\n                        width: winWidth-200,\n                        modal: true,\n\n                        close: function() {\n\n                            //form[ 0 ].reset();\n                            //allFields.removeClass( "ui-state-error" );\n                        },\n                        buttons: {\n                            "')
        __M_writer(escape(_('Agregar')))
        __M_writer('": function() {\n                                alertaPrestamo();\n                                 $(\'#dialogActivityVenus4\').html("");\n                                Dialog01.dialog( "close" );\n\n                },\n             },\n                 });\n                 $.ajax({\n                    type: "GET",\n                    url: "')
        __M_writer(escape(tg.url('/libreria/prestamosTemplate')))
        __M_writer('",\n                    contentType: "application/json; charset=utf-8",\n                    data: { \'param\':\'gaugeParameters\' },\n                    success: function(parameterdata) {\n                        //Insert HTML code\n                        $( "#dialogForm01" ).html(parameterdata.prestamostemplate);\n                        $( "#dialogForm01" ).show();\n                        Dialog01.dialog( "open" );\n                    },\n                    error: function() {\n                        alert("Error accessing server /prestamostemplate")\n                    },\n                    complete: function() {\n                    }\n                 });\n\n        }\n   </script>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/libreria/testbasededatos.mak", "uri": "/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/libreria/testbasededatos.mak", "source_encoding": "utf-8", "line_map": {"28": 0, "36": 1, "37": 69, "38": 69, "39": 88, "40": 88, "41": 89, "42": 89, "43": 115, "44": 115, "45": 137, "46": 137, "47": 147, "48": 147, "54": 48}}
__M_END_METADATA
"""
