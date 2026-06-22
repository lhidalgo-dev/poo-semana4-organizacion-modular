# modelos/cliente.py
# Este módulo define la clase Cliente, que representa a una persona registrada en el sistema del restaurante.


class Cliente:
    """
    Representa a un cliente del restaurante.
    Almacena su información personal y el historial de productos que ha pedido.
    """

    def __init__(self, nombre, cedula, telefono):
        """
        Constructor de la clase Cliente.

        Parámetros:
            nombre (str): Nombre completo del cliente.
            cedula (str): Número de cédula de identidad del cliente.
            telefono (str): Número de teléfono de contacto.
        """
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
        self.pedidos = []  # Lista de productos solicitados por el cliente

    def agregar_pedido(self, producto):
        """
        Registra un producto en el historial de pedidos del cliente.

        Parámetros:
            producto (Producto): Objeto de tipo Producto que el cliente ha solicitado.
        """
        self.pedidos.append(producto)

    def calcular_total(self):
        """
        Calcula el total acumulado de todos los pedidos realizados por el cliente.

        Retorna:
            float: Suma de los precios de todos los productos pedidos.
        """
        return round(sum(p.precio for p in self.pedidos), 2)

    def mostrar_pedidos(self):
        """
        Muestra en consola el detalle de todos los pedidos registrados para el cliente.
        """
        if not self.pedidos:
            print(f"  El cliente {self.nombre} no tiene pedidos registrados.")
            return
        for i, producto in enumerate(self.pedidos, start=1):
            print(f"  {i}. {producto.nombre} - ${producto.precio:.2f}")

    def __str__(self):
        """
        Representación en texto del cliente para mostrar en consola.
        """
        return (
            f"Cliente: {self.nombre} | "
            f"Cédula: {self.cedula} | "
            f"Teléfono: {self.telefono} | "
            f"Total pedidos: ${self.calcular_total():.2f}"
        )
