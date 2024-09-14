from sympy import symbols, log, sqrt, S
from sympy.calculus.util import continuous_domain
from sympy.parsing.sympy_parser import parse_expr

def format_domain(domain):
    """Formatta il dominio in una stringa leggibile in italiano."""
    if domain == S.Reals:
        return "tutti i numeri reali"
    
    intervals = []
    if domain.is_Union:
        for interval in domain.args:
            if interval.start == -S.Infinity and interval.end == S.Infinity:
                intervals.append("tutti i numeri reali")
            else:
                start = f"({interval.start}" if interval.left_open else f"[{interval.start}"
                end = f"{interval.end})" if interval.right_open else f"{interval.end}]"
                intervals.append(f"{start}, {end}")
    else:
        start = f"({domain.start}" if domain.left_open else f"[{domain.start}"
        end = f"{domain.end})" if domain.right_open else f"{domain.end}]"
        intervals.append(f"{start}, {end}")
    
    return " U ".join(intervals)

def find_domain(function_str, var='x'):
    # Definisce la variabile
    x = symbols(var)
    
    # Parse della funzione
    function = parse_expr(function_str, local_dict={var: x})
    
    # Trova il dominio continuo della funzione
    domain = continuous_domain(function, x, S.Reals)
    
    # Determina il tipo di funzione e le restrizioni
    restrictions = []
    function_type = []

    # Verifica se la funzione è razionale (contiene un denominatore)
    if function.has(x):
        for term in function.atoms():
            if term.func == log:
                restrictions.append(f"L'argomento del logaritmo {term.args[0]} deve essere positivo")
                function_type.append("logaritmica")
            if term.func == sqrt:
                restrictions.append(f"L'argomento della radice {term.args[0]} deve essere non negativo")
                function_type.append("con radice")
            if term.func == symbols(var).func:
                # Cerca termini con denominatori
                if term.is_Pow and term.args[1] < 0:
                    denominators = [denom for denom in term.atoms() if denom.has(x)]
                    for denom in denominators:
                        denom_zero = solve(denom, x)
                        restrictions.extend([f"Il denominatore {denom} non deve essere zero: {zero}" for zero in denom_zero])
                        function_type.append("razionale")

    # Se non sono state trovate specifiche funzioni, assume che sia un tipo generico
    if not function_type:
        function_type.append("generica")
    
    return domain, restrictions, function_type

def print_examples():
    """Stampa degli esempi di funzioni da utilizzare."""
    print("Esempi di funzioni da utilizzare:")
    print("- Funzione razionale: x/(x**2 - 1)")
    print("- Funzione con radice: sqrt(x - 1)")
    print("- Funzione con logaritmo: log(x - 1)")
    print("- Funzione generica: (x**2 - 4)/(x - 2)")

# Esempio di utilizzo
if __name__ == "__main__":
    # Stampa esempi di funzioni
    print_examples()
    
    # Inserisci l'espressione della funzione
    function_input = input("Inserisci la funzione: ")
    
    # Trova il dominio della funzione
    domain, restrictions, function_type = find_domain(function_input)
    
    # Determina se il dominio è in tutti i numeri reali
    is_all_reals = domain == S.Reals

    # Stampa il tipo di funzione
    print(f"Tipo di funzione: {', '.join(set(function_type))}")
    
    # Stampa il dominio
    formatted_domain = format_domain(domain)
    if is_all_reals:
        print("Il dominio della funzione comprende tutti i numeri reali.")
    else:
        print(f"Il dominio della funzione è: {formatted_domain}")
    
    if restrictions:
        print("Restrizioni trovate nel dominio:")
        for restriction in restrictions:
            print(f"- {restriction}")
