# Estructura de datos

# Son un modo de representar información en una computadora, además, cuentan con un comportamiento interno. Quiere decir que se rige por unas determinadas reglas y/o restricciones que han sido dadas por la forma en que está construida internamente. 
# ¿Cuál es su importancia?, cuando se mete al mundo de la programación, las estructuras de datos son fundamentales. Este te permite organizar mejor la información y crear código más eficiente. Además, es clave para mejorar las habilidades técnicas.

# ¿Para qué sirven las estructuras de datos?
# Son aquellas que nos permiten, como desarrollador, organizar la información de manera eficiente, y en definitiva diseñar la solución correcta para así evitar problemas.

# Más sobre listas:

# list.append(x)
# Agrega un ítem al final de la lista. Equivale a[len(a):] = [x].

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

#ejercicio 1
fruits.append('mango')
print('append:', fruits)

# list.extend(iterable)
# Extiende la lista agregándole todos los ítems del iterable. Equivale a a[len(a):] = iterable.

#ejercicio 2 
dulces =  ['chocolate','oreo']

dulces.extend(fruits)
print('extend:',dulces)

# list.insert(i, x)
# Inserta un ítem en una posición dada. El primer argumento es el índice del ítem delante del cual se insertará, por lo tanto, a.insert(0, x) inserta al principio de la lista y a.insert(len(a), x) equivale a.append(x).

#ejercicio 3
Numeros = ['1','2','3','4','5','6','7','8','9']

Numeros.insert(1,'wenas')
print('insert:',Numeros)


# list.remove(x)
# Quita el primer ítem de la lista cuyo valor sea x. Lanza un ValueError si no existe tal ítem.

#ejercicio 4
px = [2,4,6,8,10,12]

px.remove(6)

print('remove: ', px)

# list.pop([i])
# Elimina un elemento de la posición dada en la lista y lo devuelve. Si no se especifica ningún índice, a.pop() aparece y devuelve el último elemento de la lista. (Los corchetes alrededor de i en la firma del método significan que el parámetro es opcional, no que escriba los corchetes en el campo. Verá este texto a menudo en la Referencia de la biblioteca de Python).

#ejercicio 5
prime = [1,3,5,7]

removed = prime.pop(3)

print('Removed Element:', removed)
print('Updated List:', prime)

# list.clear()
# Elimina todos los elementos de la lista. Equivalente a de la[:].

#ejercicio 6
pag = ['Google', 'w3big', 'Taobao', 'Baidu']

pag.clear()
print ("clear : ", pag)

# list.index(x[, start[, end]])
# Retorna el índice basado en cero del primer elemento cuyo valor sea igual a x. Lanza una excepción ValueError si no existe tal elemento.
# El primer y último grupo se definen como contenido textual y se utilizan para limitar la búsqueda a una parte específica de la lista. La lista devuelta coincide con el comienzo de la lista completa, que no coincide con el primer argumento.

#ejercicio 7
print(fruits.index('banana'))
print(fruits.index('banana', 2))

# list.count(x)
# Retorna el número de veces que x aparece en la lista.

#ejercicio 8
print(fruits.count('apple'))

# list.sort(*, key=None, reverse=False)
# Ordena los elementos de la lista in situ (los argumentos pueden ser empleados para personalizar el orden de la lista, ver sorted() para su explicación).

#ejercicio 9
N = [2, 8, 1, 6, 3, 7, 4, 9]

N_sorted = sorted(N)
print(N_sorted)

# list.reverse()
# Invierte los elementos de la lista in situ.

#ejercicio 10
fruits.reverse()
print(fruits)

# list.copy()
# Retorna una copia superficial de la lista. Equivalente a a[:].

#ejercicio 11
Nr = [2, 4, 6,]

numbers = Nr.copy()

print('Copied List:', numbers)



# listas como pilas
# Los métodos de lista hacen que resulte muy fácil usar una lista como una pila, donde el último elemento añadido es el primer elemento retirado («último en entrar, primero en salir»). Para agregar un elemento a la cima de la pila, utiliza append(). Para retirar un elemento de la cima de la pila, emplea pop() sin un índice explícito.

