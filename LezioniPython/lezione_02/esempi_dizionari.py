dizionario_spese = {
    "Gen": 10,
    "Feb": 24,
    "Mar": 67,
    "Apr": 47,
    "Mag": 88,
    "Giu": 92,
    "Lug": 65,
    "Ago": 98,
    "Set": 73,
    "Ott": 22,
    "Nov": 12,
    "Dic": 7
}
# Otteniamo le chiavi del dizionario
print(f"Chiavi de dizionario: {dizionario_spese.keys()}")

# Otteniamo i valori
print({dizionario_spese.values()})

print(f"Coppie chiave-valore del dizionario: {dizionario_spese.items()}")

print(f"Media delle chiavi del dizionario: {sum(dizionario_spese.values()) / len(dizionario_spese.values()):.2f}")
print(f"Spesa massima: {max(dizionario_spese.values())}")
print(f"Spesa minima: {min(dizionario_spese.values())}")