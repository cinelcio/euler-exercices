<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
	"http://www.w3.org/TR/html4/loose.dtd">
<html>
	<head>
		<title>Soluction for number 1</title>
	</head>
	<body>
	<?php 
/*
Calculate the sum of multiples of 3 and 5 until 1000
*/

	function sum($until) {
		$sum = 0;
		for ($i=0; $i < $until; $i++) { 
			if ($i % 3 === 0 || $i % 5 === 0) {
				$sum = $sum + $i;
			}
		}
		return $sum;
	}

	echo sum(1000);
 ?>
	<h1></h1>
	</body>
</html>
