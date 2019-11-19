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
    </table>
<script type="text/javascript">
        $(document).ready(
        function () {
            var grid_name = '#jqGridTable';
            var grid_pager= '#listPagerTables';
            var update_url='/updateTest2';
            var load_url='/loadTest2/';
            var header_container='Test 2';
            var addParams = {left: 0,width: window.innerWidth-600,top: 20,height: 200,url: update_url, closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var editParams = {left: 0,width: window.innerWidth-400,top: 20,height: 200,url: update_url,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,
                    width: "500",
                    editfunc: function (rowid) {
                    alert('The "Edit" button was clicked with rowid=' + rowid);
                    }
                };
            var deleteParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var viewParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var searchParams = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url,modal: true, };
            var grid = jQuery(grid_name);
            grid.jqGrid({
                url: load_url,
                datatype: 'json',
                mtype: 'GET',
                colNames: ['id', 'imei','ticket','nombre'],
                colModel: [
                    {name: 'id',index: 'id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: false}},
                    {name: 'imei',index: 'imei', width: 30, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'ticket',index: 'ticket', width: 30, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'name',index: 'name', width: 30, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                ],
                pager: jQuery(grid_pager),
                rowNum: 10,
                rowList: [10, 50, 100],
                sortname: 'imei',
                sortorder: "desc",
                autowidth: true,
                shrinkToFit: true,
                viewrecords: true,
                height: 250,
                caption: header_container,

            });
            grid.jqGrid('navGrid',grid_pager,{edit:true,add:true,del:true, search:true},
                            editParams,
                            addParams,
                            deleteParams,
                            searchParams,
                            viewParams);
        });
        $.extend($.jgrid.nav,{alerttop:1});
    </script>


</body>
</html>