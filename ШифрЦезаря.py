def shifr(text, shift):
    shifr_text = ""
    for i in text:
        if i.isalpha():
            start = ord('A') if i.isupper() else ord('a')
            encrypted_char = chr((ord(i) - start + shift) % 26 + start)
            shifr_text += encrypted_char
        else:
            shifr_text += i
    return shifr_text

def rashifr(encrypted_text, shift):
    rashifr_text = ""
    for i in encrypted_text:
        if i.isalpha():
            start = ord('A') if i.isupper() else ord('a')
            decrypted_char = chr((ord(i) - start - shift) % 26 + start)
            rashifr_text += decrypted_char
        else:
            rashifr_text += i
    return rashifr_text

is_ok_2=False
while is_ok_2 == False:
     try:
          shift = int(input('Введите шаг сдвига (целое число):'))
          if shift > 0:
               is_ok_2 = True
          else:
               print('шаг должен быть больше 0')
     except ValueError:
          print('Шаг сдвига должен быть целым числом')
         
text = input("Введите текст: ")
shifr_text = shifr(text, shift)
print("Зашифрованный текст: ", shifr_text)
rashifr_text = rashifr(shifr_text, shift)
print("Расшифрованный текст: ", text)