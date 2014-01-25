# -*- coding: utf-8 -*-

def decoracion_condicional(fbool):
	def decorador(f):
		def aux (*args,**kwargs):
			if fbool(*args,**kwargs):
				return f(*args,**kwargs)
		return aux
	return decorador
	
	
def imprimi_argu(*args,**kwargs):
	print args
	print kwargs
	
def cardinalidad(*args,**kwargs):
	return len(args)!= len(kwargs)
	
prueba=imprimi_argu
fbool=cardinalidad
decorador=decoracion_condicional(fbool)	

funcion_decorada=decorador(prueba)

args=(1,2, )
kwargs={'a':10,'b':20,'c':30}

funcion_decorada(*args,**kwargs)
