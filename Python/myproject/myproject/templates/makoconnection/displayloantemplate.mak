<html lang="en">
<head>
<body>
    <table style="width:100%;overflow:auto;">
    <table id="jgGridLoans" class="scroll" cellpadding="0" cellspacing="0"></table>
    <div id="listPagerLoans" class="scroll" style="text-align:center;"></div>
    <div id="listPsetcols" class="scroll" style="text-align:center;"></div>
    <div id="dialogLoanWindow"  title="Add a Loan"></div>
    </table>
    <script type="text/javascript">
        $(document).ready(
        function () {
            var grid_name = '#jgGridLoans';
            var grid_pager= '#listPagerLoans';
            var load_url='/loadjqgridloans?loanid=${loanid}';
            var header_container='Deudas';
            var grid = jQuery(grid_name);
            grid.jqGrid({
                url: load_url,
                datatype: 'json',
                mtype: 'GET',
                colNames: ['id', 'Amount','DueDate'],
                                colModel: [
                    {name: 'id',index: 'id', width: 5,align: 'left',key:true,hidden: true, editable: true,edittype: 'text',editrules: {required: false}},
                    {name: 'amount',index: 'amount', width: 25, align: 'right', hidden: false, editable: true, edittype: 'text',editrules: {required: false}},
                    {name: 'due_date',index: 'due_date', width: 5, align: 'right',hidden: false,editable: true, edittype: 'text',editrules: {required: false}},

                ],
                pager: jQuery(grid_pager),
                rowNum: 10,
                rowList: [10, 50, 100],
                sortname: 'due_date',
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