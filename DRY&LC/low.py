from abc import ABC, abstractmethod

# 1️ Abstracciones (Contratos)

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
        print(f"Procesando pago con tarjeta por ${monto}")
        return True


class PagoPayPal(MetodoPago):
    def pagar(self, monto):
        print(f"Procesando pago con PayPal por ${monto}")
        return True


class NotificacionEmail(ServicioNotificacion):
    def enviar(self, mensaje):
        print(f"Enviando EMAIL: {mensaje}")


class NotificacionSMS(ServicioNotificacion):
    def enviar(self, mensaje):
        print(f"Enviando SMS: {mensaje}")


# 3️ Clase principal (Low Coupling aplicado)

class Pedido:
    def __init__(self, metodo_pago: MetodoPago, notificacion: ServicioNotificacion):
        self.metodo_pago = metodo_pago
        self.notificacion = notificacion

    def crear_pedido(self, monto):
        print("Creando pedido...")
        if self.metodo_pago.pagar(monto):
            print("Pedido guardado en base de datos")
            self.notificacion.enviar(f"Tu pedido por ${monto} fue exitoso")
        else:
            print("Error en el pago")


# 4️ Uso del sistema

pago = PagoTarjeta()
notificacion = NotificacionEmail()

pedido = Pedido(pago, notificacion)
pedido.crear_pedido(150000)
