# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1574787165.488443
_enable_loop = True
_template_filename = '/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/displaybooks.mak'
_template_uri = '/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/displaybooks.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<html lang="en">\n<head></head>\n<body>\n    <table style="width:100%;overflow:auto;">\n    <table id="jqGridTableBooks" class="scroll" cellpadding="0" cellspacing="0"></table>\n    <div id="listPagerTablesBooks" class="scroll" style="text-align:center;"></div>\n    <div id="listPsetcolsBooks" class="scroll" style="text-align:center;"></div>\n    </table>\n    <script type="text/javascript">\n        $(document).ready(\n        function () {\n            var grid_name_books= \'#jqGridTableBooks\';\n            var grid_pager_books= \'#listPagerTablesBooks\';\n            var update_url_books=\'/libreria/updateBook\';\n            var load_url_books=\'/libreria/loadBook/\';\n            var header_container_books=\'Lista de Libros\';\n            var viewParams_books = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url_books,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}\n            var searchParams_books = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url_books,modal: true, };\n            var grid_books = jQuery(grid_name_books);\n            grid_books.jqGrid({\n                url: load_url_books,\n                datatype: \'json\',\n                mtype: \'GET\',\n                colNames: [\'Num_Libro\', \'Nombre de Libro\', \'Fecha de Publicación\', \'Fecha de registro\', \'Autor\'],\n                colModel: [\n                    {\n                        name: \'book_id\',\n                        index: \'book_id\',\n                        width: 5,\n                        align: \'left\',\n                        key: true,\n                        hidden: true,\n                        editable: true,\n                        edittype: \'text\',\n                        editrules: {required: false}\n                    },\n                    {\n                        name: \'book_name\',\n                        index: \'book_name\',\n                        width: 30,\n                        align: \'right\',\n                        hidden: false,\n                        editable: true,\n                        edittype: \'text\',\n                        editrules: {required: false}\n                    },\n                    {\n                        name: \'publication_date\',\n                        index: \'publication_date\',\n                        width: 30,\n                        align: \'right\',\n                        hidden: false,\n                        editable: true,\n                        edittype: \'text\',\n                        editrules: {required: false}\n                    },\n                    {\n                        name: \'created\',\n                        index: \'created\',\n                        width: 30,\n                        align: \'right\',\n                        hidden: false,\n                        editable: true,\n                        edittype: \'text\',\n                        editrules: {required: false}\n                    },\n                    {\n                        name: \'author_id\',\n                        index: \'author_id\',\n                        width: 30,\n                        align: \'right\',\n                        hidden: false,\n                        editable: true,\n                        edittype: \'text\',\n                        editrules: {required: false}\n                    },\n                ],\n                pager: jQuery(grid_pager_books),\n                rowNum: 10,\n                rowList: [10, 50, 100],\n                sortname: \'book_name\',\n                sortorder: "desc",\n                autowidth: true,\n                shrinkToFit: true,\n                viewrecords: true,\n                height: 150,\n                caption: header_container_books,\n            });\n            grid_books.jqGrid(\'navGrid\',grid_pager_books,{edit:false,add:false,del:false, search:false},\n                            searchParams_books,\n                            viewParams_books);\n        });\n        $.extend($.jgrid.nav,{alerttop:1});\n\n    </script>\n</body>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/displaybooks.mak", "uri": "/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/libreria/displaybooks.mak", "source_encoding": "utf-8", "line_map": {"17": 0, "22": 1, "28": 22}}
__M_END_METADATA
"""
