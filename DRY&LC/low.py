#  Violación de Low Coupling (GRASP)
class Pedido:
    def crear_pedido(self, monto):
        print("Creando pedido...")

        # Pedido crea y controla todo (mal diseño)
        pago = PagoTarjeta()
        notificacion = NotificacionEmail()

        if pago.pagar(monto):
            print("Pedido guardado en BD")
            notificacion.enviar(f"Pedido por ${monto} exitoso")
        else:
            print("Error en el pago")
            
class PagoTarjeta:
    def pagar(self, monto):
        print(f"Procesando pago con tarjeta ${monto}")
        return True
        
class NotificacionEmail:
    def enviar(self, mensaje):
        print("Enviando EMAIL:", mensaje)



#  Aplicando  Low Coupling (GRASP)
from abc import ABC, abstractmethod
# 1️ Abstracciones (Reducen dependencia directa)

class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass
class ServicioNotificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass
        
# 2️ Implementaciones concretas
class PagoTarjeta(MetodoPago):
    def pagar(self, monto):
        print(f"Procesando pago con tarjeta ${monto}")
        return True
class NotificacionEmail(ServicioNotificacion):
    def enviar(self, mensaje):
        print("Enviando EMAIL:", mensaje)
        
# 3️ Pedido solo coordina (Responsabilidad correcta)
class Pedido:
    def __init__(self, metodo_pago: MetodoPago, notificacion: ServicioNotificacion):
        self.metodo_pago = metodo_pago
        self.notificacion = notificacion
    def crear_pedido(self, monto):
        print("Creando pedido...")
        if self.metodo_pago.pagar(monto):
            print("Pedido guardado en BD")
            self.notificacion.enviar(f"Pedido por ${monto} exitoso")
        else:
            print("Error en el pago")
