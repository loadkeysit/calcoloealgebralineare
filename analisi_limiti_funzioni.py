import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Impostazioni iniziali
x = sp.symbols('x')

# Funzioni di esempio
funzioni_base = {
    '1/x': 1/x,
    'sin(x)/x': sp.sin(x)/x,
    '(1 + 1/x)^x': (1 + 1/x)**x,
    'log(x)/x': sp.log(x)/x,
    'x^2': x**2,
    '2^x': 2**x,
    'factorial(x)': sp.factorial(x)
}

# Calcolo del limite con controllo delle forme indeterminate
def calcola_limite_con_analisi(funzione, punto=sp.oo):
    limite = sp.limit(funzione, x, punto)
    forma_indeterminata = None
    try:
        limite_evaluato = funzione.subs(x, punto)
        if limite_evaluato.is_infinite:
            forma_indeterminata = 'Infinity'
        elif limite_evaluato.is_zero:
            forma_indeterminata = 'Zero'
    except:
        pass
    
    if forma_indeterminata:
        print(f"Forma indeterminata rilevata: {forma_indeterminata}. Applico de l'Hôpital se possibile...")
        derivata_num = sp.diff(funzione.as_numer_denom()[0], x)
        derivata_den = sp.diff(funzione.as_numer_denom()[1], x)
        limite = sp.limit(derivata_num / derivata_den, x, punto)
    
    print(f"Il limite di {funzione} per x -> {punto} è: {limite}")
    return limite

# Funzione interattiva di confronto tra funzioni
def confronto_interattivo():
    print("\nSeleziona due funzioni da confrontare:")
    for i, nome in enumerate(funzioni_base.keys()):
        print(f"{i}: {nome}")
    indice_1 = int(input("\nIndice della prima funzione: "))
    indice_2 = int(input("Indice della seconda funzione: "))

    f1 = list(funzioni_base.values())[indice_1]
    f2 = list(funzioni_base.values())[indice_2]

    lim_f1 = calcola_limite_con_analisi(f1)
    lim_f2 = calcola_limite_con_analisi(f2)
    
    plt.figure()
    x_vals = np.linspace(1, 100, 400)
    y1_vals = [float(sp.N(f1.subs(x, val))) for val in x_vals]
    y2_vals = [float(sp.N(f2.subs(x, val))) for val in x_vals]

    plt.plot(x_vals, y1_vals, label=str(list(funzioni_base.keys())[indice_1]))
    plt.plot(x_vals, y2_vals, label=str(list(funzioni_base.keys())[indice_2]))
    plt.yscale('log')
    plt.legend()
    plt.title("Confronto della crescita delle funzioni selezionate")
    plt.show()

# Analisi interattiva dei limiti
def analisi_limite_interattiva():
    print("\nSeleziona una funzione per calcolare il limite:")
    for i, nome in enumerate(funzioni_base.keys()):
        print(f"{i}: {nome}")
    indice = int(input("\nIndice della funzione: "))
    funzione = list(funzioni_base.values())[indice]
    punto = input("\nInserisci il punto (esempio: 0, oo, -oo): ")
    
    if punto == 'oo':
        punto = sp.oo
    elif punto == '-oo':
        punto = -sp.oo
    else:
        punto = float(punto)
    
    calcola_limite_con_analisi(funzione, punto)

# Funzione principale dello script
if __name__ == "__main__":
    print("Strumenti per l'analisi dei limiti e confronto di crescita:")
    while True:
        print("\n1. Calcolo del limite di una funzione con analisi della forma")
        print("2. Confronto tra due funzioni")
        print("3. Esci")
        scelta = input("\nScegli una funzionalità: ")
        
        if scelta == '1':
            analisi_limite_interattiva()
        elif scelta == '2':
            confronto_interattivo()
        elif scelta == '3':
            print("Uscita...")
            break
        else:
            print("Scelta non valida. Riprova.")
