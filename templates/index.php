<?php
    include 'cn.php';
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <link rel="stylesheet" href="/static/style.css">
    <title>RFID</title>
</head>
<body>
    <header>
        <a href="#" class="logo">
            <img src="/static/logo.png" alt="logo-proyecto">
            <h2 class="nombre-empresa">RFID</h2>
        </a>
    
       <nav class="nav-link">
           
           
            <a href="{{url_for('usuarios')}}">Usuarios</a>
           
           <a href="{{url_for('asistencias')}}">Asistencia</a>
            
        </nav>
    
    </header>
    <form action="/clic">
      <button> <b href="#" style ="--clr:#ff1867"><span>Pulsar para pasar Asistencia</span><i></i></b></button>
    </form>
</body>
</html>
