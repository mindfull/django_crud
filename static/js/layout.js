$(function(){
	$("#boardList tr").click(function(){
		window.location.href = $(this).children("th").children("a").attr("href");
	});
});