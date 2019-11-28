<script type="text/javascript">
    $('.datepicker').datepicker({
        dateFormat: 'yy-mm-dd',
    startDate: '-3d'
    });
</script>

<html lang="en">
<head></head>
<body>
<form id="addUsuasrio">
    <input hidden type="text" id="user_id" value='${usuario_id}'>
    <fieldset>
        <table style="width:100%">
            <tr>
                <td style="width:30%">
                    ${_('Nombre')}:
                </td>
                <td>
                    <input type="text" maxlength="40" id="user_name" style="width: 40%" value='${handler.name}'>
                </td>
            </tr>

            <tr>
                <td style="width:30%">
                    <br>
                    ${_('Edad')}:
                </td>
                <td>
                    <br>
                    <input type="text" maxlength="40" id="user_edad" style="width: 40%" value='${handler.age}'>
                </td>
            </tr>

              <tr>
                <td style="width:30%">
                    <br>
                    ${_('Telefono')}:
                </td>
                <td>
                    <br>
                    <input type="text" maxlength="40" id="user_tel" style="width: 40%" value='${handler.phone}'>
                </td>
            </tr>

              <tr>
                <td style="width:30%">
                    <br>
                    ${_('Email')}:
                </td>
                <td>
                    <br>
                    <input type="text" maxlength="40" id="user_email" style="width: 40%" value='${handler.email_address}'>
                </td>
            </tr>

            <tr style="height: 10px">
                <td></td>
            </tr>
            <tr>
                <td style="width:30%" >
                    ${_('Imagen')}:
                </td>
                <td>
                    <input type="file" value='${handler.image}'>
                </td>
            </tr>
        </table>
    </fieldset>
</form>
</body>
