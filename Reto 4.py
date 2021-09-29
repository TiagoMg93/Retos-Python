def promedio_facultades(info: dict, contando_externos : bool = True ) -> tuple:
    
    diccionario = info.items()
    facultades_universidad = set()
    correos_estudiantes = set()
    diccionario_promedio = {}
    diccionario_credito = {}
    
    
    
    for keys, values in diccionario:
        
        codigo_estudiante = str(keys)
        b = codigo_estudiante[5]
        nombre = values['nombres']
        apellido = values['apellidos']
        ID = values['documento']
        ID = str(ID)
        programa = values['programa']
        materias = values["materias"]
        
        
        
        if len(materias)==0:
            continue
        
        if b == '5' and contando_externos == False:
            continue
        i=0
        
        while i < len(materias):
            facultad = materias[i]['facultad']
            codigo_asignatura = materias[i]['codigo']
            nota = materias[i]['nota']
            creditos = materias[i]['creditos']
            retirada = materias[i]['retirada']
            c = codigo_asignatura[0:4]
            
            if contando_externos == False and c != programa:
                i = i + 1
                continue
            
            if creditos == 0 or retirada == 'Si':
                i = i + 1
                continue
            
            facultades_universidad.add(facultad)
            
            try:
                promedio = nota*creditos
                
            except:
                return 'Error numérico.'
            
            if facultad in diccionario_promedio or facultad in diccionario_credito:
                try:
                    diccionario_promedio[facultad] = promedio + diccionario_promedio[facultad]
                    diccionario_credito[facultad] = creditos + diccionario_credito[facultad]
                except:
                    return 'Error numérico.'
                dos_nombres = True
                if ' ' in nombre:
                    dos_nombres = True
                else:
                    dos_nombres = False
                    
                if  dos_nombres == True:
                    m = nombre.index(' ')+1
                    n = apellido.index(' ')+1
                    correo = nombre[0] + nombre[m] + '.' + apellido[n:] + ID[6:]
                    correo = correo.lower()
                    for letra in correo:
                        if letra == 'á':
                            correo = correo.replace('á','a')
                        elif letra == 'é':
                            correo = correo.replace('é','e')
                        elif letra == 'í':
                            correo = correo.replace('í','i')
                        elif letra == 'ó':
                            correo = correo.replace('ó','o')
                        elif letra == 'ú':
                            correo = correo.replace('ú','u')
                        elif letra == 'ñ':
                            correo = correo.replace('ñ','n')
                    
                    correos_estudiantes.add(correo)
                    
                else:
                    m = apellido.index(' ')+1
                    n = apellido.index(',')
                    correo = nombre[0] + apellido[m] + '.' + apellido[:n] + ID[6:]
                    correo = correo.lower()
                    for letra in correo:
                        if letra == 'á':
                            correo = correo.replace('á','a')
                        elif letra == 'é':
                            correo = correo.replace('é','e')
                        elif letra == 'í':
                            correo = correo.replace('í','i')
                        elif letra == 'ó':
                            correo = correo.replace('ó','o')
                        elif letra == 'ú':
                            correo = correo.replace('ú','u')
                        elif letra == 'ñ':
                            correo = correo.replace('ñ','n')
                    correos_estudiantes.add(correo)
                    
            else:
                diccionario_promedio[facultad] = promedio
                diccionario_credito[facultad] = creditos
                
                dos_nombres = True
                
                if ' ' in nombre:
                    dos_nombres = True
                else:
                    dos_nombres = False
                    
                if  dos_nombres == True:
                    m = nombre.index(' ')+1
                    n = apellido.index(' ')+1
                    correo = nombre[0] + nombre[m] + '.' + apellido[n:] + ID[6:]
                    correo = correo.lower()
                    for letra in correo:
                        if letra == 'á':
                            correo = correo.replace('á','a')
                        elif letra == 'é':
                            correo = correo.replace('é','e')
                        elif letra == 'í':
                            correo = correo.replace('í','i')
                        elif letra == 'ó':
                            correo = correo.replace('ó','o')
                        elif letra == 'ú':
                            correo = correo.replace('ú','u')
                        elif letra == 'ñ':
                            correo = correo.replace('ñ','n')
                    correos_estudiantes.add(correo)
                    
                else:
                    m = apellido.index(' ')+1
                    n = apellido.index(',')
                    correo = nombre[0] + apellido[m] + '.' + apellido[:n] + ID[6:]
                    correo = correo.lower()
                    for letra in correo:
                        if letra == 'á':
                            correo = correo.replace('á','a')
                        elif letra == 'é':
                            correo = correo.replace('é','e')
                        elif letra == 'í':
                            correo = correo.replace('í','i')
                        elif letra == 'ó':
                            correo = correo.replace('ó','o')
                        elif letra == 'ú':
                            correo = correo.replace('ú','u')
                        elif letra == 'ñ':
                            correo = correo.replace('ñ','n')
                    correos_estudiantes.add(correo)
                
            
            i = i + 1
    
    correos_institucionales = list(correos_estudiantes)
    fac_universidad = list(facultades_universidad)
    fac_universidad.sort()
    correos_institucionales.sort()
    respuesta = {}
    largo = len(fac_universidad)
    i = 0
    while i < largo:
        respuesta[fac_universidad[i]] = diccionario_promedio[fac_universidad[i]]/diccionario_credito[fac_universidad[i]]
        respuesta[fac_universidad[i]] = round(respuesta[fac_universidad[i]],2)
        i = i + 1
    
    respuesta_final = (respuesta,correos_institucionales)
    
    return  respuesta_final
    
    


