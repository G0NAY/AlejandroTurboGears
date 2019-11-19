<html lang="en">
<head>
<body>
    <table style="width:100%;overflow:auto;">
    <table id="jqGridTableUsuarios" class="scroll" cellpadding="0" cellspacing="0"></table>
    <div id="listPagerTablesUsuarios" class="scroll" style="text-align:center;"></div>
    <div id="listPsetcolsUsuarios" class="scroll" style="text-align:center;"></div>
    </table>
<script type="text/javascript">
        $(document).ready(
        function () {
            var grid_name_usuarios= '#jqGridTableUsuarios';
            var grid_pager_usuarios= '#listPagerTablesUsuarios';
            var update_url_usuarios='/libreria/updateUsuarios';
            var load_url_usuarios='/libreria/loadUsuario/';
            var header_container_usuarios='Registro de Usuarios';
            var addParams_usuarios = {left: 0,width: window.innerWidth-400,top: 20,height: 250,url: update_url_usuarios, closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var editParams_usuarios = {left: 0,width: window.innerWidth-400,top: 20,height: 250,url: update_url_usuarios,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true,
                    width: "500",
                    editfunc: function (rowid) {
                    alert('The "Edit" button was clicked with rowid=' + rowid);
                    }
                };
            var deleteParams_usuarios = {left: 0,width: window.innerWidth-500,top: 20,height: 130,url: update_url_usuarios,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var viewParams_usuarios = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url_usuarios,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var searchParams_usuarios = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url_usuarios,modal: true, };
            var grid_usuarios = jQuery(grid_name_usuarios);
            grid_usuarios.jqGrid({
                url: load_url_usuarios,
                datatype: 'json',
                mtype: 'GET',
                colNames: ['Num_Usuario', 'Nombre','Edad','Telefono','Email','Fecha de ingreso'],
                colModel: [
                    {name: 'usuario_id',index: 'usuario_id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: false}},
                    {name: 'name',index: 'name', width: 30, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'age',index: 'age', width: 30, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'phone',index: 'phone', width: 30, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'email_address',index: 'email_address', width: 30, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'created',index: 'created', width: 30, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},

                ],
                pager: jQuery(grid_pager_usuarios),
                rowNum: 10,
                rowList: [10, 50, 100],
                sortname: 'name',
                sortorder: "desc",
                autowidth: true,
                shrinkToFit: true,
                viewrecords: true,
                height: 150,
                caption: header_container_usuarios,
            });
            grid_usuarios.jqGrid('navGrid',grid_pager_usuarios,{edit:false,add:false,del:false, search:false},
                            editParams_usuarios,
                            addParams_usuarios,
                            deleteParams_usuarios,
                            searchParams_usuarios,
                            viewParams_usuarios);
        });
        $.extend($.jgrid.nav,{alerttop:1});

    </script>
</body>