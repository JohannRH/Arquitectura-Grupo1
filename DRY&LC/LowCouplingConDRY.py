#
# Código sin DRY y acoplado
#

import sqlite3

class OrderProcessor:
    def __init__(self, db_path):
        self.db_path = db_path
    
    def create_order(self, customer_email, items):
        total = sum(item['price'] * item['quantity'] for item in items)
        if total > 100:
            total = total * 0.9

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO orders (email, total) VALUES (?, ?)",
            (customer_email, total)
        )
        order_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        print(f"Order {order_id} created. Total: ${total:.2f}")
        return order_id
    
    def update_order(self, order_id, items):
        total = sum(item['price'] * item['quantity'] for item in items)
        if total > 100:
            total = total * 0.9

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE orders SET total = ? WHERE id = ?",
            (total, order_id)
        )
        conn.commit()
        conn.close()
        
        print(f"Order {order_id} updated. New Total: ${total:.2f}")
    
#    
# Código con DRY y bajo acoplamiento
#

class PriceCalculator:
    
    def calculate_total(self, items):
        total = sum(item['price'] * item['quantity'] for item in items)
        return total * 0.9 if total > 100 else total

class OrderRepository:
    
    def __init__(self, db_connection):
        self.db = db_connection
    
    def save_order(self, email, total):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO orders (email, total) VALUES (?, ?)", (email, total))
        self.db.commit()
        return cursor.lastrowid
    
    def update_order(self, order_id, total):
        cursor = self.db.cursor()
        cursor.execute("UPDATE orders SET total = ? WHERE id = ?", (total, order_id))
        self.db.commit()


class NotificationService:
    
    def notify(self, message):
        print(message)


class OrderService:
    
    def __init__(self, repository, calculator, notifier):
        self.repository = repository
        self.calculator = calculator
        self.notifier = notifier
    
    def create_order(self, customer_email, items):
        total = self.calculator.calculate_total(items)
        order_id = self.repository.save_order(customer_email, total)
        self.notifier.notify(f"Order {order_id} created. Total: ${total:.2f}")
        return order_id
    
    def update_order(self, order_id, items):
        total = self.calculator.calculate_total(items)
        self.repository.update_order(order_id, total)
        self.notifier.notify(f"Order {order_id} updated. New Total: ${total:.2f}")