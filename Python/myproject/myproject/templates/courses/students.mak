
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
            var update_url_student='/students/updateStudent';
            var load_url_student='/students/loadStudent/';
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
                    {name: 'student_id',index: 'student_id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: false}},
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
