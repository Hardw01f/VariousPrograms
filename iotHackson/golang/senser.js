	var date=new Date();
	var year = date.getFullYear();
	var month = date.getMonth()+1;
	//var week = date.getDay();
	var day = date.getDate();
	var hours = date.getHours();
  	var minutes = date.getMinutes();	

	var now = year + '-' + month + '-' + day + '-' + hours + '-' + minutes; 	
	console.log(now);
