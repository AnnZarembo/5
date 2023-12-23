def shifr(text,shift):
    shifr_text=''
    for i in text:
        if i.isupper():
            i_index=ord(i) - ord('А')
            i_shifted=(i_index + shift) % 26 + ord('А')
            i_new=chr(i_shifted)
            shifr_text+=i_new
        elif i.islower():
            i_index=ord(i)-ord('а')
            i_shifted=(i_index + shift)%26+ord('а')
            i_new=chr(i_shifted)
            shifr_text+=i_new
        elif i.isdigit():
            i_new=(int(i)+shift)%10
            shifr_text+=str(i_new)
        else:
            shifr_text+=i
    return shifr_text

def shifr_rashifr(text,shift):
    rashifr_text=''
    for i in text:
        if i.isupper():
            i_index=ord(i) - ord('А')
            i_levo_pos=(i_index - shift) % 26 + ord('А')
            i_levo=chr(i_levo_pos)
            rashifr_text+=i_levo
        elif i.islower():
            i_index=ord(i) - ord('а')
            i_levo_pos=(i_index - shift) % 26 + ord('а')
            i_levo=chr(i_levo_pos)
            rashifr_text+=i_levo
        elif i.isdigit():
            i_levo =(int(i)-shift) % 10
            rashifr_text+=str(i_levo)
        else:
            rashifr_text+=i
    return rashifr_text

iscl=' ,.*()_+{["|\/}]№@#$^&;%:%*-=~1234567890!?<>'
while True:
        a_1 = True
        a_2 = True

        text = input('Введите текст:')
        for letter in text:
            if letter=='Ё'or letter=='ё':
                a_1 = False
            if letter not in iscl:
                if ord(letter) < 1040 or ord(letter) > 1103:
                    a_2 = False
        if a_1 == False:
            print('Введите текст без буквы ё')
        elif a_2 == False:
            print('Введите текст на русском языке')
        else:
            break
while True:
    try:
        shift = int(input('Введите шаг сдвига (целое число):'))
        break
    except ValueError:
        print('Шаг сдвига должен быть целым числом')

shifr_text=shifr(text,shift)
print('Зашифрованный текст:',shifr_text)
shifr_text_text=shifr_rashifr(text,shift)
print('Расшифрованный текст:',shifr_text)