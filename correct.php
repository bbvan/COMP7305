<?php
ini_set('display_errors', 'On');
$arg="";
if (!empty($_GET["tag1"])) {
	$foo=$_GET["tag1"]; 
	echo "Tag 1 : ";
	system("./similarity.py $foo");
	echo "<br>";
}
if (!empty($_GET["tag2"])) {
	$foo=$_GET["tag2"]; 
	echo "Tag 2 : ";
	system("./similarity.py $foo");
	echo "<br>";
}
if (!empty($_GET["tag3"])) {
	$foo=$_GET["tag3"]; 
	echo "Tag 3 : ";
	system("./similarity.py $foo");
	echo "<br>";
}
if (!empty($_GET["tag4"])) {
	$foo=$_GET["tag4"]; 
	echo "Tag 4 : ";
	system("./similarity.py $foo");
	echo "<br>";
}

?>
