from models import Estudiante
from models import Profesor
from models import Asignatura
from nose.tools import assert_equal

# Create your tests here.

class Test:
	def testCrearEstudiante(self):
		usuario = Estudiante(nombre='nuevoE', dni='12345678A')
		assert_equal(usuario.nombre, 'nuevoE')
		assert_equal(usuario.dni, '12345678A')
		
	def testCrearProfesor(self):
		usuario = Profesor('nuevoP')
		response = usuario.nombre
		assert_equal(response, 'nuevoP') 
		
	def testCrearAsignatura(self):
		asig = Asignatura('nuevaA')
		response = asig.nombre
		assert_equal(response, 'nuevaA') 
