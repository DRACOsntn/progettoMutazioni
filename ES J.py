# Il codice simula una popolazione
# formata da persone che possiedono proprietà che differiscono per il colore, taglio e velocità. 


import random  #serve per generare caratteristiche differenti ( colori,nucleotidi,taglio..) 
 
 
popolazione = []  # creamo una lista attualmente vuota, che servirà per segnare gli individui
 
colori = ["rosso", "verde", "blu"]  # prima lista possibile dei colori 
nucleotidi = ["A", "T", "G", "C"]  # seconda lista delle quattro basi azzotate del DNA 
num_individui = 5 # numero di individui di partenza in questo caso sono 5
num_generazioni = 3  # numero di generazioni che si creano qui sono 3 
 
 
for i in range(num_individui):  # ciclo che ripete il numero di generazioni da creare 
    dna = ''.join(random.choice(nucleotidi) for _ in range(20))  # con questa dicitura si crea una stringa
#composta da 20 caratteri  ogni carattere è scelto in modo casuale tra le basi azzotate 
    individuo = {
        "id": i + 1,  # ID è la chiave del dizzionario e l'aggiunta di + 1 ci evita (ID=0) così che id assegnati non sono 0,1,2,3,4 ma 1,2,3,4,5.
#Quindi serve solo per un conteggio più comune
        "colore": random.choice(colori),   #colore preso in modo casuale
        "taglia": random.randint(1, 10),  # numeri casuali di tra 1 e 10 compreso 
        "velocità": random.randint(1, 10),  # numeri casuali di tra 1 e 10 compreso 
        "DNA": dna
    }  #queste parentisi ci indicano che tutte queste caratteristiche fanno parte di un dizzionarui
 
     popolazione.append(in o) #con esso si aggiunge l'individuo alla lista nominata popolazione
 


for _ in range(num_generazioni): # ciclo che ripete le stesse cose dello scorso ciclo 
    figli = []  #creazione di una nuova lista 
    for ind in popolazione:  # scorre ogni individuo dalla lista popolazione
        # tramite queste coppie si fa in modo che il figlio ereda dei caratteri del genitore
        colore = ind["colore"]
        taglia = ind["taglia"]
        velocità = ind["velocità"]
 
        
        dna = list(ind["DNA"]) #tramite esso si trasforma la stringa creata prima in una lista che possiamo modificare
        posizione = random.randint(0, 19)  #ci indica in modo casuale la posizione del DNA tra 0-19 dato che può avere 20 posizioni 
        dna[posizione] = random.choice(nucleotidi)  # si sostituisce la posizione ad un nucleotidi, così facendo è possibile  che ci si ripete, quindi la mutazione è obbligatoria 
        dna_mutato = ''.join(dna)  # si ricostruisce la stringa del DNA mutata
 
        # Crea il figlio
        figlio = {
            "id": len(popolazione) + len(figli) + 1,  # prima ci indica il numero di generazioni iniziale che sono 5 e poi aggiungere figli creati in questa generazione,
            #quindi si sommano prima i due valorie poi si aggiunge 1 per ottenere un  numero progressivo  
            "colore": colore, #non c'è miutazione
            "taglia": taglia,  #nessuna mutazione
            "velocità": velocità,  #non c'è mutazione
            "DNA": dna_mutato # adesso invece abbiamo il DNA mutato,trasformato in una lista, entra la varazione genetica nel codice 
        }
        figli.append(figlio) # si aggiunge il nuovo figlio dentro la lista 
    popolazione.extend(figli) # dopo aver creato tutti i figlio relativi ad ogni generazione , li aggiunge alla lista popolazione 
 

media_taglia = sum(ind["taglia"] for ind in popolazione) / len(popolazione)  #crea una lista virtuale e ci somma tutti i valori e dividendo per il numero totale degli individui trovati 
media_velocità = sum(ind["velocità"] for ind in popolazione) / len(popolazione)
 
print("\n=== RISULTATI FINALI ===")
print(f"Totale individui: {len(popolazione)}")
print(f"Media taglia: {media_taglia:.2f}")
print(f"Media velocità: {media_velocità:.2f}")
print("Percentuale di mutati: 100%  (tutti mutano in ogni generazione)")
 
print("\nEsempio DNA degli individui finali:")
for ind in popolazione:
    print(f"ID {ind['id']}: {ind['DNA']}")            