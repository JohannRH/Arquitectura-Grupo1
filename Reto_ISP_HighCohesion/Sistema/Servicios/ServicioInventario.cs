using System;
using TiendaD1_antes.Sistema.Interfaces;

namespace TiendaD1_antes.Sistema.Servicios
{
    internal class ServicioInventario : IServicioInventario
    {
        public void ActualizarInventario(int idProducto, int cantidad)
        {
            Console.WriteLine($"[Inventario] Inventario actualizado: Producto {idProducto}, Ajuste {cantidad}");
        }
    }
}