print(promedio_facultades({
					20180258748:{
								"nombres" : "Laura Carolina",
								"apellidos" : "Cuellar, Martínez",
								"documento" : 56903142,
								"programa" : "IIND",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-7343",
												"nota" : 3.42,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-9484",
												"nota" : 4.06,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-7543",
												"nota" : 3.55,
												"creditos" : 3,
												"retirada" : "Si",
												},
											]
								},
					20200161520:{
								"nombres" : "Gabriela Maria",
								"apellidos" : "Torres, Torres",
								"documento" : 33383264,
								"programa" : "HART",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-5406",
												"nota" : 3.38,
												"creditos" : 3,
												"retirada" : "Si",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-8321",
												"nota" : 4.5,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-8634",
												"nota" : 2.43,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20180275516:{
								"nombres" : "Camila Maria",
								"apellidos" : "Pardo, Moreno",
								"documento" : 16460416,
								"programa" : "MEDI",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-8291",
												"nota" : 3.63,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-6474",
												"nota" : 3.91,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-6559",
												"nota" : 4.87,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-6400",
												"nota" : 3.98,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20130237460:{
								"nombres" : "Sara Daniela",
								"apellidos" : "Fernández, Pérez",
								"documento" : 50851757,
								"programa" : "DIGR",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-9511",
												"nota" : 2.88,
												"creditos" : 3,
												"retirada" : "Si",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-7820",
												"nota" : 4.5,
												"creditos" : 0,
												"retirada" : "No",
												},
											]
								},
					20150225965:{
								"nombres" : "Catalina Sara",
								"apellidos" : "Pérez, Fernández",
								"documento" : 56904845,
								"programa" : "DIGR",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-7820",
												"nota" : 2.6,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-9590",
												"nota" : 3.45,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-1863",
												"nota" : 3.73,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-7837",
												"nota" : 2.42,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-2013",
												"nota" : 2.77,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20150220803:{
								"nombres" : "Laura Gabriela",
								"apellidos" : "Moreno, Álvarez",
								"documento" : 23932358,
								"programa" : "ICIV",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-5962",
												"nota" : 2.56,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-6796",
												"nota" : 3.71,
												"creditos" : 2,
												"retirada" : "Si",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-7476",
												"nota" : 4.82,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20150137119:{
								"nombres" : "Camilo Oscar",
								"apellidos" : "Pérez, Álvarez",
								"documento" : 70531411,
								"programa" : "HART",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-2388",
												"nota" : 4.1,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-8458",
												"nota" : 2.52,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-4558",
												"nota" : 2.15,
												"creditos" : 2,
												"retirada" : "Si",
												},
											]
								},
					20200255611:{
								"nombres" : "Mateo",
								"apellidos" : "Ochoa, Gómez",
								"documento" : 88455293,
								"programa" : "ICIV",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-4627",
												"nota" : 2.4,
												"creditos" : 3,
												"retirada" : "Si",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-5019",
												"nota" : 3.97,
												"creditos" : 4,
												"retirada" : "No",
												},
											]
								},
					20180243721:{
								"nombres" : "Julio Julián",
								"apellidos" : "Guitiérrez, Gómez",
								"documento" : 82734307,
								"programa" : "DIIN",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-8894",
												"nota" : 4.73,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-4822",
												"nota" : 2.56,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-2252",
												"nota" : 2.83,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20170128822:{
								"nombres" : "Catalina Camila",
								"apellidos" : "Cuellar, Suárez",
								"documento" : 50244386,
								"programa" : "DIMD",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-4014",
												"nota" : 4.46,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-7470",
												"nota" : 3.05,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-2531",
												"nota" : 2.42,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-5945",
												"nota" : 4.99,
												"creditos" : 4,
												"retirada" : "No",
												},
											]
								},
					20170250887:{
								"nombres" : "Andres Gabriel",
								"apellidos" : "Romero, Fernández",
								"documento" : 59716178,
								"programa" : "HAMO",
								"materias" : [
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-1258",
												"nota" : 4.19,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-1938",
												"nota" : 3.69,
												"creditos" : 2,
												"retirada" : "Si",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-3145",
												"nota" : 4.8,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-3743",
												"nota" : 4.2,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-2432",
												"nota" : 3.07,
												"creditos" : 1,
												"retirada" : "No",
												},
											]
								},
					20110264007:{
								"nombres" : "Julián Daniel",
								"apellidos" : "López, Niño",
								"documento" : 32543959,
								"programa" : "ARQU",
								"materias" : [
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-8743",
												"nota" : 2.53,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-5122",
												"nota" : 2.39,
												"creditos" : 3,
												"retirada" : "Si",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-1033",
												"nota" : 3.82,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-7824",
												"nota" : 2.37,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20150132819:{
								"nombres" : "Camila Gabriela",
								"apellidos" : "Romero, Hernández",
								"documento" : 27075752,
								"programa" : "IBIO",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-9454",
												"nota" : 2.73,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-8357",
												"nota" : '4,54',
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-3425",
												"nota" : 4.69,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-9454",
												"nota" : 3.04,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20180354205:{
								"nombres" : "Nicolas Andres",
								"apellidos" : "Jiménez, López",
								"documento" : 36852757,
								"programa" : "DIMD",
								"materias" : [
											]
								},
					20150144454:{
								"nombres" : "Daniel Andres",
								"apellidos" : "Ramírez, Álvarez",
								"documento" : 18621326,
								"programa" : "IIND",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-3557",
												"nota" : 2.65,
												"creditos" : 1,
												"retirada" : "No",
												},
											]
								},
					20200161348:{
								"nombres" : "Camila Paula",
								"apellidos" : "Jiménez, Jiménez",
								"documento" : 95052431,
								"programa" : "MEDI",
								"materias" : [
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-8607",
												"nota" : 2.78,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-4689",
												"nota" : 2.68,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20170313423:{
								"nombres" : "Mateo Andres",
								"apellidos" : "Córdoba, Pérez",
								"documento" : 34429692,
								"programa" : "DIMD",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-4470",
												"nota" : 2.77,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-7107",
												"nota" : 3.17,
												"creditos" : 4,
												"retirada" : "No",
												},
											]
								},
					20170326003:{
								"nombres" : "Camila Laura",
								"apellidos" : "Moreno, Fernández",
								"documento" : 68731744,
								"programa" : "IIND",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-5406",
												"nota" : 2.59,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-5433",
												"nota" : 3.18,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-5055",
												"nota" : 3.96,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-3008",
												"nota" : 3.76,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20170365049:{
								"nombres" : "Camila Andrea",
								"apellidos" : "Jiménez, López",
								"documento" : 58154488,
								"programa" : "DISE",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-6981",
												"nota" : 3.82,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-6515",
												"nota" : 2.98,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-5596",
												"nota" : 3.07,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-5596",
												"nota" : 2.75,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20180341955:{
								"nombres" : "Sara Maria",
								"apellidos" : "Guitiérrez, Moreno",
								"documento" : 74599213,
								"programa" : "IIND",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-2619",
												"nota" : 3.9,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-9208",
												"nota" : 2.34,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-1447",
												"nota" : 3.14,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20180158352:{
								"nombres" : "Mateo Nicolas",
								"apellidos" : "Sánchez, Hernández",
								"documento" : 48956920,
								"programa" : "HART",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-1893",
												"nota" : 4.12,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-4540",
												"nota" : 2.71,
												"creditos" : 4,
												"retirada" : "No",
												},
											]
								},
					20130175938:{
								"nombres" : "Julián Oscar",
								"apellidos" : "Torres, Ramírez",
								"documento" : 79099097,
								"programa" : "HART",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-4328",
												"nota" : 2.96,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-4558",
												"nota" : 2.41,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-7452",
												"nota" : 3.74,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-5285",
												"nota" : 1.72,
												"creditos" : 0,
												"retirada" : "Si",
												},
											]
								},
					20170125563:{
								"nombres" : "Laura Maria",
								"apellidos" : "López, Ramírez",
								"documento" : 90235907,
								"programa" : "DIIN",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-4067",
												"nota" : 2.91,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-6616",
												"nota" : 2.51,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-4773",
												"nota" : 4.85,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-2390",
												"nota" : 2.69,
												"creditos" : 0,
												"retirada" : "No",
												},
											]
								},
					20190134014:{
								"nombres" : "Jorge Mateo",
								"apellidos" : "Fernández, García",
								"documento" : 92067080,
								"programa" : "ARQD",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-5194",
												"nota" : 3.54,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-8904",
												"nota" : 4.51,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-9114",
												"nota" : 3.07,
												"creditos" : 3,
												"retirada" : "Si",
												},
											]
								},
					20170273043:{
								"nombres" : "Camila Maria",
								"apellidos" : "Álvarez, Díaz",
								"documento" : 48481864,
								"programa" : "DIIN",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-1173",
												"nota" : 4.4,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-6748",
												"nota" : 3.15,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-9865",
												"nota" : 4.79,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-5441",
												"nota" : 4.76,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-3583",
												"nota" : 3.71,
												"creditos" : 4,
												"retirada" : "No",
												},
											]
								},
					20170272657:{
								"nombres" : "Laura Camila",
								"apellidos" : "Fernández, Gómez",
								"documento" : 38458203,
								"programa" : "HAMO",
								"materias" : [
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-7286",
												"nota" : 4.45,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-7667",
												"nota" : 3.54,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20140240515:{
								"nombres" : "Camila Catalina",
								"apellidos" : "Niño, López",
								"documento" : 72978501,
								"programa" : "DIMD",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-7666",
												"nota" : 2.89,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-6337",
												"nota" : 4.36,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-4067",
												"nota" : 4.6,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20110361896:{
								"nombres" : "Nicolas Gabriel",
								"apellidos" : "Jiménez, Martínez",
								"documento" : 24390101,
								"programa" : "ARQD",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-2553",
												"nota" : 2.88,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-3843",
												"nota" : 2.81,
												"creditos" : 0,
												"retirada" : "Si",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-1864",
												"nota" : 2.61,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-5405",
												"nota" : 4.29,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20140530242:{
								"nombres" : "Daniela Sofia",
								"apellidos" : "García, Ramírez",
								"documento" : 51195781,
								"programa" : "IIND",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-5821",
												"nota" : 3.83,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-4333",
												"nota" : 3.59,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20190357498:{
								"nombres" : "Valentina Catalina",
								"apellidos" : "Suárez, Niño",
								"documento" : 12006504,
								"programa" : "ISIS",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "ISIS-4305",
												"nota" : 2.55,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ISIS-6565",
												"nota" : 2.75,
												"creditos" : 3,
												"retirada" : "Si",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ISIS-7601",
												"nota" : 4.31,
												"creditos" : 0,
												"retirada" : "No",
												},
											]
								},
					20160234611:{
								"nombres" : "Andrea Sofia",
								"apellidos" : "Niño, Ramírez",
								"documento" : 99066142,
								"programa" : "DISE",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-6026",
												"nota" : 4.02,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-9206",
												"nota" : 4.13,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-5161",
												"nota" : 3.63,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-1821",
												"nota" : 2.8,
												"creditos" : 4,
												"retirada" : "No",
												},
											]
								},
					20180231918:{
								"nombres" : "Camila",
								"apellidos" : "Cuellar, Díaz",
								"documento" : 76315685,
								"programa" : "MENF",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-4810",
												"nota" : 3.25,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-4702",
												"nota" : 3.02,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-9442",
												"nota" : 2.83,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-2072",
												"nota" : 3.2,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-8291",
												"nota" : 4.37,
												"creditos" : 1,
												"retirada" : "No",
												},
											]
								},
					20100134260:{
								"nombres" : "Andres Mateo",
								"apellidos" : "Martínez, Álvarez",
								"documento" : 14991799,
								"programa" : "DIIN",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-7926",
												"nota" : 3.73,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-9865",
												"nota" : 3.52,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20200245086:{
								"nombres" : "Maria Catalina",
								"apellidos" : "Ramírez, Sánchez",
								"documento" : 93214275,
								"programa" : "DIIN",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-9838",
												"nota" : 3.51,
												"creditos" : '2',
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-5835",
												"nota" : 3.53,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-1652",
												"nota" : 3.67,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-5158",
												"nota" : 4.7,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-7888",
												"nota" : 2.47,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20190536642:{
								"nombres" : "Mateo Pablo",
								"apellidos" : "Ramírez, Pérez",
								"documento" : 51730947,
								"programa" : "DISE",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-9838",
												"nota" : 3.98,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-6777",
												"nota" : 4.84,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-8797",
												"nota" : 2.62,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20090357760:{
								"nombres" : "Jose Pablo",
								"apellidos" : "Álvarez, Romero",
								"documento" : 93191384,
								"programa" : "HAMO",
								"materias" : [
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-5327",
												"nota" : 3.4,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-9435",
												"nota" : 2.66,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-7355",
												"nota" : 3.88,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-6328",
												"nota" : 4.69,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-1069",
												"nota" : 4.22,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20200383664:{
								"nombres" : "Catalina Andrea",
								"apellidos" : "Moreno, Cuellar",
								"documento" : 51313239,
								"programa" : "MEDI",
								"materias" : [
											]
								},
					20090116467:{
								"nombres" : "Nicolas Gabriel",
								"apellidos" : "García, Fernández",
								"documento" : 52393411,
								"programa" : "HAMO",
								"materias" : [
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-7665",
												"nota" : 4.26,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-8607",
												"nota" : 3.18,
												"creditos" : 0,
												"retirada" : "Si",
												},
											]
								},
					20120243135:{
								"nombres" : "Oscar Andres",
								"apellidos" : "Guitiérrez, Ochoa",
								"documento" : 29004076,
								"programa" : "IBIO",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-8942",
												"nota" : 3.15,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-5266",
												"nota" : 2.79,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20200295005:{
								"nombres" : "Camila Sara",
								"apellidos" : "Fernández, Cuellar",
								"documento" : 72005742,
								"programa" : "MENF",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-5889",
												"nota" : 4.28,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-9442",
												"nota" : 2.56,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-6067",
												"nota" : 3.6,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-1415",
												"nota" : 2.73,
												"creditos" : 3,
												"retirada" : "Si",
												},
											]
								},
					20170186478:{
								"nombres" : "Jose",
								"apellidos" : "López, Moreno",
								"documento" : 11640390,
								"programa" : "DIIN",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-7915",
												"nota" : 4.92,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-3136",
												"nota" : 4.38,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-7888",
												"nota" : 1.81,
												"creditos" : 2,
												"retirada" : "Si",
												},
											]
								},
					20200133687:{
								"nombres" : "Laura Daniela",
								"apellidos" : "Ramírez, Fernández",
								"documento" : 79751620,
								"programa" : "ARQD",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-6822",
												"nota" : 3.75,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-6074",
												"nota" : 3.33,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20120175303:{
								"nombres" : "Natalia Catalina",
								"apellidos" : "Cuellar, Córdoba",
								"documento" : 95268184,
								"programa" : "MEDI",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-6559",
												"nota" : 3.3,
												"creditos" : 1,
												"retirada" : "Si",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-2339",
												"nota" : 4.69,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20110158990:{
								"nombres" : "Maria Carolina",
								"apellidos" : "Romero, García",
								"documento" : 93538878,
								"programa" : "IBIO",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-1999",
												"nota" : 3.52,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-2514",
												"nota" : 2.65,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-4686",
												"nota" : 3.28,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20140139618:{
								"nombres" : "Oscar Mateo",
								"apellidos" : "Martínez, Hernández",
								"documento" : 68038752,
								"programa" : "IBIO",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-8544",
												"nota" : 3.02,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-8074",
												"nota" : 3.08,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-8672",
												"nota" : 3.59,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-4502",
												"nota" : 3.73,
												"creditos" : 3,
												"retirada" : "Si",
												},
											]
								},
					} ))
