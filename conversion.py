def binaire_to_decimal(binary):
    binary = "".join(reversed(binary))
    decimal = 0
    for number in range(len(binary)):
        if binary == '1':
           decimal += pow(2, number)
    print(decimal)   


binaire_to_decimal('10010')