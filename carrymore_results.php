<html>
	<head>
	  <meta charset="utf-8">
	  <link href="https://fonts.googleapis.com/css?family=Taviraj:100,200,300,400,700" rel="stylesheet">
	  <link href='css/styles.css' rel='stylesheet' type='text/css'>
	  <title>Carrymore</title>
		<script src="js/jquery.js"></script>
		<script src="js/animation.js"></script>
	</head>
	<body>
		<h1>Carrymore</h1>
		<?php 
				function clean($string) {
			   	$string = str_replace('"', '', $string);
		  	 	$string = str_replace("'", '', $string);
			   	$string = strtolower($string);
			}

			$champ_name = $_POST["champ"];
			clean($champ_name);
			$path = '/var/www/html/carrymore/Main.py';
			$python = '/usr/bin/python2.7';
			$script = $python . " " . $path . " " . $champ_name;

			$results = exec($command, $my_output, $status);

			$data_array = explode(",", $results);
		?>
			<div class="col-1"></div>
			<div class="col-2" id="champ1"><p><?php echo $champ_name ?></p></div>
			<div class="col-2" id="champ2"></div>
			<div class="col-2" id="champ3"></div>
			<div class="col-2" id="champ4"></div>
			<div class="col-2" id="champ5"></div>
			<div class="col-1"></div>
	</body>
</html>