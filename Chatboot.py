
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

    # Definir respuestas predefinidas y palabras clave asociadas
    #respuesta('Hola', ['hola', 'klk', 'saludos', 'buenas'], respuesta_unica=True)
    #respuesta('Estoy bien y tú?', ['como', 'estas', 'va', 'vas', 'sientes'], palabras_requeridas=['como'])
    #respuesta('Estamos ubicados en la calle 23 numero 123', ['ubicados', 'direccion', 'donde', 'ubicacion'], respuesta_unica=True)
    #respuesta('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], respuesta_unica=True)

     # Respuestas relacionadas con servicios escolares
    respuesta('¡Hola! ¿En qué puedo ayudarte?', ['hola', 'klk', 'saludos', 'buenas'], respuesta_unica=True)
    respuesta('Estoy bien, gracias por preguntar. ¿En qué puedo asistirte?', ['como', 'estas', 'va', 'vas', 'sientes'], palabras_requeridas=['como'])
    respuesta('La dirección de Servicios Escolares es en la avenida principal #456.', ['ubicados', 'direccion', 'donde', 'ubicacion'], respuesta_unica=True)
    respuesta('Siempre estamos disponibles para ayudarte. ¿En qué más puedo asistirte?', ['gracias', 'te lo agradezco', 'thanks'], respuesta_unica=True)

    # Respuestas adicionales (puedes agregar más según sea necesario)
    respuesta('¿Cómo puedo ayudarte con tu inscripción?', ['inscripción', 'matrícula', 'registro'], respuesta_unica=True, palabras_requeridas=['ayuda'])
    respuesta('Para obtener tu horario de clases, visita nuestro portal en línea.', ['horario', 'clases', 'portal'], respuesta_unica=True)
    respuesta('Para solicitar un certificado, llena el formulario disponible en el sitio web de la institución.', ['certificado', 'formulario', 'solicitud'], respuesta_unica=True)
    respuesta('Los trámites administrativos se realizan en la oficina de Servicios Escolares. ¿En qué más puedo orientarte?', ['trámites', 'administrativos', 'oficina'], respuesta_unica=True)

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
    respuesta = ['¿Puedes decirlo de nuevo?', 'No estoy seguro de lo que quieres', 'Búscalo en Google a ver qué tal'][random.randrange(3)]
    return respuesta

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Bot de Chat")

# Crear elementos de la interfaz gráfica
texto_chat = tk.Text(ventana, state=tk.DISABLED, wrap=tk.WORD, width=50, height=20)
entrada_usuario = tk.Entry(ventana, width=50)
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)

# Colocar elementos en la ventana
texto_chat.pack(pady=10)
entrada_usuario.pack(pady=10)
boton_enviar.pack(pady=10)

# Iniciar bucle principal de la interfaz gráfica
ventana.mainloop()