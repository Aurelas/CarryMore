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
			$champ_name = $_POST["champ"];
			function clean_name($string){
				$string = str_replace(" ", "", $string);
				$string = str_replace("'", "", $string);
				$string = strtolower($string);
			}
			$clean_name = clean_name($champ_name);
			$path = '/var/www/html/carrymore/Main.py';
			$python = '/usr/bin/python';
			$script = $python . " " . $path . " " . $clean_name;
			$command = escapeshellcmd($script);
			$results = exec($command, $my_output, $status);
			$data_array = explode(" , ", $results);

			$user_role = $data_array[0];
			$user_champ = $data_array[1];

		?>
		<div class="col-2" id="champ1" name="<?php echo $user_champ; ?>">
			<p class="tileName">
				<?php echo $user_champ; ?>
			</p>
			<p class="tileRole">
				<?php echo $user_role; ?>
			</p>
		</div>
		<div class="col-2" id="champ2" name="<?php echo $data_array[3]; ?>">
		<p class="tileName">
				<?php echo $data_array[3]; ?>
			</p>
			<p class="tileRole">
				<?php echo $data_array[2]; ?>
			</p>
		</div>
		<div class="col-2" id="champ3" name="<?php echo $data_array[5]; ?>">
		<p class="tileName">
				<?php echo $data_array[5]; ?>
			</p>
			<p class="tileRole">
				<?php echo $data_array[4]; ?>
			</p>
		</div>
		<div class="col-2" id="champ4" name="<?php echo $data_array[7]; ?>">
		<p class="tileName">
				<?php echo $data_array[7]; ?>
			</p>
			<p class="tileRole">
				<?php echo $data_array[6]; ?>
			</p>
		</div>
		<div class="col-2" id="champ5" name="<?php echo $data_array[9]; ?>">
		<p class="tileName">
				<?php echo $data_array[9]; ?>
			</p>
			<p class="tileRole">
				<?php echo $data_array[8]; ?>
			</p>
		</div>
	</body>
</html>