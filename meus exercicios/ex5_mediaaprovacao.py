def ex5_media_aprovacao(notas: list[float]) ->  dict[str, float | str]:
    if not notas:
        return {"media": 0.0, "status": "sem notas"}

    soma_notas = 0.0
    for nota in notas:
        soma_notas += nota

    media = soma_notas / len(notas)

    if media >= 7:
        status = "Aprovado"
    elif media >= 5:
        status = "Recuperação"
    else:
        status = "Reprovado"

    return {
        "media": round(media, 2),
        "status": status
         } 
    
notas_semestre = [8.5, 7.0, 8.0, 6.0] 

resultado = ex5_media_aprovacao(notas_semestre)           
print(resultado)