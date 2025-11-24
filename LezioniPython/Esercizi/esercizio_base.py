"""
Stai pianificando un viaggio in auto partendo da casa tua a Torino verso una località di mare.
La destinazione scelta è la città di "Otranto", che dista esattamente 1025 chilometri.
La tua auto, una vecchia "fiat punto", ha un consumo medio dichiarato di 16.5 chilometri con un litro
di carburante. Sapendo che il prezzo attuale della benzina è di 1.829 euro al litro e che dovrai
sostenere una spesa fissa per i pedaggi autostradali pari a 74.50 euro, scrivi uno script che calcoli
la quantità di litri necessari, il costo del solo carburante e infine il costo totale del viaggio.
"""

distanza_km = 1025
km_per_litro = 16.5
prezzo_carburante_per_litro = 1.829
spesa_pedaggi = 74.50

litri_necessari = distanza_km / km_per_litro
costo_carburante = litri_necessari * prezzo_carburante_per_litro
costo_totale_viaggio = costo_carburante + spesa_pedaggi

print("====VIAGGIO TORINO-OTRANTO====")
print(f"Distanza: {distanza_km} km")
print(f"Costo del carburante al litro: {prezzo_carburante_per_litro}€ al l")
print(f"Costo dei pedaggi autostradali: {spesa_pedaggi}€")
print(f"Km percorsi dall'auto per ogni litro di carburante: {km_per_litro} km/l")
print('-' * 50)
print(f"Quantità di litri di carburante necessari per il viaggio: {litri_necessari:.2f} l")
print(f"Costo totale carburante per l'intero viaggio: {costo_carburante:.2f}€")
print('-' * 50)
print(f"costo totale del viaggio: {costo_totale_viaggio:.2f}€")

