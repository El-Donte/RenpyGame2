python:
    choices = []


label terrifying_forest:
    scene bg forest
    "помоги  нам…"

    show chara scared at right
    chara "Кто это??? Что это???"

    show kids at left
    kids "Не бойся нас, мы тебя не обидим"

    chara "Кто вы такие?"

    kids "Мы дети ужасающего монстра Чуши, нам нужна твоя помощь"

    show chara question at right
    chara "Чем мне вам помочь?"

    show kids smile
    kids """
        У нашей мамы завтра день рождения, мы хотим подарить ей какое-нибудь представление,
        помоги нам и мы поможем тебе выбраться из ужасающего леса
        """

    show chara scared at right
    chara "Хорошо…"
    extend "Я вам помогу…"

    
    

label chooce_outfits:
    python:
        choices.clear()

    menu:
        "Выберите образы выступающих"
        "1. Аборигены":
            pass
        "2. Куклы":
            pass
        "3. Повара":
            pass

    menu:
        "Выберите вспомогательные предметы"
        "1. Коробки":
            pass
        "2. Игрушка в виде человека":
            pass
        "3. Колпаки и поварёшки":
            pass

    menu:
        "Выберите детали костюма"
        "1. Фартуки  + деловой костюм":
            pass
        "2. Бусы + блестящие юбки":
            pass
        "3. Бантики + цветные платья":
            pass

label choice_result:
    python:
        result = all(x == choices[0] for x in choices)

    if result:
        '''
        Детям очень понравилось, поставленное вами выступление, только посмотрите, какое чудо получилось
        '''
        jump strange_world
    else:
        '''
        Дети были не в восторге от танца, попробуйте ещё раз, помните, что это дети монстров, 
        вам стоит постараться лучше, чтобы не быть съеденным
        '''
        jump chooce_outfits
