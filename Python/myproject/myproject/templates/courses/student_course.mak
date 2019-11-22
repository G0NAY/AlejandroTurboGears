
<table style="width:100%;overflow:auto;">
<table id="jqGridTableRegistered" class="scroll" cellpadding="0" cellspacing="0"></table>
    <div id="listPagerTablesRegistered" class="scroll" style="text-align:center;"></div>
    <div id="listPsetcolsRegistered" class="scroll" style="text-align:center;"></div>
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
            var deleteParams_registered = {left: 0,width: window.innerWidth-500,top: 20,height: 130,url: update_url_registered,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var viewParams_registered = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url_registered,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var searchParams_registered = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url_registered,modal: true, };
            var grid_registered = jQuery(grid_name_registered);
            grid_registered.jqGrid({
                url: load_url_registered,
                datatype: 'json',
                mtype: 'GET',
                colNames: ['ID de Estudiantes', 'ID Cursor'],
                colModel: [
                    {name: 'student_id',index: 'name', width: 30, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'course_id',index: 'code', width: 30, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},

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
                subgrid:true,

                caption: header_container_registered,
                ondblClickRow: function(rowId) {
                    closeVenusActivity(rowId);
                }
            });
            grid_registered.jqGrid('navGrid',grid_pager_registered,{edit:true,add:true,del:true, search:true},
                            editParams_registered,
                            addParams_registered,
                            deleteParams_registered,
                            searchParams_registered,
                            viewParams_registered);
        });
        $.extend($.jgrid.nav,{alerttop:1});
</script>
