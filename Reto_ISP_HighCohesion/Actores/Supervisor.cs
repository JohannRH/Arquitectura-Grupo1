using TiendaD1_antes.Sistema.Interfaces;

namespace TiendaD1_antes.Actores
{
    internal class Supervisor
    {
        private readonly IServicioSupervisor _servicioSupervisor;

        public Supervisor(IServicioSupervisor servicioSupervisor)
        {
            _servicioSupervisor = servicioSupervisor;
        }

        public void AutorizarDevolucion(int idVenta)
        {
            _servicioSupervisor.ProcesarDevolucion(idVenta);
        }

        public void VerReporteDiario()
        {
            _servicioSupervisor.GenerarReporteDiario();
        }
    }
}