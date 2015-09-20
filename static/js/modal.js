var windowHeight = $(window).height();
var boxHeight = $('.modal-dialog').height();
$('.modal-dialog').css({'margin-top' : ((windowHeight - boxHeight )/4)});
