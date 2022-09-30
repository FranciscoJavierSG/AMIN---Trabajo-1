# Algoritmos Metaheurísticos Inspirados en la Naturaleza
*Autores: José Avilán (javilan@ing.ucsc.cl) y Francisco Salazar (fsalazarg@ing.ucsc.cl)*

El programa tiene como objetivo encontrar una distribución de n reinas en un tablero de nxn, de tal modo que éstas no colisionen entre sí.

## Instalación
Antes de ejecutar el programa, es necesario:
- Tener instalado Python 3.8.10 en su sistema.
- Para descargar el programa, presione en el siguiente [enlace](https://codeload.github.com/FranciscoJavierSG/AMIN---Trabajo-1/zip/refs/heads/main?token=AJXTOXE4F3DK6UAFPFH5NPLDGZ436).

## Ejecución 
Para ejecutar el programa, escriba lo siguiente en la consola o terminal de su sistema operativo:

```       
py reinas.py <Semilla><Tamaño_Tablero><Tamaño_Pob><Prob_Cruza><Prob_Mutación><Num_It>
```

Donde:
- **Semilla**: Número entero positivo que representa el valor de la semilla.
- **Tamaño_Tablero**: Dimensiones del tablero, expresadas en valores enteros positivos. Por ejemplo, en caso de querer un tablero de 8x8, se debe ingresar 8.
- **Tamaño_Pob**: Valor entero positivo que representa la cantidad de cromosomas a crear y replicar.
- **Prob_Cruza**: Valor decimal entre 0.0 y 1.0, que representa la probabilidad de que dos cromosomas se crucen y generen descendencia.
- **Prob_Mutación**: Valor entre 0.0 y 1.0 que representa la probabilidad de que la cruza entre dos cromosomas genere una mutación de sus genes.
- **Num_It**: Número entero positivo mayor que 1 que representa la cantidad de iteraciones a realizar. El programa se ejecutará hasta encontrar esta limitante o hasta encontrar un individuo que tenga el fitness máximo.

## Ejemplo de Ejecución

```
py reinas.py 0 8 8 0.99 1 100000
```

