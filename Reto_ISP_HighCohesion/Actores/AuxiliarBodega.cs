using TiendaD1_antes.Sistema.Interfaces;

namespace TiendaD1_antes.Actores
{
    internal class AuxiliarBodega
    {
        private readonly IServicioInventario _servicioInventario;

        public AuxiliarBodega(IServicioInventario servicioInventario)
        {
            _servicioInventario = servicioInventario;
        }

        public void AjustarInventario(int idProducto, int cantidad)
        {
            _servicioInventario.ActualizarInventario(idProducto, cantidad);
        }
    }
}