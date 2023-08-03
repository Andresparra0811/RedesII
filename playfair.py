def cifrado_playfair(clave, texto_plano):
    # Crea la matriz de 5x5 a partir de la clave
    # Convierte la clave a mayúsculas y elimina espacios
    clave = clave.replace(" ", "").upper() 
    # Define el alfabeto sin la letra "J"
    letras = "ABCDEFGHIKLMNOPQRSTUVWXYZ" 
    matriz = ""
    for i in clave:
        # Agrega cada letra única de la clave a matriz
        if i not in matriz:
            matriz += i 
    for i in letras:
        # Agrega las letras restantes del alfabeto a matriz
        if i not in matriz:
            matriz += i 
        # Divide matriz en filas de 5 letras para crear la matriz de 5x5
    key_matrix = [matriz[i:i+5] for i in range(0, 25, 5)] 
    
    # Preprocesa el texto plano
    texto_plano = texto_plano.upper().replace(" ", "").replace("J", "I") 
    if len(texto_plano) % 2 == 1:
        # Si la longitud del texto plano es impar, agrega una "X" al final para obtener un número par de letras
        texto_plano += "X" 
    # Cifra el texto plano
    cifrado = ""
    for i in range(0, len(texto_plano), 2):
        a = texto_plano[i]
        # Obtiene pares de letras a y b del texto plano
        b = texto_plano[i+1] 
        # Obtiene la fila y columna de la letra a en la matriz de clave
        a_row, a_col = divmod(matriz.index(a), 5) 
        # Obtiene la fila y columna de la letra b en la matriz de clave
        b_row, b_col = divmod(matriz.index(b), 5) 
        # Si a y b están en la misma fila, desplaza cada letra una columna hacia la derecha
        if a_row == b_row:
            a_col = (a_col + 1) % 5
            b_col = (b_col + 1) % 5 
        # Si a y b están en la misma columna, desplaza cada letra una fila hacia abajo
        elif a_col == b_col:
            a_row = (a_row + 1) % 5
            b_row = (b_row + 1) % 5 
        else:
            # Si a y b no están en la misma fila o columna, intercambia sus columnas
            a_col, b_col = b_col, a_col 
            # Agrega las letras cifradas correspondientes a ciphertext
        cifrado += key_matrix[a_row][a_col] + key_matrix[b_row][b_col] 
    # Devuelve el texto cifrado
    return(cifrado) 

print(cifrado_playfair("COLOMBIA TIERRA QUERIDA","SOY EAN"))