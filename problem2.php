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

	function fibo($endFibo, $printSequence) {
		$a0 = 0;
		$a1 = 1;
		$a2 = 0;
		 do {
		 	$a2 = $a1 + $a0;
			$a0 = $a1;
			$a1 = $a2;
			if($printSequence === true) {echo $a0."<br>";}
		 } while ($a2 <= $endFibo);
	}

	function result($end) {
		$n0 = 0;
		$n1 = 1;
		$n2 = 0;
		$sum = 0;
		 do {
		 	$n2 = $n1 + $n0;
			$n0 = $n1;
			$n1 = $n2;
			if ($n0 % 2 == 1) {
				$sum = $sum + $n0;
			}
		 } while ($n1 <= $end);
			echo "Soma ".$sum;
	}

		fibo (4000000,true);
		result (4000000);
 ?>
	<h1></h1>
	</body>
</html>
