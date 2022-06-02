<?php
    include("cn.php"); 
    $asistencia = "SELECT * FROM asistencia";
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="estilosasistencia.css">
    <title>Asistencia</title>
</head>
<body>
   <div class="container-table">
       <div class="table-title">REGISTROS</div>
       <div class="table-header">ID</div>
       <div class="table-header">ID USUARIO</div>
       <div class="table-header">Fecha y Hora</div>
       <?php $resultado = mysqli_query($conexion,
       $asistencia);
       while($row=mysqli_fetch_assoc($resultado)) { ?>
        <div class="table__item"><?php echo $row["id"];?></div>
        <div class="table__item"><?php echo $row["user_id"];?></div>
        <div class="table__item"><?php echo $row["clock_in"];?></div>
        <?php } mysqli_free_result($resultado);?>
   </div>
</body>
</html>