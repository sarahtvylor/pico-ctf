CIPHERTEXT = "Ta _7N6DDDhlg:W3D_H3C31N__0D3ef sHR053F38N43D0F i33___NA"
KEY = 4

def decode(ciphertext, rails):
    railfence = [["\n" for i in range(len(ciphertext))]
                       for j in range(rails)]
    downwards = True
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if row == 0:
            downwards = True
        if row == rails-1:
            downwards = False
        
        railfence[row][col] = "*"
        col += 1

        if downwards:
            row += 1
        else:
            row -= 1

    char = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if railfence[i][j] == "*":
                railfence[i][j] = ciphertext[char]
                char += 1
    

    plaintext = []
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if row == 0:
            downwards = True
        if row == rails-1:
            downwards = False
    
        plaintext.append(railfence[row][col])
        col += 1

        if downwards:
            row += 1
        else:
            row -= 1
    
        
    return("".join(plaintext))

print(decode(CIPHERTEXT, KEY))