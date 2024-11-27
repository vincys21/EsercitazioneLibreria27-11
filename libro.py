Libreria=["picccolo principe","re leone","harry potter"]
CatalogoDisponibile=["picccolo principe","re leone","harry potter"]
ListaPresito=[]
#DATI DELLA BIBLIOTECA CON LISTE


print("Buongiorno, vuoi aggiungre un libro nella libreria?")
while True:
    RispostaAggiunta=str(input())
    if RispostaAggiunta=="si"or"SI":
        print("Quale libro desideri aggiungere?")
        CatalogoDisponibile.append(input())
        break
    elif RispostaAggiunta=="no"or"NO":
        print ("Il catalogo disponibile aggiornato è ",CatalogoDisponibile)
        break
    else:
        print("Selezionare una risposta valida,riprova")
#FINE AGGIUNTA EFFETTIVA DEL LIBRO


print("Desideri prenderne in prestito qualcuno?")
while True:
    RispostaPrestito=str(input()) #stringa per la risposta alla richiesta del prestito

    if RispostaPrestito=="si"or"SI":
        print("Perfetto, seleziona il libro che preferisci")
        Prestito=CatalogoDisponibile.remove and ListaPresito.append (input())
        print ("Adesso il CatalogoDisponibile aggiornato è ",CatalogoDisponibile)
        print ("Invece la lista dei libri in prestito è ",ListaPresito)
        break #porta alla domanda successiva
        
    elif RispostaPrestito=="no"or"NO":
        print("Grazie") 
        break #porta alla domanda successiva

    else:
        print("Selezionare una risposta valida,riprova")
# FINE DEL CICLO PER LA DOMANDA PRESTITO


print("Hai invece qualche libro da restituire?")
while True:
    RispostaReso=str(input()) #stringa per la risposta alla richiesta del reso

    if RispostaReso=="si"or"SI":
        print("Perfetto, selezidimmi il libro che devi restituire")
        Prestito=CatalogoDisponibile.append and ListaPresito.remove (input())
        print ("Adesso il CatalogoDisponibile aggiornato è ",CatalogoDisponibile)
        print ("Invece la lista dei libri in prestito è ",ListaPresito)
        break #porta alla domanda successiva
        
    elif RispostaReso=="no"or"NO":
        print("Grazie") 
        break #porta alla domanda successiva

    else:
        print("Selezionare una risposta valida,riprova")
# FINE DEL CICLO PER LA DOMANDA RESO


print("Desideri vedere il catalogo disponibile completo?")
while True:
    RispostaDisponibilità=str(input()) #stringa per la risposta alla richiesta della libreria completa
    if RispostaDisponibilità=="si"or"SI":
        print("Perfetto, il nostro catalogo completo è: ",Libreria)
        print("Attualmente disponiamo dei libri: ",CatalogoDisponibile)
        print("Ci scusiamo per il disagio ma non disponiamo attualmente dei libri in prestito, cioè: ",ListaPresito)
        break #porta alla domanda successiva
        
    elif RispostaDisponibilità=="no"or"NO":
        print("Grazie e arrivederci") 
        break #porta alla domanda successiva

    else:
        print("Selezionare una risposta valida,riprova")
# FINE DEL CICLO PER LA DOMANDA DELLE LISTE DELLA BIBLIOTECA