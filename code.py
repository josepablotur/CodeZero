def find_max(numbers: list) -> int:
    # Verifica si la lista está vacía
    if not numbers:
        raise ValueError("La lista no puede estar vacía")
    
    # Inicializa el valor máximo con el primer elemento de la lista
    max_number = numbers[0]
    
    # Recorre la lista desde el segundo elemento hasta el final
    for num in numbers[1:]:
        # Si el número actual es mayor que el valor máximo actual, lo actualiza
        if num > max_number:
            max_number = num
    
    return max_number



numbers = [3, 5, 7, 2, 8, 1, 4]
max_value = find_max(numbers)
print(f"El número máximo en la lista es: {max_value}")

