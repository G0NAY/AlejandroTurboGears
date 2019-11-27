<HTML>
    <HEAD>
    <TITLE>Datos</TITLE>
    </HEAD>
    <BODY BGCOLOR="FFFFFF">
        <CENTER>
            <form>


        <table>
		<caption>Datos de usuario</caption>

        <tr>
            <td colspan="2">
                <img src="data:image/png;base64,${image}" width="150" height="100" />
            </td>
        </tr>
		<tr>
			<td>Id de Usuario:</td>
			<td>${usuario.usuario_id}</td>
		</tr>
		<tr>
			<td>Nombre de usuario:</td>
			<td>${usuario.name}</td>
		</tr>
        <tr>
            <td>Libros de usuario:</td>
            % for it in book:
                         <tr><td>${it['book_name']} </td></tr>
                    %endfor
        </tr>
		</table>
            </form>

        </CENTER>
        <HR>
    </BODY>
</HTML>