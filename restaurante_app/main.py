# main.py
# Punto de arranque del sistema de gestión del restaurante.
# Aquí se crean los objetos y se ejecutan los métodos para demostrar el funcionamiento del sistema.

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():
    """
    Función principal que inicializa el sistema y demuestra su funcionamiento.
    """

    # Creación del restaurante principal
    restaurante = Restaurante(
        nombre="El Sabor Amazónico",
        direccion="Av. Principal s/n, Puyo, Pastaza"
    )

    print("=" * 60)
    print("SISTEMA DE GESTION DE RESTAURANTE")
    print("Programacion Orientada a Objetos - Semana 4")
    print("=" * 60)
    print(f"\nIniciando sistema...")
    print(f"  {restaurante}")

    # --------------------------------------------------
    # Registro de productos en el menú
    # --------------------------------------------------
    p1 = Producto("Caldo de patas",   "Sopa",        4.50)
    p2 = Producto("Seco de pollo",    "Plato fuerte", 5.75)
    p3 = Producto("Tilapia frita",    "Plato fuerte", 6.00)
    p4 = Producto("Jugo de naranja",  "Bebida",       1.50)
    p5 = Producto("Agua mineral",     "Bebida",       0.75)
    p6 = Producto("Maduro con queso", "Postre",       2.00)

    # Agregar productos al menú del restaurante
    for producto in [p1, p2, p3, p4, p5, p6]:
        restaurante.agregar_producto(producto)

    # Mostrar el menú completo
    restaurante.mostrar_menu()

    # --------------------------------------------------
    # Demostración: cambio de disponibilidad y descuento
    # --------------------------------------------------
    print("\nACTUALIZACIONES EN EL MENU:")
    print("-" * 60)

    # El caldo de patas ya no está disponible hoy
    p1.cambiar_disponibilidad(False)
    print(f"  Disponibilidad actualizada -> {p1}")

    # Descuento del 10% al seco de pollo
    p2.aplicar_descuento(10)
    print(f"  Descuento aplicado        -> {p2}")
    print("-" * 60)

    # --------------------------------------------------
    # Registro de clientes y sus pedidos
    # --------------------------------------------------
    c1 = Cliente("María Fernanda Ríos",  "0102345678", "0991234567")
    c2 = Cliente("Carlos Andrés Mora",   "0987654321", "0987654321")
    c3 = Cliente("Lucía Esperanza Vera", "0112233445", "0976543210")

    # Pedidos del cliente 1
    c1.agregar_pedido(p2)  # Seco de pollo (con descuento)
    c1.agregar_pedido(p4)  # Jugo de naranja
    c1.agregar_pedido(p6)  # Maduro con queso

    # Pedidos del cliente 2
    c2.agregar_pedido(p3)  # Tilapia frita
    c2.agregar_pedido(p5)  # Agua mineral

    # El cliente 3 aún no ha pedido nada (caso borde)

    # Registrar clientes en el sistema del restaurante
    for cliente in [c1, c2, c3]:
        restaurante.agregar_cliente(cliente)

    # Mostrar todos los clientes con sus pedidos
    restaurante.mostrar_clientes()

    # --------------------------------------------------
    # Demostración: búsqueda de producto
    # --------------------------------------------------
    print("\nBUSQUEDA DE PRODUCTO EN EL MENU:")
    print("-" * 60)
    nombre_buscado = "Tilapia frita"
    resultado = restaurante.buscar_producto(nombre_buscado)
    if resultado:
        print(f"  Producto encontrado -> {resultado}")
    else:
        print(f"  El producto '{nombre_buscado}' no fue encontrado en el menú.")
    print("-" * 60)

    # --------------------------------------------------
    # Resumen final del sistema
    # --------------------------------------------------
    print("\nRESUMEN FINAL DEL SISTEMA:")
    print("-" * 60)
    print(f"  {restaurante}")
    print("=" * 60)
    print("Programa finalizado correctamente.")
    print("=" * 60)


# Punto de entrada del programa
if __name__ == "__main__":
    main()
