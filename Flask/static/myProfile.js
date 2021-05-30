$(document).ready(function(){
		
		$.ajax({
            url: '/myProfileJS',
            dataType: 'json',
            success: function(response) {
				document.getElementById('login').innerHTML = response[0][1]
                document.getElementById('email').innerHTML = response[0][2]
                document.getElementById('password').innerHTML = response[0][3]
			}
		});

});