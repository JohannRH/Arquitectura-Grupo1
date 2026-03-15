using System;

namespace TiendaD1_antes.Sistema
{
    internal class SistemaTienda : ISistemaTienda
    {
        public void RegistrarVenta(int idProducto, int cantidad)
        {
            Console.WriteLine($"[Caja] Venta registrada: Producto {idProducto}, Cantidad {cantidad}");
        }

        public void CobrarPago(int idProducto, int cantidad)
        {
            Console.WriteLine($"[Caja] Pago cobrado: Producto {idProducto}, Cantidad {cantidad}");
        }

        public void GenerarFactura(int idProducto, int cantidad)
        {
            Console.WriteLine($"[Facturación] Factura generada: Producto {idProducto}, Cantidad {cantidad}");
        }

        public void ActualizarInventario(int idProducto, int cantidad)
        {
            Console.WriteLine($"[Inventario] Inventario actualizado: Producto {idProducto}, Ajuste {cantidad}");
        }

        public void ProcesarDevolucion(int idVenta)
        {
            Console.WriteLine($"[Supervisor] Devolución procesada para venta {idVenta}");
        }

        public void GenerarReporteDiario()
        {
            Console.WriteLine("[Supervisor] Reporte diario generado");
        }

        public void AtenderReclamo(int idReclamo)
        {
            Console.WriteLine($"[Soporte] Reclamo atendido: {idReclamo}");
        }
    }
}