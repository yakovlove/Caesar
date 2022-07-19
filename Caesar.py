alphabetENG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabetRU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
lang = input('Выберети язык(RU or ENG)')
offset = int(input('шаг шифра'))
message = input('текст').upper()
result = ''
if lang == 'RU':
    for i in message:
        position = alphabetRU.find(i)
        newPosition = position + offset
        if i in alphabetRU:
            result += alphabetRU[newPosition]
        else:
            result += i
else:
    for i in message:
        position = alphabetENG.find(i)
        newPosition = position + offset
        if i in alphabetENG:
            result += alphabetENG[newPosition]
        else:
            result += i
print(result)
