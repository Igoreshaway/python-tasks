from itertools import zip_longest

pigeons = ['Бакинский агаран', 'Богемская волшебная ласточка', 'Чёрно-пегий турман', 'Английский поутер',
           'Благодарненский', 'Ташкентский двухчубый', 'Бабочка', 'Панцирный сорочий', 'Чайка немецкая щитковая',
           'Крюковский', 'Николаевский белый', 'Пермский белоголовый', 'Ленточный турман', 'Люцерн', 'Московский монах',
           'Тюрингский врюстер', 'Свердловский серо-голубой крапчато-головый голубь (en)', 'Тюрингский белохвостый',
           'Русский барабанщик', 'Китайская чайка', 'Дутыш бриенский', 'Кременчугские цветные', 'Английский крестовый',
           'Гамбургский шиммель', 'Английская совиная чайка', 'Воронежский белозобый', 'Павлин черночистый',
           'Армавирский белоголовый короткоклювый космач', 'Польский белоголовый', 'Новочеркасский чернохвостый',
           'Антверпенский голубь', 'Смоленский грач', 'Саксонская волшебная ласточка', 'Русский выставочный',
           'Франконский вельветовый щитковый', 'Бакинский бойный', 'Тюрингский пламенок', 'Запорожский чубатый',
           'Вольский турман', 'Дубовский', 'Кинг', 'Одесский турман', 'Ржевский ленточный турман',
           'Тюрингский белогрудый', 'Шейк бакинский красный ленточный', 'Кофейный турман', 'Тульский чеграш',
           'Кёнигсбергский цветнохвостый', 'Южно-немецкий черноголовый голубь', 'Якобин краснорябый',
           'Венгерский высоколётный', 'Турецкий черный', 'Тюрингский одноцветный', 'Тюрингский аист', 'Ржевская чайка',
           'Уды двухчубые', 'Доминикан (Польская чайка)', 'Камыш', 'Штральзундский высоколетный',
           'Индийский королевский высоколётный', 'Воронежский чернохвостый', 'Волжский желтогрудый',
           'Черный белоголовый высоколетный', 'Тюрингский мышиный', 'Жарый ленточный турман', 'Ташкентский белый',
           'Берлинский короткий', 'Нежинский', 'Спортивный рябой', 'Тюрингский щитокрылый',
           'Саксонский монах (голубокружевной, полосатый)', 'Тюрингский лунный', 'Краснодарский голубой',
           'Якобин белый', 'Николаевский тучерез', 'Аргавский белохвостый', 'Архангел', 'Спортивный сизый',
           'Нюрембургский жаворонок', 'Царицинский', 'Николаевский красный белохвостый', 'Дутыш английский',
           'Армавирский белоголовый длинноклювый космач (лысый)', 'Немецкий выставочный', 'Очаковский',
           'Коморненский турман', 'Старая немецкая чайка', 'Саксонский щитковый муфтовый', 'Чайка московская',
           'Луганский', 'Орловский бородун', 'Казанский панцирный', 'Казанский цветнохвостый', 'Гривун', 'Мурый',
           'Ростовский статный', 'Лагор', 'Тюрингский дутыш', 'Лимбургский Воротниковый голубь', 'Саксонский пятнистый',
           'Астраханский', 'Башкирский Спартак', 'Немецкий крестовый монах', 'Киевский светлый',
           'Гданьский высоколётный', 'Волжский ленточный', 'Челябинский чернокрылый', 'Тюрингский монах',
           'Николаевский черный', 'Николаевский желтый белохвостый', 'Бухарский барабанщик', 'Урюпинский', 'Агаран',
           'Уральский белобокий', 'Турман чёрно-пёстрый', 'Волжский красногрудый', 'Тюрингский белоголовый',
           'Свердловский высоколетный голубь', 'Тюрингский спортивный', 'Краснодарский белоголовый',
           'Анатолийская чайка', 'Кёнигсбергский', 'Турецкий желтый', 'Аахенская чайка с лаковым щитком',
           'Тульская сорока', 'Багдет нюрнбергский', 'Николаевский высоколетный', 'Типлер', 'Кобургский жаворонок',
           'Кишеневский турман', 'Тюрингская ласточка', 'Ташкентский двухчубый желтый', 'Датский сьюбиан',
           'Южнонемецкая голова мавра', 'Пермский желтый высоколётный', 'Орловский белый', 'Дрезденский барабанщик',
           'Турецкий голубой', 'Узбекский белый короткоклювый']

print(len(pigeons))


def get_group_of_pigeons(iter_pigeons: iter, number_pigeons_for_group=2) -> list[str]:
    group_pigeons = []
    while len(group_pigeons) < number_pigeons_for_group:
        try:
            group_pigeons.append(next(iter_pigeons))
        except StopIteration:
            difference_len_between_last_and_need_groups = number_pigeons_for_group - len(group_pigeons)
            filling_last_group_none = [None] * difference_len_between_last_and_need_groups
            group_pigeons.extend(filling_last_group_none)
            return group_pigeons

    return group_pigeons


def get_groups_of_pigeons(pigeons: list, number_pigeons_for_group=2) -> list[list]:
    iter_pigeons = iter(pigeons)
    groups_pigeons = []

    while len(groups_pigeons) < len(pigeons) / number_pigeons_for_group:
        group_pigeons = get_group_of_pigeons(iter_pigeons, number_pigeons_for_group)
        groups_pigeons.append(group_pigeons)
    return groups_pigeons


pairs_pigeons = get_groups_of_pigeons(pigeons, number_pigeons_for_group=6)
print(len(pairs_pigeons))
print(pairs_pigeons)
