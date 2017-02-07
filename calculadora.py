#!/usr/bin/python3
import sys 
sys.argv

if len(sys.argv) != 4:
	sys.exit("Debes poner: calculadora.py operacion operando1 operando2")

operacion = sys.argv[1]
operando1 = sys.argv[2]
operando2 = sys.argv[3]


def sumar(operando1,operando2):
	return(float(operando1) + float(operando2))

def restar(operando1,operando2):
	return(float(operando1) - float(operando2))

def multiplicar(operando1,operando2):
	return(float(operando1) * float(operando2))

def dividir(operando1,operando2):
	return(float(operando1) / float(operando2))

try:
	if operacion == 'suma':
		print(sumar(operando1,operando2))
	elif operacion == 'resta':
		print(restar(operando1,operando2))
	elif operacion == 'mult':
		print(multiplicar(operando1,operando2))
	elif operacion == 'dividir':
		print(dividir(operando1,operando2))
	else: 
		print("Operacion invalida")
except ZeroDivisionError:
	print("No puedes dividir por cero")
	
