# Tabella di valori per AND
# AND | V   F             # OR | V  F
#-------                  # ----------
# V  | V  F               # V | V  V
# F  | F  F               # F | V  F

piove = True
sono_in_ritardo = True

print(f"Prendo la macchina se piove E sono in ritardo, con i valori: {piove and sono_in_ritardo}")
print(f"Prendo la macchina se piove O sono in ritardo, con i valori: {piove or sono_in_ritardo}")

print(f"Prendo la macchina se (NON piove) O sono in ritardo, con i valori: {not piove or sono_in_ritardo}")
print(f"Prendo la macchina se NON (piove O sono in ritardo), con i valori: {not (piove or sono_in_ritardo)}")
print(f"Prendo la macchina se (NON piove) E (NON sono in ritardo), con i valori: {not piove and not sono_in_ritardo}")

