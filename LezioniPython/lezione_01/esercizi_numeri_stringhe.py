#Scriviamo uno script che calcoli il totale di una lista di oggetti che abbiamo comprato e ne stampi un resoconto
tavolo = 230
sedia = 45
n_sedie = 4
piatto_fondo = 3.4
piatto_piano = 4.2
numero_persone_servizio = 6

costo_sedie = sedia * n_sedie
costo_piatti = (piatto_fondo + piatto_piano) * numero_persone_servizio

costo_totale = tavolo + costo_sedie + costo_piatti

print("Riepilogo dei costi: ")
print(f" - Tavolo: {tavolo} €")
print(f" - Piatti: ({piatto_fondo} + {piatto_piano}) * {numero_persone_servizio}  -> {costo_piatti}€")
print(f" - Sedie: {sedia}  * {n_sedie}  -> {costo_sedie}€")

print(f"Totale: {costo_totale}€")
print() # va a capo di una riga nel terminale
# Creiamo un sistema che date 3 dimensioni di un parallelepipedo restituisca:
# Area di base: base * profondita
# Volume totale: base * altezza * profondita
# Diagonale: (base ** 2 + altezza ** 2 + profondita ** 2) ** 1/2

#Una volta calcolate le informazioni richieste, fare un print dettagliato
# 6 ** 2 -> 36
#16 ** (1/2) -> 4 Radice quadrata


base = 15
altezza = 30
profondita = 25

area_base = base * profondita
volume_totale = base * altezza * profondita
diagonale = (base ** 2 + altezza ** 2 + profondita ** 2) ** 1/2

print(f"L'area di base del parallelepipedo è {area_base} cm2, il volume è {volume_totale} cm3, e la diagonale è {diagonale} cm")
print()





