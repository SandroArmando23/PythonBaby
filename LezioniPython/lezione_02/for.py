#ripetiamo un blocco di codice 5 volte
for i in range(5):
    print(f"Il contatore 'i' vale {i}")

# creiamo una lista
lista_mesi = ['Gen','Feb','Mar','Apr','Mag','Giu']

for i in range(len(lista_mesi)): # il range va da 0 alla lunghezza della lista (-1)
    print(f"{i + 1}. {lista_mesi[i]}")

lista_costi = [
    [12, 23, 10],
    [45, 12,  7],
    [34, 75,  3],
]

#Per ogni lista calcoliamo la media
for lista_mensile in lista_costi:   # per ogni elemento della lista_costi
    print(f"Media: {sum(lista_mensile) / len(lista_mensile):.2f}")  # calcoliamo la sua media

for indice, lista_mensile in enumerate(lista_costi): # due variabili nel for
    print(f"Media elemento alla posizione {indice + 1}: {sum(lista_mensile) / len(lista_mensile):.2f}") # facciamo +1 solo per partire da uno con l'indice e non da 0
print(f"\n{'-' * 100}")
#--------------------------------------------------------------------------------------------------------------
# Definiamo un dizionario di spese
diz_spese = {
    "Gen": [23, 54, 23, 6],
    "Feb": [56, 12, 23],
    "Mar": [10, 54, 45, 45],
    "Apr": [69],
    "Mag": [78, 54, 12, 6, 7, 9],
    "Giu": [10, 120, 3, 45],
}

# Stampiamo l'elenco dei mesi che fanno parte del nostro dizionario
for mese in diz_spese.keys():
    print(f"* {mese}")

  # stampiamo elenco delle spese che fanno parte del nostro dizionario
for spese in diz_spese.values():
    print(f"* {spese}")

# Calcoliamo per ogni mese la spesa totale e la spesa media
for mese, spese in diz_spese.items():
    tot = sum(spese)  # Calcoliamo le spese
    media = tot / len(spese)  # Calcoliamo la spesa media
    spesa_massima = max(spese)
    spesa_minima = min(spese)
    print(f"Spese di {mese}:")
    print(f"Spesa minima: {spesa_minima:.2f}")
    print(f"Spesa massima: {spesa_massima:.2f}")
    print(f" * Media: {media:.2f}")
    print(f" * Totale: {tot:.2f} ")
