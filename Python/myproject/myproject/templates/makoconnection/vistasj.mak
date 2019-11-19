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
    <table id="jqGrid">jqGrid</table>
    <div id="jqGridPager"></div>
</div>
    <script type="text/javascript">
        $(document).ready(function () {

            $("#jqGrid").jqGrid({
                url: "${tg.url('/loadweather')}",
                datatype: "json",
                colNames:['id','main', 'description','icon'],
                colModel: [
                    { name: 'id', index :'id', width: 75 },
                    { name: 'main', index :'main',width: 150 },
                    { name: 'descripion', index :'description',width: 150 },
                    { name: 'icon',index :'icon', width: 150 }
                ],
				viewrecords: true,
                height: 250,
                rowNum: 20,
                pager: "#jqGridPager"

            });
        });

   </script>
</body>
</html>