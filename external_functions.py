def find_max(numbers: list) -> int:
    # Verifica si la lista está vacía
    if not numbers:
        raise ValueError("La lista no puede estar vacía")
    
    # Inicializa el valor máximo con el primer elemento de la lista
    maximo = numbers[0]
    
    # Recorre la lista desde el segundo elemento hasta el final
    for num in numbers[1:]:
        if num > maximo:
            maximo = num
    
    return maximo

def testing():
    testing_var = 5
    return testing_var