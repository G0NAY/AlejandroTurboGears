<html lang="en">
<head>
<body>
    <table style="width:100%;overflow:auto;">
    <table id="jqGridTableBooks" class="scroll" cellpadding="0" cellspacing="0"></table>
    <div id="listPagerTablesBooks" class="scroll" style="text-align:center;"></div>
    <div id="listPsetcolsBooks" class="scroll" style="text-align:center;"></div>
    </table>
    <script type="text/javascript">
        $(document).ready(
        function () {
            var grid_name_books= '#jqGridTableBooks';
            var grid_pager_books= '#listPagerTablesBooks';
            var update_url_books='/libreria/updateBook';
            var load_url_books='/libreria/loadBook/';
            var header_container_books='Lista de Libros';
            var viewParams_books = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url_books,closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true}
            var searchParams_books = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url_books,modal: true, };
            var grid_books = jQuery(grid_name_books);
            grid_books.jqGrid({
                url: load_url_books,
                datatype: 'json',
                mtype: 'GET',
                colNames: ['Num_Libro', 'Nombre de Libro', 'Fecha de Publicación', 'Fecha de registro', 'Autor'],
                colModel: [
                    {
                        name: 'book_id',
                        index: 'book_id',
                        width: 5,
                        align: 'left',
                        key: true,
                        hidden: true,
                        editable: true,
                        edittype: 'text',
                        editrules: {required: false}
                    },
                    {
                        name: 'book_name',
                        index: 'book_name',
                        width: 30,
                        align: 'right',
                        hidden: false,
                        editable: true,
                        edittype: 'text',
                        editrules: {required: false}
                    },
                    {
                        name: 'publication_date',
                        index: 'publication_date',
                        width: 30,
                        align: 'right',
                        hidden: false,
                        editable: true,
                        edittype: 'text',
                        editrules: {required: false}
                    },
                    {
                        name: 'created',
                        index: 'created',
                        width: 30,
                        align: 'right',
                        hidden: false,
                        editable: true,
                        edittype: 'text',
                        editrules: {required: false}
                    },
                    {
                        name: 'author_id',
                        index: 'author_id',
                        width: 30,
                        align: 'right',
                        hidden: false,
                        editable: true,
                        edittype: 'text',
                        editrules: {required: false}
                    },
                ],
                pager: jQuery(grid_pager_books),
                rowNum: 10,
                rowList: [10, 50, 100],
                sortname: 'book_name',
                sortorder: "desc",
                autowidth: true,
                shrinkToFit: true,
                viewrecords: true,
                height: 150,
                caption: header_container_books,
            });
            grid_books.jqGrid('navGrid',grid_pager_books,{edit:false,add:false,del:false, search:false},
                            searchParams_books,
                            viewParams_books);
        });
        $.extend($.jgrid.nav,{alerttop:1});

    </script>
</body>