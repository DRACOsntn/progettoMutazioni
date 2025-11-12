# progettoMutazioni

-introduzione


Per generare questa simulazione, il codice crea inizialmente una popolazione di individui.
 Ogni individuo è rappresentato da:
•	un colore (scelto casualmente),
•	una taglia e una velocità (valori numerici casuali tra 1 e 10),
•	una sequenza di DNA
Durante ogni generazione:
Ogni individuo genera un figlio con le stesse caratteristiche,ma il DNA del figlio subisce una mutazione obbligatoria in una posizione casuale.Alla fine di tutte le generazioni, il programma: mostra quanti individui esistono in totale e indicandoci quanti individui mutati per capire come si è evoluta popolazione

Dal punto di vista biologico, ogni individuo è caratterizzato da alcune proprietà, come il colore e la sequenza di nucleotidi del DNA.
In questo progetto abbiamo voluto rappresentare, in modo semplificato, come una popolazione può cambiare nel tempo.
Una popolazione è formata da individui della stessa specie che vivono nello stesso ambiente
Durante la simulazione avvengono mutazioni, cioè cambiamenti casuali nel DNA che modificano alcuni individui.
Con il passare delle generazioni, queste mutazioni possono diffondersi e far evolvere la popolazione, proprio come accade in natura.



-strategia adottata


la strategia da noi adottata è stata quella di creare prima una poplazione dotata di un certo numero di individui assegando loro un certo tipo di DNA,
e tramite delle funzioni, modificarne la sequenza  sostituendo una lettera con un'altra cosicchè gli individui possano mutare e poi poter creare dei figli 
con il DNA mutato, creando così un'altra popolazione

-commento generale al codice


Per generare questa simulazione, il codice crea inizialmente una popolazione di individui.
 Ogni individuo è rappresentato da:
•	un colore (scelto casualmente),
•	una taglia e una velocità (valori numerici casuali tra 1 e 10),
•	una sequenza di DNA
Durante ogni generazione:
Ogni individuo genera un figlio con le stesse caratteristiche,ma il DNA del figlio subisce una mutazione obbligatoria in una posizione casuale.Alla fine di tutte le generazioni, il programma: mostra quanti individui esistono in totale e indicandoci quanti individui mutati per capire come si è evoluta popolazione














-strategie di testing


Per testare il programma sono stati eseguiti diversi controlli per verificare il corretto funzionamento. Inizialmente è stata eseguita la simulazione per verificare la creazione della            popolazione iniziale. Ogni individuo è stato controllato per assicurarsi che possedesse tutti i dati     richiesti: colore, taglia, velocità e una sequenza di DNA composta da 20 lettere. Successivamente è      stato verificato che, dopo ogni generazione, il numero totale di individui aumentasse come previsto.     Partendo da 5 individui iniziali e con 3 generazioni, il totale finale doveva essere di 20 individui.    È   stato poi controllato il meccanismo di mutazione del DNA, confrontando il DNA di un genitore con     quello del figlio. In ogni caso è risultata una sola lettera diversa, confermando che la mutazione       obbligatoria veniva applicata correttamente in ogni generazione. Infine, sono stati verificati i         calcoli delle medie della taglia e della velocità, oltre alla corretta stampa dei risultati finali.     Come previsto, taglia e velocità non subiscono variazioni durante le generazioni, mentre il DNA cambia   a ogni passaggio. In conclusione, i test hanno dimostrato che il programma funziona correttamente:       genera la popolazione iniziale, produce nuove generazioni con mutazioni del DNA e calcola in modo        corretto le medie finali.



-
