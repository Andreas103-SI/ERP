# Sistema ERP para Concesionaria de Vehículos

Este es un sistema ERP (Enterprise Resource Planning) desarrollado con Django para la gestión de una concesionaria de vehículos. El sistema incluye módulos para ventas, inventario, empleados, pedidos, finanzas y reportes.

## Características Principales

- **Gestión de Ventas**: Registro y seguimiento de ventas de vehículos
- **Control de Inventario**: Gestión de stock de vehículos y repuestos
- **Gestión de Empleados**: Administración del personal y sus roles
- **Control de Pedidos**: Seguimiento de pedidos de vehículos y repuestos
- **Gestión Financiera**: Control de ingresos, gastos y nómina
- **Reportes**: Generación de reportes y análisis de datos

## Requisitos del Sistema

- Python 3.11 o superior
- PostgreSQL 13 o superior
- Django 5.1.7
- Django REST Framework 3.15.2

## Instalación

1. Clonar el repositorio:
```bash
git clone [https://github.com/Andreas103-SI/ERP.git]
cd ERP
```

2. Crear y activar el entorno virtual:
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # En Windows
source venv/bin/activate     # En Linux/Mac
```

3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar la base de datos:
- Crear una base de datos PostgreSQL llamada 'erp_coches'
- Configurar las credenciales en `erp_config/settings.py`

5. Realizar las migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Crear un superusuario:
```bash
python manage.py createsuperuser
```

7. Iniciar el servidor de desarrollo:
```bash
python manage.py runserver
```

## Estructura del Proyecto

```
ERP/
├── core/               # Módulo central con funcionalidades comunes
├── erp_config/        # Configuración principal del proyecto
├── ventas/            # Módulo de gestión de ventas
├── inventario/        # Módulo de control de inventario
├── empleados/         # Módulo de gestión de empleados
├── pedidos/           # Módulo de control de pedidos
├── finanzas/          # Módulo de gestión financiera
├── reportes/          # Módulo de generación de reportes
├── static/            # Archivos estáticos (CSS, JS, imágenes)
├── templates/         # Plantillas HTML
├── out/              # Archivos de salida (diagramas PNG y documentación)
├── puml/             # Diagramas PlantUML
├── requirements.txt  # Dependencias del proyecto
└── manage.py         # Script de administración de Django
```

## Módulos Principales

### Ventas
- Registro de ventas de vehículos
- Seguimiento de clientes
- Historial de transacciones

### Inventario
- Gestión de stock de vehículos
- Control de repuestos
- Alertas de stock bajo

### Empleados
- Gestión de personal
- Control de roles y permisos
- Registro de asistencia

### Pedidos
- Gestión de pedidos de vehículos
- Control de pedidos de repuestos
- Seguimiento de estado

### Finanzas
- Control de ingresos y gastos
- Gestión de nómina
- Reportes financieros

### Reportes
- Reportes de ventas
- Análisis de inventario
- Reportes financieros

## API Endpoints

### Reportes
- `/api/reportes/ventas-mes/`: Reporte de ventas por mes
- `/api/reportes/inventario-disponible/`: Estado del inventario
- `/api/reportes/gastos-nomina/`: Reporte de gastos por nómina
- `/api/reportes/ventas-mes/`: Reporte de ventas por mes.
- `/api/reportes/inventario-disponible/`: Estado del inventario.
- `/api/reportes/gastos-nomina/`: Reporte de gastos por nómina.
### Ventas
- `/api/ventas/clientes/`: Lista de clientes (GET) o creación de un cliente (POST).
- `/api/ventas/ventas/`: Lista de ventas (GET) o creación de una venta (POST).
### Inventario
- `/api/inventario/vehiculos/`: Lista de vehículos (GET) o creación de un vehículo (POST).
- (Consulta la documentación completa de las API en el código o en un futuro archivo de documentación de la API.)     


## Uso del Sistema
1. Acceso al Panel de Administración:
- Una vez que el servidor esté corriendo (python manage.py runserver), accede a [http://localhost:8000/admin/] e inicia sesión con las credenciales del superusuario.
- Desde el panel de administración, puedes gestionar empleados, ventas, pedidos, finanzas, inventario y reportes.   

2. Uso de las API:
- Las API REST están disponibles para sistemas externos. Por ejemplo, para obtener un reporte de ventas por mes, haz una solicitud GET a [http://localhost:8000/api/reportes/ventas-mes/].
- Asegúrate de incluir un token de autenticación en las solicitudes, ya que las API requieren que el usuario esté autenticado.


## Diagramas UML
El proyecto incluye diagramas UML que describen el diseño y la arquitectura del sistema. Estos diagramas fueron generados con PlantUML y están disponibles en las siguientes carpetas:

- Archivos fuente: puml/ (archivos .puml).
- Diagramas generados: out/ (archivos PNG).

# Despliegue en Producción

Para desplegar el sistema en un entorno de producción, sigue estos pasos básicos:

1.  **Configura un servidor web como Gunicorn y un proxy inverso como Nginx:**

    ```bash
    pip install gunicorn
    gunicorn --bind 0.0.0.0:8000 erp_config.wsgi
    ```

    * Configura Nginx como proxy inverso (consulta la configuración en el Diagrama de Despliegue).

2.  **Asegúrate de configurar las variables de entorno en `erp_config/settings.py`:**

    * Por ejemplo, `DEBUG=False`, credenciales de la base de datos.

3.  **Usa un servicio de base de datos gestionado (como PostgreSQL en AWS RDS) para mayor escalabilidad.**

4.  **Configura HTTPS con un certificado SSL (por ejemplo, usando Let's Encrypt).**

Para más detalles, consulta el [Diagrama de Despliegue].

## Contribución

1. Fork el repositorio
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

# Contacto

Andrea Sierra - [andreasierra103@email.com](mailto:andreasierra103@email.com)

LinkedIn: [Andrea Sierra](https://www.linkedin.com/in/tu-perfil-de-linkedin)  (Añade tu enlace de LinkedIn)

URL del Proyecto: [https://github.com/Andreas103-SI/ERP](https://github.com/Andreas103-SI/ERP)