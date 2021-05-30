$(document).ready(function(){
	var temp1
	$("#editfile1").click(function(){
		$.ajax({
			url: '/edit1File',
			dataType: 'json',
			success: function(response){
				console.log(response);
				temp1 = response;
			}
		})
	});
	$("#editfile2").click(function(){
		$.ajax({
			url: '/edit2File',
			dataType: 'json',
			success: function(response){
				console.log(response);
				temp1 = response;
			}
		})
	});
	$("#editfile3").click(function(){
		$.ajax({
			url: '/edit3File',
			dataType: 'json',
			success: function(response){
				console.log(response);
				temp1 = response;
			}
		})
	});
	$("#editfile4").click(function(){
		$.ajax({
			url: '/edit4File',
			dataType: 'json',
			success: function(response){
				console.log(response);
				temp1 = response;
			}
		})
	});
	$("#editfile5").click(function(){
		$.ajax({
			url: '/edit5File',
			dataType: 'json',
			success: function(response){
				console.log(response);
				temp1 = response;
			}
		})
	});
	
});