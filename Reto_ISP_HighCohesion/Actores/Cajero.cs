using TiendaD1_antes.Sistema.Interfaces;

namespace TiendaD1_antes.Actores
{
    internal class Cajero
    {
        private readonly IServicioCaja _servicioCaja;
        private readonly IServicioFacturacion _servicioFacturacion;

        public Cajero(IServicioCaja servicioCaja, IServicioFacturacion servicioFacturacion)
        {
            _servicioCaja = servicioCaja;
            _servicioFacturacion = servicioFacturacion;
        }

        public void RegistrarVenta(int idProducto, int cantidad)
        {
            _servicioCaja.RegistrarVenta(idProducto, cantidad);
            _servicioCaja.CobrarPago(idProducto, cantidad);
            _servicioFacturacion.GenerarFactura(idProducto, cantidad);
        }
    }
}