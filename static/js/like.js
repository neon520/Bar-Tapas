$(document).ready(function() {

  $('[id^="likes"]').click(function(){
      var tapas;
      tapas = $(this).attr("data-tapa");
      $.get('/like_tapa/', {tapa_id : tapas}, function(data){
                 $('#like_count'+tapas).html(data);
                 $('#likes'+tapas).hide();
      });
  });
});
