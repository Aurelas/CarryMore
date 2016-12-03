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
			$ns_champ_name = str_replace(" ", "", $champ_name);
			$cleaned_champ_name = str_replace("'", "", $ns_champ_name);
			$lc_clean_name = strtolower($cleaned_champ_name);
			$path = '/var/www/html/carrymore/Main.py';
			$python = '/usr/bin/python';
			$script = $python . " " . $path . " " . $champ_name;
			$command = escapeshellcmd($script);
			$results = exec($command, $my_output, $status);
			$data_array = explode(" , ", $results);

			$user_role = $data_array[0];
			$user_champ = $data_array[1];

			$champ_name[0] = $data_array[1];
			$champ_name[1] = $data_array[3];
			$champ_name[2] = $data_array[5];
			$champ_name[3] = $data_array[7];
			$champ_name[4] = $data_array[9];

			for ($i = 0; $i <= 4; $i++) {
				switch ($champ_name[i]) {
					case "aurelionsol":
						$champ_name[i] = "Aurelion Sol";
						break;
					case "chogath":
						$champ_name[i] = "Cho'Gath";
						break;
					case "drmundo":
						$champ_name[i] = "Dr. Mundo";
						break;
					case "jarvaniv":
						$champ_name[i] = "Jarvan IV";
						break;
					case "khazix":
						$champ_name[i] = "Kha'Zix";
						break;
					case "kogmaw":
						$champ_name[i] = "Kog'Maw";
						break;
					case "leesin":
						$champ_name[i] = "Lee Sin";
						break;
					case "masteryi":
						$champ_name[i] = "Master Yi";
						break;
					case "missfortune":
						$champ_name[i] = "Miss Fortune";
						break;
					case "reksai":
						$champ_name[i] = "Rek'Sai";
						break;
					case "aurelionsol":
						$champ_name[i] = "Aurelion Sol";
						break;
					case "tahmkench":
						$champ_name[i] = "Tahm Kench";
						break;
					case "twistedfate":
						$champ_name[i] = "Twisted Fate";
						break;
					case "velkoz":
						$champ_name[i] = "Vel'Koz";
						break;
					case "xinzhao":
						$champ_name[i] = "Xin Zhao";
						break;
				}
			}
			$c1 = ucfirst($champ_name[0]);
		?>
		<div class="outer">
			<div class="inner">
				<div class="col-1" id="champ1" name="<?php echo $user_champ; ?>"><p class="tileName"><?php echo $c1; ?></p><p class="tileRole"><?php echo $user_role; ?></p>
				</div>
				<div class="col-1" id="champ2" name="<?php echo $data_array[3]; ?>"><p class="tileName"><?php echo ucwords($champ_name[1]); ?></p><p class="tileRole"><?php echo $data_array[2]; ?></p>
				</div>
				<div class="col-1" id="champ3" name="<?php echo $data_array[5]; ?>"><p class="tileName"><?php echo ucwords($champ_name[2]); ?></p><p class="tileRole"><?php echo $data_array[4]; ?></p>
				</div>
				<div class="col-1" id="champ4" name="<?php echo $data_array[7]; ?>"><p class="tileName"><?php echo ucfirst($champ_name[3]); ?></p><p class="tileRole"><?php echo $data_array[6]; ?></p>
				</div>
				<div class="col-1" id="champ5" name="<?php echo $data_array[9]; ?>"><p class="tileName"><?php echo ucfirst($champ_name[4]); ?></p><p class="tileRole"><?php echo $data_array[8]; ?></p>
				</div>
			</div>
		</div>
	</body>
</html>