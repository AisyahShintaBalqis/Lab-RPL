<html>
    <head><title>membuat form login dengan php dan mysql</title>
    <style type="text/css">
    table {
        font-family: Verdana, Arial, Helvetica, sans-serif;
        font-size: 11px;
    }
    input {
        font-family: Verdana, Arial, Helvetica, sans-serif;
        font-size: 11px;
        height: 20px;
    }
    </style>
    </head>
    <body bgcolor="#cccccc"><br />
        <div align="center">
            <form name="form-login" method="POST" action="login.php">
                <table width="310" border="0" cellpadding="0" cellspacing="0">
                    <tr bgcolor="blue">
                        <td height="25" colspan="2" align="center"><font color="#FFFFFF">Form Login PHP - MySQL</font></td>
                    </tr>
                    <tr>
                        <td width="106" height="16"> </td>
                        <td width="180"> </td>
                    </tr>
                    <tr>
                        <td height="18" align="right">Username : </td>
                        <td><input type="text" name="user" size="20" maxlength="9"></td>
                    </tr>
                    <tr>
                        <td> </td>
                        <td> </td>
                    </tr>
                    <tr>
                        <td height="18" align="right" >Password : </td>
                        <td><input type="password" name="password" size="20"></td>
                    </tr>
                    <tr>
                        <td height="16"> </td>
                        <td> </td>
                    </tr>
                    <tr>
                        <td height="18" align="top"> </td>
                        <td align="left"><input type="submit" value=" Login "></td>
                    </tr>
                    <tr>
                        <td height="16"> </td>
                        <td> </td>
                    </tr>
                    <tr bgcolor="blue">
                        <td height="25" colspan="2" align="top"> </td>
                    </tr>
                </table>
            </form>
        </div>
    </body>
</html>