# Nombre del archivo: estructura_blog.py

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
    "autor": perfil_autor,
    "tags": ["Python", "Web"],
    "estado": "publicado"
},
{
    "id": 2,
    "titulo": "Apps y herramientas para viajar por Benín",
    "autor": perfil_autor,
    "tags": ["IA", "Desarrollo"],
    "estado": "archivado"
},
{
    "id": 3,
    "titulo": "Tecnología que me ayudó a recorrer Nueva York",
    "autor": perfil_autor,
    "tags": ["Desarrollo", "Web"],
    "estado": "borrador"
}]

print("Autor del segundo post: ",posts[1]["autor"]["nombre"])
print("Lista de los posts guardados: ")
print(posts)