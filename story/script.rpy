label start:
    stop music fadeout 1
    play music musbacground fadein 1 volume 0.5
    scene black

    '''
    В самом обыкновенном  мире жил самый обыкновенный абитуриент. Он задумался, казалось, над самым обыкновенным вопросом

    кем ему быть, но ответ на этот вопрос совершенно необыкновенный.....
    '''

    scene bg room with fade

    show chara neutralpc at screen_right with easeinright

    chara "Наконец-то прошли все экзамены, я могу расслабиться и отдохнуть, поиграть в свои любимые игры."

    show mom kind at screen_left with easeinleft:
            zoom 1.2
    
    mom "Сынок, ты молодец, сдал все экзамены, теперь нужно думать о поступлении"

    chara "Мама, я так устал ничего не хочу слышать про это, я просто хочу отдохнуть и поиграть"

    show mom angry
    mom "Ну ты же понимаешь, что от этого будет зависеть вся твоя дальнейшая жизнь"

    menu:
        "Мама, отстань, дай мне поиграть!":
            pass

        "Хорошо, но я подумаю об этом потом":
            pass
    
    show mom superangry with vpunch
    mom "{b}ТЫ МЕНЯ НЕ ПОНЯЛ??? Я СКАЗАЛА ЭТО НУЖНО СДЕЛАТЬ СЕЙЧАС{/b}"

    show chara angrypc with vpunch
    chara   '''
            Мама, ты меня вообще не понимаешь, твои слова мне никак не помогут,
            
            твоё давление на меня, просто вынуждает  поехать к бабушке
            '''
    
    scene bg stairs with fade
    "спускается по лестнице и выходит на улицу"

    scene bg path with fade

    show chara calm at screen_left with easeinleft
    play sound birds fadein 0.2 loop volume 0.3
    chara "Как же тут красиво и спокойно, птички поют, светит капризное солнце"

    scene bg station with fade
    stop sound fadeout 0.5
    play sound road fadein 0.2 loop volume 0.2
    show chara happy at screen_left with easeinleft
    chara "Вот и автобус"

    scene bg bus with fade
    chara "Сейчас у бабушки всё наладится, она не будет ничего от меня требовать, я отдохну"

    scene black with dissolve
    stop sound fadeout 0.5

    jump bus
