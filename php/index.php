<?php

require __DIR__.'/vendor/autoload.php';

use Kreait\Firebase\Factory;

$factory = (new Factory)->withServiceAccount('llave.json')->withDatabaseUri('https://carrouisrael-default-rtdb.firebaseio.com/');


$database = $factory->createDatabase();

$bloqueo = $database->getReference('bloqueo')->getSnapshot()->getValue();
$activacion = $database->getReference('activacion')->getSnapshot()->getValue();

$respuesta['estados'] = array(
    "bloqueo" => (bool) $bloqueo,
    "activacion" => (bool) $activacion
);

echo json_encode($respuesta);

// $database->getReference('locacion')->set('New name');