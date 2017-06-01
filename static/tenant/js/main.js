$( document ).ready(function(){
  $(".alert").fadeIn("slow").delay(2000).fadeOut("slow");
  $('.datepicker').pikaday({ firstDay: 1 });
  $('#id_file').addClass('inputfile');



  function tabActive(id){
    $('.active').removeClass('active');
    $(id).addClass('active')
  }

  

});
