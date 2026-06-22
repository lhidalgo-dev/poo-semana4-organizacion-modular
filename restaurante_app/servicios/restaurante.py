# servicios/restaurante.py
# Este módulo define la clase Restaurante, que actúa como el servicio central del sistema.
# Gestiona el registro de productos en el menú y los clientes del restaurante.

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """
    Clase de servicio que administra el funcionamiento general del restaurante.
    Centraliza el registro de productos disponibles y los clientes del sistema.
    """

    def __init__(self, nombre, direccion):
        """
        Constructor de la clase Restaurante.

        Parámetros:
            nombre (str): Nombre comercial del restaurante.
            direccion (str): Dirección física del establecimiento.
        """
        self.nombre = nombre
        self.direccion = direccion
        self.menu = []      # Lista de objetos Producto registrados en el menú
        self.clientes = []  # Lista de objetos Cliente registrados en el sistema

    def agregar_producto(self, producto):
        """
        Agrega un producto al menú del restaurante.

        Parámetros:
            producto (Producto): Objeto de tipo Producto a registrar.
        """
        self.menu.append(producto)

    def agregar_cliente(self, cliente):
        """
        Registra un cliente nuevo en el sistema del restaurante.

        Parámetros:
            cliente (Cliente): Objeto de tipo Cliente a registrar.
        """
        self.clientes.append(cliente)

    def buscar_producto(self, nombre_producto):
        """
        Busca un producto en el menú por su nombre (búsqueda insensible a mayúsculas).

        Parámetros:
            nombre_producto (str): Nombre del producto a buscar.

        Retorna:
            Producto o None: El producto encontrado, o None si no existe.
        """
        for producto in self.menu:
            if producto.nombre.lower() == nombre_producto.lower():
                return producto
        return None

    def mostrar_menu(self):
        """
        Muestra en consola todos los productos registrados en el menú del restaurante.
        """
        print(f"\nMENU DEL RESTAURANTE {self.nombre.upper()}")
        print("-" * 60)
        if not self.menu:
            print("  No hay productos registrados en el menú.")
            return
        for producto in self.menu:
            print(f"  {producto}")
        print("-" * 60)

    def mostrar_clientes(self):
        """
        Muestra en consola la información de todos los clientes registrados.
        """
        print(f"\nCLIENTES REGISTRADOS EN {self.nombre.upper()}")
        print("-" * 60)
        if not self.clientes:
            print("  No hay clientes registrados.")
            return
        for cliente in self.clientes:
            print(f"  {cliente}")
            print(f"  Detalle de pedidos:")
            cliente.mostrar_pedidos()
            print()
        print("-" * 60)

    def __str__(self):
        """
        Representación en texto del restaurante para mostrar en consola.
        """
        return (
            f"Restaurante: {self.nombre} | "
            f"Dirección: {self.direccion} | "
            f"Productos en menú: {len(self.menu)} | "
            f"Clientes registrados: {len(self.clientes)}"
        )
