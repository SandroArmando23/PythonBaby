"""
Il team di Risk Management sospetta che ci siano gruppi di utenti fittizi ("Sybil ring")
gestiti dalla stessa persona fisica; ci hanno fornito i log di accesso (utenti_metadata)
e le transazioni finanziarie (transazioni) chiedendoti di sviluppare un algoritmo
che raggruppi gli utenti in "Super-Identità" univoche basandosi sulla transitività delle
connessioni (ovvero: se A condivide un IP/Device con B, e B condivide un IP/Device con C,
allora A, B e C appartengono tutti alla stessa Super-Identità anche se A e C non hanno
nulla in comune direttamente) e, una volta mappati questi cluster, generare un report che
evidenzi esclusivamente le transazioni "Cross-Cluster", ovvero quei movimenti di denaro
che avvengono tra due Super-Identità completamente distinte, le quali sono le uniche che ci
interessano per le indagini di riciclaggio.
"""

utenti_metadata = {
    "user_01": {"ip": {"192.168.1.10", "10.0.0.1"}, "device_id": {"dev_A", "dev_B"}},
    "user_02": {"ip": {"192.168.1.10"}, "device_id": {"dev_C"}}, # Condivide IP con user_01
    "user_03": {"ip": {"10.0.0.5"}, "device_id": {"dev_B"}},     # Condivide Device con user_01
    "user_04": {"ip": {"172.16.0.1"}, "device_id": {"dev_D"}},
    "user_05": {"ip": {"172.16.0.1"}, "device_id": {"dev_E"}},   # Condivide IP con user_04
    "user_06": {"ip": {"10.0.0.99"}, "device_id": {"dev_F"}},    # Isolato
    "user_07": {"ip": {"192.168.1.20"}, "device_id": {"dev_G"}},
    "user_08": {"ip": {"192.168.1.20"}, "device_id": {"dev_H"}}, # Condivide IP con user_07
}

transazioni = [
    {"from": "user_01", "to": "user_02", "amount": 500},   # Interna al cluster (01-02-03)
    {"from": "user_02", "to": "user_03", "amount": 1500},  # Interna
    {"from": "user_03", "to": "user_04", "amount": 8000},  # Sospetta: Tra cluster diversi (01-02-03 -> 04-05)
    {"from": "user_04", "to": "user_05", "amount": 200},   # Interna
    {"from": "user_06", "to": "user_01", "amount": 50},    # Sospetta: Isolato -> Cluster
    {"from": "user_07", "to": "user_08", "amount": 1000},  # Interna
]

utenti = list(utenti_metadata.keys())    #tutti user id
visitati = set()                         # chi gia in un cluster
cluster_counter = 0                      #numero cluster corrente
utente_to_cluster = {}                   #user_01 -> 0, user_02 -> 0 ecc

for _ in range(len(utenti)):             # uso _ per variabile che non serve se non per far girare il ciclo (sostituisce la classica i)
    trovato_nuovo = False
    for utente in utenti:
        if utente not in visitati:
            trovato_nuovo = True        # se non è ancora nel set allora nuovo cluster

 # aggiungo al cluster quelli collegati anche indirettamente
 # ciclo finche non c'è piu nessuno da aggiungere
 # creo lista temporanea di chi va ancora controllato
        da_aggiungere = [utente]

        for _ in range(len(utenti)):           # ripeto tante volte quanti sono gli utenti
            ancora_da_aggiungere = []          # nuova lista per giro successivo

            for utente_corrente in da_aggiungere:
                if utente_corrente not in visitati:
                    visitati.add(utente_corrente)
                    utente_to_cluster[utente_corrente] = cluster_counter

#devo cercare tutti gli altri utenti che condividono IP o Device con "utente_corrente"

                    for altro in utenti:
                        if altro not in visitati and altro != utente_corrente:
                            ip1 = utenti_metadata[utente_corrente] ["ip"]
                            ip2 = utenti_metadata[altro] ["ip"]
                            dev1 = utenti_metadata[utente_corrente] ["device_id"]
                            dev2 = utenti_metadata[altro] ["device_id"]
# se condividono almeno un ip o un device -> sono collegati
                            if ip1.intersection(ip2) or dev1.intersection(dev2):
                                ancora_da_aggiungere.append(altro)


            da_aggiungere = ancora_da_aggiungere
            # se non trovo nessuno da aggiungere esci da ciclo interno
            if not da_aggiungere:
                break

# a questo punto torno a ciclo esterno e cerco nuovo cluster

        cluster_counter += 1
# se non trovo piu nessuno allora ha finito
    if not trovato_nuovo:
        break

#Stampo cluster trovati
print("Super-Identità trovate:")
for user in utenti:
    print(f"{user} -> Cluster {utente_to_cluster[user]}")

#Stampo report transazioni sospette
print("\nTransazioni sospette:")
for trans in transazioni:
    mittente = trans["from"]
    destinatario = trans ["to"]
    importo = trans ["amount"]

    # sono sospetti se appartengono a cluster diversi
    if utente_to_cluster[mittente] != utente_to_cluster[destinatario]:
        print(f"-> {mittente} -> {destinatario} -> {importo} €")