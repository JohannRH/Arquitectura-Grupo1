using TiendaD1_antes.Sistema.Interfaces;

namespace TiendaD1_antes.Actores
{
    internal class AgenteSoporte
    {
        private readonly IServicioSoporte _servicioSoporte;

        public AgenteSoporte(IServicioSoporte servicioSoporte)
        {
            _servicioSoporte = servicioSoporte;
        }

        public void GestionarReclamo(int idReclamo)
        {
            _servicioSoporte.AtenderReclamo(idReclamo);
        }
    }
}