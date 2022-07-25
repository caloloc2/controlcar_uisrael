from libs.gpio import GPIORasp
import time 

ledrojo = GPIORasp(19)
lednaranja = GPIORasp(26)
ledverde = GPIORasp(21)
ledamarillo = GPIORasp(20)
ledazul = GPIORasp(16)

try:
    while (True):
        ledrojo.accion(True)
        time.sleep(0.5)
        lednaranja.accion(True)
        time.sleep(0.5)
        ledverde.accion(True)
        time.sleep(0.5)
        ledamarillo.accion(True)
        time.sleep(0.5)
        ledazul.accion(True)
        
        time.sleep(1)
        
        ledrojo.accion(False)
        time.sleep(0.5)
        lednaranja.accion(False)
        time.sleep(0.5)
        ledverde.accion(False)
        time.sleep(0.5)
        ledamarillo.accion(False)
        time.sleep(0.5)
        ledazul.accion(False)

        time.sleep(1)
except KeyboardInterrupt:
    ledrojo.cancel()
    lednaranja.cancel()
    ledverde.cancel()
    ledamarillo.cancel()
    ledazul.cancel()
    print("cancelado")
