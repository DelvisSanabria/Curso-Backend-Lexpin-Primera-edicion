#Pywhatkit es una libreria que nos permite interactuar con whatsapp desde python

import pywhatkit

#Enviar un mensaje a un numero de forma automatica

pywhatkit.sendwhatmsg_instantly("+584129240174", "Hola Jesus desde python") # type: ignore


group_id = "Iv1YpX94pkJBv2IkUt6FLD"
#Enviar un mensaje a un grupo de forma automatica
pywhatkit.sendwhatmsg_to_group_instantly(group_id, "Hola Grupo desde python") # type: ignore

#Podemos programar el envio de mensajes automaticos en una hora y minuto especifico

# la estructura es la siguiente: pywhatkit.sendwhatmsg("numero", "mensaje", hora, minutos, segundos, (cierra el chat true o false), (tiempo de espera de cerrar la ventana en segundos))

pywhatkit.sendwhatmsg("+584129240174", "Hola Jesus desde python a una hora especifica", 18, 44, 20, True, 5) # type: ignore

pywhatkit.sendwhatmsg_to_group(group_id, "Hola Grupo desde python a una hora especifica", 18, 49, 20, True, 5) # type: ignore

#Enviar imagenes a un numero de forma automatica


pywhatkit.sendwhats_image("+584129240174","Python/especializado/auto_whatsApp/Lexpin_Icono_color.png", "Hola Jesus desde python") # type: ignore

#Para grupos de whatsapp
pywhatkit.sendwhats_image(group_id, "Python/especializado/auto_whatsApp/Lexpin_Icono_color.png", "Hola Jesus desde python") # type: ignore
