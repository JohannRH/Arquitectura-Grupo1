# Principios de Arquitectura de Software: DRY & Low Coupling

Este repositorio contiene ejemplos prácticos en Python diseñados para ilustrar dos de los principios fundamentales en el desarrollo de software moderno: **DRY (Don't Repeat Yourself)** y **Bajo Acoplamiento (Low Coupling)**.

El objetivo es demostrar cómo la refactorización y el uso de patrones de diseño pueden transformar código monolítico y difícil de mantener en sistemas modulares, testables y extensibles.

## 📂 Contenido del Repositorio

El código fuente se encuentra en el directorio `DRY&LC` y consta de tres ejemplos clave:

### 1. `LowCouplingConDRY.py` (Refactorización Completa)
Este archivo es el ejemplo más exhaustivo. Muestra la transformación de un sistema de procesamiento de órdenes:
- **Antes:** Una clase `OrderProcessor` monolítica que mezclaba lógica de negocio, persistencia de datos (SQLite) y notificaciones.
- **Después:** Una arquitectura desacoplada utilizando inyección de dependencias:
  - `PriceCalculator`: Encapsula la lógica de negocio pura.
  - `OrderRepository`: Maneja la persistencia.
  - `NotificationService`: Gestiona la salida de información.
  - `OrderService`: Orquesta el flujo sin conocer los detalles de implementación.

### 2. `dry.py` (Don't Repeat Yourself)
Ilustra cómo evitar la duplicación de lógica de validación.
- Compara una implementación de `UserService` donde las reglas de validación de email y contraseña se repiten, contra una versión donde se centralizan en métodos reutilizables, facilitando cambios futuros en las reglas de negocio.

### 3. `low.py` (Inversión de Dependencias)
Un ejemplo claro del principio de Inversión de Dependencias (parte de SOLID) para lograr bajo acoplamiento.
- Muestra la evolución desde una clase `Pedido` que instancia directamente sus dependencias (`PagoTarjeta`, `NotificacionEmail`), hacia una que depende de abstracciones (`MetodoPago`, `ServicioNotificacion`). Esto permite cambiar implementaciones (ej. enviar SMS en lugar de Email) sin modificar la clase principal.

## 🚀 Cómo Ejecutar

No se requieren librerías externas. Todos los ejemplos funcionan con una instalación estándar de Python 3.x.

```bash
# Ejecutar el ejemplo de refactorización de órdenes
python "DRY&LC/LowCouplingConDRY.py"

# Ejecutar el ejemplo de DRY
python "DRY&LC/dry.py"

# Ejecutar el ejemplo de Low Coupling
python "DRY&LC/low.py"
```

## 🛠 Requisitos

*   Python 3.6 o superior.
*   Librerías estándar: `sqlite3`, `abc`.

---
**Curso:** Arquitectura de Software - Grupo 1  
**Año:** 2026
