import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.special import factorial

# Funzione per calcolare il limite di una successione
def limite_successione():
    n_values = np.arange(1, 100, 1)  # valori di n da 1 a 100
    successione = (n_values - 4) / (2 * n_values + 5)
    limite = 1/2
    print(f"Limite calcolato: {successione[-1]} (verso {limite})")
    print("La successione converge verso il limite teorico 1/2 per valori grandi di n.\n")

# Funzione per visualizzare le velocità di crescita di diverse funzioni
def crescita_funzioni():
    n_values = np.arange(1, 20, 1)
    
    log_n = np.log(n_values)
    n_alpha = n_values**2   # Esempio di crescita n^2
    exp_a_n = 2**n_values   # Esempio di crescita esponenziale
    fattoriali = [math.factorial(n) for n in n_values]
    super_exp = [n**n for n in n_values]
    
    # Plot delle funzioni
    plt.plot(n_values, log_n, label="log(n)")
    plt.plot(n_values, n_alpha, label="n^2")
    plt.plot(n_values, exp_a_n, label="2^n")
    plt.plot(n_values, fattoriali, label="n!")
    plt.plot(n_values, super_exp, label="n^n")
    
    plt.yscale('log')  # Scala logaritmica per visualizzare meglio le differenze
    plt.xlabel("n")
    plt.ylabel("Valore della funzione (scala logaritmica)")
    plt.title("Velocità di crescita delle funzioni")
    plt.legend()
    plt.show()
    print("Grafico delle velocità di crescita delle funzioni mostrato.\n")

# Funzione per calcolare il fattoriale e fare il confronto con altri numeri
def confronto_fattoriale():
    # Esempio di confronto: 10010 vs 10!
    num = 10010
    fattoriale_10 = factorial(10)
    rapporto = num / fattoriale_10
    print(f"10010 / 10! = {rapporto:.10f}")
    if rapporto < 10**-14:
        print("Il rapporto è inferiore a 10^-14\n")
    else:
        print("Il rapporto è superiore a 10^-14\n")

# Funzione per calcolare il limite del numero di Nepero e
def limite_nepero():
    n_values = np.arange(1, 1000, 1)
    successione = (1 + 1/n_values)**n_values
    plt.plot(n_values, successione)
    plt.axhline(y=np.e, color='r', linestyle='--', label='e')
    plt.title('Convergenza verso il numero di Nepero')
    plt.xlabel('n')
    plt.ylabel(r'$\left(1 + \frac{1}{n}\right)^n$')
    plt.legend()
    plt.show()
    print("Grafico della convergenza verso il numero di Nepero e mostrato.\n")

# Helper parlante che guida l'utente nello script
def helper_parlante():
    print("Benvenuto nello script didattico sui limiti e la crescita delle funzioni!")
    print("Le funzioni disponibili sono le seguenti:")
    print("1. Calcolo del limite della successione (n-4)/(2n+5)")
    print("2. Visualizzazione delle velocità di crescita delle funzioni")
    print("3. Confronto tra 10010 e 10!")
    print("4. Convergenza verso il numero di Nepero (e)")
    print("\nPer favore seleziona una funzione da eseguire.\n")
    print("Digita '1' per il calcolo del limite della successione.")
    print("Digita '2' per visualizzare le velocità di crescita.")
    print("Digita '3' per il confronto tra 10010 e 10!.")
    print("Digita '4' per la convergenza verso il numero di Nepero.")
    print("Digita 'exit' per uscire.\n")

    while True:
        scelta = input("Seleziona una funzione da eseguire: ")
        
        if scelta == '1':
            limite_successione()
        elif scelta == '2':
            crescita_funzioni()
        elif scelta == '3':
            confronto_fattoriale()
        elif scelta == '4':
            limite_nepero()
        elif scelta == 'exit':
            print("Uscita dallo script. Buono studio!")
            break
        else:
            print("Scelta non valida. Riprova.")

# Eseguiamo l'helper parlante che guida l'utente nello script
helper_parlante()
