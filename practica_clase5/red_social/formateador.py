def crear_separador():
    return "-" * 120

def formatear_publicacion(publicacion):
    titulo = publicacion["descripcion_publicacion"]
    estado = publicacion["estado"]
    usuario = publicacion["nombre_usuario"]
    likes = publicacion["cantidad_likes"]
    return f"""Titulo_ {titulo} | Usuario: {usuario} | Estado: {estado} | Likes{likes}"""

def listar_publicaciones(lista_publi):
    for publi in lista_publi:
        print(crear_separador())
        print(formatear_publicacion(publi))