<?php

$query = 'python main.py "' . $_GET["message"] . '"' . " " . $_GET["pil"] . " " . $_GET["range"];
$ans = shell_exec($query);
echo $ans;

?>