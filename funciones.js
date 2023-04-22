/*var form = document.getElementById('registro');
    form.addEventListener('submit',function(evento){
        evento.preventDefault();
        var mensajeError=[];
        if(nombre.value === null || nombre.value ==='' ){
            mensajeError.push('Ingresa tu nombre');
        }
        if(usuario.value === null || usuario.value ==='' ){
            mensajeError.push('Ingresa tu usuario');
        }
        if(mail.value === null || mail.value ==='' ){
            mensajeError.push('Ingresa tu Email');
        }
        if(mail2.value === null || mail2.value ==='' ){
            mensajeError.push('ambos campos deben coincidir');
        }
        if(password.value === null || password.value ==='' ){
            mensajeError.push('Ingresa tu contraseña');
        }
        if(password2.value === null || password2.value ==='' ){
            mensajeError.push('Ingresa tu contraseña');
        }
        s
    });*/

function validarform(){
    var nombre = document.getElementById('nombre');
    var usuario = document.getElementById('usuario');
    var mail = document.getElementById('mail');
    var mail2 = document.getElementById('mail2');
    var password = document.getElementById('password');
    var password2 = document.getElementById('password2');
    
    if(nombre.value == null || nombre.value == '' ){
        //mensajeError.push('Ingresa tu nombre');
        document.getElementById('msj_nombre').innerHTML = 'Ingresa tu nombre porfavor';
        document.getElementById('msj_nombre').classList = 'text-warning';
    }
    if(usuario.value === null || usuario.value ==='' ){
        //mensajeError.push('Ingresa tu usuario');
    }
    if(mail.value === null || mail.value ==='' ){
        //mensajeError.push('Ingresa tu Email');
    }
    if(mail2.value === null || mail2.value ==='' ){
        //mensajeError.push('ambos campos deben coincidir');
    }
    if(password.value === null || password.value ==='' ){
        //mensajeError.push('Ingresa tu contraseña');
    }
    if(password2.value === null || password2.value ==='' ){
        //mensajeError.push('Ingresa tu contraseña');
    }

    return false;
}