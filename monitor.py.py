import os
import platform

def limpiar_pantalla():
    # Esta funcion limpia la consola para que el menu siempre se vea ordenado
    os.system('cls' if os.name == 'nt' else 'clear')
    
def verificar_ip(ip):
    # Verificar el SO utilizado para evitar incovenientes de incompatibilidad
    sistema = platform.system().lower()
    parametro = "-n" if sistema == "windows" else "-c"
    
    if sistema == "windows": 
        comando = f"ping {parametro} 1 -w 1000 {ip} > nul"
    else:
        comando = f"ping {parametro} 1 -W 1 {ip} > /dev/null 2>&1"
        
    return os.system(comando) == 0

# Aqui guardaremos la Ips y sus nombres temporalmente mientras el programa este abierto
equipos = {}

while True:
    limpiar_pantalla()
    print("=" * 55)
    print("\n HERRAMIENTA DE DIAGNOSTICO DE RED (SOPORTE TI) ")
    print("=" * 55)
    print("1. Agregar un equipo a la lista (IP y Nombre)")
    print("2. Ver lista de equipos a monitorear")
    print("3. Ejecutar escaneo de conectividad")
    print("4. Salir del programa")
    print("=" * 55)
    
    opcion = input("Elige una opcion (1-4): ")
    
    if opcion == "1":
        print("\n--- AGREGAR EQUIPO ---")
        ip = input("Ingrese la direccion IP (ej. 192.168.1.1): ")
        nombre = input("Ingresa una descripción (ej. Switch Core, Router Cliente): ")
        equipos[ip] = nombre
        print(f"\n[+] Equipo '{nombre}' con IP {ip} agregado correctamente.")
        input("\nPresiona Enter para volver al menú...")
        
    elif opcion == "2":
        print("\n--- LISTA DE EQUIPOS ACTUAL ---")
        if not equipos:
            print("La lista está vacía. No hay equipos registrados.")
        else:
            for ip, nombre in equipos.items():
                print(f"- {nombre}: {ip}")
        input("\nPresiona Enter para volver al menú...")
        
    elif opcion == "3":
        print("\n--- ESCANEO DE RED EN PROGRESO ---\n")
        if not equipos:
            print("No hay equipos para escanear. Agrega uno en la opción 1.")
        else:
            for ip, nombre in equipos.items():
                # Formateamos el texto para que se vea alineado y profesional
                print(f"Probando {nombre} ({ip})...".ljust(45), end=" ")
                if verificar_ip(ip):
                    print("✅ [ONLINE]")
                else:
                    print("❌ [OFFLINE - Revisar enlace o energía]")
        input("\nPresiona Enter para volver al menú...")
        
    elif opcion == "4":
        print("\nCerrando herramienta de diagnóstico. ¡Hasta luego!")
        break
        
    else:
        print("\n⚠️ Opción no válida. Por favor, ingresa un número del 1 al 4.")
        input("\nPresiona Enter para continuar...")

