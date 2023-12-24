def shifr(text, shift):
    shifr_text = ''
    for i in text:
        if i.isalpha():
            start = ord('A') if i.isupper() else ord('a')
            shifr_char = chr((ord(i) - start + shift) % 26 + start)
            shifr_text += shifr_char
        else:
            shifr_text+=i
    return shifr_text

def rashifr(text, shift):
    rashifr_text = ''
    for i in text:
        if i.isalpha():
            start = ord('A') if i.isupper() else ord('a')
            rashifr = chr((ord(i) - start - shift) % 26 + start)
            rashifr_text += rashifr
        else:
            rashifr_text += i
    return rashifr_text

alphabet_of_exceptions = '.!?&*(|\/}]№;%:@#$%^* <>,-=~123456)_+{["7890'
while True:
        a1 = True
        a2 = True
        text = input('Введите текст: ')
        for i in text:
            if i == 'ё' or i == 'Ё':
                a1 = False
            if i not in alphabet_of_exceptions:
                if ord(i) < 1040 or ord(i) > 1103:
                    a2 = False
        if a1==False:
            print('Введите текст без буквы ё')
        elif a2==False:
            print('Введите текст на русском языке')
        else:
            break


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

shifr_text = shifr(text, shift)
print('Зашифрованный текст:', shifr_text)
rashifr_text = rashifr(shifr_text, shift)
print('Расшифрованный текст:', text)