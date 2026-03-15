namespace TiendaD1_antes.Sistema
{
    internal interface ISistemaTienda
    {
        // Caja venta
        void RegistrarVenta(int idProducto, int cantidad);
        void CobrarPago(int idProducto, int cantidad);
        void GenerarFactura(int idProducto, int cantidad);

        // Bodega
        void ActualizarInventario(int idProducto, int cantidad);

        // Supervisor  Reportes  Devoluciones
        void ProcesarDevolucion(int idVenta);
        void GenerarReporteDiario();


        // Soporte
        void AtenderReclamo(int idReclamo);


    }
}