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

<br>
</br>

<table style="width:100%;overflow:auto;">
<table id="jqGridTableStudent" class="scroll" cellpadding="0" cellspacing="0"></table>
    <div id="listPagerTablesStudent" class="scroll" style="text-align:center;"></div>
    <div id="listPsetcolsStudent" class="scroll" style="text-align:center;"></div>
</table>
<script type="text/javascript">
        $(document).ready(
        function () {
            var grid_name_student= '#jqGridTableStudent';
            var grid_pager_student= '#listPagerTablesStudent';
            var update_url_student='/courses/updateStudent';
            var load_url_student='/courses/loadStudent/';
            var header_container_student='Registro de Estudiantes';
            var addParams_student = {left: 0,width: window.innerWidth-400,top: 20,height: 250,url: update_url_student, closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var editParams_student = {left: 0,width: window.innerWidth-400,top: 20,height: 250,url: update_url_student,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,
                    width: "500",
                    editfunc: function (rowid) {
                    alert('The "Edit" button was clicked with rowid=' + rowid);
                    }
                };
            var deleteParams_student = {left: 0,width: window.innerWidth-500,top: 20,height: 130,url: update_url_student,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var viewParams_student = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url_student,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var searchParams_student = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url_student,modal: true, };
            var grid_student = jQuery(grid_name_student);
            grid_student.jqGrid({
                url: load_url_student,
                datatype: 'json',
                mtype: 'GET',
                colNames: ['ID de Estudiante', 'Nombre','Apellido'],
                colModel: [
                    {name: 'student_id',index: 'student_id', width: 5,align: 'left',key:true,hidden: false, editable: true,edittype: 'text',editrules: {required: false}},
                    {name: 'name',index: 'name', width: 30, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'lastname',index: 'code', width: 30, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},

                ],
                pager: jQuery(grid_pager_student),
                rowNum: 10,
                rowList: [10, 50, 100],
                sortname: 'student_id',
                sortorder: "desc",
                autowidth: true,
                shrinkToFit: true,
                viewrecords: true,
                height: 150,
                subGrid:true,
                subGridRowExpanded: showChildGridRegistro,
                caption: header_container_student,
                ondblClickRow: function(rowId) {
                    closeVenusActivity(rowId);
                }
            });
            grid_student.jqGrid('navGrid',grid_pager_student,{edit:true,add:true,del:true, search:true},
                            editParams_student,
                            addParams_student,
                            deleteParams_student,
                            searchParams_student,
                            viewParams_student);
        });
        $.extend($.jgrid.nav,{alerttop:1});
</script>

<br></br>


<table style="width:100%;overflow:auto;">
<table id="jqGridTableRegistered" class="scroll" cellpadding="0" cellspacing="0"></table>
    <div id="listPagerTablesRegistered" class="scroll" style="text-align:center;"></div>
    <div id="listPsetcolsRegistered" class="scroll" style="text-align:center;"></div>
    <div id="dialogForm01"  title="Elimina Registros"></div>
</table>
<script type="text/javascript">
        $(document).ready(
        function () {
            var grid_name_registered= '#jqGridTableRegistered';
            var grid_pager_registered= '#listPagerTablesRegistered';
            var update_url_registered='/courses/updateRegistered';
            var load_url_registered='/courses/loadRegistered/';
            var header_container_registered='Registros de Curso';
            var addParams_registered = {left: 0,width: window.innerWidth-400,top: 20,height: 250,url: update_url_registered, closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var editParams_registered = {left: 0,width: window.innerWidth-400,top: 20,height: 250,url: update_url_registered,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,
                    width: "500",
                    editfunc: function (rowid) {
                    alert('The "Edit" button was clicked with rowid=' + rowid);
                    }
                };
            var deleteParams_registered = {left: 0,width: window.innerWidth-500,top: 20,height: 130,url: '/courses/DeleteRegistered/',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var viewParams_registered = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url_registered,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var searchParams_registered = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url_registered,modal: true, };
            var grid_registered = jQuery(grid_name_registered);
            grid_registered.jqGrid({
                url: load_url_registered,
                datatype: 'json',
                mtype: 'GET',
                colNames: ['ClaveEstudiante','courses_id' ,'Nombre de estudiante', 'Curso'],
                colModel: [
                    {name: 'student_id',index: 'student_id', width: 5, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'course_id',index: 'course_id', width: 5, align: 'right',hidden: true,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'student_name',index: 'name', width: 30, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'course_name',index: 'name', width: 30, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},

                ],
                pager: jQuery(grid_pager_registered),
                rowNum: 10,
                rowList: [10, 50, 100],
                sortname: 'registered_id',
                sortorder: "desc",
                autowidth: true,
                shrinkToFit: true,
                viewrecords: true,
                height: 150,
                caption: header_container_registered,
                ondblClickRow: function(rowId) {

                }
            });
            grid_registered.jqGrid('navGrid',grid_pager_registered,{edit:false,add:true,del:false, search:false},
                            editParams_registered,
                            addParams_registered,
                            deleteParams_registered,
                            searchParams_registered,
                            viewParams_registered);
            grid_registered.navButtonAdd(grid_pager_registered,
                {
                    buttonicon: " ui-icon-trash",
                    title: "Eliminar",
                    caption: " ",
                    position: "last",
                    onClickButton: function(rowId){
                        EliminaFila(rowId);
                    }
                })
            .navButtonAdd(grid_pager_registered,{
                    caption:"",
                    buttonicon:"ui-icon-del",
                    onClickButton: function(){
                    alert("Surprise!!!");
                    },
                    position:"last"
                });
        });

        $.extend($.jgrid.nav,{alerttop:1});

        function EliminaFila(rowId){
            var selRowId = jQuery('#jqGridTableRegistered').jqGrid ('getGridParam', 'selrow');
            var rowData = jQuery("#jqGridTableRegistered").getRowData(selRowId);
            var student_id = rowData['student_id'];
            var course_id = rowData['course_id'];


                if (!selRowId){
                 alert("Seleccione una fila")
               }
           else {
                    $('#dialogForm01').html("¿Deseas eliminar este registro?");
                    var winHeight = Math.round(window.innerHeight * .345)
                    var winWidth = Math.round(window.innerWidth * .445)
                    var ContDialog = $("#dialogForm01").dialog({
                        autoOpen: false,
                        height: winHeight - 100,
                        width: winWidth - 300,
                        modal: true,
                        title: "${_('Eliminar')}",
                        dialogClass: "noclose",
                        closeOnEscape: false,
                        buttons: {
                            "${_('Si')}": function () {
                                $('#dialogForm01').html("");

                                    <!-- Aquí inicia la funcion para enviar los datos del row al EndPoint-->
                                    var formData = new FormData();
                                    formData.append("student_id", student_id);
                                    formData.append("course_id", course_id);
                                    var request = new XMLHttpRequest();
                                    request.open("POST", '${h.url()}/courses/DeleteRegistered');
                                    request.send(formData);
                                    $('#jqGridTableRegistered').trigger( 'reloadGrid' );

                                ContDialog.dialog("close");
                            },
                            "${_('No')}": function () {
                                $('#dialogForm01').html("");
                                ContDialog.dialog("close");
                            }
                        },
                        close: function () {
                        }
                    });
                    ContDialog.dialog("open");
                }

}

function showChildGridRegistro(parentRowID, parentRowKey) {
     var childGridID = parentRowID + "_table";
     var childGridPagerID = parentRowID + "_pager";

     // send the parent row primary key to the server so that we know which grid to show
     var childGridURL = "${h.url()}/courses/loadSubGridCursos";
     childGridURL = childGridURL + "?student_id=" + encodeURIComponent(parentRowKey);

     // add a table and pager HTML elements to the parent grid row - we will render the child grid here
     $('#' + parentRowID).append('<table id='+childGridID+'><div id='+childGridPagerID+'class=scroll></div>');

     $("#" + childGridID).jqGrid({
          url: childGridURL,
          mtype: "GET",
          datatype: "json",
          page: 1,
          sortname: 'course_id',
          sortorder: "desc",
          colModel: [
                 {name: 'course_id',index: 'course_id', align: 'center',key:true,hidden: false, editable: false,edittype: 'text',editrules: {required: true},search:false},
                 {name: 'code', index: 'code',align: 'left',hidden: false, editable: true, edittype: 'text', editrules: {required: false}},
                 {name: 'name', index: 'name',align: 'left',hidden: false, width:90,editable: true, edittype: 'text', editrules: {required: false}},
                ],
          loadonce: true,
          scroll:true,
          width: 500,
          height: 75,
          rowNum: 5,
          rowList: [5,10],
          pager: "#" + childGridPagerID,
          autowidth: true,
          });
}

function imageUp() {
        var formData = new FormData();
        var request = new XMLHttpRequest();
        formData.append("application_id", "12345");
        var input = document.querySelector('input[type=file]');
        if(input != null){
            var file = input.files[0];
            formData.append("file", file);
        }
        request.open("POST", '${h.url()}/ticket/save?'+info);
        request.send(formData);
        request.onload  = function() {
            var response = JSON.parse(request.responseText);
            if (response.error == "ok"){
               alert("TODO OK");
            }else{
                alert("HUBO PROBLEMA");
            }
        };
}
</script>



</body>
</html>