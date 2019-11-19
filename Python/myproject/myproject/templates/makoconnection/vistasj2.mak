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
<div style="margin-left:20px">
    <table id="list2"></table>
    <div id="pager2"></div>
</div>
    <script type="text/javascript">
        $(document).ready(function () {

            jQuery("#list2").jqGrid({
                url:"http://trirand.com/blog/phpjqgrid/examples/jsonp/getjsonp.php?callback=?&qwery=longorders",
                datatype: "json",
                mtype: "GET",
                colNames:['OrderID','CustomerID', 'OrderDate', 'Freight','ShipName'],
                colModel:[
                    {name:'OrderID',index:'OrderID', width:55},
                    {name:'CustomerID',index:'CustomerID', width:90},
                    {name:'OrderDate',index:'OrderDate', width:100},
                    {name:'Freight',index:'Freight', width:80, align:"right"},
                    {name:'ShipName',index:'ShipName', width:80, align:"right"},
                ],
                rowNum:10,
                pager: '#pager2',
                height: 250,
                viewrecords: true,
            });
                });

   </script>
</body>
</html>