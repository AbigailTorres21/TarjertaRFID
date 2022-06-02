<?php
    include("cn.php"); 
    $usuarios = "SELECT * FROM usuarios";
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="estilostablas.css">
    <title>Asistencias</title>
</head>
<body>
   <div class="container-table">
       <div class="table-title">DATOS DE LOS USUARIOS</div>
       <div class="table-header">ID</div>
       <div class="table-header">RFID ID</div>
       <div class="table-header">Nombre Completo</div>
       <div class="table-header">Fecha Creacion</div>
       <?php $resultado = mysqli_query($conexion,
       $usuarios);
       while($row=mysqli_fetch_assoc($resultado)) { ?>
        <div class="table__item"><?php echo $row["id"];?></div>
        <div class="table__item"><?php echo $row["rfid_uid"];?></div>
        <div class="table__item"><?php echo $row["name"];?></div>
        <div class="table__item"><?php echo $row["created"];?></div>
        <?php } mysqli_free_result($resultado);?>
   </div>
</body>
</html>