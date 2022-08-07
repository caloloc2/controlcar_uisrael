<?php

require __DIR__.'/vendor/autoload.php';

use Kreait\Firebase\Factory;

$factory = (new Factory)->withServiceAccount('llave.json')->withDatabaseUri('https://carrouisrael-default-rtdb.firebaseio.com/');


$database = $factory->createDatabase();

$bloqueo = $database->getReference('bloqueo')->getSnapshot()->getValue();
$activacion = $database->getReference('activacion')->getSnapshot()->getValue();
$desactivacion = $database->getReference('desactivacion')->getSnapshot()->getValue();
$apagado = $database->getReference('apagado')->getSnapshot()->getValue();

$nuevoUsuario = $database->getReference('nuevoUsuario')->getSnapshot()->getValue();

$respuesta['estados'] = array(
    "bloqueo" => (int) $bloqueo,
    "activacion" => (int) $activacion,
    "desactivacion" => (int) $desactivacion,
    "apagado" => (int) $apagado,
    "nuevoUsuario" => (int) $nuevoUsuario
);

echo json_encode($respuesta);

// $database->getReference('locacion')->set('New name');