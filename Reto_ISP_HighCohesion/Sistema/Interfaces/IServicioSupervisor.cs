namespace TiendaD1_antes.Sistema.Interfaces
{
    internal interface IServicioSupervisor
    {
        void ProcesarDevolucion(int idVenta);
        void GenerarReporteDiario();
    }
}
