class ServicioNotificacion:
    def enviar(self, mensaje):
        raise NotImplementedError("Debe implementar el método enviar")
    
class NotificacionEmail(ServicioNotificacion):
    def enviar(self, mensaje):
        print(f"Enviando EMAIL: {mensaje}")

class NotificacionSMS(ServicioNotificacion):
    def enviar(self, mensaje):
        print(f"Enviando SMS: {mensaje}")

class NotificacionWhatsApp(ServicioNotificacion):
    def enviar(self, mensaje):
        print(f"Enviando WHATSAPP: {mensaje}")

class Transferencia:
    def __init__(self, servicio_notificacion: ServicioNotificacion):
        self.servicio_notificacion = servicio_notificacion

    def ejecutar(self, monto, cuenta_destino):
        print(f"Transferencia de ${monto} a la cuenta {cuenta_destino} realizada.")
        
        self.servicio_notificacion.enviar(
            f"Se realizó una transferencia de ${monto} a la cuenta {cuenta_destino}"
        )

email = NotificacionEmail()
transferencia1 = Transferencia(email)
transferencia1.ejecutar(500000, "123-456")

print("-----")

sms = NotificacionSMS()
transferencia2 = Transferencia(sms)
transferencia2.ejecutar(200000, "789-000")