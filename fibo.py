# Se importa la librería unittest para poder trabajar con sus funciones 
import unittest

# Se define una lista inicial de Fibonacci con los dos primeros elementos
lista_fibonacci = [0,1]

# Aquí empieza el algoritmo propiamente de Fibonacci
def fibonacci ():
    numero_1 = 0
    numero_2 = 1
    numero_fibonacci = 0

    # Solicita cuántas cifras vamos a querer en nuestra lista de Fibonacci
    numero_sucesion = int(input ("Escriba el número de cifras que tendrá la sucesión de Fibonacci deseada: "))
    print ("\n")

    # Bucle en el que se calculan los números, iterando numero_sucesion-2 veces ya que los dos primeros 
    # números de Fibonacci ya están en la lista, y actualizando la lista en cada iteración
    for iterador in range (0, numero_sucesion-2):
        numero_fibonacci = numero_1 + numero_2
        lista_fibonacci.append(numero_fibonacci)
        numero_1 = numero_2
        numero_2 = numero_fibonacci

    # Se hace la impresión por pantalla de la lista completa
    print (*lista_fibonacci, sep=", ")
    print ("\n")

# Se declara la clase de testeo para definir en ella la función para comprobar el valor de una posición dada
class Test(unittest.TestCase):
    def test_Check_Position(self):
        posicion_pedida = int (input ("Escriba la posición a comprobar deseada: "))
        valor_esperado = int (input ("Escriba el valor que debería estar en la posición deseada: "))
        self.assertEqual(lista_fibonacci[posicion_pedida-1], valor_esperado)


# Inicio del main del programa, en el que se llama a la función de Fibonacci y al main de unittest   
if __name__ == "__main__":
    fibonacci ()
    unittest.main()


