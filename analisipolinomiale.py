from sympy import symbols, div, simplify, solve
from sympy.parsing.sympy_parser import parse_expr

def find_zeros_and_factorize():
    # Definire la variabile
    x = symbols('x')
    
    # Richiedere all'utente di inserire il polinomio
    polynomial_input = input("Inserisci il polinomio (ad esempio, x**3 - 2*x**2 - x + 2): ")
    polynomial = parse_expr(polynomial_input, local_dict={'x': x})
    polynomial = simplify(polynomial)  # Assicuriamoci che sia semplificato
    print(f"\nIl polinomio inserito è: P(x) = {polynomial}\n")
    
    # Trovare gli zeri razionali possibili usando il Teorema degli Zeri Razionali
    coeffs = polynomial.as_coefficients_dict()
    constant_term = coeffs.get(1, 0)  # Termine costante è il coefficiente di x^0
    leading_coefficient = polynomial.as_poly().LC()  # Leading coefficient

    # Possibili zeri razionali
    possible_zeros = set()
    for i in range(1, abs(constant_term) + 1):
        if constant_term % i == 0:
            possible_zeros.add(i)
            possible_zeros.add(-i)
    for i in range(1, abs(leading_coefficient) + 1):
        if leading_coefficient % i == 0:
            possible_zeros.update({pz/i for pz in possible_zeros})

    print("Possibili zeri razionali:", possible_zeros)

    # Verificare i candidati come zeri
    zeros = []
    for pz in possible_zeros:
        if polynomial.subs(x, pz) == 0:
            zeros.append(pz)
    print("\nZeri trovati:")
    for zero in zeros:
        print(f"x = {zero}")

    # Iniziare con la fattorizzazione usando solo uno zero alla volta
    factorized_polynomial = polynomial
    factors = []

    if zeros:
        # Prendiamo il primo zero trovato e usiamo la regola di Ruffini
        zero = zeros[0]
        quotient, remainder = div(factorized_polynomial, x - zero)
        if remainder == 0:
            factors.append(x - zero)
            factorized_polynomial = quotient

    # A questo punto, mostriamo il polinomio nella forma intermedia
    print(f"\nPolinomio dopo la divisione iniziale: P(x) = ({factors[0]})({factorized_polynomial})")

    # Se il polinomio rimanente è di grado 2, fattorizzare ulteriormente
    if factorized_polynomial.as_poly().degree() == 2:
        print(f"\nIl polinomio rimanente è di grado 2: {factorized_polynomial}")
        # Fattorizziamo il polinomio quadratico rimanente
        remaining_zeros = solve(factorized_polynomial, x)
        for zero in remaining_zeros:
            factors.append(x - zero)

    print("\nFattorizzazione passo passo:")
    for i, factor in enumerate(factors):
        print(f"Passo {i+1}: {factor}")

    # Visualizzare la forma finale del polinomio fattorizzato
    factorized_form = " * ".join([f"({simplify(factor)})" for factor in factors])
    print("\nPolinomio fattorizzato:")
    print(f"P(x) = {factorized_form}")

# Esegui la funzione per trovare gli zeri e fattorizzare
find_zeros_and_factorize()
