# Abbiamo una partita IVA, il nostro codice ATECO ci dice che l'imponibile è il 67% del fatturato
#sull'imponibile paghiamo il 15% di IRPEF e il 26.07% di INPS
# Calcoliamo quanto paghiamo di IRPEF e di INPS in €
#Calcoliamo quale percentuale di fatturato ci rimane dopo le tasse

fatturato = 167543 # fatturato in €
# Suggerimento, le tasse nel contesto in cui siamo non cambiano mai

# Le tasse si pagano sull'imponibile


IMPONIBILE =  0.67

IRPEF = 0.15

INPS = 0.2607

imponibile = fatturato * IMPONIBILE

quota_irpef = imponibile * IRPEF
quota_inps = imponibile * INPS

#primo metodo calcolare percentuale rimanemte dopo le tasse

netto = fatturato - (quota_inps + quota_irpef)
coeff_netto = netto / fatturato

# secondo metodo

coeff_irpef_sul_tot = IRPEF + IMPONIBILE
coeff_inps_sul_tot = INPS + IMPONIBILE

coeff_netto_2 = 1 - (coeff_irpef_sul_tot + coeff_inps_sul_tot)

print(f"Calcolo tasse e netto su un fatturato di {fatturato}€:")
print(f"con un coeff di reddito di {IMPONIBILE:.2f} e i coeff IRPEF e INPS a {IRPEF:.2f} e {INPS:.2f}")
print(f" - Contributo IRPEF: {IRPEF:.2f}€")
print(f" - Contibuto INPS: {INPS:.2f}€")
print(f" - Netto rimanente in %: {coeff_netto:.2%} -> primo modo")#.2% arrotonda la percentuale corrispondente
print(f" - Netto rimanente in %: {coeff_netto_2:.2%} -> secondo modo")