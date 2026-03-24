# 🌐 Monitor de Redes Interactivo (Python)

Herramienta por consola diseñada para el diagnóstico rápido de conectividad en redes locales (LAN) y verificación de salida a Internet mediante el protocolo ICMP.

## 🛠️ ¿Qué hace este script?
Este programa automatiza el envío de paquetes **Ping** para verificar el estado de múltiples equipos (Routers, Switches, Access Points, DNS, etc.) desde una interfaz limpia y amigable para mesas de ayuda o soporte de nivel 1.

### Características principales:
* **Menú Dinámico:** Permite agregar direcciones IP en tiempo real sin tener que modificar el código fuente.
* **Contexto de Red:** Asocia cada IP con un nombre o descripción (ej. "Switch Core", "Router Cliente").
* **Multiplataforma:** El código detecta automáticamente si el sistema operativo es Windows o Linux/macOS para adaptar la sintaxis del comando nativo.

## 🚀 Cómo utilizarlo
1. Asegúrate de tener Python instalado en el sistema.
2. Descarga el archivo principal del código.
3. Abre una terminal (CMD o PowerShell) en la ruta del archivo y ejecuta: `python monitor.py`

## 🤝 Feedback y Contribuciones

Este script nació de la necesidad de crear algo verdaderamente útil y funcional para el día a día. Está pensado tanto para verificar equipos en redes domésticas como para agilizar los diagnósticos en el soporte técnico de proveedores de internet (ISPs).

Sé que la teoría a veces choca con la práctica, así que si al usar esta herramienta en un entorno real notas detalles que no "acoplan" del todo bien, encuentras errores o tienes ideas para que funcione mejor, ¡estoy totalmente abierto a escucharlas!

**¿Cómo puedes aportar?**
* Ve a la pestaña de **[Issues]** aquí en GitHub y cuéntame qué se puede mejorar o qué falló.
* Si sabes cómo optimizar el código, siéntete libre de hacer un **Fork** y enviarme un **Pull Request**.

📬 **Contacto:** Si quieres charlar sobre redes, Python o darme feedback directo, puedes escribirme a: jdanielpintotrabajo@gmail.com
