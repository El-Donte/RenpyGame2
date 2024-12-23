$ kinghtBool = False

label kinght:
    scene bg castle with dissolve

    show chara calm at screen_left with easeinleft
    chara 'Здравствуйте, а что вы тут делаете?'

    show knight sword at screen_right with easeinright:
            zoom 1.1
    kinght '''
            Привет, да мне в замок попасть надо. 
            
            Видишь, там в окне вон принцесса, спасти её надо, 
            
            но для начала дракона вырубить, иначе вообще принцессу не вытащить
            '''

    menu:
        "Я ничего не смогу с этим сделать, до свидания":
            pass
        "Давайте я вам мост через пропасть нарисую и вы попадёте в замок":
            show chara write
            show bg castle brige
            chara 'Ну вроде должно сработать'
            
            scene bg castle fall with fade
            '''
            Мост не выдержал рыцаря, вы не помогли ему, но что же, это позади?

            Ещё одно загадочное свечение, надо отправляться в путь
            '''
            
            '{b}ИЗВИНИСЬ ПЕРЕД РЫЦАРЕМ!!!{/b}'
            pass
    
    jump final

label knight_dev:
    
    $ kinghtBool = True

    scene bg castle with dissolve

    show dev happy at screen_left with easeinleft:
        linear 0.0 xzoom -1.0 yzoom 1.0
        zoom 1.1
    dev '''
        {b}О!{/b} 

        Я знаю это место! 

        Привет, Вова, чем занят?
        '''

    show knight calm at character_right with easeinright:
            zoom 1.1
    kinght '''
            Привет, Никита, да мне в замок попасть надо, перед ним пропасть, меч вообще в этой ситуации не поможет. 

            Видишь, там в окне вон принцесса, спасти её надо, но для начала дракона вырубить, иначе вообще принцессу не вытащить.
            '''
    show dev happy at more_right with easeinleft:
            linear 0.0 xzoom 1.0 yzoom 1.0

    show chara write at screen_left with easeinleft
    chara 'Давайте я нарисую оружие, это должно помочь'

    show knight cannon:
        zoom 1.2
    kinght 'Ого, интересный у тебя блокнот...'

    show dev love
    dev 'Попробуй из неё по дракону пульнуть'

    show knight question
    kinght 'Три раза уже выстрелил ничего не долетает'

    show chara question
    chara 'Судя по разной траектории полёта, в вашем ужасающем лесе напрочь отсутствует физика, в том числе баллистическое движение'

    show dev idea
    dev 'Я могу пофиксить этот баг, нужна всего лишь формула дальности полёта'

    #мини игра
    $ quick_menu = False
    scene bg castle cannon with fade
    pause 1.0
    scene bg castle destroied with fade
    pause 1.0
    scene bg castle destroied2 with fade
    $ quick_menu = True

    show chara happy at screen_left with easeinleft

    show knight calm at character_right with easeinright:
            zoom 1.1
    kinght 'А из вас, ребята получился отличный дуэт! Ну а мне пора совершать подвиг, удачи вам'

    show dev happy at more_right with easeinright:
            zoom 1.1
    dev 'И тебе всего хорошего! Нам пора идти дальше.'

    jump final




