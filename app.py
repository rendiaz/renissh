import os
os.system("cls")
# ETAPAS:
# Un sistema que consulte la edad, y de acuerdo a ella indique si la persona es mayor de edad o no.
print("ejercicio 1:consultar edad")
try:
    edad= int(input("ingrese su edad\n"))
    if edad >= 18 and edad <= 100:
        
        print("mayor de edad")
    elif edad < 18 and edad > 1:
        print("menor de edad")
    else: 
        edad= False
        print("ingrese valor numerico")
except:("valor edad debe ser numerico ")


# Crear un programa de validación de usuario y contraseña (consultar usuario y contraseña), los únicos dos usuarios conectados son:
# User1: pedro   	Contraseña1: 1234
# User2: angel		Contraseña2: a4s1

# Solicitar el ingreso de 3 notas por pantalla, luego calcular el promedio de las 3 notas (cada nota tiene la misma ponderación), finalmente indicar con una salida de pantalla “Aprobado” en el caso de que el promedio sea igual o mayor a 4.0.

# Crear una salida por pantalla con la siguiente información:

# ¿Cuál de los siguientes animales vive en el agua?
# Perro
# Cocodrilo
# Conejo
# Tiburón

# Si la respuesta es Cocodrilo, asignar +0.5 a puntaje, si la res-puesta es Tiburón asignar +1.0 a puntaje, del cualquier otro caso, no asignar valor, finalmente crear una salida por panta-lla para mostrar el puntaje obtenido.

# De la misma forma del ejercicio anterior, debes crear un formulario con 3 pre-guntas (4 respuestas por cada pregunta) de un tema a elección, ya sea pe-lículas, series, caricaturas, entre otras.

# Asignar puntaje a cada pregunta y dependiendo del puntaje generar una escala de notas, así cuando los usuarios respondan las 3 preguntas se les muestra mediante una salida por pantalla su puntaje obtenido y la nota que equivale.

# Instrucciones para el envío de la actividad

# El representante del grupo deberá comprimir los programas y enviar al docente a través de Mensajes de AVA, utilizando el siguiente formato para el nombre del archivo:
# NombreApellido_NombreApellido_NombreApellido.RAR

