import numpy as np
import matplotlib.pyplot as plt

def calcola_retta(p1, p2):
    # Estrai le coordinate dei punti
    x1, y1 = p1
    x2, y2 = p2
    
    # Calcola il coefficiente angolare m
    if x2 - x1 != 0:  # Evita la divisione per zero
        m = (y2 - y1) / (x2 - x1)
    else:
        m = None  # La retta è verticale

    # Calcola l'ordinata all'origine q
    if m is not None:
        q = y1 - m * x1
    else:
        q = None  # La retta è verticale

    return m, q

def disegna_grafico(p1, p2):
    # Calcola m e q
    m, q = calcola_retta(p1, p2)
    
    # Stampare i passaggi
    if m is not None:
        print(f"Coefficiente angolare (m) = (y2 - y1) / (x2 - x1) = ({p2[1]} - {p1[1]}) / ({p2[0]} - {p1[0]})")
        print(f"m = ({p2[1] - p1[1]}) / ({p2[0] - p1[0]}) = {m}")
        print(f"Ordinata all'origine (q) = y1 - m * x1 = {p1[1]} - {m} * {p1[0]}")
        print(f"q = {p1[1]} - ({m} * {p1[0]}) = {q}")
        print(f"L'equazione della retta è: y = {m:.2f}x + {q:.2f}")
    else:
        print("La retta è verticale e non può essere espressa nella forma y = mx + q.")
        print(f"L'equazione della retta è: x = {p1[0]}")

    # Creare il grafico
    plt.figure(figsize=(8, 6))
    
    # Definire la gamma di x per il grafico
    x_vals = np.linspace(min(p1[0], p2[0]) - 1, max(p1[0], p2[0]) + 1, 100)
    
    if m is not None:
        # Calcolare i valori di y usando l'equazione della retta
        y_vals = m * x_vals + q
        plt.plot(x_vals, y_vals, label=f'y = {m:.2f}x + {q:.2f}', color='blue')
    else:
        # Caso della retta verticale
        plt.axvline(x=p1[0], color='blue', label=f'x = {p1[0]}')
    
    # Tracciare i punti dati
    plt.scatter(*p1, color='red', zorder=5)
    plt.scatter(*p2, color='red', zorder=5)
    plt.text(p1[0], p1[1], f' ({p1[0]}, {p1[1]})', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
    plt.text(p2[0], p2[1], f' ({p2[0]}, {p2[1]})', fontsize=12, verticalalignment='bottom', horizontalalignment='right')

    # Aggiungere assi
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    # Etichette e titolo
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Grafico della retta passante per i punti dati')
    plt.legend()
    plt.grid(True)

    # Mostrare il grafico
    plt.show()

# Richiedere i punti all'utente
x1 = float(input("Inserisci la coordinata x del primo punto: "))
y1 = float(input("Inserisci la coordinata y del primo punto: "))
x2 = float(input("Inserisci la coordinata x del secondo punto: "))
y2 = float(input("Inserisci la coordinata y del secondo punto: "))

punto1 = (x1, y1)
punto2 = (x2, y2)

disegna_grafico(punto1, punto2)
