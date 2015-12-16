from models import Usuario
from models import Asignatura
from nose.tools import assert_equal

# Create your tests here.

class Test:
	def testCrearEstudiante(self):
		usuario = Usuario(nombre='nuevoE', email='direccion@correo.ugr.es', tipo='Estudiante')
		assert_equal(usuario.nombre, 'nuevoE')
		assert_equal(usuario.email, 'direccion@correo.ugr.es') 
		assert_equal(usuario.tipo, 'Estudiante')
		
	def testCrearProfesor(self):
		usuario = Usuario(nombre='nuevoP', email='direccion@ugr.es', tipo='Profesor')
		assert_equal(usuario.nombre, 'nuevoP')
		assert_equal(usuario.email, 'direccion@ugr.es') 
		assert_equal(usuario.tipo, 'Profesor')
		
	def testCrearAsignatura(self):
		asig = Asignatura('nuevaA')
		response = asig.nombre
		assert_equal(response, 'nuevaA') 
