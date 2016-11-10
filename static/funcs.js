	function hideind(){$('#index').css("display","none");};
	function hidewin(){$('#success').css("display","none");};
	function hideboot(){$('#bootstrap').css("display","none");};
	function visind(){hidewin();
	hideboot();
	$('#index').css("display","inline");};
	function viswin(){hideind();
	hideboot();
	$('#success').css("display","inline");};
	function visboot(){hideind();
	hideboot();
	$('#bootstrap').css("display","inline");}
	
	function runcaru(){$('#carousel-example-generic').carousel({interval: 200});};
	
	function first(){$('#carousel-example-generic').carousel(0);};
