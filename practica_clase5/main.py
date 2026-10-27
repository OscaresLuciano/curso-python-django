#Importacion de un modulo
import red_social.datos as datos
import red_social.formateador as formateador
from red_social import publicaciones, listar_publicaciones, validar_publi

#Importacion con alias
import red_social.formateador as fmt

print(datos.publicaciones[0])

#Esto:
from red_social.formateador import listar_publicaciones
listar_publicaciones(datos.publicaciones)

#Es lo mismo que hacer esto:
fmt.listar_publicaciones(datos.publicacion)

from red_social.validaciones import validar_publi

for publi in datos.publicaciones:
    if validar_publi(publi):
        print(f"La descripcion '{publi['descripcion_publicacion']} es valida")
    else:
        print(f"La publicacion con ID {publi[id]} tiene datos incompletos")


#Importacion de varios elementos
from red_social.formateador import crear_separador, formatear_publicacion
print(crear_separador())
print(formatear_publicacion(datos.publicaciones[0]))
