<?php
    ob_start();
    session_start();
    $user        = $_POST['user'];
    $password    = $_POST['password'];
    $_SESSION['user'] = $user;
        $Open = mysqli_connect("localhost","root","");
            if (!$Open){
            die ("Koneksi ke Engine MySQL Gagal !");
                }
        $Koneksi = mysqli_select_db($Open, "login");
            if (!$Koneksi){
            die ("Koneksi ke Database Gagal !");
            }
    $sql = "SELECT * FROM admin where user='$user'";
    $qry = mysqli_query($sql);
    $num = mysqli_num_rows($qry);
    $row = mysqli_fetch_array($qry);

    if ($num==0 OR $password!=$row['password']) {
    ?>
        <script language="JavaScript">
            alert('Username atau Password tidak sesuai !');
            document.location='index.php';
        </script>
    <?php
    }
    else {
        $_SESSION['login']=1;
        header("Location: home.php");
    }
    mysqli_close($Open); //Tutup koneksi engine MySQL
?>