<script>
    function agregaUsuario() {

                    var rowId =$("#jqGridTableUsuarios").jqGrid('getGridParam','selrow');
                    var rowData = jQuery("#jqGridTableUsuarios").getRowData(rowId);
                    var rowNameUser = rowData['name'];
                    var usuario_id= rowData['usuario_id'];

                    if (!rowId){
                      alert("Select a row")
                    }
                      else {
                      <!--alert('{' + 'usuario_id:' + usuario_id +','+'name:' + rowName +'}');-->
                      document.getElementById("usuarios").value = rowNameUser;
                      document.getElementById("usuarios_id").value = usuario_id;
                    }

    }
    function agregaLibro() {
                    var rowId = $("#jqGridTableBooks").jqGrid('getGridParam', 'selrow');
                    var rowData = jQuery("#jqGridTableBooks").getRowData(rowId);
                    var rowNameBook = rowData['book_name'];
                    var book_id = rowData['book_id'];

                    if (!rowId){
                      alert("Select a row")
                    }
                      else {
                      <!--alert('book_id:'+book_id +','+'book_name:' + rowName);-->

                      document.getElementById("libros").value = rowNameBook;
                      document.getElementById("libros_id").value = book_id;
                    }

    }

function  displayUsuarios() {
                var winHeight=Math.round(window.innerHeight*.75)
                var winWidth=Math.round(window.innerWidth*.86)
                // Create Dialog
                var Dialog02 = $( "#dialoForm02" ).dialog({
                        autoOpen: false,
                        height: winHeight-100,
                        width: winWidth-200,
                        modal: true,
                        title: "${_('Agregar Usuario')}",
                        buttons: {
                            "${_('Agregar')}": function () {
                              agregaUsuario();
                              $('#dialogActivityVenus4').html("");
                                Dialog02.dialog( "close" );
                            },
                        },
                        close: function() {
                        }
                 });
                $.ajax({
                    type: "GET",
                    url: "${tg.url('/libreria/displayUsuarios')}",
                    contentType: "application/json; charset=utf-8",
                    data: { 'param':'gaugeParameters'},
                    success: function(parameterdata) {
                        //Insert HTML code
                        $( "#dialoForm02" ).html(parameterdata.displayusuarios);
                        Dialog02.data('rowId',1);
                        Dialog02.dialog( "open" );
                    },
                    error: function() {
                        alert("Error accessing server /libreria/displayusuarios")
                    },
                    complete: function() {
                    }
                 });
        }

function displayLibros() {
                var winHeight=Math.round(window.innerHeight*.75)
                var winWidth=Math.round(window.innerWidth*.86)
                // Create Dialog
                var Dialog03 = $( "#dialoForm03" ).dialog({
                        autoOpen: false,
                        height: winHeight-100,
                        width: winWidth-200,
                        modal: true,
                        title: "${_('Agregar Libro')}",
                        dialogClass: "noclose",
                        closeOnEscape: false,
                        close: function() {
                        },
                        buttons: {
                            "${_('Agregar')}": function () {
                                agregaLibro();
                                $('#dialogActivityVenus4').html("");
                                Dialog03.dialog( "close" );
                            },
                        },
                 });
                $.ajax({
                    type: "GET",
                    url: "${tg.url('/libreria/displayBooks')}",
                    contentType: "application/json; charset=utf-8",
                    data: { 'param':'gaugeParameters'},
                    success: function(parameterdata) {
                        //Insert HTML code
                        $( "#dialoForm03" ).html(parameterdata.displaybooks);
                        Dialog03.data('rowId',1);
                        Dialog03.dialog( "open" );
                    },
                    error: function() {
                        alert("Error accessing server /libreria/displayBooks")
                    },
                    complete: function() {
                    }
                 });
}
</script>

<form id="prestamoForm">
  <div class="form-group">
    <label for="usuarios">Nombre de usuario</label>
    <input id="usuarios" type="text" onclick="displayUsuarios()" class="form-control" name="usuario">
    <input id="usuarios_id" type="text" name="usuarios" hidden >
    <div id="dialoForm02"  title="Display Usuarios"></div>
  </div>
    <br>
  <div class="form-group">
    <label for="libros">Nombre de Libro</label>
    <input id="libros" type="text" onclick="displayLibros()" class="form-control" name="libro">
    <input id="libros_id" type="text" name="libros" hidden >
    <div id="dialoForm03"  title="Display Libros"></div>
  </div>
</form>