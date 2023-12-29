def russia(text, shift):
    russia_text = ''
    for i in text:
        if i.isalpha():
            if i.isupper():
                encrypted_char = chr((ord(i) - ord('А') + shift) % 32 + ord('А'))
            else:
                encrypted_char = chr((ord(i) - ord('а') + shift) % 32 + ord('а'))
            russia_text += encrypted_char
        else:
            russia_text += i
    return russia_text

def rushifr_russia(text, shift):
    rushifr_russia_text = ''
    for i in text:
        if i.isalpha():
            if i.isupper():
                decrypted_char = chr((ord(i) - ord('А') - shift) % 32 + ord('А'))
            else:
                decrypted_char = chr((ord(i) - ord('а') - shift) % 32 + ord('а'))
            rushifr_russia_text += decrypted_char
        else:
            rushifr_russia_text += i
    return rushifr_russia_text


def angl(text, shift):
    angl_text = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            angl_text += encrypted_char
        else:
            angl_text += char
    return angl_text

def rashifr_angl(encrypted_text, shift):
    rashifr_angl_text = ""
    for char in encrypted_text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - start - shift) % 26 + start)
            rashifr_angl_text += decrypted_char
        else:
            rashifr_angl_text += char
    return rashifr_angl_text




while True:
    vibor = input("Введите на каком языке делать расшифровку(русский или английский): ")
    if vibor in ['русский', 'английский']:
        while True:
            try:
                shift = int(input('Введите шаг сдвига (целое число): '))
                if vibor == 'русский':
                    text = input('Введите текст: ')
                    russia_text = russia(text, shift)
                    print('Зашифрованный текст:', russia_text)
                    rushifr_russia_text = rushifr_russia(russia_text, shift)
                    print('Расшифрованный текст:', rushifr_russia_text)
                    break
                if vibor == 'английский':
                    text = input('Введите текст: ')
                    angl_text = angl(text, shift)
                    print("Зашифрованный текст: ", angl_text)
                    rashifr_angl_text = rashifr_angl(angl_text, shift)
                    print("Расшифрованный текст: ", rashifr_angl_text)
                    break
            except ValueError:
                print('Шаг сдвига должен быть целым числом')
    else:
        print("Неправильный ввод,выберите русский или анлийский(пишите с маленькой буквы русскими буквами)")





