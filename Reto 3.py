def ruteo(distancias: dict, ruta_inicial: list)-> dict:
    cov_distancia = distancias.items()
    valores = distancias.values()
    
    for i in valores:
        if i < 0:
            return 'Por favor revisar los datos de entrada.'
    
    for i, j in cov_distancia:
        if i[0] == i[1]:
            if j != 0:
                return 'Por favor revisar los datos de entrada.'
                     
    distancia_inicial = 0
    for i in range(0,len(ruta_inicial)-1):
        distancia_inicial = distancia_inicial + distancias[ruta_inicial[i],ruta_inicial[i+1]]

    ruta_iteracion = ruta_inicial.copy()
    distancia_iteracion = 0
    distancia_mejor = distancia_inicial
    ruta_mejor = ruta_inicial
    respuesta = ''
    salida = 1
    llegada = 2
    mejoro = True
    
    while mejoro == True:
        while salida < len(ruta_inicial)-1:
            while llegada < len(ruta_inicial)-1:
                  if salida < llegada:
                        
                      comp1=ruta_inicial[salida]
                      comp2= ruta_inicial[llegada]
                      ruta_iteracion[salida]= comp2
                      ruta_iteracion[llegada]= comp1
                      
                      for i in range(0,len(ruta_inicial)-1):
                          distancia_iteracion = distancia_iteracion + distancias[ruta_iteracion[i],ruta_iteracion[i+1]]
                      
                      
                      if distancia_iteracion < distancia_mejor:
                          distancia_mejor = distancia_iteracion
                          ruta_mejor = ruta_iteracion.copy()
                
                  
                  distancia_iteracion = 0
                  ruta_iteracion = ruta_inicial.copy()
                  llegada = llegada + 1
            
            salida = salida + 1
            llegada = 2
        if ruta_mejor == ruta_inicial:
            mejoro = False
        ruta_inicial = ruta_mejor.copy()
        ruta_iteracion = ruta_inicial.copy()
        salida = 1
        llegada = 2
        
        
    for i in range (0,len(ruta_inicial)-1):
        respuesta = respuesta + ruta_inicial[i] + "-"
    respuesta = respuesta + ruta_inicial[len(ruta_inicial)-1]
    d= {'ruta': respuesta, 'distancia': distancia_mejor}
    return d
               
print(ruteo({('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241,
('A', 'H'): 127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41,
('B', 'H'): 153, ('B', 'A'): 252, ('B', 'B'): 0, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269,
('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0, ('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180,
('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'): 194, ('D', 'F'): 109,
('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119,
('F', 'H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0}
,['H', 'A', 'B', 'C', 'D', 'E', 'F', 'H']))
    
    
    
    
    
        
        