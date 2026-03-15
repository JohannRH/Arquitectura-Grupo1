using System;
using TiendaD1_antes.Sistema.Interfaces;

namespace TiendaD1_antes.Sistema.Servicios
{
    internal class ServicioFacturacion : IServicioFacturacion
    {
        public void GenerarFactura(int idProducto, int cantidad)
        {
            Console.WriteLine($"[Facturación] Factura generada: Producto {idProducto}, Cantidad {cantidad}");
        }
    }
}
