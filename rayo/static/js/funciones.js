var nombre = document.getElementById('nombre');
var usuario = document.getElementById('usuario');
var rut = document.getElementById('rut');
var mail = document.getElementById('mail');
var mail2 = document.getElementById('mail2');
var password = document.getElementById('password');
var password2 = document.getElementById('password2');

var error = document.getElementById('error');
var error2 = document.getElementById('error2');
var error3 = document.getElementById('error3');
var error4 = document.getElementById('error4');
var error5 = document.getElementById('error5');
var error6 = document.getElementById('error6');
var error7 = document.getElementById('error7');

var Fn = {
  validaRut: function (rutCompleto) {
    rutCompleto = rutCompleto.replace("‐", "-");
    if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rutCompleto))
      return false;
    var tmp = rutCompleto.split("-");
    var digv = tmp[1];
    var rut = tmp[0];
    if (digv == 'K') digv = 'k';

    return (Fn.dv(rut) == digv);
  },
  dv: function (T) {
    var M = 0,
      S = 1;
    for (; T; T = Math.floor(T / 10))
      S = (S + T % 10 * (9 - M++ % 6)) % 11;
    return S ? S - 1 : 'k';
  }
};

error.style.color = 'red';
error2.style.color = 'red';
error3.style.color = 'red';
error4.style.color = 'red';
error5.style.color = 'red';
error6.style.color = 'red';
error7.style.color = 'red';

function validarform() {
  var mensajeError = [];
  var mensajeError2 = [];
  var mensajeError3 = [];
  var mensajeError4 = [];
  var mensajeError5 = [];
  var mensajeError6 = [];
  var mensajeError7 = [];
  console.log('enviado');

  if (nombre.value === null || nombre.value === '') {
    mensajeError.push('Ingresa tu nombre');
    error.innerHTML = mensajeError;
  } else {
    mensajeError.push('');
    error.innerHTML = mensajeError;
  }

  if (usuario.value === null || usuario.value === '') {
    mensajeError2.push('Ingresa apellido');
    error2.innerHTML = mensajeError2;
  } else {
    mensajeError2.push('');
    error2.innerHTML = mensajeError2;
  }

  if (mail.value === null || mail.value === '') {
    mensajeError3.push('Ingresa tu Email');
    error3.innerHTML = mensajeError3;
  } else {
    mensajeError3.push('');
    error3.innerHTML = mensajeError3;
  }

  if (mail2.value === null || mail2.value === '' || mail.value != mail2.value) {
    mensajeError4.push('Ambos campos deben coincidir');
    error4.innerHTML = mensajeError4;
  } else {
    mensajeError4.push('');
    error4.innerHTML = mensajeError4;
  }

  if (password.value === null || password.value === '') {
    mensajeError5.push('Ingresa tu contraseña');
    error5.innerHTML = mensajeError5;
  } else {
    mensajeError5.push('');
    error5.innerHTML = mensajeError5;
  }

  if (password2.value === null || password2.value === '') {
    mensajeError6.push('Repite tu contraseña');
    error6.innerHTML = mensajeError6;
  } else if (password2.value != password.value) {
    mensajeError6.push('Ambas contraseñas deben coincidir');
    error6.innerHTML = mensajeError6;
  } else {
    mensajeError6.push('');
    error6.innerHTML = mensajeError6;
  }

  if (rut.value === null || rut.value === '') {
    mensajeError7.push('Ingresa tu rut');
    error7.innerHTML = mensajeError7;
  } else {
    if (Fn.validaRut(rut.value)) {
      mensajeError7.push('');
      error7.innerHTML = mensajeError7;
      document.getElementById("msgerror").innerHTML = "El rut ingresado es válido";
      document.getElementById("msgerror").style.color = "green";
    } else {
      mensajeError7.push('');
      error7.innerHTML = mensajeError7;
      document.getElementById("msgerror").innerHTML = "El Rut no es válido";
      document.getElementById("msgerror").style.color = "red";
    }
  }

  return false;
}

var form = document.getElementById('registro');
form.addEventListener('submit', function (evt) {
  console.log('enviando formulario');
});

   

    