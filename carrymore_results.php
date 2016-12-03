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
				if ($champion[i] == "aurelionsol") {
					$champions[i] = "Aurelion Sol";
				}
				elseif ($champion[i] == "chogath"){
					$champions[i] = "Cho'Gath";
				}
				elseif ($champion[i] == "drmundo"){
					$champions[i] = "Dr. Mundo";
				}
				elseif ($champion[i] == "jarvaniv"){
					$champions[i] = "Jarvan IV";
				}
				elseif ($champion[i] == "khazix"){
					$champions[i] = "Kha'Zix";
				}
				elseif ($champion[i] == "kogmaw"){
					$champions[i] = "Kog'Maw";
				}
				elseif ($champion[i] == "leesin"){
					$champions[i] = "Lee Sin";
				}
				elseif ($champion[i] == "masteryi"){
					$champions[i] = "Master Yi";
				}
				elseif ($champion[i] == "missfortune"){
					$champions[i] = "Miss Fortune";
				}
				elseif ($champion[i] == "reksai"){
					$champions[i] = "Rek'Sai";
				}
				elseif ($champion[i] == "aurelionsol"){
					$champions[i] = "Aurelion Sol";
				}
				elseif ($champion[i] == "tahmkench"){
					$champions[i] = "Tahm Kench";
				}
				elseif ($champion[i] == "twistedfate")
					$champions[i] = "Twisted Fate";
				}
				elseif ($champion[i] == "velkoz"){
					$champions[i] = "Vel'Koz";
				}
				elseif ($champion[i] == "xinzhao"){
					$champions[i] = "Xin Zhao";
				}
				else {
					#nothing
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