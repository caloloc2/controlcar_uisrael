<?php

require __DIR__.'/vendor/autoload.php';

use Kreait\Firebase\Factory;

$factory = (new Factory)->withServiceAccount('llave.json')->withDatabaseUri('https://carrouisrael-default-rtdb.firebaseio.com/');


$database = $factory->createDatabase();

$respuesta['estado'] = false;

$database->getReference('alarma')->set($_GET['valor']);
$respuesta['estado'] = true;

echo json_encode($respuesta);