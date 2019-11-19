<HTML>
    <HEAD>
    <TITLE>Datos</TITLE>
    </HEAD>
    <BODY BGCOLOR="FFFFFF">
        <CENTER>
        <table>
		<caption>Datos de usuario</caption>
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

        </CENTER>
        <HR>
    </BODY>
</HTML>