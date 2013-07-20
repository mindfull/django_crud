$(function(){
	$("#boardList tr").click(function(){
		window.location.href = $(this).children("th").children("a").attr("href");
	});
	
	if($(window).height()-407 > $("#pageContent").height()) {
		$("#pageContent").height($(window).height()-407);
	}
});