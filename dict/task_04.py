pushkin = '''У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.'''

pushkin = pushkin.lower()
splited_pushkin = pushkin.split()
all_letters_pushkin = ''.join(splited_pushkin)

letters_list = []

for i in all_letters_pushkin:
    letters_list.append(i)

unic_letters_list = list(set(letters_list))

letters_dict = {}

for index in range(len(unic_letters_list)):
    letters_dict[unic_letters_list[index]] = 0

for key in letters_dict:
    for letter in all_letters_pushkin:
        if key == letter:
            letters_dict[key] += 1

for symbol, times in letters_dict.items():
    if str(times)[-1] == '2' or str(times)[-1] == '3' and str(times) != '13' or str(times)[-1] == '4':
        print(f'Символ {symbol} встречается {times} раза')
    else:
        print(f'Символ {symbol} встречается {times} раз')
