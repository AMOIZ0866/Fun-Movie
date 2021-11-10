

// Function for Slider
var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < slides.length; i++) {
    slides[i].className = slides[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
 
  setTimeout(showSlides, 2000); // Change image every 2 seconds
}


$(document).ready(function(){
  $("#s1").click(function(){
      $(this).css("color", "rgba(220,180,30,1)");
      $("#s2").css("color", "rgba(20,20,20,1)");
      $("#s3").css("color", "rgba(20,20,20,1)");
      $("#s4").css("color", "rgba(20,20,20,1)");
      $("#s5").css("color", "rgba(20,20,20,1)");
  });
 $("#s2").click(function(){
      $(this).css("color", "rgba(220,180,30,1)");
      $("#s1").css("color", "rgba(220,180,30,1)");
      $("#s3").css("color", "rgba(20,20,20,1)");
      $("#s4").css("color", "rgba(20,20,20,1)");
      $("#s5").css("color", "rgba(20,20,20,1)");
  });
   $("#s3").click(function(){
      $(this).css("color", "rgba(220,180,30,1)");
      $("#s1").css("color", "rgba(220,180,30,1)");
      $("#s2").css("color", "rgba(220,180,30,1)");
      $("#s4").css("color", "rgba(20,20,20,1)");
      $("#s5").css("color", "rgba(20,20,20,1)");
  });
   $("#s4").click(function(){
      $(this).css("color", "rgba(220,180,30,1)");
      $("#s1").css("color", "rgba(220,180,30,1)");
      $("#s2").css("color", "rgba(220,180,30,1)");
      $("#s3").css("color", "rgba(220,180,30,1)");
      $("#s5").css("color", "rgba(20,20,20,1)");
  });
   $("#s5").click(function(){
      $(this).css("color", "rgba(220,180,30,1)");
      $("#s1").css("color", "rgba(220,180,30,1)");
      $("#s2").css("color", "rgba(220,180,30,1)");
      $("#s3").css("color", "rgba(220,180,30,1)");
      $("#s4").css("color", "rgba(220,180,30,1)");
  });
});