# Documentación de Diagramas UML para AutoGest S.L.

## Introducción
Este documento describe los diagramas UML generados para el sistema AutoGest S.L., una aplicación web para la gestión de un concesionario de vehículos. Los diagramas cubren diferentes aspectos del sistema, desde la estructura del código hasta la infraestructura tecnológica, y están diseñados para proporcionar una visión clara del diseño y la arquitectura del sistema.

## Lista de Diagramas
A continuación, se presenta una lista de los diagramas generados, junto con una breve descripción y el nombre del archivo PNG correspondiente:

- **Diagrama de Clases** (`class_diagram_autogest.png`): Representa la estructura estática del sistema, mostrando las clases, sus atributos, métodos y relaciones.
- **Diagrama de Objetos** (`object_diagram_autogest.png`): Muestra un snapshot de los objetos del sistema en un escenario específico (una venta de un vehículo).
- **Diagramas de Casos de Uso**:
  - `use_case_empleados.png`: Casos de uso para la aplicación `empleados`.
  - `use_case_finanzas.png`: Casos de uso para la aplicación `finanzas`.
  - `use_case_inventario.png`: Casos de uso para la aplicación `inventario`.
  - `use_case_pedidos.png`: Casos de uso para la aplicación `pedidos`.
  - `use_case_proveedores.png`: Casos de uso para la aplicación `proveedores`.
  - `use_case_ventas.png`: Casos de uso para la aplicación `ventas`.
  - `use_case_reportes.png`: Casos de uso para la aplicación `reportes`.
- **Diagramas de Secuencia**:
  - `sequence_empleados.png`: Flujo para "Crear Empleado".
  - `sequence_finanzas.png`: Flujo para "Crear Gasto".
  - `sequence_inventario.png`: Flujo para "Actualizar Vehículo".
  - `sequence_pedidos.png`: Flujo para "Eliminar Pedido".
  - `sequence_proveedores.png`: Flujo para "Listar Proveedores".
  - `sequence_ventas.png`: Flujo para "Crear Cliente".
  - `sequence_reportes.png`: Flujo para "Generar Reporte de Ingresos y Egresos".
- **Diagrama de Colaboración** (`collaboration_autogest.png`): Muestra las interacciones entre objetos para registrar una venta de un vehículo.
- **Diagrama de Estados** (`state_autogest.png`): Representa el ciclo de vida de un pedido, desde su creación hasta su recepción o cancelación.
- **Diagrama de Componentes** (`component_autogest.png`): Define la organización del código en módulos reutilizables (aplicaciones Django).
- **Diagrama de Despliegue** (`deployment_autogest.png`): Muestra la distribución del sistema en la infraestructura tecnológica.

## Instrucciones para Generar los Diagramas
Si necesitas regenerar los diagramas a partir de los archivos fuente `.puml`, sigue estos pasos:

1. Asegúrate de tener PlantUML instalado.
2. Coloca los archivos `.puml` (ubicados en la carpeta `puml`) en el directorio de trabajo.
3. Ejecuta el siguiente comando para cada archivo:  