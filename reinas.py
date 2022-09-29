import random

def cromosoma_random(size): #Haciendo cromosomas aleatorios 
    return [random.randint(1, tamano_tablero) for _ in range(tamano_tablero)]

#Función que devuelve el fitness de una composición de reinas dada por un cromosoma
def fitness(cromosoma):
    encuentro_reinas_horizontal = sum([cromosoma.count(reina)-1 for reina in cromosoma])/2
    encuentro_reinas_diag = 0

    n = len(cromosoma)
    diag_izq = [0] * 2*n
    diag_der = [0] * 2*n
    for i in range(n):
        diag_izq[i + cromosoma[i] - 1] += 1
        diag_der[len(cromosoma) - i + cromosoma[i] - 2] += 1

    encuentro_reinas_diag = 0
    for i in range(2*n-1):
        contador = 0
        if diag_izq[i] > 1:
            contador += diag_izq[i]-1
        if diag_der[i] > 1:
            contador += diag_der[i]-1
        encuentro_reinas_diag += contador / (n-abs(i-n+1))
    
    return int(maxFitness - (encuentro_reinas_horizontal + encuentro_reinas_diag))

def probabilidad(cromosoma, fitness):
    return fitness(cromosoma) / maxFitness

def seleccion_random(poblacion, probabilidades):
    poblacionProbabilidad = zip(poblacion, probabilidades)
    total = sum(w for c, w in poblacionProbabilidad)
    rand = random.uniform(0, total)
    u = 0
    for c, w in zip(poblacion, probabilidades):
        if u + w >= rand:
            return c
        u += w
        
def cruza(x, y): #Cruza entre dos cromosomas
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]

def mutar(cromosoma_antiguo):  #Muta un cromosoma aleatoriamente
    n = len(cromosoma_antiguo)
    nuevo_cromosoma = random.randint(0, n - 1)
    nuevo_index_random = random.randint(1, n)
    cromosoma_antiguo[nuevo_cromosoma] = nuevo_index_random
    return cromosoma_antiguo

def seleccion_cromosomas(poblacion, fitness, prob_mut, prob_cruza):
    probabilidad_mutacion = prob_mut
    probabilidad_cruza = prob_cruza
    nueva_poblacion = [] #Se crea un vector nueva_poblacion en donde se guardaran los hijos de los mejores cromosomas de la poblacion actual
    probabilidades = [probabilidad(n, fitness) for n in poblacion]
    for i in range(len(poblacion)): #Recorre toda la poblacion
        x = seleccion_random(poblacion, probabilidades) #Mejor cromosoma
        y = seleccion_random(poblacion, probabilidades) #Segundo mejor cromosoma

        if random.random() < probabilidad_cruza:
            hijo = cruza(x, y) #Cruzar los dos mejores cromosomas para crear un nuevo cromosoma hijo

        if random.random() < probabilidad_mutacion:
            hijo = mutar(hijo) 
        
        imprimir_cromosoma(hijo)
        nueva_poblacion.append(hijo) #Se agrega este hijo al vector creado anteriormente
        if fitness(hijo) == maxFitness: break #Si el fitness del hijo es igual al fitness máximo, termina, pues encontró una posible solución
    return nueva_poblacion

def imprimir_cromosoma(chrom):
    print("Cromosoma = {},  Fitness = {}"
        .format(str(chrom), fitness(chrom)))

def semilla(seed):
    random.seed(seed)

if __name__ == "__main__":
    
    rand_seed = int(input("Ingrese la semilla: "))
    semilla(rand_seed)

    tamano_tablero = int(input("Ingrese el tamano del tablero: ")) #digamos que N = 8
    maxFitness = (tamano_tablero*(tamano_tablero-1))/2  # 8*7/2 = 28

    prob_mut = float(input("Ingrese la probabilidad de mutacion: "))

    prob_cruza = float(input("Ingrese la probabilidad de cruza: "))

    itMax = int(input("Ingrese la cantidad maxima de iteraciones: "))
    itActual = 1

    poblacion = [cromosoma_random(tamano_tablero) for _ in range(10)]

    generacion = 1

    while (not maxFitness in [fitness(chrom) for chrom in poblacion]) and (itActual != itMax):
        print("Generacion = {}".format(generacion))
        poblacion = seleccion_cromosomas(poblacion, fitness, prob_mut, prob_cruza)
        print("")
        print("Fitness Maximo = {}".format(max([fitness(n) for n in poblacion])))
        generacion += 1
        itActual += 1

    if(itActual != itMax):
        chrom_fin = []
        print("Resuelto en la generacion = {}!".format(generacion-1))
        for chrom in poblacion:
            if fitness(chrom) == maxFitness:
                print("")
                print("La solucion encontrada es: ")
                chrom_fin = chrom
                imprimir_cromosoma(chrom)
                
        tablero = []

        #Lleno el tablero de puras 'x'
        for x in range(tamano_tablero):
            tablero.append(["x"] * tamano_tablero)

        #Cambio las 'x' por 'R', donde corresponda    
        for i in range(tamano_tablero):
            tablero[tamano_tablero-chrom_fin[i]][i]="R"

        #Funcion que imprime el tablero completo con 'x' y 'R'       
        def print_tablero(tablero):
            for row in tablero:
                print (" ".join(row))
                
        print()
        print_tablero(tablero)
    else:
        print("Se llego a la iteracion maxima sin encontrar una solucion optima.")

    print()
    input('Presiona cualquier cosa para salir.')
