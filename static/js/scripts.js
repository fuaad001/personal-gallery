$(document).ready(function(){
  $('#me').click(function(event){
    event.preventDefault()
    var copyText = document.getElementById("imageUrl");
    copyText.select();
    document.execCommand("copy");
    alert("Copied the url: " + copyText.value);
  })
})
