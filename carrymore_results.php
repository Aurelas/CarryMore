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
			$s_champ_name = str_replace(" ", "", $champ_name);
			$sq_champ_name = str_replace("'", "", $s_champ_name);
			$sqp_champ_name = str_replace(".", "", $sq_champ_name);
			$clean = strtolower($sqp_champ_name);
			$path = '/var/www/html/carrymore/Main.py';
			$python = '/usr/bin/python';
			$script = $python . " " . $path . " " . $clean;
			$command = escapeshellcmd($script);
			$results = exec($command, $my_output, $status);
			$data_array = explode(" , ", $results);
			$champions = $data_array;
			for ($i = 0; $i <= 4; $i++) {
				switch ($champions[i]) {
					case "aurelionsol":
						$champions[i] = "Aurelion Sol";
						break;
					case "chogath":
						$champions[i] = "Cho'Gath";
						break;
					case "drmundo":
						$champions[i] = "Dr. Mundo";
						break;
					case "jarvaniv":
						$champions[i] = "Jarvan IV";
						break;
					case "khazix":
						$champions[i] = "Kha'Zix";
						break;
					case "kogmaw":
						$champions[i] = "Kog'Maw";
						break;
					case "leesin":
						$champions[i] = "Lee Sin";
						break;
					case "masteryi":
						$champions[i] = "Master Yi";
						break;
					case "missfortune":
						$champions[i] = "Miss Fortune";
						break;
					case "reksai":
						$champions[i] = "Rek'Sai";
						break;
					case "aurelionsol":
						$champions[i] = "Aurelion Sol";
						break;
					case "tahmkench":
						$champions[i] = "Tahm Kench";
						break;
					case "twistedfate":
						$champions[i] = "Twisted Fate";
						break;
					case "velkoz":
						$champions[i] = "Vel'Koz";
						break;
					case "xinzhao":
						$champions[i] = "Xin Zhao";
						break;
					default:
						$placeholder = 1;
				}
			}
		?>
		<div class="outer">
			<div class="inner">
				<div class="col-1" id="champ1" name="<?php echo $data_array[1]; ?>"><p class="tileName"><?php echo ucwords($champions[1]); ?></p><p class="tileRole"><?php echo $data_array[0]; ?></p>
				</div>
				<div class="col-1" id="champ2" name="<?php echo $data_array[3]; ?>"><p class="tileName"><?php echo ucwords($champions[3]); ?></p><p class="tileRole"><?php echo $data_array[2]; ?></p>
				</div>
				<div class="col-1" id="champ3" name="<?php echo $data_array[5]; ?>"><p class="tileName"><?php echo ucwords($champions[5]); ?></p><p class="tileRole"><?php echo $data_array[4]; ?></p>
				</div>
				<div class="col-1" id="champ4" name="<?php echo $data_array[7]; ?>"><p class="tileName"><?php echo ucwords($champions[7]); ?></p><p class="tileRole"><?php echo $data_array[6]; ?></p>
				</div>
				<div class="col-1" id="champ5" name="<?php echo $data_array[9]; ?>"><p class="tileName"><?php echo ucwords($champions[9]); ?></p><p class="tileRole"><?php echo $data_array[8]; ?></p>
				</div>
			</div>
		</div>
	</body>
</html>