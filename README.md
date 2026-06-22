# Sistema de Gestión de Restaurante

**Autor:** Leython Josue Hidalgo Valdez  
**Asignatura:** Programación Orientada a Objetos  
**Actividad:** Tarea Semana 4  
**Universidad:** Universidad Estatal Amazónica

---

## Descripción del sistema

Este proyecto implementa un sistema básico de gestión de restaurante utilizando los principios de la Programación Orientada a Objetos (POO) en Python. El sistema permite registrar los productos disponibles en el menú, gestionar la información de los clientes y administrar sus pedidos, todo desde un servicio central que representa al restaurante.

El objetivo principal no es construir una aplicación con interfaz gráfica ni menú interactivo, sino demostrar la correcta organización modular del código, la separación de responsabilidades entre archivos y el uso adecuado de clases, constructores, atributos, métodos y el método especial `__str__()`.

---

## Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   └── restaurante.py
└── main.py
```

### Descripción de cada archivo

- **modelos/producto.py:** Contiene la clase `Producto`, que representa un artículo disponible en el menú del restaurante (plato, bebida o postre). Incluye atributos como nombre, categoría, precio y disponibilidad, así como métodos para actualizar el estado del producto y aplicar descuentos.

- **modelos/cliente.py:** Contiene la clase `Cliente`, que representa a una persona registrada en el sistema. Gestiona sus datos personales y el historial de pedidos realizados, con métodos para agregar pedidos y calcular el total acumulado.

- **servicios/restaurante.py:** Contiene la clase `Restaurante`, que actúa como el servicio central del sistema. Administra las listas de productos y clientes, y ofrece métodos para registrar, buscar y mostrar la información del negocio.

- **main.py:** Es el punto de arranque del programa. Crea los objetos necesarios, registra productos y clientes, ejecuta los métodos del sistema y muestra los resultados organizados en consola.

---

## Cómo ejecutar el programa

1. Clonar o descargar el repositorio.
2. Abrir una terminal en la raíz del repositorio (donde se encuentra la carpeta `restaurante_app`).
3. Ejecutar el archivo principal con el siguiente comando:

```bash
cd restaurante_app
python main.py
```

> El programa no requiere instalación de dependencias externas. Funciona con Python 3.6 o superior.

---

## Reflexión sobre la importancia de modularizar el software

Modularizar el software consiste en dividir el código en unidades independientes, cada una con una responsabilidad específica. Esta práctica ofrece ventajas fundamentales en el desarrollo de software profesional.

En primer lugar, favorece la mantenibilidad: cuando cada clase o módulo se ocupa de una sola responsabilidad, localizar y corregir errores resulta mucho más sencillo. En segundo lugar, facilita la escalabilidad, ya que incorporar nuevas funcionalidades (por ejemplo, una clase `Pedido` o una clase `Factura`) no implica modificar el código existente, sino añadir nuevos módulos. En tercer lugar, mejora la legibilidad, pues un proyecto organizado en carpetas con nombres descriptivos permite que cualquier desarrollador comprenda la estructura del sistema sin necesidad de leer todo el código.

Separar responsabilidades entre modelos y servicios es un principio derivado del diseño orientado a objetos y de patrones ampliamente utilizados en la industria. Los modelos definen qué son las entidades del sistema, mientras que los servicios definen qué puede hacer el sistema con ellas. Esta distinción hace que el código sea más limpio, reutilizable y profesional.
