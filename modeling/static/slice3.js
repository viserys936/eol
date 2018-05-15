$('#form1').submit(function(e){
				$('#btn1').click();
				e.preventDefault();
                txt = $('#locations').val();
                $.post("/evaluate_output",{locations:txt},function(result){
    				$("#show").html(result);
    				$('#show').css('float','right').css('margin-right','220px');
    				$('#showPuzzle').css('float','left');
  				});
  				$('#btn2').css('display','none');
  				$('#to_hide').css('display','none');
});