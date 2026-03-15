using System;
using TiendaD1_antes.Sistema.Interfaces;

namespace TiendaD1_antes.Sistema.Servicios
{
    internal class ServicioCaja : IServicioCaja
    {
        public void RegistrarVenta(int idProducto, int cantidad)
        {
            Console.WriteLine($"[Caja] Venta registrada: Producto {idProducto}, Cantidad {cantidad}");
        }

        public void CobrarPago(int idProducto, int cantidad)
        {
            Console.WriteLine($"[Caja] Pago cobrado: Producto {idProducto}, Cantidad {cantidad}");
        }
    }
}
