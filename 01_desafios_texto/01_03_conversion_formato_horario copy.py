def convertir_horario(hora):

    hora_lista = hora.split(":")
    if hora[-2:].lower() == "pm":
        if hora_lista[0] != "12":
            hora_lista[0] = str(int(hora_lista[0]) + 12)
    else:
        if hora_lista[0] == "12":
            hora_lista[0] = "00"

    hora_convertida = ":".join(hora_lista)

    return hora_convertida[:-2]

print(convertir_horario("12:40AM")) # 00:40
print(convertir_horario("04:59pm")) # 16:59
print(convertir_horario("10:00:00PM")) # 22:00


"""
1. - We split the string in order to have a list with the hours and minutes
2.- We check if the last two characters are "pm" or "am"
3.- If the last two characters are "pm" and the hour is different to 12, we add 12 to the hour
4.- If the last two characters are "am" and the hour is 12, we change the hour to 00
5.- We join the list of hours and minutes into a string again
6.- We return the string without the last two characters
"""
