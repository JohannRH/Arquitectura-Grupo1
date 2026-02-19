# Cambio de Impuestos: El gobierno cambió el IVA del 15% al 19%. Actualicen el sistema.
# Migración de Datos: Ya no usaremos SQLite, ahora los datos se envían a una API externa en la nube. Cambien la forma de guardar.
# Nuevos Canales: Queremos que las ventas online también notifiquen por WhatsApp, no solo por email.

import sqlite3

class SalesManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def process_online_sale(self, item_name, price, quantity, customer_email):
        tax = price * 0.15
        total = (price + tax) * quantity

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO sales (item, total, type) VALUES (?, ?, ?)",
            (item_name, total, 'ONLINE')
        )
        conn.commit()
        conn.close()

        # Notificación rígida (Feature Envy)
        print(f"ENVIANDO EMAIL A {customer_email}: Gracias por comprar {item_name}. Total: ${total}")

    def process_store_sale(self, item_name, price, quantity):
        tax = price * 0.15
        total = (price + tax) * quantity

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO sales (item, total, type) VALUES (?, ?, ?)",
            (item_name, total, 'STORE')
        )
        conn.commit()
        conn.close()

        print(f"RECIBO IMPRESO: {item_name} - Total: ${total}")