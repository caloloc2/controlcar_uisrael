<?php

require __DIR__.'/vendor/autoload.php';

use Kreait\Firebase\Factory;

$factory = (new Factory)->withServiceAccount('llave.json')->withDatabaseUri('https://carrouisrael-default-rtdb.firebaseio.com/');


$database = $factory->createDatabase();

$nuevo = $database->getReference('nuevo')->getSnapshot()->getValue();
$respuesta['estado'] = false;
if ($nuevo == 1){
    $respuesta['estado'] = true;
}

echo json_encode($respuesta);