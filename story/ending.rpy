label good_ending:
    scene bg businter with fade
    show skelet smile at screen_right with easeinright:
        linear 0.0 xzoom -1.0 yzoom 1.0
        zoom 1.2
    skelet "А ты молодец, идеально вписался в окружающую среду, тебе определённо стоит стать геймдизайнером!"

    show chara question at screen_left with easeinleft
    
    chara "Гейм кого?"

    skelet "Задания, которые ты выполнял в твоём мире делает геймдизайнер, ну а теперь тебе пора вставать"

    scene bg white with fade
    pause 1.0
    scene bg room with fade

    show mom kind at screen_left with easeinleft:
        zoom 1.1
    mom "Сынок, доброе утро, ты решил, кем хочешь стать? Пора бы уже подавать документы"

    show chara happy at screen_right with easeinright:
        linear 0.0 xzoom -1.0 yzoom 1.0
    chara "Я дома! Мама, я буду гейм-дизайнером!"

    show mom #question
    mom '''
        Саша, а где такому учат? Мне соседка говорила про ИРИТ-РТФ.
        
        У неё сын там отучился, сейчас фирму открыл, деньги куры не клюют, может ты туда поступишь? 
        '''
    
    scene radic
    show chara happymerch
    chara "Я поступлю туда и стану успешным!"

    scene absolute cinema with fade
    pause 2.4
    return 



label bad_ending:

    scene black with fade
    show skelet fury at center with easeinright:
        linear 0.0 xzoom -1.0 yzoom 1.0
        zoom 1.2
    
    skelet "Ты проиграл этот бой, но он не единственный в твоей жизни, дерзай, 
            может быть ты поймёшь для чего тебе был дан этот урок!"

    scene bg white with fade
    pause 1.0
    scene bg pvz with fade
    
    dev "Молодой человек, отдайте мой заказ!"

    show chara amazed at screen_left with easeinleft
    chara "Никита, это ты?"

    show developer human at screen_right with easeinright
    dev "Привет, Саша, это я, мне удалось выбраться из ужасающего леса "

    show chara happy
    chara "Что нового? Как дела?"

    dev 'Всё хорошо, вот учусь в ИРИТ-РТФ, зарплата-шестизначная сумма, 
                я добился чего хотел, прости пора идти, работа и учёба, понимаешь?'

    scene bg radic with fade
    chara "Хочу тоже получить профессию мечты, в следующем году поступлю в ИРИТ-РТФ!"

    scene absolute cinema with fade
    pause 2.4
    return 

    




