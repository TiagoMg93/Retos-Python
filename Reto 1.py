def nota_quices(codigo: str, nota1: int, nota2: int, nota3: int, nota4: int, nota5: int):
    nota_baja = min(nota1,nota2,nota3,nota4,nota5)
    if nota1 == nota_baja:
        promedio = (nota2+nota3+nota4+nota5)/4
        Nota_promedio = (promedio*5)/100
        Nota = "{0:.2f}".format(Nota_promedio)
        return "El promedio ajustado del estudiante {} es: {}".format(codigo,Nota)
    elif nota2 == nota_baja:
        promedio = (nota1+nota3+nota4+nota5)/4
        Nota_promedio = (promedio*5)/100
        Nota = "{0:.2f}".format(Nota_promedio)
        return "El promedio ajustado del estudiante {} es: {}".format(codigo,Nota)
    elif nota3 == nota_baja:
        promedio = (nota1+nota2+nota4+nota5)/4
        Nota_promedio = (promedio*5)/100
        Nota = "{0:.2f}".format(Nota_promedio)
        return "El promedio ajustado del estudiante {} es: {}".format(codigo,Nota)
    elif nota4 == nota_baja:
        promedio = (nota1+nota2+nota3+nota5)/4
        Nota_promedio = (promedio*5)/100
        Nota = "{0:.2f}".format(Nota_promedio)
        return "El promedio ajustado del estudiante {} es: {}".format(codigo,Nota)
    elif nota5 == nota_baja:
        promedio = (nota1+nota2+nota3+nota4)/4
        Nota_promedio = (promedio*5)/100
        Nota = "{0:.2f}".format(Nota_promedio)
        return "El promedio ajustado del estudiante {} es: {}".format(codigo,Nota)

prueba = nota_quices("AA0010276", 40, 50, 39, 76, 96)
print (prueba)