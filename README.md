## Conjunto

Establecer la forma de crear conjunto numericos.

Establecer el conjunto de referencia (o universal)


## Ejemplo:

A = conjunto[0..5]      //Define el conjunto {0,1,2,3,4,5}

B = conjunto[0..10, 2]  //Define el conjunto {0,2,4,6,8,10}


## Operaciones:

- Intersección

- Unión

- Diferencia

- Complemento

- Asignación

- Mostrar

- Pertenece Elemento

- Sumar Elementos

- Promediar Elementos

- Longitud


## Ejemplos:

A = set[1,10,2]     // {1,3,5,7,9}

A.belong(3)         // Return True

C = A.intersect(B)

o

C = A inter B

A                   // Muestra el conjunto

res = A.sum

## Tecnologias usada

  - Python3
  - Antlr4 ( https://www.antlr.org/ )

## Ejecutar proyecto

  1 - Creamos la arismetica:
      
      antlr4 Arismetica.g4
      
  2 - Ejecutamos con python3:
  
      python3 compilador.py
    
