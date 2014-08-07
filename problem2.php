<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
	"http://www.w3.org/TR/html4/loose.dtd">
<html>
	<head>
		<title>Soluction for number 2</title>
	</head>
	<body>
	<?php 
/*
Calculate the higher Fibonacci number until it
reaches the parameter set
*/

	function fibo($end) {
		$n0 = 0;
		$n1 = 1;
		$n2 = 0;
		 do {
		 	$n2 = $n1 + $n0;
			$n0 = $n1;
			$n1 = $n2;
		 } while ($n2 <= $end);
		return $n0;
	}

	function isEven($num) {
		if ($num % 2 != 0) {
			return true;
		}
	}
	
	function sumFiboEven($limit) {
		for ($counter=0; $counter < $limit; $counter++) { 
			$sum = fibo($counter);
			if (isEven($sum) === true) {
				# code...
			}
		}
	}
	
	echo sumFiboEven(10);


 ?>
	<h1></h1>
	</body>
</html>
