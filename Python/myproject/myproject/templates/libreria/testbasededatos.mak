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

<div class="h"></div>
<div>
	<input type="checkbox" id="autosearch" onclick="enableAutosubmit(this.checked)"> Autobuscador <br/><br/>
	Nombre<br />
	<input type="text" id="search_cd" onkeydown="doSearch(arguments[0]||event)" />
</div>
<div>
	Id<br>
	<input type="text" id="item" onkeydown="doSearch(arguments[0]||event)" />
	<button onclick="gridReload()" id="submitButton" style="margin-left:30px;">Search</button>
</div>

<br />


    <table style="width:100%;overflow:auto;">
    <table id="jqGrid"></table>
    <div id="jqGridPager"></div>
    <div id="dialogForm01"  title="Agregar Prestamos"></div>
    </table>

 <script type="text/javascript">

var timeoutHnd;
var flAuto = false;

function doSearch(ev){
	if(!flAuto)
		return;
//	var elem = ev.target||ev.srcElement;
	if(timeoutHnd)
		clearTimeout(timeoutHnd)
	timeoutHnd = setTimeout(gridReload,500)
}

function gridReload(){
	var nm_mask = jQuery("#item_nm").val();
	var cd_mask = jQuery("#search_cd").val();
	jQuery("#jqGrid").jqGrid('setGridParam',{url:"bigset.php?nm_mask="+nm_mask+"&cd_mask="+cd_mask,page:1}).trigger("reloadGrid");
}
function enableAutosubmit(state){
	flAuto = state;
	jQuery("#submitButton").attr("disabled",state);
}


        $(document).ready(
            function () {

            $("#jqGrid").jqGrid({
                url: "${tg.url('/libreria/tablaBaseConec')}",
                datatype: "json",
                colNames: ['Usuario', 'Libro'],
                colModel: [
                    { name: 'usuario_id', index :'usuario_id', width: 250 },
                    { name: 'book_id', index :'book_id',width: 250 },
                ],
				viewrecords: true,
                height: 250,
                rowNum: 20,
                pager: "#jqGridPager",
                caption: "Prestamos"
            });
            jQuery("#jqGrid").jqGrid('navGrid','#jqGridPager',{edit:false,add:false,del:false});


            jQuery("#jqGrid").navButtonAdd('#jqGridPager',
                {
                    buttonicon: "ui-icon-circle-plus",
                    title: "${_('Plus')}",
                    caption: "${_('Plus')}",
                    position: "first",
                    onClickButton: function(){
                        displayPrestamo();
                    }
                });
        });

function alertaPrestamo() {

                var libro = $('#libros').val();
                var libro_id = $('#libros_id').val();
                var usuario = $('#usuarios').val();
                var usuario_id = $('#usuarios_id').val();

                if (!libro_id || !usuario_id){
                      alert("Llene ambos campos")
                    }
                else {
                    <!--alert(usuario+usuario_id+'\n'+libro + libro_id)-->

                    var formData = new FormData();
                    formData.append("usuario_id", usuario_id);
                    formData.append("book_id", libro_id);

                    var request = new XMLHttpRequest();
                    request.open("POST", '${h.url()}/libreria/alertPrestamo');
                    request.send(formData);
                }

}

function  displayPrestamo() {
    // Create Dialog
                 var winHeight=Math.round(window.innerHeight*.75)
                 var winWidth=Math.round(window.innerWidth*.86)
                 var Dialog01 = $( "#dialogForm01" ).dialog({
                        autoOpen: false,
                        height: winHeight-100,
                        width: winWidth-200,
                        modal: true,

                        close: function() {

                            //form[ 0 ].reset();
                            //allFields.removeClass( "ui-state-error" );
                        },
                        buttons: {
                            "${_('Agregar')}": function() {
                                alertaPrestamo();
                                 $('#dialogActivityVenus4').html("");
                                Dialog01.dialog( "close" );

                },
             },
                 });
                 $.ajax({
                    type: "GET",
                    url: "${tg.url('/libreria/prestamosTemplate')}",
                    contentType: "application/json; charset=utf-8",
                    data: { 'param':'gaugeParameters' },
                    success: function(parameterdata) {
                        //Insert HTML code
                        $( "#dialogForm01" ).html(parameterdata.prestamostemplate);
                        $( "#dialogForm01" ).show();
                        Dialog01.dialog( "open" );
                    },
                    error: function() {
                        alert("Error accessing server /prestamostemplate")
                    },
                    complete: function() {
                    }
                 });

        }
   </script>
</body>
</html>
