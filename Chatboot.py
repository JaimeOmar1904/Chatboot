
import re
import random
import tkinter as tk

# Función para obtener la respuesta del bot
def obtener_respuesta(entrada_usuario):
    #En el mensaje que escribe el usuario tenemos que remover todos los caracteres especiales que escribe el usuario y utilizamos expresiones regulares
    mensaje_dividido = re.split(r'\s|[,:;.?!-_]\s*', entrada_usuario.lower())
    # Obtener la respuesta basada en el mensaje del usuario
    respuesta = verificar_todas_las_respuestas(mensaje_dividido)
    return respuesta

# Función para enviar el mensaje y mostrar la respuesta del bot
def enviar_mensaje():
    # Obtener el mensaje del usuario desde la entrada de texto
    mensaje_usuario = entrada_usuario.get()
    # Obtener la respuesta del bot
    respuesta_bot = obtener_respuesta(mensaje_usuario)
    # Habilitar el cuadro de texto para editar
    texto_chat.config(state=tk.NORMAL)
    # Mostrar el mensaje del usuario y la respuesta del bot en el cuadro de texto
    texto_chat.insert(tk.END, f"Usuario: {mensaje_usuario}\nBot: {respuesta_bot}\n")
    # Deshabilitar el cuadro de texto para evitar ediciones
    texto_chat.config(state=tk.DISABLED)
    # Limpiar la entrada de texto
    entrada_usuario.delete(0, tk.END)

# Función para verificar todas las respuestas predefinidas
def verificar_todas_las_respuestas(mensaje):
    mayor_probabilidad = {}

    # Función interna para registrar respuestas y palabras clave asociadas
    def respuesta(respuesta_bot, lista_de_palabras, respuesta_unica=False, palabras_requeridas=[]):
        nonlocal mayor_probabilidad
        mayor_probabilidad[respuesta_bot] = probabilidad_mensaje(mensaje, lista_de_palabras, respuesta_unica, palabras_requeridas)


     # Respuestas relacionadas con servicios escolares
    respuesta('¡Hola! ¿En qué puedo ayudarte?', ['hola', 'klk', 'saludos', 'buenas'], respuesta_unica=True)
    respuesta('Estoy bien, gracias por preguntar. ¿En qué puedo asistirte?', ['como', 'estas', 'va', 'vas', 'sientes'], palabras_requeridas=['como'])
    respuesta('La dirección de Servicios Escolares es en la avenida principal #456.', ['ubicados', 'direccion', 'donde', 'ubicacion'], respuesta_unica=True)
    respuesta('Siempre estamos disponibles para ayudarte. ¿En qué más puedo asistirte?', ['gracias', 'te lo agradezco',], respuesta_unica=True)

    # Respuestas adicionales (puedes agregar más según sea necesario)
    respuesta('¿Cómo puedo ayudarte con tu inscripción?', ['inscripción', 'matrícula', 'registro'], respuesta_unica=True, palabras_requeridas=['ayuda'])
    respuesta('Para obtener tu horario de clases, visita nuestro portal en línea de la Unam.', ['horario', 'clases', 'portal'], respuesta_unica=True)
    respuesta('Para solicitar un certificado, llena el formulario disponible en el sitio web de la institución.', ['certificado', 'formulario', 'solicitud'], respuesta_unica=True)
    respuesta('Los trámites administrativos se realizan en la oficina de Servicios Escolares. ¿En qué más puedo orientarte?', ['trámites', 'administrativos', 'oficina'], respuesta_unica=True)
    respuesta('Si experimentas dificultades técnicas durante la inscripción en línea, contacta al soporte técnico proporcionado en la página web o visita la oficina de Servicios Escolares para recibir ayuda.', ['dificultades tecnicas', 'inscripcion en linea', 'soporte tecnico', 'ayuda'], respuesta_unica=True)
    respuesta('¿Necesitas comprobante de estudios? Puedes generar un certificado de estudios desde tu cuenta en línea o solicitarlo en la oficina de Servicios Escolares.', ['comprobante', 'estudios', 'certificado', 'solicitar'], respuesta_unica=True)
    respuesta('Para realizar cambios en tu plan de estudios, programa una cita con un asesor académico en Servicios Escolares para discutir las opciones disponibles.', ['cambios', 'plan de estudios', 'cita', 'asesor academico'], respuesta_unica=True)
    respuesta('¿Necesitas realizar un trámite que no encuentras en la lista estándar? Pregunta en Servicios Escolares sobre procedimientos personalizados para casos especiales.', ['tramite', 'personalizado', 'casos especiales'], respuesta_unica=True)
    respuesta('Para obtener información sobre eventos académicos y extracurriculares, consulta el tablón de anuncios en la entrada de Servicios Escolares o visita nuestro sitio web.', ['eventos', 'academicos', 'extracurriculares', 'informacion'], respuesta_unica=True)
    respuesta('Si tienes preguntas sobre las políticas académicas de la institución, el personal de Servicios Escolares estará encantado de proporcionarte la información necesaria.', ['politicas', 'academicas', 'preguntas', 'informacion'], respuesta_unica=True)


    # Seleccionar la mejor coincidencia basada en la probabilidad
    mejor_coincidencia = max(mayor_probabilidad, key=mayor_probabilidad.get)
    # Devolver respuesta desconocida si la certeza es baja
    return desconocido() if mayor_probabilidad[mejor_coincidencia] < 1 else mejor_coincidencia

