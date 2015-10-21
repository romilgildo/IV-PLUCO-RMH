from models import Estudiante
from models import Profesor
from models import Asignatura
from nose.tools import assert_equal

class Test:
	def calcularCuadrado(self, numero):
		return numero*numero
		
	def testCuadrado(self):
		cuadrado = Test()
		response = cuadrado.calcularCuadrado(4)
		assert_equal(response, 16)

	def testCrearEstudiante(self):
		usuario = Estudiante('nuevoE')
		response = usuario.nombre
		assert_equal(response, 'nuevoE') 
		
	def testCrearProfesor(self):
		usuario = Profesor('nuevoP')
		response = usuario.nombre
		assert_equal(response, 'nuevoP') 
		
	def testCrearAsignatura(self):
		asig = Asignatura('nuevaA')
		response = asig.nombre
		assert_equal(response, 'nuevaA') 
