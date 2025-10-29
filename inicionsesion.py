#definimos usuario y contraseña
usuario_1 = "admin"
contrasena_2 = "1234"

intentos = 3

while intentos > 0:
    print("Inicio de sesion")
    usuario = input("Ingrese su usuario:")
    contrasena = input("Ingrese su contraseña:")

    if usuario == usuario_1 and contrasena == contrasena_2:
        print("Bienvenido")
        break

    else:
        intentos -= 1
        print(f"Usuario o contraseña incorrectos.Intentos restantes: {intentos}")

if intentos == 0:
        print("Ya no puedes entrar has superado el numero maximo de intentos")
