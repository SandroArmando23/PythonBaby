set_ingredienti = {"Sale", "Pepe", "Uova", "Zucchero", "Latte", "Mele", "Cannella"}
# set con gli ingredienti in dispensa

set_torta_di_mele = {
    "Uova", "Zucchero", "Latte", "Mele", "Vaniglia"
} # Ingredienti necessari per la torta di mele

# Capiamo se ci sono degli ingredienti che non abbiamo
ingredienti_mancanti = set_torta_di_mele - set_ingredienti
print(f"Ingredienti mancanti per la torta di mele: {ingredienti_mancanti}")

set_crema_pasticcera = {
    "Limone", "Uova", "Zucchero", "Farina"
}

# Vogliamo sapere quali sono tutti gli ingredienti necessari per fare entrambe le ricette
ingredienti_per_entrambe = set_torta_di_mele | set_crema_pasticcera # -> | unisce i due insiemi
print(f"Ingredienti per fare entrambe le ricette: {ingredienti_per_entrambe}")

# Vogliamo sapere quali ingredienti hanno in comune le due ricette
ingredienti_comuni = set_torta_di_mele & set_crema_pasticcera # & fa l'intersezione degli insiemi
print(f"gli ingredienti in comune sono: {ingredienti_comuni}")

# Metodi per i set
# Aggiungere un elemento alla dispensa
set_ingredienti.add("Farina")

# Rimuovere un elemento dalla dispensa
# 1 metodo
set_ingredienti.remove("Mele") # Da errore se non trova le mele
print(f"Set ingredienti dopo aver tolto le mele [remove]: {set_ingredienti}")
# 2 metodo
set_ingredienti.discard("Mele") # Non da errore se non trova le mele
print(f"Set ingredienti dopo aver tolto le mele [discard]: {set_ingredienti}")