# modelos/producto.py
# Este módulo define la clase Producto, que representa un artículo disponible en el menú del restaurante.


class Producto:
    """
    Representa un producto del menú del restaurante.
    Puede ser un plato, una bebida o cualquier artículo disponible para el consumo.
    """

    def __init__(self, nombre, categoria, precio, disponible=True):
        """
        Constructor de la clase Producto.

        Parámetros:
            nombre (str): Nombre del producto (ej. "Caldo de patas").
            categoria (str): Categoría del producto (ej. "Plato fuerte", "Bebida").
            precio (float): Precio unitario del producto en dólares.
            disponible (bool): Indica si el producto está disponible actualmente. Por defecto True.
        """
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    def cambiar_disponibilidad(self, estado):
        """
        Actualiza la disponibilidad del producto en el sistema.

        Parámetros:
            estado (bool): True si el producto está disponible, False si no lo está.
        """
        self.disponible = estado

    def aplicar_descuento(self, porcentaje):
        """
        Aplica un descuento porcentual al precio del producto.

        Parámetros:
            porcentaje (float): Porcentaje de descuento a aplicar (ej. 10 para el 10%).
        """
        if 0 < porcentaje < 100:
            self.precio = round(self.precio * (1 - porcentaje / 100), 2)

    def __str__(self):
        """
        Representación en texto del producto para mostrar en consola.
        """
        estado = "Disponible" if self.disponible else "No disponible"
        return (
            f"Producto: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Estado: {estado}"
        )
