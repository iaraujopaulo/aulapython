def parOuImpar(num):
    try:
        if num % 2 == 0:
            return "par"
    
        return "impar"
    
    except TypeError:
        print("Apenas os números são suportados")
        return
    
print(parOuImpar("a"))
