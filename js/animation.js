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
	champName = document.getElementById("champ1");
	champURL = "champions/" + champName + ".jpg";
	$('div#champ1').css({
		'background' : 'url(' + champURL +') no-repeat center center fixed',
		'-webkit-background-size' : 'cover',
		'-moz-background-size' : 'cover',
		'-o-background-size' : 'cover',
		'background-size' : 'cover',
		'transition-duration': '.5s' 
    });
});