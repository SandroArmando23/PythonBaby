"""
Il dipartimento marketing ti ha inviato i log delle vendite dell'ultima settimana
(la lista transazioni) e ha urgente bisogno di segmentare l'utenza per una nuova campagna
pubblicitaria mirata; il tuo script deve processare i dati per generare un report che identifichi
univocamente i "Top Spender" (clienti che hanno speso in totale più di 1000€ sommando tutti
i loro ordini) restituendo per ciascuno di essi l'insieme delle categorie merceologiche
uniche a cui si sono interessati, e contemporaneamente deve isolare un gruppo di "Tech Purists",
ovvero quei clienti che hanno acquistato almeno un prodotto della categoria "Tech" ma non hanno
mai comprato nulla dalla categoria "Books" in nessun ordine, calcolando infine quale categoria
merceologica è la più popolare in assoluto basandosi sul numero totale di volte che appare
nei carrelli di tutti i clienti indistintamente.
"""

transazioni = [
    {"id_ordine": 101, "cliente": "Marco_R", "prodotti": ["Laptop", "Mouse"], "categorie": ["Tech", "Tech"], "totale": 1200.00},
    {"id_ordine": 102, "cliente": "Giulia_S", "prodotti": ["Libro Python", "Caffè"], "categorie": ["Books", "Food"], "totale": 45.50},
    {"id_ordine": 103, "cliente": "Marco_R", "prodotti": ["Monitor", "Cavo HDMI"], "categorie": ["Tech", "Tech"], "totale": 300.00},
    {"id_ordine": 104, "cliente": "Luca_B", "prodotti": ["Tastiera", "Libro Java"], "categorie": ["Tech", "Books"], "totale": 150.00},
    {"id_ordine": 105, "cliente": "Sara_L", "prodotti": ["Smartphone"], "categorie": ["Tech"], "totale": 800.00},
    {"id_ordine": 106, "cliente": "Giulia_S", "prodotti": ["Webcam"], "categorie": ["Tech"], "totale": 60.00},
    {"id_ordine": 107, "cliente": "Luca_B", "prodotti": ["Cuffie"], "categorie": ["Tech"], "totale": 120.00},
    {"id_ordine": 108, "cliente": "Matteo_P", "prodotti": ["Tablet", "Custodia"], "categorie": ["Tech", "Accessories"], "totale": 450.00},
    {"id_ordine": 109, "cliente": "Sara_L", "prodotti": ["Smartwatch"], "categorie": ["Tech"], "totale": 250.00},
    {"id_ordine": 110, "cliente": "Elena_N", "prodotti": ["Romanzo", "Tè"], "categorie": ["Books", "Food"], "totale": 35.00},
    {"id_ordine": 111, "cliente": "Marco_R", "prodotti": ["Sedia Gaming"], "categorie": ["Furniture"], "totale": 200.00},
]

#Creo dizionario per sommare spesa di ogni cliente
spesa_totale = {}

# Dizionario per: cliente -> set categorie che ha acquistato
categorie_per_cliente = {}

# Contatore per vedere quante volte appare ogni categoria
conteggio_categorie = {}   # es. Tech:8,  Books:2

#Ciclo per tutte le transazioni
for ordine in transazioni:
    cliente = ordine["cliente"]
    totale = ordine["totale"]
    categorie = ordine["categorie"]

    # Somma spese cliente
    spesa_attuale = spesa_totale.get(cliente,0)
    spesa_totale[cliente] = spesa_attuale + totale

    # Aggiungere categorie (uso set per evitare duplicati)
    if cliente not in categorie_per_cliente:
        categorie_per_cliente[cliente] = set()

    for cat in categorie:
        categorie_per_cliente[cliente].add(cat)  # aggiunge categoria al set

# Conta quante volte appare la categoria per tutti gli ordini
    for cat in categorie:
        conteggio_attuale = conteggio_categorie.get(cat, 0)
        conteggio_categorie[cat]= conteggio_attuale +1


# TOP Spender
print("Top Spender:")
for cliente, spesa in spesa_totale.items():
    if spesa > 1000:
        categorie_uniche = categorie_per_cliente[cliente]
        print(f"-> {cliente}: {spesa}€ -> categorie: {categorie_uniche}")

# Tech Purist
print("\nTech Purist:")
for cliente in categorie_per_cliente:
    categorie= categorie_per_cliente[cliente]

    ha_tech = "Tech" in categorie
    ha_books = "Books" in categorie

    if ha_tech and not ha_books:
        spesa = spesa_totale.get(cliente, 0)
        print(f"-> {cliente} -> (speso {spesa}€)")

# Categoria popolare
print("\nCategoria più Popolare:")
max_num = 0
categoria_top = ""

for cat, conteggio in conteggio_categorie.items():
    if conteggio > max_num:
        max_num = conteggio
        categoria_top = cat

print(f"-> {categoria_top} (compare in {max_num} ordini)")