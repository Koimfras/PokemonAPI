usuario = {
    "nombre": "Rodolfo",
    "edad": 30,
    "color_favorito": "negro"
}

print("Datos actuales del usuario:")
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

nuevo_dato = input("Escribe el nombre del nuevo dato que quieres agregar: ")
valor = input(f"Escribe el valor para '{nuevo_dato}': ")
usuario[nuevo_dato] = valor

print("Datos despues de agregar un nuevo dato:")
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

dato_a_eliminar = input("Escribe el nombre del dato que deseas eliminar: ")
if dato_a_eliminar in usuario:
    del usuario[dato_a_eliminar]
    print(f"\nDato '{dato_a_eliminar}' eliminado.")
else:
    print("\nEse dato no existe.")

print("\nDatos finales del usuario:")
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")
