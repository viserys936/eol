$('#form1').submit(function(e){
				$('#btn1').click();
				e.preventDefault();
                txt = $('#locations').val();
                $.post("/location_detail",{locations:txt},function(result){
    				$("#show").html(result);
  				});
  				$('#btn2').css('display','none');
  				$('#to_hide').css('display','none');
});