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

    <meta charset="utf-8" />
    <title>jqGrid Loading Data - Million Rows from a REST service</title>
</head>
<body>

    <table style="width:100%;overflow:auto;">
    <table id="jqGridTable" class="scroll" cellpadding="0" cellspacing="0"></table>
    <div id="listPagerTables" class="scroll" style="text-align:center;"></div>
    <div id="listPsetcols" class="scroll" style="text-align:center;"></div>
    <div id="dialogLoanWindow"  title="Add a Loan"></div>
    </table>
    <script type="text/javascript">
        $(document).ready(
        function () {
            var grid_name = '#jqGridTable';
            var grid_pager= '#listPagerTables';
            var load_url='/loadjqgridtelefonica/';
            var header_container='Phone Book';
            var grid = jQuery(grid_name);
            grid.jqGrid({
                url: load_url,
                datatype: 'json',
                mtype: 'GET',
                colNames: ['id', 'ICC','life cicle status'],
                                colModel: [
                    {name: 'id',index: 'id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: false}},
                    {name: 'icc',index: 'icc', width: 25, align: 'right', hidden: false, editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'lifecyclestatus',index: 'lifeciclestatus', width: 5, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},

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
                    doDoubleClick(rowId)
                },
                caption: header_container,

            });

        });
        $.extend($.jgrid.nav,{alerttop:1});

    </script>
</body>
</html>