<?php

require __DIR__.'/vendor/autoload.php';

use Kreait\Firebase\Factory;

$factory = (new Factory)->withServiceAccount('llave.json')->withDatabaseUri('https://carrouisrael-default-rtdb.firebaseio.com/');


$database = $factory->createDatabase();


if (((isset($_GET['lng'])) && (!empty($_GET['lng']))) && ((isset($_GET['lat'])) && (!empty($_GET['lat'])))){
    
    $database->getReference('locacion/longitud')->set($_GET['lng']);
    $database->getReference('locacion/latitud')->set($_GET['lat']);

    echo "ok";
}
