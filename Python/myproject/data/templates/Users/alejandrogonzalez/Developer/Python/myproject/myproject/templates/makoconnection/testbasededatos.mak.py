# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1573242611.5938492
_enable_loop = True
_template_filename = '/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/testbasededatos.mak'
_template_uri = '/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/testbasededatos.mak'
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
        _ = context.get('_', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<html lang="en">\n<head>\n<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>\n  <script src="//cdn.jsdelivr.net/free-jqgrid/4.8.0/js/i18n/grid.locale-es.js"></script>\n  <script src="//cdn.jsdelivr.net/free-jqgrid/4.8.0/js/jquery.jqgrid.min.js"></script>\n  <link rel="stylesheet" href="//cdn.jsdelivr.net/free-jqgrid/4.8.0/css/ui.jqgrid.css">\n\n  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">\n  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">\n  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>\n\n  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>\n  <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/themes/redmond/jquery-ui.css" type="text/css"/>\n    <meta charset="utf-8" />\n    <title>jqGrid Loading Data - Million Rows from a REST service</title>\n</head>\n<body>\n<div id="dialogActivityVenus4" title="')
        __M_writer(escape(_('Close Activity')))
        __M_writer('"></div>\n\n    <table id="jqGrid"></table>\n    <div id="jqGridPager"></div>\n    <div id="dialogForm01"  title="Display Prestamos">\n    </table>\n</div>\n\n <script type="text/javascript">\nfunction OpenVenusActivity(rowID) {\n        $.ajax({\n            type: "GET",\n            url: \'')
        __M_writer(escape(h.url()))
        __M_writer('/openClose?id=\'+rowID,\n            contentType: "application/json; charset=utf-8",\n            data: { },\n            success: function(parameterdata) {\n                //Insert HTML code\n                $( "#dialogActivityVenus4" ).html(parameterdata.dialogtemplate);\n                $("#dialogActivityVenus4").show();\n            },\n            error: function() {\n                $.alert("')
        __M_writer(escape(_('Error accessing server')))
        __M_writer(' /ticket/openClose",{type: "danger"});\n            },\n            complete: function() {\n            }\n        });\n\n        var ContDialog = $( "#dialogActivityVenus4" ).dialog({\n            autoOpen: false,\n            height: Math.round(window.innerHeight*.6),\n            width: Math.round(window.innerWidth*.6),\n            modal: true,\n            title: "')
        __M_writer(escape(_('Registros de usuario')))
        __M_writer('",\n            dialogClass: "noclose",\n            closeOnEscape: false,\n            buttons: {\n                "')
        __M_writer(escape(_('Salir')))
        __M_writer('": function() {\n                    $(\'#dialogActivityVenus4\').html("");\n                    ContDialog.dialog( "close" );\n                },\n            },\n            close: function() {\n            }\n        });\n        ContDialog.dialog( "open" );\n    }\n        $(document).ready(\n            function () {\n\n            $("#jqGrid").jqGrid({\n                url: "')
        __M_writer(escape(tg.url('/tablaBaseConec')))
        __M_writer('",\n                datatype: "json",\n                colNames: [\'Usuario\', \'Libro\'],\n                colModel: [\n                    { name: \'usuario_id\', index :\'usuario_id\', width: 250 },\n                    { name: \'book_id\', index :\'book_id\',width: 250 },\n                ],\n\t\t\t\tviewrecords: true,\n                height: 250,\n                rowNum: 20,\n                pager: "#jqGridPager",\n                caption: "Prestamos"\n            });\n            jQuery("#jqGrid").jqGrid(\'navGrid\',\'#jqGridPager\',{edit:false,add:false,del:false});\n\n\n            jQuery("#jqGrid").navButtonAdd(\'#jqGridPager\',\n                {\n                    buttonicon: "ui-icon-circle-plus",\n                    title: "')
        __M_writer(escape(_('Plus')))
        __M_writer('",\n                    caption: "')
        __M_writer(escape(_('Plus')))
        __M_writer('",\n                    position: "first",\n                    onClickButton: function(){\n                        displayPrestamo();\n                    }\n                });\n        });\n\nfunction  displayPrestamo() {\n    // Create Dialog\n                 var winHeight=Math.round(window.innerHeight*.75)\n                 var winWidth=Math.round(window.innerWidth*.86)\n                 var Dialog01 = $( "#dialogForm01" ).dialog({\n                        autoOpen: false,\n                        height: winHeight-100,\n                        width: winWidth-200,\n                        modal: true,\n                        close: function() {\n                            $(\'#prestamoForm\')[0].reset();\n                            //form[ 0 ].reset();\n                            //allFields.removeClass( "ui-state-error" );\n                        }\n                 });\n                 $.ajax({\n                    type: "GET",\n                    url: "')
        __M_writer(escape(tg.url('/prestamosTemplate')))
        __M_writer('",\n                    contentType: "application/json; charset=utf-8",\n                    data: { \'param\':\'gaugeParameters\' },\n                    success: function(parameterdata) {\n                        //Insert HTML code\n                        $( "#dialogForm01" ).html(parameterdata.prestamostemplate);\n                        $( "#dialogForm01" ).show();\n                        Dialog01.dialog( "open" );\n                    },\n                    error: function() {\n                        alert("Error accessing server /prestamostemplate")\n                    },\n                    complete: function() {\n                    }\n                 });\n\n        }\n   </script>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/testbasededatos.mak", "uri": "/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/testbasededatos.mak", "source_encoding": "utf-8", "line_map": {"28": 0, "36": 1, "37": 19, "38": 19, "39": 31, "40": 31, "41": 40, "42": 40, "43": 51, "44": 51, "45": 55, "46": 55, "47": 69, "48": 69, "49": 88, "50": 88, "51": 89, "52": 89, "53": 114, "54": 114, "60": 54}}
__M_END_METADATA
"""
