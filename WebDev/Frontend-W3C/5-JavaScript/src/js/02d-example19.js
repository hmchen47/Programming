

var m = ['client','page','screen']; // mods
$(document).mousemove(function(e){
  for(var i=0; i<3; i++){
    $('#'+m[i]).text((e[m[i]+'X'])+' '+ (e[m[i]+'Y']));
  }
  $('#scrollTop').text(
    $('html, body').scrollTop()
  );
});

