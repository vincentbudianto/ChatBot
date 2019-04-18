<?php

$query = 'python main.py "' . $_GET["message"] . '"' . " " . $_GET["pil"];
$ans = shell_exec($query);
echo $ans;

?>