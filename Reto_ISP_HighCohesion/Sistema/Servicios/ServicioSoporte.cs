using System;
using TiendaD1_antes.Sistema.Interfaces;

namespace TiendaD1_antes.Sistema.Servicios
{
    internal class ServicioSoporte : IServicioSoporte
    {
        public void AtenderReclamo(int idReclamo)
        {
            Console.WriteLine($"[Soporte] Reclamo atendido: {idReclamo}");
        }
    }
}
