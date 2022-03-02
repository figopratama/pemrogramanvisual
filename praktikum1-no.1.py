import string

letters = string.ascii_lowercase + string.ascii_lowercase

text = list(input('masukkan kata: ').lower())

key = int(input('masukkan kunci: '))

end_program = False

while not end_program:
    for i in range(len(text)):
        if text[i] == ' ':
            text[i] = ' '
        else:
            enkripsi_text = letters.index(text[i]) + key
            text[i] = letters[enkripsi_text]
    print('\n'.join(map(str, text)))
    end_program = True

    
    
