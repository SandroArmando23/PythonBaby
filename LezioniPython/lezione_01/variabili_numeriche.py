#alcoliamo l' area di un triangolo date base e altezza
base = 23 #la base del triangolo vale 23
altezza = 27.9 #altezza del triangolo
area = base * altezza / 2 #calcolo area

# Stampare il riusltato si usa la funzione print che ci fa vedere ciò che il nostro programma calcola nel terminal
print(area)

#Convertiamo un tempo in secondi in ore:minuti:secondi
tempo = 49767 #Tempo iniziale in secondi

ore = tempo // (60 *60) #Calcoliamo a quante ore intere corrispondomo i secondi
secondi = tempo % (60 * 60) #Calcoliamo quanti secondi rimangono fuori dalle ore intere

minuti = secondi // 60 # calcoliampo a quanti minuti interi corrispondono i secondi rimanenti
secondi = tempo % 60 # calcoliamo secondi rimanenti

print(ore,minuti, secondi) #Stampiamo il nostro risultato