pila = [1,2,4]
pila.append(8)
pila.append(9)
print(pila)

# Listas como colas
# También es posible utilizar una lista como una cadena, donde el primer elemento agregado es el primer elemento eliminado (“antes de, antes de”); sin embargo, los nombres no funcionan para este propósito. Sumar y restar desde el final de la lista es rápido, pero sumar o restar desde el principio de la lista es lento (porque cada elemento debe ser reemplazado por otro). Para crear una cola, use collections.deque, que está diseñado para agregarse y eliminarse rápidamente en ambos lados.


from collections import deque
cola = deque(['Hector','Juan','Miguel'])
cola.append('Maria')
cola.append('Arnaldo')
print(cola.popleft())
persona = cola.popleft()
print(persona)
print(cola)

# Comprensión de listas
# Comprender los guiones proporciona un atajo para ocasionar conversaciones. A menudo se usa para crear nuevos registros donde cada elemento es el resultado de una operación diferente aplicada a cada miembro de una secuencia o repetición, o para crear una secuencia de estos elementos para satisfacer la condición dada.

lista = []
for numero in range(0,11):
    lista.append(numero**2)

pares = []   
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

#Listas por comprensión anidadas
# El primer tipo de comprensión narrativa puede ser cualquier afirmación abstracta, incluida alguna comprensión narrativa.

matriz = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]
matrix = [] 
  
for i in range(5): 
      
    
    matrix.append([]) 
      
    for j in range(5): 
        matrix[i].append(j) 
          
print(matrix) 

# La instrucción de1
# Hay una manera de eliminar un elemento de una lista por su índice en lugar de su valor:
# Declaración Esto es diferente del método pop(), que devuelve un valor. La declaración del también se puede utilizar para eliminar elementos de una lista o para eliminar una lista completa.

a = [-2, 1, 77.5, 888, 888, 5123.9]
del a[0]
print(a)
del a[2:4]
print(a)

# Tuplas y secuencias
# Hemos visto que las matrices y las cadenas comparten propiedades, como las operaciones de indexación y partición. Estos son dos ejemplos de tipos de datos. Dado que Python es un lenguaje cruzado, se puede agregar cierta información de cadena. 

x = ("manzana", "plátano", "cereza")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

lista_enteros = [10, 5, 1, 130, -2]
print(f'El tipo de {lista_enteros} es {type(lista_enteros)}.')
x = lista_enteros[0]
y = lista_enteros[1]
z = lista_enteros[4]
print(x, y, z)

# Conjuntos
# Python también incluye un tipo de datos para matrices. Un conjunto es una colección aleatoria sin elementos repetidos. Su uso principal consiste en verificar miembros y eliminar duplicados. Los conjuntos también admiten operaciones matemáticas como unión, intersección, diferencia y diferencia simétrica.

group_a = set(['Ali', 'Moria', 'Luffy', 'Zoro'])
group_b = {'Roger', 'Garp', 'Nami', 'Robin'}
group_c = {'boa', 'Franky', 'Shanks', 'Pepe'}
all_students = group_a.union(group_b).union(group_c)
print(all_students)

# Diccionarios
# Otro cualquiera de apunte herramienta incluido en Python es el diccionario. Los diccionarios se encuentran a veces en otros lenguajes como «autobiografía asociativa» o «arreglos asociativos». A discrepancia de las secuencias, que se indexan mediante una jerarquía numérica, los diccionarios se indexan con claves, que pueden ser cualquier cualquiera inmutable; las esposas y números siempre pueden ser claves. Las tuplas pueden estar de moda como claves si nada más contienen esposas, números o tuplas; si una tupla contiene cualquier impresión mutable directa o indirectamente, no puede estar de moda como clave. No puedes disfrutar listas como claves, ya que las listas pueden variar usando paga por índice, paga por sección, o métodos como append() y extend().
import random
clientes = ["Alex","Rick","Brayan","Miguel","Luis","Jose","Juan"]
diccionario_descuentos = {cliente:random.randint(1,100) for cliente in clientes}
print(diccionario_descuentos)