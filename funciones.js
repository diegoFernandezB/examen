var nombre = document.getElementById('nombre');
var usuario = document.getElementById('usuario');
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


error.style.color = 'red';
error2.style.color = 'red';
error3.style.color = 'red';
error4.style.color = 'red';
error5.style.color = 'red';
error6.style.color = 'red';

function validarform(){
    var mensajeError = [];
    var mensajeError2 = [];
    var mensajeError3 = [];
    var mensajeError4 = [];
    var mensajeError5 = [];
    var mensajeError6 = [];
    console.log('enviado')

    if(nombre.value === null || nombre.value === '' ){
        mensajeError.push('Ingresa tu nombre');
        error.innerHTML = mensajeError
        // document.getElementById('msj_nombre').innerHTML = 'Ingresa tu nombre poorfavor';
        // document.getElementById('msj_nombre').classList = 'text-warning';
    }
     if(usuario.value === null || usuario.value ==='' ){
        mensajeError2.push('Ingresa tu usuario');
        error2.innerHTML = mensajeError2
        // document.getElementById('msj_usuario').innerHTML = 'Ingresa un usuario valido';
        // document.getElementById('msj_usuario').classList = 'text-warning';
    }
    if(mail.value === null || mail.value ==='' ){
        mensajeError3.push('Ingresa tu Email');
        error3.innerHTML = mensajeError3
        // document.getElementById('msj_mail').innerHTML = 'Ingresa un Mail Valido';
        // document.getElementById('msj_mail').classList = 'text-warning';
    }
    if(mail2.value === null || mail2.value ==='' || mail.value != mail2.value){
        mensajeError4.push('ambos campos deben coincidir');
        error4.innerHTML = mensajeError4
        // document.getElementById('msj_mail2').innerHTML = 'Los campos no coinciden';
        // document.getElementById('msj_mail2').classList = 'text-warning';
    }
    if(password.value === null || password.value ==='' ){
        mensajeError5.push('Ingresa tu contraseña');
        error5.innerHTML = mensajeError5
        // document.getElementById('msj_pass').innerHTML = 'Contraseña invalida';
        // document.getElementById('msj_pass').classList = 'text-warning';
    }
    if(password2.value === null || password2.value ==='' ){
        mensajeError6.push('Ingresa tu contraseña');
        error6.innerHTML = mensajeError6
    //     document.getElementById('msj_pass2').innerHTML = 'Las contarseñas no coinciden';
    //     document.getElementById('msj_pass2').classList = 'text-warning';
    }
    if(password2.value != password.value ){
        mensajeError6.push('Ambas contraseñas deben coincidir');
        error6.innerHTML = mensajeError6
    //     document.getElementById('msj_pass2').innerHTML = 'Las contarseñas no coinciden';
    //     document.getElementById('msj_pass2').classList = 'text-warning';
    }

    return false;
}

var form = document.getElementById('registro');
    form.addEventListener('submit', function(evt){
        console.log('enviando formulario')
    });
