usuario = {
    "nombre": "Rodolfo",
    "edad": 29,
    "color_favorito": "azul"
}

saludos = ["¡Hola!", "¡Buenas!", "¡Qué tal!", "¡Hey!"]
indice_saludo = 0 

print("Asistente: ¡Hola! Soy tu asistente. Escribe 'salir' para terminar la conversación.\n")

while True:
    entrada = input("Tú: ").lower() 

    if entrada == "salir":
        print("Asistente: ¡Hasta luego!")
        break

    elif entrada in ["hola", "buenas", "buenos días", "buenas tardes", "hey"]:
        print("Asistente:", saludos[indice_saludo])
        indice_saludo = (indice_saludo + 1) % len(saludos) 

    elif "mi nombre" in entrada:
        print("Asistente:Tu nombre es",usuario.get("nombre", "desconocido"))
    elif "mi edad" in entrada:
        print("Asistente: Tienes",usuario.get("edad", "desconocida"), "años")
    elif "mi color favorito" in entrada:
        print("Asistente:Tu color favorito es",usuario.get("color_favorito", "desconocido"))
    else:
        print("Asistente:No tengo informacion sobre eso aun.")