<?php

require __DIR__.'/vendor/autoload.php';

use Kreait\Firebase\Factory;

$factory = (new Factory)->withServiceAccount('llave.json')->withDatabaseUri('https://carrouisrael-default-rtdb.firebaseio.com/');


$database = $factory->createDatabase();

$respuesta['estado'] = false;

if (isset($_GET['info'])){
    $database->getReference('informacion')->set($_GET['info']);
    $respuesta['estado'] = true;
}

echo json_encode($respuesta);