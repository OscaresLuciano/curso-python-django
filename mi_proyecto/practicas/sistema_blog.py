# Nombre del archivo "sistema_blog.py"

perfil_autor = {
    "nombre": "Edgar López",
    "bio": "Explorador de lugares exóticos",
    "especialidad": "Tecnología aplicada a viajes y turismo",
    "redes_sociales": ["@edgar_lopez", "@edgar_viaja"]
}

estados_post = ("borrador", "publicado", "archivado")

etiquetas_blog = {"Python", "Desarrollo", "Web", "IA", "Web"}

posts = [
{
    "id": 1,
    "titulo": "Cómo uso la tecnología para viajar por China",
    "contenido": "Consejos practicos para vencer las barreras del lenguaje",
    "autor": perfil_autor,
    "tags": ["Python", "Web"],
    "estado": "publicado"
},
{
    "id": 2,
    "titulo": "Apps y herramientas para viajar por Benín",
    "contenido": "Cómo lo tecnología actual nos facilita movernos por lugares desconocidos",
    "autor": perfil_autor,
    "tags": ["IA", "Desarrollo"],
    "estado": "archivado"
},
{
    "id": 3,
    "titulo": "Tecnología que me ayudó a recorrer Nueva York",
    "contenido": "Facilidades de viajar por una ciudad avanzada",
    "autor": perfil_autor,
    "tags": ["Desarrollo", "Web"],
    "estado": "borrador"
}]

print("\n--- MENÚ DEL BLOG ---\n")
print("1. Ver todos los posts")
print("2. Buscar por título")
print("3. Filtrar por tag")
print("4. Salir\n")

while True:
    opcion_elegida = input("\nIngrese el número de la opción que desea: ")
    print("\nOpción", opcion_elegida, "seleccionada")
    if opcion_elegida == "1":
        print("\nPosts disponibles:\n")
        for post in posts:
            print(post["titulo"], " | Autor: ", post["autor"]["nombre"])
    elif opcion_elegida == "2":
        titulo_elegido = input("Ingrese el titulo del post que busca: ").lower()
        for post in posts:
            if titulo_elegido in post["titulo"].lower():
                print("\nPost encontrado: ",post["titulo"])
    elif opcion_elegida == "3":
        tag_elegido = input("Ingrese la etiqueta que desea buscar: ").lower()
        print("Posts con el tag ",tag_elegido)
        for post in posts:
            for tag in post["tags"]:
                if tag_elegido == tag.lower():
                    print("\nPost encontrados: ",post["titulo"])
    elif opcion_elegida == "4":
        print("\nGracias por usar el sistema del blog. ¡Hasta luego!\n")
        break
    else:
        print("\nOpción inválida, intenta de nuevo")
