#___________FUNCIONES____________

# Crear una función
def guardar_publicacion():
    print("Publicación guardada")

# Llamada a la funcion
guardar_publicacion()

#Funcion con un parametro
guardada = False
def guardar_publicacion_con_parametro(publicacion):
    guardada = True
    print("Publicación guardada con parametro")

guardar_publicacion_con_parametro(guardada)

#Funcion con mas de un parametro
nombre_usuario = "Raul"

def guardar_publicacion(publicacion, usuario):
    guardada = True
    print(f"Publicación de {usuario} guardada con éxito")

guardar_publicacion(guardada, nombre_usuario)

#Funcion con condicional if
cantidad_likes = 105
def validacion_publicacion(publicacion):
    if cantidad_likes < 50:
        print(f"La publi tiene pocas interacciones")
    elif cantidad_likes < 100:
        print(f"La publi tiene buenas interacciones")
    else:
        print("La publicación es muy popular!!!")

validacion_publicacion(cantidad_likes)

comentarios = ["Comentario 1", "Comentario 2", "Otro comentario"]

def agregar_comentrio(publi):
    nuevo_comentario = input("Ingrese un nuevo comentario: ")
    comentarios.append(nuevo_comentario)
    print(comentarios)
    print("El comentario se agregó con éxito")

#agregar_comentrio(comentarios)

#Función con Return
comentarios = ["Comentario 1", "Comentario 2", "Otro comentario"]

def contar_comentarios(publi):
    cantidad_comentarios = len(publi)
    return cantidad_comentarios

cantidad_comentarios = contar_comentarios(comentarios)
print(cantidad_comentarios)

def validar_comentario():
    nuevo_comentario = input("Ingrese el nuevo comentario: ")
    if nuevo_comentario == "":
        return "Error: el comentario no puede estar vacio"
    return "Comentario valido"

"""if validar_comentario():
    print("El comentario puede agregarse a la publicación")
else:
    print("El comentario no puede ser agregado")"""

#Funcion con return de multiples valores
usuario = {
    "nombre": "Luciano",
    "ubicacion": "Glew"
    }

def normalizar_datos(usuario):
    nombre_normalizado = usuario["nombre"].lower()
    ubicacion_normalizada = usuario["ubicacion"].strip()
    return nombre_normalizado, ubicacion_normalizada

resultado = normalizar_datos(usuario)
print(resultado)


#________ TRY - EXCEPT ___________

"""try:
    #Codigo q genera un error
    numero = int(input("Ingrese un numero: "))
    print(numero)
except ValueError:
    #qué hacemos si ocurre el error
    print("Tenes que ingresar un numero")"""

def pedir_id():
    try:
        id_post = int(input("Ingrese el ID del post: "))
        print(id_post)
    except ValueError:
        print("El ID ingresado es incorrecto")
        return None

#pedir_id()

posts = {
    "id": 1
}

def buscar_post():
    try:
        id_buscado = int(input("Ingresa el ID del post que queres buscar: "))
        encontrado = False

        for post in posts:
            if post["id"] == id_buscado:
                print("¡POST ENCONTRADO!")
                encontrado = True
                break
        if not encontrado:
            print("No existe un post con ese ID")

    except ValueError:
        print("El ID ingresado es incorrecto")

#buscar_post()

#KEY ERROR

def mostrar_autor():
    post = {
        "titulo": "Probando errores",
        "contenido": "Estoy probando los errores"
    }

    try:
        print(f"Autor: {post["autor"]}")

    except KeyError:
        print("Error, el post no tiene el autor cargado")

#mostrar_autor()

#EXCEPT ZERODIVISIONERROR

def dividir():
    try:
        num1 = int(input("Ingrese un número "))
        num2 = int(input("Ingrese otro número "))

        resultado = num1 // num2
        print(f"Resultado: {resultado}")
    except ValueError:
        print("ERROR: Tenes que ingresar numeros")
    except ZeroDivisionError:
        print("ERROR: No se puede dividir por cero")

#dividir()

#ELSE
def ingresar_edad():
    try:
        edad = int(input("Ingrea tu edad "))
    except ValueError:
        print("Error: Tenes q ingresar un numero")
    else:
        print(f"Edad ingresada correctamente {edad}")

#ingresar_edad()

#FINALLY

def ingresar_numero():
    try:
        numero = int(input("Ingresa un numero "))
        print(numero)

    except ValueError:
        print("Error tenes q ingresar un numero")

    finally:
        print("FIN DEL PROGRAMA")

ingresar_numero()