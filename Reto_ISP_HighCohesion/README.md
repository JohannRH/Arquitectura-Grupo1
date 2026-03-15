--Reto de Refactorización: Operación Tienda D1 (High Cohesion + ISP)

Tienes un sistema interno de una tienda tipo D1. Al inicio era una tienda pequeña y una persona hacía de todo, por eso se creó una sola interfaz con todo mezclado. Hoy la tienda creció y ya existen roles separados: caja, bodega y soporte. El sistema funciona, pero el diseño está mal para escalar.

--El estado actual (ANTES)

El código de esta carpeta (reto) presenta problemas de diseño claros:

Interfaz gigante (ISP roto)
Existe una sola interfaz con funciones de cajas, bodega, compras y servicio al cliente. Todos los roles dependen del mismo contrato, aunque no usen todo.

Clase “Dios” (baja cohesión)
Una sola clase implementa todo: ventas, inventario, facturación, devoluciones, reclamos, reportes. Tiene demasiadas responsabilidades y demasiadas razones para cambiar.

Cambios con efecto dominó
Un ajuste en devoluciones o facturación obliga a tocar el mismo núcleo que usa caja y bodega, aumentando el riesgo de romper cosas.

Escalabilidad organizacional pobre
En la vida real D1 tiene roles separados (cajero, supervisor, bodega, soporte). Aquí todos quedan amarrados al mismo sistema.

--Objetivo del reto

Refactoriza para cumplir:

ISP: separar la interfaz grande en interfaces pequeñas por rol.

High Cohesion: separar la clase central en clases cohesionadas (cada una con propósito claro).

--Solución Implementada (DESPUÉS)

**Interface Segregation Principle (ISP) Aplicado**

Se reemplazó la interfaz gigante `ISistemaTienda` por interfaces específicas por rol:

- `IServicioCaja` - Métodos: RegistrarVenta, CobrarPago
- `IServicioFacturacion` - Método: GenerarFactura  
- `IServicioInventario` - Método: ActualizarInventario
- `IServicioSupervisor` - Métodos: ProcesarDevolucion, GenerarReporteDiario
- `IServicioSoporte` - Método: AtenderReclamo

**High Cohesion Aplicado**

Se dividió la clase "Dios" `SistemaTienda` en clases cohesionadas:

- `ServicioCaja` - Solo operaciones de caja
- `ServicioFacturacion` - Solo facturación
- `ServicioInventario` - Solo inventario
- `ServicioSupervisor` - Solo supervisor
- `ServicioSoporte` - Solo soporte

**Actores Actualizados**

Los actores ahora dependen solo de las interfaces que necesitan:

- `Cajero` → `IServicioCaja` + `IServicioFacturacion`
- `AuxiliarBodega` → `IServicioInventario`
- `Supervisor` → `IServicioSupervisor`
- `AgenteSoporte` → `IServicioSoporte`

**Beneficios Alcanzados**

- **Sin efecto dominó**: Cambios aislados por responsabilidad
- **Escalabilidad organizacional**: Diseño refleja estructura real
- **Mantenibilidad**: Cada componente evoluciona independientemente
- **Testabilidad**: Pruebas unitarias simples y específicas

**Estructura Final**

```
Sistema/
├── Interfaces/
│   ├── IServicioCaja.cs
│   ├── IServicioFacturacion.cs
│   ├── IServicioInventario.cs
│   ├── IServicioSupervisor.cs
│   └── IServicioSoporte.cs
└── Servicios/
    ├── ServicioCaja.cs
    ├── ServicioFacturacion.cs
    ├── ServicioInventario.cs
    ├── ServicioSupervisor.cs
    └── ServicioSoporte.cs
```

**Resultado**: Sistema escalable, mantenible y cumple con principios SOLID.
