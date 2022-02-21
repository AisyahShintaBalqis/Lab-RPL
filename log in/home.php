<?php
    session_start();
    if(!isset($_SESSION['login'])) {
        include("index.php");
    }
    else {
    ?>
    <html>
        <head><title>membuat form login dengan php dan mysql</title></head>
        <body bgcolor="#cccccc"><br />    
            <font face="vivaldi" color="blue" size="7">Login Berhasil !</font><br />
            <center><font face="arial" color="black" size="2"><a href="logout[dot]php">Logout</a></font></center>    
        </body>
    </html>
    <?php
    }
?>