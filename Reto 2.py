def prestamo(informacion:dict):
    
    ID = informacion['id_prestamo']
    casado = informacion['casado']
    dep = informacion['dependientes']
    edu = informacion['educacion']
    ind = informacion['independiente']
    i_d = informacion['ingreso_deudor']
    i_c = informacion['ingreso_codeudor']
    c_p = informacion['cantidad_prestamo']
    p_p = informacion['plazos_prestamo']
    hist = informacion['historia_credito']
    prop = informacion['tipo_propiedad']
    
    if dep == '3+':
       dep = 3  
    if hist =='Si' :
       hist = 1
    else:
        hist = 0    
    if ind == 'Si':
        ind = 1
    else:
        ind = 0
    if casado == 'Si':
       casado = 1
    else:
       casado = 0
    if prop == 'Rural':
       prop = 0
    else:
       if prop == 'Urbano':
           prop = 1
       else:
           prop = 2
   
    if hist > 0:
       if i_c > 0 and (i_d/9) > c_p:
           d2 = dict(id_prestamo=ID,aprobacion=True)
           return(d2)
       else:
            if int(dep) > 2 and int(ind) > 0:
                if i_c/12 > c_p:
                    d2 = dict(id_prestamo=ID,aprobacion=True)
                    return(d2)
                else:
                    d2 = dict(id_prestamo=ID,aprobacion=False)
                    return(d2)
            else:
                if c_p < 200:
                    d2 = dict(id_prestamo=ID,aprobacion=True)
                    return(d2)
                else:
                    d2 = dict(id_prestamo=ID,aprobacion=False)
                    return(d2)
              
    else:
        
        if int(ind) > 0: 
            if not(casado > 0 and dep>1):
                if i_d/10 > c_p or i_c/10 > c_p:
                    if c_p < 180:
                        d2 = dict(id_prestamo=ID,aprobacion=True)
                        return(d2)
            
                    else:
                        d2 = dict(id_prestamo=ID,aprobacion=False)
                        return(d2)
                else:
                     d2 = dict(id_prestamo=ID,aprobacion=False)
                     return(d2)
            else:
                 d2 = dict(id_prestamo=ID,aprobacion=False)
                 return(d2)
        else:   
            if int(prop) < 2 and int(dep) < 2:
                if str(edu) == 'Graduado':
                    if i_d/11 > c_p and i_c/11 > c_p:
                        d2 = dict(id_prestamo=ID,aprobacion=True)
                        return(d2)
                    else:
                        d2 = dict(id_prestamo=ID,aprobacion=False)
                        return(d2)
                else:
                    d2 = dict(id_prestamo=ID,aprobacion=False)
                    return(d2)
            else:
                d2 = dict(id_prestamo=ID,aprobacion=False)
                return(d2)
            
print("Ingrese los siguientes datos de acuerdo a lo solicitado")
print("teniendo en cuenta mayúsculas y sin tildes")
d = dict(id_prestamo = input("Ingrese el ID del préstamo "),casado = str(input("¿Es casado? Si/No ")),dependientes = input("Ingrese la cantidad de personas que dependen de usted  0/1/2/3+ "),
       educacion = str(input("¿Está usted graduado? Graduado/No Graduado ")),independiente = str(input("¿Es usted independiente? Si/No ")),
       ingreso_deudor = float(input("Digite la cantidad de ingresos que tiene el deudor: $")),ingreso_codeudor = float(input("Digite la cantidad de ingresos del codeudor: $")),
       cantidad_prestamo = float(input("Ingrese la cantidad del préstamo: $")),plazos_prestamo = int(input("Ingrese el plazo a pagar el préstamo ")),
       historia_credito = str(input("¿Cuenta usted con historial crediticio? Si/No ")),tipo_propiedad = str(input("¿Qué tipo de propiedad tiene: Urbano/Rural/Semiurbano ")))

diccionario = prestamo(d)
print (diccionario)