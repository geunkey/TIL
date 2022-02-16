def profile(name, age, *language):
    print(f'이름 : {name}, 나이 : {age}', end = '   ')
    for lang in language:
        print(lang, end = '  ')
    print()

profile('유재석', 17, '파이썬', 'java', 'lan', 'kaka')
profile('geunho', 17, '파이썬')
profile('geunkh', 32, '파이썬')
 