# Función para calcular la probabilidad de coincidencia de palabras clave
def probabilidad_mensaje(mensaje_usuario, palabras_reconocidas, respuesta_unica=False, palabras_requeridas=[]):
    certeza_mensaje = 0
    tiene_palabras_requeridas = True

    # Calcular la certeza basada en las palabras clave reconocidas
    for palabra in mensaje_usuario:
        #Vamos validando si las palabras estan entre las palabras reconocidas
        if palabra in palabras_reconocidas:
            certeza_mensaje += 1

    # Calcular el porcentaje de certeza
    porcentaje = float(certeza_mensaje) / float(len(palabras_reconocidas))

    # Verificar si se cumplen las palabras clave requeridas
    for palabra in palabras_requeridas:
        if palabra not in mensaje_usuario:
            tiene_palabras_requeridas = False
            break

    # Devolver el porcentaje de certeza si se cumplen las condiciones
    if tiene_palabras_requeridas or respuesta_unica:
        return int(porcentaje * 100)
    else:
        return 0

# Función para respuestas desconocidas
def desconocido():
    respuesta = ['¿Puedes decirlo de nuevo?', 'No estoy seguro de lo que quieres', 'Nesecitaras contactarte con uno de nuestros asesores'][random.randrange(3)]
    return respuesta

def limpiar_chat():
    texto_chat.config(state=tk.NORMAL)
    texto_chat.delete('1.0', tk.END)
    entrada_usuario.delete(0, tk.END)
    texto_chat.config(state=tk.DISABLED)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Bot de Chat")  #Cambiar el nombre de la ventana 
ventana.iconbitmap("bot-conversacional.ico") #Cambiar el icono
ventana.config(bg="#D5F5E3") #Cambiar color de fondo
ventana.resizable(0,0)

# Crear elementos de la interfaz gráfica
texto_chat = tk.Text(ventana, state=tk.DISABLED, wrap=tk.WORD, width=50, height=20)
entrada_usuario = tk.Entry(ventana, width=50)
#photo = PhotoImage(file = "path_of_file")
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_chat)

# Colocar elementos en la ventana
texto_chat.pack(pady=10)
entrada_usuario.pack(pady=10)
boton_enviar.pack(pady=10)
boton_limpiar.pack(pady=10, side=tk.RIGHT)
# Iniciar bucle principal de la interfaz gráfica
ventana.mainloop()