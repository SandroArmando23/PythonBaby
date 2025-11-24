"""
Lo Chef ti ha lanciato il foglio con gli ordini del pranzo (comande)
e ti ha chiesto di preparare immediatamente la linea per la cucina;
il tuo script deve analizzare gli ordini per stampare un resoconto che dica ai
cuochi esattamente quanti piatti preparare per ogni tipo (es. "3 Carbonara"),
e contemporaneamente deve consultare il ricettario per generare una "Lista della Spesa"
contenente l'elenco di tutti gli ingredienti grezzi necessari per coprire il servizio,
assicurandosi che nella lista ogni ingrediente compaia una volta sola
(non importa se il Pecorino serve per 3 ricette diverse,
nella lista deve apparire solo come "Pecorino").
"""

ricettario = {
    "Carbonara": ["Guanciale", "Uova", "Pecorino", "Pepe"],
    "Amatriciana": ["Guanciale", "Pomodoro", "Pecorino", "Peperoncino"],
    "Cacio e Pepe": ["Pecorino", "Pepe"],
    "Gricia": ["Guanciale", "Pecorino", "Pepe"]
}

comande = [
    "Carbonara",
    "Amatriciana",
    "Carbonara",
    "Cacio e Pepe",
    "Carbonara",
    "Gricia",
    "Amatriciana"
]
# 1 quantita piatti da fare per ogni tipologia di piatto
# 1.0 definiamo un dizionario vuoto in cui metteremo le coppie "piatto, numero da preparare"
# 1.1 ciclo all'interno delle comande poi per ogni comanda
# 1.2 per ogni comanda aggiorniamo il contatore che tiene conto di quanti piatti del suo tipo ci sono da fare
# Stampiamo il resoconto

diz_resoconto = {}
for comanda in comande:
    conteggio_piatto = diz_resoconto.get(comanda, 0)
    conteggio_piatto += 1
    diz_resoconto[comanda] = conteggio_piatto
print("Resoconto piatti da preparare")
for nome_piatto, n_da_preparare in diz_resoconto.items():
    print(f" * {nome_piatto}: {n_da_preparare}")


# 2 Lista per linea
ingredienti_unici = set()
# 2.1 Capiamo qual'è l' elenco completo di tutti gli ingredienti
for comanda in comande:
    ingredienti = ricettario[comanda]
# 2.2 Capiamo quali ingredienti "unici" dobbiamo comprare
    for ingrediente in ingredienti:
        ingredienti_unici.add(ingrediente)
# 2.3 Stampiamo lista della spesa
print("Lista ingredienti neccessari per preparare le comande:")
for ingrediente in ingredienti_unici:
    print(f" * {ingrediente}")

