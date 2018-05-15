$(window).load(function(){
	var puzzleX = 64, 
		puzzleY = 64;
 
	var $puzzleImg = $('#puzzleImg'), 
		puzzleImgSrc = $puzzleImg.attr('src');

	var puzzleWidth = parseInt($puzzleImg.css('width'), 10), 
		puzzleHeight = parseInt($puzzleImg.css('height'), 10);

	$('#showPuzzle').css({
		width: puzzleWidth + 1,
		height: puzzleHeight + 1
	});

	var picW = Math.round(puzzleWidth / puzzleX), 
		picH = Math.round(puzzleHeight / puzzleY);

for(var i=0;i<puzzleX;i++){
	for(var j=0;j<puzzleY;j++){

		var _posLeft = Math.round(-i * picW)+'px', 
			_posTop = Math.round(-j * picH)+'px';

			var _span = $('<span />').css({
				position: 'absolute',
				overflow: 'hidden',
				width: picW - 1,
				height: picH - 1,
				left: i * picW + 1,
				top: j * picH + 1,
				backgroundImage: 'url(' + puzzleImgSrc + ')',
				backgroundPosition: _posLeft + ' ' + _posTop,
				opacity: 0.6
			}).click(function(){
				$(this).css('opacity', 1);
				//$(this).html('<div style="width:16px;height:16px;background:#F00;opacity:0.2"></div>');
				record();
			})


		$('#showPuzzle').append(_span);
	}
}

});

function record(){
	
	var mx = x.value - window.pageYOffset;
	var my = y.value;
	
	var px = Math.ceil((mx-8)/16);
	var py = Math.ceil((my-8)/16);
	//alert(px+' , '+py);
	
	var n = (py-1) * 64 +px;
	alert(n);
	setTrue(n);
}

function doFirst(){
					//alert("First");
					array = new Array(4096);
					for (i = 0 ; i < 4096 ; i++) {
						array[i] = false;
					}
					locations = "";
					
}

function setTrue(n){
					//alert("this is " + n);					
					array[n-1] = true;
					locations += String(n-1) + ",";
}
				
function calSum(array){
	var count = 0;
	for (i = 0 ; i < 4096 ; i++) {
		if(array[i]==true){
			count++;
		}
	}
	var loc = document.getElementById("locations");
	loc.setAttribute("value", locations);
//	var form1 = document.getElementById("form1");
//	form1.submit();
}