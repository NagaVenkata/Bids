/**
 * 
 */

var $item;
var count;


function initImageSlider()
{
	var $imageslider = $('#image_slider');
	
	$items_length = $imageslider.children.length;
	
	$items = $('#image_slider').children();
	
	$item = $('.active1');
	
	console.log($item);
	
	count = 0;
	
	$('#nextImage').click(function(){
		
		 nextImage();
		
		
		
	});
	
    $('#backImage').click(function(){
		
    	
    		backImage();
		
		
	});
	
	
	
	/*var ss_timer = setInterval(function() {
		nextImage();
	  },3000)*/
}

function nextImage()
{
	
	$item.removeClass('.active1');
	
	$item.animate({
	        "margin-left": (-250.0)
	      }, 3000);
	$item.next().addClass('active1');
	$item = $item.next();
	
	$item.animate({
        "margin-left": (0.0)
      }, 3000);
}

function backImage()
{
	
	$item.removeClass('.active1');
	
	$item.animate({
	        "margin-left": 250.0
	      }, 3000);
	$item.prev().addClass('active1');
	
	$item = $item.prev();
	
	$item.animate({
        "margin-left": 0.0
      }, 3000);
	
}