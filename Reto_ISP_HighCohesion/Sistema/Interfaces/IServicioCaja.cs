namespace TiendaD1_antes.Sistema.Interfaces
{
    internal interface IServicioCaja
    {
        void RegistrarVenta(int idProducto, int cantidad);
        void CobrarPago(int idProducto, int cantidad);
    }
}
