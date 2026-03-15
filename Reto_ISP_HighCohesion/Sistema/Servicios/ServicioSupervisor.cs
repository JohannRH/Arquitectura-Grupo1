using System;
using TiendaD1_antes.Sistema.Interfaces;

namespace TiendaD1_antes.Sistema.Servicios
{
    internal class ServicioSupervisor : IServicioSupervisor
    {
        public void ProcesarDevolucion(int idVenta)
        {
            Console.WriteLine($"[Supervisor] Devolución procesada para venta {idVenta}");
        }

        public void GenerarReporteDiario()
        {
            Console.WriteLine("[Supervisor] Reporte diario generado");
        }
    }
}
