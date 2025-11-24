"""Scenario: Il Calcolatore di Token
Stai sviluppando un modulo per un tuo cliente che monitora quanto spende per ogni risposta generata dal tuo agente AI.
Devi calcolare il costo totale di una singola interazione basandoti sul numero di token di input (il prompt)
e di output (la risposta), e generare un report leggibile.

Dati di partenza (Variabili)
Crea uno script Python e inizializza queste variabili:

nome_modello: Una stringa (es. "GPT-4-Turbo").

token_input: Un numero intero che rappresenta la lunghezza del prompt (es. 1250).

token_output: Un numero intero che rappresenta la lunghezza della risposta (es. 450).

costo_per_1k_input: Un numero decimale (float) per il costo ogni 1000 token di input (es. 0.01 dollari).

costo_per_1k_output: Un numero decimale (float) per il costo ogni 1000 token di output (es. 0.03 dollari).

tasso_cambio_usd_eur: Un float per convertire il costo in euro (es. 0.92)."""

nome_modello = "GPT-4-Turbo"

token_input = 1250

token_output = 450

costo_per_1k_input = 0.01  # dollari

costo_per_1k_output = 0.03  #dollari

TASSO_CAMBIO_USD_EUR = 0.92 # 1 USD = 0.92 €

costo_input = (token_input / 1000) * costo_per_1k_input #costo input in dollari

costo_output = (token_output / 1000) * costo_per_1k_output #costo output in dollari

costo_totale = costo_input + costo_output

#conversione in euro

costo_input_euro = costo_input * TASSO_CAMBIO_USD_EUR
costo_output_euro = costo_output * TASSO_CAMBIO_USD_EUR
costo_totale_euro = costo_totale * TASSO_CAMBIO_USD_EUR

print(f"====== REPORT COSTO SINGOLA INTERAZIONE AI ======")
print(f"Modello in uso: {nome_modello}")
print(f"Token in input: {token_input}")
print(f"Token in output: {token_output}")
print(f"Costo per 1k token in input: {costo_per_1k_input:.2f}")
print(f"Costo per 1k token in output: {costo_per_1k_output:.2f}")
