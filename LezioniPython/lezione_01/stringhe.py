persona1 = "Francesco"
persona2 = "Alice"
persona3 = "Tommaso"

print(f"Ciao {persona1},{persona2} e {persona3}")


titolo = "Calcolo area"
separatore = f"{'-' * 50} {titolo} {'-' * 50}"
print(separatore)

#Esempi di informazioni che possiamo ottenere su una stringa

titolo = ("Ricerca del minimo")
lunghezza = len(titolo)
print(f"La lunghezza della parola {titolo} è: {lunghezza}")

#Stampare le lettere che compongonmo la stringa dalla seconda alla ultima
print(titolo[1:])

#Stampare le lettere che compongonmo la stringa dalla prima alla quarta
print(titolo[:3])

#Stampare le lettere che compongonmo la stringa dalla terza alla penultima
print(titolo[2:-1])


