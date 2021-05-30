$(document).ready(function(){
	$("#editfile1").hide()
	$("#downoloadfile1").hide()
	$("#delfile1").hide()
	
	$("#editfile2").hide()
	$("#downoloadfile2").hide()
	$("#delfile2").hide()
	
	$("#editfile3").hide()
	$("#downoloadfile3").hide()
	$("#delfile3").hide()
	
	$("#editfile4").hide()
	$("#downoloadfile4").hide()
	$("#delfile4").hide()
	
	$("#editfile5").hide()
	$("#downoloadfile5").hide()
	$("#delfile5").hide()
	
        $.ajax({
            url: '/myFilesJS',
            dataType: 'json',
            success: function(response) {
                var count = Object.keys(response).length;
                document.getElementById('file1').innerHTML = "wolne miejsce"
                document.getElementById('file2').innerHTML = "wolne miejsce"
                document.getElementById('file3').innerHTML = "wolne miejsce"
                document.getElementById('file4').innerHTML = "wolne miejsce"
                document.getElementById('file5').innerHTML = "wolne miejsce"
                if (count == 1){
                    document.getElementById('file1').innerHTML = response[0][2]
                    document.getElementById('file2').innerHTML = "wolne miejsce"
                    document.getElementById('file3').innerHTML = "wolne miejsce"
                    document.getElementById('file4').innerHTML = "wolne miejsce"
                    document.getElementById('file5').innerHTML = "wolne miejsce"
					$("#editfile1").show()
					$("#downoloadfile1").show()
					$("#delfile1").show()
                }
                if (count == 2){
                    document.getElementById('file1').innerHTML = response[0][2]
                    document.getElementById('file2').innerHTML = response[1][2]
                    document.getElementById('file3').innerHTML = "wolne miejsce"
                    document.getElementById('file4').innerHTML = "wolne miejsce"
                    document.getElementById('file5').innerHTML = "wolne miejsce"
					$("#editfile1").show()
					$("#downoloadfile1").show()
					$("#delfile1").show()
					$("#editfile2").show()
					$("#downoloadfile2").show()
					$("#delfile2").show()
                }
                if (count == 3){
                    document.getElementById('file1').innerHTML = response[0][2]
                    document.getElementById('file2').innerHTML = response[1][2]
                    document.getElementById('file3').innerHTML = response[2][2]
                    document.getElementById('file4').innerHTML = "wolne miejsce"
                    document.getElementById('file5').innerHTML = "wolne miejsce"
					$("#editfile1").show()
					$("#downoloadfile1").show()
					$("#delfile1").show()
					$("#editfile2").show()
					$("#downoloadfile2").show()
					$("#delfile2").show()
					$("#editfile3").show()
					$("#downoloadfile3").show()
					$("#delfile3").show()
					
                }
                if (count == 4){
                    document.getElementById('file1').innerHTML = response[0][2]
                    document.getElementById('file2').innerHTML = response[1][2]
                    document.getElementById('file3').innerHTML = response[2][2]
                    document.getElementById('file4').innerHTML = response[3][2]
                    document.getElementById('file5').innerHTML = "wolne miejsce"
					$("#editfile1").show()
					$("#downoloadfile1").show()
					$("#delfile1").show()
					$("#editfile2").show()
					$("#downoloadfile2").show()
					$("#delfile2").show()
					$("#editfile3").show()
					$("#downoloadfile3").show()
					$("#delfile3").show()
					$("#editfile4").show()
					$("#downoloadfile4").show()
					$("#delfile4").show()
					
                }
                if (count == 5){
                    document.getElementById('file1').innerHTML = response[0][2]
                    document.getElementById('file2').innerHTML = response[1][2]
                    document.getElementById('file3').innerHTML = response[2][2]
                    document.getElementById('file4').innerHTML = response[3][2]
                    document.getElementById('file5').innerHTML = response[4][2]
					$("#editfile1").show()
					$("#downoloadfile1").show()
					$("#delfile1").show()
					$("#editfile2").show()
					$("#downoloadfile2").show()
					$("#delfile2").show()
					$("#editfile3").show()
					$("#downoloadfile3").show()
					$("#delfile3").show()
					$("#editfile4").show()
					$("#downoloadfile4").show()
					$("#delfile4").show()
					$("#editfile5").show()
					$("#downoloadfile5").show()
					$("#delfile5").show()
					
                }
            }
        });
});