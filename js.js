
var miBoton = document.getElementById("miBoton");
var miModal = document.getElementById("miModal");
var cerrar = document.getElementsByClassName("cerrar")[0];

miBoton.onclick = function() {
  miModal.style.display = "block";
}

cerrar.onclick = function() {
  miModal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == miModal) {
    miModal.style.display = "none";
  }
 
}



