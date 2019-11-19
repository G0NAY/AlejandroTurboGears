# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1573580021.687053
_enable_loop = True
_template_filename = '/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/displayloantemplate.mak'
_template_uri = '/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/displayloantemplate.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        loanid = context.get('loanid', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<html lang="en">\n<head>\n<body>\n    <table style="width:100%;overflow:auto;">\n    <table id="jgGridLoans" class="scroll" cellpadding="0" cellspacing="0"></table>\n    <div id="listPagerLoans" class="scroll" style="text-align:center;"></div>\n    <div id="listPsetcols" class="scroll" style="text-align:center;"></div>\n    <div id="dialogLoanWindow"  title="Add a Loan"></div>\n    </table>\n    <script type="text/javascript">\n        $(document).ready(\n        function () {\n            var grid_name = \'#jgGridLoans\';\n            var grid_pager= \'#listPagerLoans\';\n            var load_url=\'/loadjqgridloans?loanid=')
        __M_writer(escape(loanid))
        __M_writer('\';\n            var header_container=\'Deudas\';\n            var grid = jQuery(grid_name);\n            grid.jqGrid({\n                url: load_url,\n                datatype: \'json\',\n                mtype: \'GET\',\n                colNames: [\'id\', \'Amount\',\'DueDate\'],\n                                colModel: [\n                    {name: \'id\',index: \'id\', width: 5,align: \'left\',key:true,hidden: true, editable: true,edittype: \'text\',editrules: {required: false}},\n                    {name: \'amount\',index: \'amount\', width: 25, align: \'right\', hidden: false, editable: true, edittype: \'text\',editrules: {required: false}},\n                    {name: \'due_date\',index: \'due_date\', width: 5, align: \'right\',hidden: false,editable: true, edittype: \'text\',editrules: {required: false}},\n\n                ],\n                pager: jQuery(grid_pager),\n                rowNum: 10,\n                rowList: [10, 50, 100],\n                sortname: \'due_date\',\n                sortorder: "asc",\n                viewrecords: true,\n                autowidth: true,\n                height: 250,\n                ondblClickRow: function(rowId) {\n                    doDoubleClick(rowId)\n                },\n                caption: header_container,\n            });\n\n        });\n        $.extend($.jgrid.nav,{alerttop:1});\n\n    </script>\n</body>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/displayloantemplate.mak", "uri": "/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/displayloantemplate.mak", "source_encoding": "utf-8", "line_map": {"17": 0, "23": 1, "24": 15, "25": 15, "31": 25}}
__M_END_METADATA
"""
