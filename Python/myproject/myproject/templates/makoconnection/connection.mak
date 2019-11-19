<%inherit file="local:templates.master"/>

<HTML>
    <HEAD>
    <TITLE>Datos</TITLE>
    </HEAD>
    <BODY BGCOLOR="FFFFFF">
        <CENTER>
                    % for it in kw['tracker']:
                        <p> No de registro: ${it['id']} IMEI: ${it['imei']} No.Ticket: ${it['ticket']} Nombre: ${it['name']} </p>
                    %endfor
        </CENTER>
        <HR>
    </BODY>
</HTML>