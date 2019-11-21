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
  <link rel="stylesheet" type="text/css" media="screen" href="${tg.url('/css/dot-luv/jquery-ui.css')}" />
    <meta charset="utf-8" />
    <title>jqGrid Loading Data - Million Rows from a REST service</title>
</head>
<body>

<table style="width:100%;overflow:auto;">
    <table id="jqGridTableCourses" class="scroll" cellpadding="0" cellspacing="0"></table>
    <div id="listPagerTablesCourses" class="scroll" style="text-align:center;"></div>
    <div id="listPsetcolsCourses" class="scroll" style="text-align:center;"></div>
</table>
<script type="text/javascript">
        $(document).ready(
        function () {
            var grid_name_course= '#jqGridTableCourses';
            var grid_pager_course= '#listPagerTablesCourses';
            var update_url_course='/courses/updateCourses';
            var load_url_course='/courses/loadCourses/';
            var header_container_course='Registro de Cursos';
            var addParams_course = {left: 0,width: window.innerWidth-400,top: 20,height: 250,url: update_url_course, closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var editParams_course = {left: 0,width: window.innerWidth-400,top: 20,height: 250,url: update_url_course,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,
                    width: "500",
                    editfunc: function (rowid) {
                    alert('The "Edit" button was clicked with rowid=' + rowid);
                    }
                };
            var deleteParams_course = {left: 0,width: window.innerWidth-500,top: 20,height: 130,url: update_url_course,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var viewParams_course = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url_course,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var searchParams_course = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url_course,modal: true, };
            var grid_course = jQuery(grid_name_course);
            grid_course.jqGrid({
                url: load_url_course,
                datatype: 'json',
                mtype: 'GET',
                colNames: ['ID de Curso', 'Registro','Nombre'],
                colModel: [
                    {name: 'course_id',index: 'course_id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: false}},
                    {name: 'code',index: 'code', width: 30, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'name',index: 'name', width: 30, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},

                ],
                pager: jQuery(grid_pager_course),
                rowNum: 10,
                rowList: [10, 50, 100],
                sortname: 'course_id',
                sortorder: "desc",
                autowidth: true,
                shrinkToFit: true,
                viewrecords: true,
                height: 150,
                caption: header_container_course,
                ondblClickRow: function(rowId) {
                    closeVenusActivity(rowId);
                }
            });
            grid_course.jqGrid('navGrid',grid_pager_course,{edit:true,add:true,del:true, search:true},
                            editParams_course,
                            addParams_course,
                            deleteParams_course,
                            searchParams_course,
                            viewParams_course);



        });
        $.extend($.jgrid.nav,{alerttop:1});
</script>
</body>
</html>