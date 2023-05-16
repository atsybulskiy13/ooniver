products_santa = {
    'mango': 1,
    'apple': 3,
    'carrot': 0
}
products_kopeechka = {
    'pineapple': 3,
    'rapsberry': 0,
    'carrot': 1
}

products_santa.update(products_kopeechka)

products_evroopt = {**products_santa, **products_kopeechka}

products_gippo = products_evroopt.copy()

print(products_santa)
print()
print(products_evroopt)
print()
print(products_gippo)
