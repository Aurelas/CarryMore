$(document).ready(function(){
    $('#champ').mouseenter(function(){
   		$('#champ').css({
			'border-color': 'rgba(35, 32, 32, 1)',			
			'border-right-width': 3,
			'border-left-width': 3,
			'border-top-width': 1,
			'border-bottom-width': 1,
	    });
	}); 
    $('#champ').mouseleave(function(){
    	$('#champ').css({
			'border-color': 'rgba(239, 236, 202, 1)',			
			'border-right-width': 10,
			'border-left-width': 10,
			'border-top-width': 0,
			'border-bottom-width': 0,
		});
    });
    $('#champnum').mouseenter(function(){
   		$('#champnum').css({
			'border-color': '#40a0a5',			
			'border-right-width': 3,
			'border-left-width': 3,
			'border-top-width': 1,
			'border-bottom-width': 1,
	    });
	}); 
    $('#champnum').mouseleave(function(){
    	$('#champnum').css({
			'border-color': 'rgba(20, 91, 95, .5)',	
			'border-right-width': 10,
			'border-left-width': 10,
			'border-top-width': 0,
			'border-bottom-width': 0,
		});
    });



	// input box pretty stuff

	$('input:text').one('focus', function(){
	    this.value = '';
	}); 

	$('input:text').one('focus blur', function() {
	    $(this).toggleClass('glow');
	    $(this).css({
			'border-right-width': 10,
			'border-left-width': 10,
			'border-top-width': 0,
			'border-bottom-width': 0,
	    })
	});
	//backgrounds for the champions
	champ1Name = document.getElementById("champ1").getAttribute("name");
	champ1URL = "champions/" + champ1Name + ".jpg";
	$('div#champ1').css({
		'background' : 'url(' + champ1URL +') no-repeat left top',
		'transition-duration': '.5s',
		'background-size' : '100%'
    });

	champ2Name = document.getElementById("champ2").getAttribute("name");
	champ2URL = "champions/" + champ2Name + ".jpg";
	$('div#champ2').css({
		'background' : 'url(' + champ2URL +') no-repeat left top',
		'transition-duration': '.5s',
		'background-size' : '100%'
    });

	champ3Name = document.getElementById("champ3").getAttribute("name");
	champ3URL = "champions/" + champ3Name + ".jpg";
	$('div#champ3').css({
		'background' : 'url(' + champ3URL +') no-repeat left top',
		'transition-duration': '.5s',
		'background-size' : '100%' 
    });

	champ4Name = document.getElementById("champ4").getAttribute("name");
	champ4URL = "champions/" + champ4Name + ".jpg";
	$('div#champ4').css({
		'background' : 'url(' + champ4URL +') no-repeat left top',
		'transition-duration': '.5s',
		'background-size' : '100%' 
    });

	champ5Name = document.getElementById("champ5").getAttribute("name");
	champ5URL = "champions/" + champ5Name + ".jpg";
	$('div#champ5').css({
		'background' : 'url(' + champ5URL +') no-repeat left top',
		'transition-duration': '.5s',
		'background-size' : '100%' 
    });
});