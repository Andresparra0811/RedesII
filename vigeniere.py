def vigenere_cipher(texto_plano, clave):

    # Convertimos el texto y la clave a mayúsculas
    texto_plano = texto_plano.upper()
    clave = clave.upper()
    
    # Creamos una cadena con todas las letras del alfabeto
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Creamos una matriz de 26 x 26 para almacenar la tabla de Vigenère
    vigeniere = []
    for i in range(26):
        row = alfabeto[i:] + alfabeto[:i]
        vigeniere.append(row)
    
    # Ciframos el texto letra por letra
    texto_encriptado = ''
    clave_index = 0
    for i in texto_plano:
        if i in alfabeto:
            # Encontramos el índice de la letra en el alfabeto
            fila_index = alfabeto.index(clave[clave_index])
            columna_index = alfabeto.index(i)
            # Obtenemos la letra cifrada de la tabla de Vigenère
            letra_encriptada = vigeniere[fila_index][columna_index]
            # Agregamos la letra cifrada al texto cifrado
            texto_encriptado += letra_encriptada
            # Incrementamos el índice de la clave
            clave_index = (clave_index + 1) % len(clave)
        else:
            # Si la letra no está en el alfabeto, la agregamos tal cual al texto cifrado
            texto_encriptado += i
    
    return texto_encriptado

# Ejemplo de uso
print(vigenere_cipher('SOY EAN', 'COLOMBIA TIERRA QUERIDA'))