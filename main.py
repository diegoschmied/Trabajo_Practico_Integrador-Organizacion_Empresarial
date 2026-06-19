# importo librerias
import csv
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
tickets_path = os.path.join(script_dir, "tickets.csv")
problemas_path = os.path.join(script_dir, "problemas.csv")

# Funcion para arreglar los tickets generada por la ia de VScode

def normalizar_tickets_csv():
    if not os.path.exists(tickets_path):
        return

    try:
        with open(tickets_path, "r", encoding="utf-8", newline="") as f:
            filas = list(csv.reader(f))
    except Exception:
        return

    if not filas:
        return

    header = ["id", "usuario", "problema", "estado"]
    primer_fila = [celda.strip() for celda in filas[0]]

    if primer_fila == header and all(len(fila) == 4 for fila in filas[1:]):
        return

    if len(filas) == 1 and len(primer_fila) >= 7 and primer_fila[:3] == header[:3] and primer_fila[3].startswith("estado"):
        valor_id = primer_fila[3][len("estado"):]
        resto = primer_fila[4:]

        if valor_id and len(resto) == 3:
            with open(tickets_path, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerow([valor_id] + resto)
            return

    if len(filas) == 1 and len(primer_fila) == 8 and primer_fila[:4] == header:
        with open(tickets_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow(primer_fila[4:8])
        return

    if len(primer_fila) > 4 and primer_fila[:4] == header and len(filas) == 1:
        data_row = primer_fila[4:]
        if len(data_row) == 3:
            with open(tickets_path, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerow(data_row)
            return

# Funcion para cargar los problemas de la base de datos

def cargar_problemas():
    data = {}

    try:
        with open(problemas_path, mode="r", encoding="utf-8-sig", newline="") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                if not isinstance(fila, dict):
                    continue

                fila = {(k or "").strip().lower(): (v or "").strip() for k, v in fila.items()}
                problema = fila.get("problema", "").lower()
                solucion = fila.get("solucion", "")

                if not problema or not solucion:
                    continue

                data[problema] = solucion

    except FileNotFoundError:
        print("Sistema no disponible en este momento.")
        exit()

    except Exception:
        print("Sistema no disponible en este momento.")
        exit()

    return data

# Funcion para utilizar los problemas de la base de datos

def elegir_problema(problemas_dict):
    print("\nTecniBot ;)")

    opciones = list(problemas_dict.keys())

    print("\n¿Con que te puedo ayudar?\n")
    for i, op in enumerate(opciones, start=1):
        print(f"{i}. {op}")

    print(f"{len(opciones)+1}. Tengo otro problema")

    while True:
        opcion = input("\nElegí una opción:").strip()

        if not opcion.isnumeric():
            print("Por favor ingresá un número válido.")
            continue

        opcion = int(opcion)

        if 1 <= opcion <= len(opciones):
            return opciones[opcion - 1]

        elif opcion == len(opciones) + 1:
            texto = input("Describí el problema: ").strip().lower()
            return texto if texto else "problema no especificado"

        else:
            print("Opción inválida.")

# FUncion que genera id del ticket

def generar_id():
    id_ticket = 1

    if not os.path.exists(tickets_path):
        return id_ticket

    try:
        with open(tickets_path, "r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                try:
                    id_ticket = max(id_ticket, int(fila.get("id", 0)) + 1)
                except Exception:
                    continue

    except Exception:
        return id_ticket

    return id_ticket

# Funcion que registra los datos en el csv

def guardar_ticket(ticket):
    existe = os.path.exists(tickets_path)

    try:
        with open(tickets_path, "a", newline="", encoding="utf-8") as f:
            campos = ["id", "usuario", "problema", "estado"]
            writer = csv.DictWriter(f, fieldnames=campos)

            if not existe or os.path.getsize(tickets_path) == 0:
                writer.writeheader()

            writer.writerow(ticket)
        return True

    except Exception:
        return False

# Funcion con el funcionamiento principal del programa

def main():
    normalizar_tickets_csv()
    problemas = cargar_problemas()
    id_ticket = generar_id()

    while True:
        nombre = input("Hola, yo soy TecniBot. ¿Como te llamas?:").strip()

        if not nombre:
            print("Ingresa tu nombre por favor.")
            continue

        if nombre.isnumeric():
            print("Nombre inválido.")
            continue

        break

    ticket = {
        "id": id_ticket,
        "usuario": nombre,
        "problema": "",
        "estado": "ABIERTO"
    }

    solucion = None

    while True:
        if ticket["estado"] == "ABIERTO":
            problema = elegir_problema(problemas)
            ticket["problema"] = problema
            ticket["estado"] = "EN_ANALISIS"

        elif ticket["estado"] == "EN_ANALISIS":
            clave = ticket["problema"].strip().lower()
            solucion = problemas.get(clave)

            if solucion:
                ticket["estado"] = "SOLUCION_PROPUESTA"
            else:
                ticket["estado"] = "DERIVADO_N2"

        elif ticket["estado"] == "SOLUCION_PROPUESTA":
            print(f"Solución sugerida: {solucion}")

            respuesta = input("¿Funcionó? (si/no):").strip().lower()

            if respuesta in ["si", "sí", "s"]:
                ticket["estado"] = "RESUELTO"
            elif respuesta in ["no", "n"]:
                ticket["estado"] = "DERIVADO_N2"
            else:
                print("Respuesta inválida.")
                continue

        elif ticket["estado"] == "RESUELTO":
            print("Problema resuelto.")
            ticket["estado"] = "CERRADO"

        elif ticket["estado"] == "DERIVADO_N2":
            print("Su caso fue derivado a Soporte Nivel 2.")
            ticket["estado"] = "CERRADO"

        elif ticket["estado"] == "CERRADO":
            if guardar_ticket(ticket):
                print("Ticket registrado correctamente.")
            else:
                print("No se pudo registrar el ticket. Intente nuevamente más tarde.")
            break

        else:
            print("Sistema en estado inconsistente.")
            break


if __name__ == "__main__":
    main()