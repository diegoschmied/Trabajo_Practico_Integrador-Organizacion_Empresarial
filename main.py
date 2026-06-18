problemas = {
    "internet lento": "Reiniciar router",
    "impresora no imprime": "Reiniciar servicio de impresión",
    "pc sin sonido": "Verificar dispositivo predeterminado"
}

estado_ticket = "ABIERTO"

while True:
    try:
        nombre = input("Ingrese su nombre: ").strip()

        if nombre == "":
            print("Error: debe ingresar un nombre.")
            continue

        if nombre.isdigit():
            print("Error: el nombre no puede ser numérico.")
            continue

        break

    except Exception:
        print("Error al ingresar el nombre.")

while True:

    try:

        if estado_ticket == "ABIERTO":

            problema = input("Describa el problema: ").strip()

            if problema == "":
                print("Error: debe describir el problema.")
                continue

            estado_ticket = "EN_ANALISIS"

        elif estado_ticket == "EN_ANALISIS":

            if problema.lower() in problemas:
                solucion = problemas[problema.lower()]
                estado_ticket = "SOLUCION_PROPUESTA"
            else:
                estado_ticket = "DERIVADO_N2"

        elif estado_ticket == "SOLUCION_PROPUESTA":

            print(f"Solución sugerida: {solucion}")

            respuesta = input("¿Funcionó? (si/no): ").strip().lower()

            if respuesta == "si":
                estado_ticket = "RESUELTO"

            elif respuesta == "no":
                estado_ticket = "DERIVADO_N2"

            else:
                print("Respuesta inválida. Ingrese si o no.")

        elif estado_ticket == "RESUELTO":

            print("Problema resuelto.")
            estado_ticket = "CERRADO"

        elif estado_ticket == "DERIVADO_N2":

            print("Caso derivado a Soporte Nivel 2.")
            estado_ticket = "CERRADO"

        elif estado_ticket == "CERRADO":

            print("Ticket cerrado.")
            break

    except KeyboardInterrupt:
        print("\nProceso cancelado por el usuario.")
        break

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")