# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4
print(f'{apples} яблука і {banana} бананів.')

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(f'Периметр фігури = {perimetery}')


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
print('Task 07')
apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = apple_trees - 2
total = apple_trees + pear_trees + plum_trees
print(f'В саду посадили {apple_trees} яблуні, {pear_trees} груш, {plum_trees} слив. Всього посадили {total} дерев в саду.')

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
print('Task 08')
t_before_lunch = 5
t_afternoon = t_before_lunch - 10
t_evening = t_afternoon + 4
print(f'Надвечір температура повітря {t_evening} градус.')

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
print('Task 09')
boys = 24
girls = boys // 2
today_boys = boys - 1
today_girls = girls - 2
number_of_children_today = today_boys + today_girls
print(f'Сьогодні у театральному гуртку {number_of_children_today} дитини. А саме {today_boys} хлопчики та {today_girls} дівчат.')

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
print('Task 10')
first_book = 8
print(f'Перша книжка коштує {first_book} грн.')
second_book = first_book + 2
print(f'Друга книжка коштує {second_book} грн.')
third_book = (first_book + second_book) // 2
print(f'Третя книжка коштує {third_book} грн.')
total = first_book + second_book + third_book
print(f'Усі книги будуть коштувати {total} грн.')
