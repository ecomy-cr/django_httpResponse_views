from django.http import HttpResponse
import datetime
from django.template import Template, Context
# from django.template import loader

from django.template.loader import get_template
from django.shortcuts import render

def bienvenida(request): 
	return HttpResponse("Bienvenido o bienvenida a este curso de Django. =)")

def bienvenidaRojo(request):
	return HttpResponse("<p style='color: red;'>Bienvenido o bienvenida a este curso de Django. ;)</p>")

def categoriaEdad(request, edad):
	if edad >= 18:
		if edad >= 60:
			categoria = "Tercera edad"
		else:
			categoria = "Adultez"
	else:
		if edad < 10:
			categoria = "Infancia"
		else:
			categoria = "Adolescencia"
	resultado = "<h1>Categoría de la edad: %s</h1>" %categoria
	return HttpResponse(resultado)

def obtenerMomentoActual(request):
	# respuesta = "<h1>Momento actual: {0}</h1>".format(datetime.datetime.now())
	respuesta = "<h1>Momento actual: {0}</h1>".format(datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
	return HttpResponse(respuesta)
	
def contenidoHTML(request, nombre, edad):
	contenido =  """
	<html>
	<body>
	<p>Nombre: %s / Edad: %s</p>
	</body>
	</html>
	""" % (nombre, edad)
	return HttpResponse(contenido)
