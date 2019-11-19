<%inherit file="local:templates.master"/>
<html lang="en">
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
  <script src="//cdn.jsdelivr.net/free-jqgrid/4.8.0/js/i18n/grid.locale-es.js"></script>
  <script src="//cdn.jsdelivr.net/free-jqgrid/4.8.0/js/jquery.jqgrid.min.js"></script>
  <link rel="stylesheet" href="//cdn.jsdelivr.net/free-jqgrid/4.8.0/css/ui.jqgrid.css">

  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/themes/redmond/jquery-ui.css" type="text/css"/>
        <script src="${tg.url('/javascript/jquery-validation-1.17.0/dist/jquery.validate.js')}"></script>
    <meta charset="utf-8" />
    <title>jqGrid Loading Data - Million Rows from a REST service</title>
</head>
<body>
    <table style="width:100%;overflow:auto;">
    <table id="jqGridTable" class="scroll" cellpadding="0" cellspacing="0"></table>
    <div id="listPagerTables" class="scroll" style="text-align:center;"></div>
    <div id="listPsetcols" class="scroll" style="text-align:center;"></div>
    <div id="dialogForm01"  title="Add a Loan">
    <div id="dialogForm02"  title="Display Loans">
    </table>
    <script type="text/javascript">
        $(document).ready(
        function () {
            var grid_name = '#jqGridTable';
            var grid_pager= '#listPagerTables';
            var update_url='/updatePhoneBook';
            var load_url='/loadPhoneBook/';
            var header_container='Phone Book';
            var addParams = {left: 0,width: window.innerWidth-600,top: 20,height: 220,url: update_url, closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var editParams = {left: 0,width: window.innerWidth-400,top: 20,height: 220,url: update_url,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,
                    width: "500",
                    editfunc: function (rowid) {
                    alert('The "Edit" button was clicked with rowid=' + rowid);
                    }
                };
            var deleteParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var viewParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var searchParams = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url,modal: true, };
            var grid = jQuery(grid_name);
            var rowKey = grid.getGridParam('selrow')
            grid.jqGrid({
                url: load_url,
                datatype: 'json',
                mtype: 'GET',
                colNames: ['id', 'Name','Birthday','Age','Phone'],
                                colModel: [
                    {name: 'id',index: 'id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: false}},
                    {name: 'name',index: 'name', width: 25, align: 'right', hidden: false, editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'birthday',index: 'birthday', formatter: 'date', width: 10,sortable: false,align: 'right',editable: true, editoptions: {size: 20,maxlengh: 10,
                                            dataInit: function (element) {
                                                $(element).datepicker({
                                                    dateFormat: 'yy-mm-dd',
                                                    constrainInput: false,
                                                    showOn: 'button',
                                                    buttonText: '...'
                                                });
                                            }
                            },
                            formatoptions: {
                                newformat: "Y-m-d"
                            },

                    },
                    {name: 'age',index: 'age', width: 5, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'phone', index: 'phone', width: 20,align: 'left',hidden: false, editable: true, edittype: 'text', editrules: {required: false}},

                ],
                pager: jQuery(grid_pager),
                rowNum: 10,
                rowList: [10, 50, 100],
                sortname: 'name',
                sortorder: "asc",
                viewrecords: true,
                autowidth: true,
                height: 250,
                ondblClickRow: function(rowId) {
                    displayLoans(rowId)
                },
                caption: header_container,

            });
            grid.jqGrid('navGrid',grid_pager,{edit:true,add:true,del:true, search:true},
                            editParams,
                            addParams,
                            deleteParams,
                            searchParams,
                            viewParams);
             grid.navButtonAdd(grid_pager,
                {
                    buttonicon: "ui-icon-key",
                    title: "Loan",
                    caption: "Loan",
                    position: "last",
                    onClickButton: loanButtonClicked
                });
        });
        $.extend($.jgrid.nav,{alerttop:1});

        function  loanButtonClicked() {
             var grid = $("#jqGridTable");
             var rowid = grid.jqGrid('getGridParam', 'selrow');
             if (!rowid){
              alert("Select a row")
             }
             else
             {
                var winHeight=Math.round(window.innerHeight*.75)
                var winWidth=Math.round(window.innerWidth*.86)
                // Setup Jquery Validate
                var addFilter01Buttons = {
                        "Add": function() {
                            if($("#loanForm").valid()){   // test for validity
                                var am = $('#amount').val();
                                var dd = $('#due_date').val();
                                $.ajax({
                                    type: "GET",
                                    url: "${tg.url('/addLoan')}"+"?phone_id="+rowid+"&amount="+am+"&due_date="+dd,
                                    contentType: "application/json; charset=utf-8",
                                    data: { 'param':'gaugeParameters' },
                                    success: function(data) {
                                        // data.value is the success return json. json string contains key value
                                         $('#jqGridTable').trigger( 'reloadGrid' );
                                    },
                                    error: function() {
                                    //alert("#"+ckbid);
                                         $.alert("Error accessing tables/addFilter01", { autoClose:false,});
                                        return true;
                                    },
                                    complete: function() {
                                    }
                                    });
                                $('#loanForm')[0].reset();
                                Dialog01.dialog( "close" );
                            }


                        },
                        "Close": function() {
                            $('#loanForm')[0].reset();
                            Dialog01.dialog( "close" );
                        }
                };

                 // Create Dialog
                 var Dialog01 = $( "#dialogForm01" ).dialog({
                        autoOpen: false,
                        height: winHeight-100,
                        width: winWidth-200,
                        modal: true,
                        buttons: addFilter01Buttons,
                        close: function() {
                            $('#loanForm')[0].reset();
                            //form[ 0 ].reset();
                            //allFields.removeClass( "ui-state-error" );
                        }
                 });

                 // Append html
                 $.ajax({
                    type: "GET",
                    url: "${tg.url('/loanTemplate')}",
                    contentType: "application/json; charset=utf-8",
                    data: { 'param':'gaugeParameters' },
                    success: function(parameterdata) {
                        //Insert HTML code
                        $( "#dialogForm01" ).html(parameterdata.loantemplate);

                        $( "#loanForm" ).validate({
                                  rules: {
                                                amount: {
                                                required: true,
                                                min: 500,
                                                number: true
                                            },
                                                due_date: {
                                                required: true,

                                            },
                                         }
                                });
                        Dialog01.data('rowId',1);
                        Dialog01.dialog( "open" );

                    },
                    error: function() {
                        alert("Error accessing server /loantemplate")
                    },
                    complete: function() {
                    }
                 });
             }


        }
        //
        function  displayLoans(id) {
                var winHeight=Math.round(window.innerHeight*.75)
                var winWidth=Math.round(window.innerWidth*.86)
                // Create Dialog
                var Dialog02 = $( "#dialogForm02" ).dialog({
                        autoOpen: false,
                        height: winHeight-100,
                        width: winWidth-200,
                        modal: true,
                        close: function() {
                        }
                 });

                 // Append html to jquery dialog
                 $.ajax({
                    type: "GET",
                    url: "${tg.url('/displayLoanTemplate')}",
                    contentType: "application/json; charset=utf-8",
                    data: { 'param':'gaugeParameters','id':id },
                    success: function(parameterdata) {
                        //Insert HTML code
                        $( "#dialogForm02" ).html(parameterdata.displayloantemplate);
                        Dialog02.data('rowId',1);
                        Dialog02.dialog( "open" );

                    },
                    error: function() {
                        alert("Error accessing server /displayloantemplate")
                    },
                    complete: function() {
                    }
                 });

        }
    </script>
</body>
</html>
