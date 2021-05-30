$(document).ready(function(){

    $('#buttonSignUp').click(function() {
        $.ajax({
            url: '/signUp',
            data: $('form').serialize(),
            type: 'POST',
            dataType: 'text',
            success: function(response) {
                document.getElementById("registertry").innerHTML = response;
            },

        });
    });
});