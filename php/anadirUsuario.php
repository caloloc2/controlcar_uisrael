<?php

require __DIR__.'/vendor/autoload.php';

use Kreait\Firebase\Factory;

$factory = (new Factory)->withServiceAccount('llave.json')->withDatabaseUri('https://carrouisrael-default-rtdb.firebaseio.com/');


$database = $factory->createDatabase();

$nombreUsuario = "";
$nuevo = $database->getReference('nuevo')->getSnapshot()->getValue();
$nombreUsuario = $database->getReference('nombreUsuario')->getSnapshot()->getValue();

$respuesta['estado'] = false;
if ($nuevo == 1){
    $respuesta['estado'] = true;
    $respuesta['nombre'] = $nombreUsuario;
}

echo json_encode($respuesta);