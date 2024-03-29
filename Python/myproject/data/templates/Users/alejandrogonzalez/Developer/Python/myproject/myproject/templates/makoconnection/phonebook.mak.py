# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1573668475.839466
_enable_loop = True
_template_filename = '/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/phonebook.mak'
_template_uri = '/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/phonebook.mak'
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
        __M_writer('\n<html lang="en">\n<head>\n<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>\n  <script src="//cdn.jsdelivr.net/free-jqgrid/4.8.0/js/i18n/grid.locale-es.js"></script>\n  <script src="//cdn.jsdelivr.net/free-jqgrid/4.8.0/js/jquery.jqgrid.min.js"></script>\n  <link rel="stylesheet" href="//cdn.jsdelivr.net/free-jqgrid/4.8.0/css/ui.jqgrid.css">\n\n  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">\n  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">\n  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>\n\n  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>\n  <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/themes/redmond/jquery-ui.css" type="text/css"/>\n        <script src="')
        __M_writer(escape(tg.url('/javascript/jquery-validation-1.17.0/dist/jquery.validate.js')))
        __M_writer('"></script>\n    <meta charset="utf-8" />\n    <title>jqGrid Loading Data - Million Rows from a REST service</title>\n</head>\n<body>\n    <table style="width:100%;overflow:auto;">\n    <table id="jqGridTable" class="scroll" cellpadding="0" cellspacing="0"></table>\n    <div id="listPagerTables" class="scroll" style="text-align:center;"></div>\n    <div id="listPsetcols" class="scroll" style="text-align:center;"></div>\n    <div id="dialogForm01"  title="Add a Loan">\n    <div id="dialogForm02"  title="Display Loans">\n    </table>\n    <script type="text/javascript">\n        $(document).ready(\n        function () {\n            var grid_name = \'#jqGridTable\';\n            var grid_pager= \'#listPagerTables\';\n            var update_url=\'/updatePhoneBook\';\n            var load_url=\'/loadPhoneBook/\';\n            var header_container=\'Phone Book\';\n            var addParams = {left: 0,width: window.innerWidth-600,top: 20,height: 220,url: update_url, closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}\n            var editParams = {left: 0,width: window.innerWidth-400,top: 20,height: 220,url: update_url,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,\n                    width: "500",\n                    editfunc: function (rowid) {\n                    alert(\'The "Edit" button was clicked with rowid=\' + rowid);\n                    }\n                };\n            var deleteParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}\n            var viewParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}\n            var searchParams = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url,modal: true, };\n            var grid = jQuery(grid_name);\n            var rowKey = grid.getGridParam(\'selrow\')\n            grid.jqGrid({\n                url: load_url,\n                datatype: \'json\',\n                mtype: \'GET\',\n                colNames: [\'id\', \'Name\',\'Birthday\',\'Age\',\'Phone\'],\n                                colModel: [\n                    {name: \'id\',index: \'id\', width: 5,align: \'left\',key:true,hidden: true, editable: true,edittype: \'text\',editrules: {required: false}},\n                    {name: \'name\',index: \'name\', width: 25, align: \'right\', hidden: false, editable: true, edittype: \'text\',editrules: {required: false}},\n                    {name: \'birthday\',index: \'birthday\', formatter: \'date\', width: 10,sortable: false,align: \'right\',editable: true, editoptions: {size: 20,maxlengh: 10,\n                                            dataInit: function (element) {\n                                                $(element).datepicker({\n                                                    dateFormat: \'yy-mm-dd\',\n                                                    constrainInput: false,\n                                                    showOn: \'button\',\n                                                    buttonText: \'...\'\n                                                });\n                                            }\n                            },\n                            formatoptions: {\n                                newformat: "Y-m-d"\n                            },\n\n                    },\n                    {name: \'age\',index: \'age\', width: 5, align: \'right\',hidden: false,editable: true, edittype: \'text\',editrules: {required: false}},\n                    {name: \'phone\', index: \'phone\', width: 20,align: \'left\',hidden: false, editable: true, edittype: \'text\', editrules: {required: false}},\n\n                ],\n                pager: jQuery(grid_pager),\n                rowNum: 10,\n                rowList: [10, 50, 100],\n                sortname: \'name\',\n                sortorder: "asc",\n                viewrecords: true,\n                autowidth: true,\n                height: 250,\n                ondblClickRow: function(rowId) {\n                    displayLoans(rowId)\n                },\n                caption: header_container,\n\n            });\n            grid.jqGrid(\'navGrid\',grid_pager,{edit:true,add:true,del:true, search:true},\n                            editParams,\n                            addParams,\n                            deleteParams,\n                            searchParams,\n                            viewParams);\n             grid.navButtonAdd(grid_pager,\n                {\n                    buttonicon: "ui-icon-key",\n                    title: "Loan",\n                    caption: "Loan",\n                    position: "last",\n                    onClickButton: loanButtonClicked\n                });\n        });\n        $.extend($.jgrid.nav,{alerttop:1});\n\n        function  loanButtonClicked() {\n             var grid = $("#jqGridTable");\n             var rowid = grid.jqGrid(\'getGridParam\', \'selrow\');\n             if (!rowid){\n              alert("Select a row")\n             }\n             else\n             {\n                var winHeight=Math.round(window.innerHeight*.75)\n                var winWidth=Math.round(window.innerWidth*.86)\n                // Setup Jquery Validate\n                var addFilter01Buttons = {\n                        "Add": function() {\n                            if($("#loanForm").valid()){   // test for validity\n                                var am = $(\'#amount\').val();\n                                var dd = $(\'#due_date\').val();\n                                $.ajax({\n                                    type: "GET",\n                                    url: "')
        __M_writer(escape(tg.url('/addLoan')))
        __M_writer('"+"?phone_id="+rowid+"&amount="+am+"&due_date="+dd,\n                                    contentType: "application/json; charset=utf-8",\n                                    data: { \'param\':\'gaugeParameters\' },\n                                    success: function(data) {\n                                        // data.value is the success return json. json string contains key value\n                                         $(\'#jqGridTable\').trigger( \'reloadGrid\' );\n                                    },\n                                    error: function() {\n                                    //alert("#"+ckbid);\n                                         $.alert("Error accessing tables/addFilter01", { autoClose:false,});\n                                        return true;\n                                    },\n                                    complete: function() {\n                                    }\n                                    });\n                                $(\'#loanForm\')[0].reset();\n                                Dialog01.dialog( "close" );\n                            }\n\n\n                        },\n                        "Close": function() {\n                            $(\'#loanForm\')[0].reset();\n                            Dialog01.dialog( "close" );\n                        }\n                };\n\n                 // Create Dialog\n                 var Dialog01 = $( "#dialogForm01" ).dialog({\n                        autoOpen: false,\n                        height: winHeight-100,\n                        width: winWidth-200,\n                        modal: true,\n                        buttons: addFilter01Buttons,\n                        close: function() {\n                            $(\'#loanForm\')[0].reset();\n                            //form[ 0 ].reset();\n                            //allFields.removeClass( "ui-state-error" );\n                        }\n                 });\n\n                 // Append html\n                 $.ajax({\n                    type: "GET",\n                    url: "')
        __M_writer(escape(tg.url('/loanTemplate')))
        __M_writer('",\n                    contentType: "application/json; charset=utf-8",\n                    data: { \'param\':\'gaugeParameters\' },\n                    success: function(parameterdata) {\n                        //Insert HTML code\n                        $( "#dialogForm01" ).html(parameterdata.loantemplate);\n\n                        $( "#loanForm" ).validate({\n                                  rules: {\n                                                amount: {\n                                                required: true,\n                                                min: 500,\n                                                number: true\n                                            },\n                                                due_date: {\n                                                required: true,\n\n                                            },\n                                         }\n                                });\n                        Dialog01.data(\'rowId\',1);\n                        Dialog01.dialog( "open" );\n\n                    },\n                    error: function() {\n                        alert("Error accessing server /loantemplate")\n                    },\n                    complete: function() {\n                    }\n                 });\n             }\n\n\n        }\n        //\n        function  displayLoans(id) {\n                var winHeight=Math.round(window.innerHeight*.75)\n                var winWidth=Math.round(window.innerWidth*.86)\n                // Create Dialog\n                var Dialog02 = $( "#dialogForm02" ).dialog({\n                        autoOpen: false,\n                        height: winHeight-100,\n                        width: winWidth-200,\n                        modal: true,\n                        close: function() {\n                        }\n                 });\n\n                 // Append html to jquery dialog\n                 $.ajax({\n                    type: "GET",\n                    url: "')
        __M_writer(escape(tg.url('/displayLoanTemplate')))
        __M_writer('",\n                    contentType: "application/json; charset=utf-8",\n                    data: { \'param\':\'gaugeParameters\',\'id\':id },\n                    success: function(parameterdata) {\n                        //Insert HTML code\n                        $( "#dialogForm02" ).html(parameterdata.displayloantemplate);\n                        Dialog02.data(\'rowId\',1);\n                        Dialog02.dialog( "open" );\n\n                    },\n                    error: function() {\n                        alert("Error accessing server /displayloantemplate")\n                    },\n                    complete: function() {\n                    }\n                 });\n\n        }\n    </script>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/phonebook.mak", "uri": "/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/phonebook.mak", "source_encoding": "utf-8", "line_map": {"28": 0, "34": 1, "35": 15, "36": 15, "37": 123, "38": 123, "39": 167, "40": 167, "41": 218, "42": 218, "48": 42}}
__M_END_METADATA
"""
