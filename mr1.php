<?php
$arg="";
if (!empty($_GET["tag1"])) $arg.=" ".$_GET["tag1"];
	else $arg.=" ! ";
if (!empty($_GET["tag2"])) $arg.=" ".$_GET["tag2"];
	else $arg.=" ! ";
if (!empty($_GET["tag3"])) $arg.=" ".$_GET["tag3"];
	else $arg.=" ! ";
if (!empty($_GET["tag4"])) $arg.=" ".$_GET["tag4"];
	else $arg.=" ! ";

system("./mr1.sh $arg");

