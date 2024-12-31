label final:
    stop music fadeout 1.0
    play music fightmusic loop volume 0.3
    scene bg forest with fade
    show laziness sleep at screen_right with easeinright
    laziness '''
            Здравствуй, Саша, узнаёшь меня? 
            
            Обычно я прихожу, когда ты не хочешь мыть посуду, 
            
            заниматься спортом и делать домашнее задание. 
            '''
    show laziness smile

    laziness'''
            Я поглощаю каждую клеточку твоего мозга, 
            
            заставляю лежать на диване, 

            листать тик ток, 

            смотреть ютуб и играть в видеоигры 
            '''
    
    if farmerBool:
        show chara calm at screen_left with easeinleft
        chara '{b}Достаточно!{/b}'

        show chara idea
        chara '''
            {b}Да{/b}, я не идеален, 
            
            но я стал сильнее, 

            Маша мне дала зачарованное золотое яблоко и оно сделает меня неуязвимым!
            '''

        laziness "{b}НЕЕЕЕТ! НЕ ЕШЬ ЕГО!!!{/b}"

        chara 'Тебе меня не остановить!'

        show chara glow with dissolve
        show laziness puddle at puddle with dissolve 
        laziness "Ну ничего, мои братья с тобой разберутся!"

    else:
        show chara sleepy at screen_left with easeinleft
        chara "Мне так лень тебе что-то отвечать"
        jump bad

    scene bg forest2 with fade
    show badthoungts at center with dissolve:
        zoom 1.3
    
    bad_thoughts '''
                Нас ты просто так не одолеешь! 
                
                Твои яблоки тебе не помогут, мы уже внутри тебя, всегда с тобой,

                благодаря нам ты такой неудачник, прислушивайся к своему разуму чаще, нам это нравится
                '''
    if developerBool:
        show dev find at left with easeinleft:
            linear 0.0 xzoom -1.0 yzoom 1.0
        dev   '''
                Саша, не слушай их, они могут забрать тебя навсегда, раз силой ты их не сможешь победить, сделай это умом.

                Я помещу тебя в игру с этими монстрами, выиграешь-победишь их и в этом мире
                '''

        show space
        stop music fadeout 1.0
        play music space loop fadein 0.2 volume 0.3 
        call screen space_invaders
        $ is_win = False
        while not is_win:
            $ is_win = _return
            if is_win:
                play sound ypee
                "Ты победил"
            else:
                "Еще раз)))"
                call screen space_invaders

    else:
        chara "{b}Прекратите{/b}"
        bad_thoughts "{b}АХАХАХА МЫ ТЕБЯ ПОГЛОТИМ ТЫ НЕУДАЧНИК, У ТЕБЯ НИЧЕГО НЕ ПОЛУЧИТСЯ{/b}"
        jump bad

    
    scene bg forest with dissolve
    stop music fadeout 1.0
    play music fightmusic loop fadein 0.2 volume 0.3 
    show chara scared at screen_left with easeinleft
    chara 'Силы уже на исходе, но кто это? Ещё один монстр?'

    show fear at screen_right with easeinright:
        zoom 1.4
    fear '''
        Я здесь, адреналин-моя пища, как и твои нервные клетки, 
        
        со мной ты выступаешь перед публикой, 

        со мной ты встречал маму с родительского собрания! 
        '''
    
    if kinghtBool:
        show chara scared with dissolve
        chara 'Что же делать, сил уже просто нет'

        
        show knight cannon at character_left with easeinleft:
            linear 0.0 xzoom -1.0 yzoom 1.0
            zoom 1.2
        kinght "Мне кажется или тебе нужна была моя помощь?"
        
        play sound cannon 
        show fear shotted with vpunch
        pause 1.5
        hide fear with dissolve

        show chara happy
        chara "Вова, ты победил его!"
        play sound ypee
        show dev love at screen_right with easeinright:
            zoom 1.1
        
        stop music fadeout 1.0
        play music final fadein 0.2 loop volume 0.3
        dev "Гони плохие мысли прочь, теперь ты сам всё сможешь!"
        
        kinght "Да, ничего не бойся, помни, что ты кузнец своей судьбы!"

        show knight indicate:
                zoom 1.1

        kinght "Кажется, этот автобус за тобой приехал"

        show chara sad
        chara "Кажется, этот автобус за тобой приехал"

        show dev sad:
            zoom 1.4
        dev "Мы будем гостить у тебя во снах, а сейчас тебе пора."

        chara "Прощайте!"

        scene bg bus with fade
        pause 1.5

        jump good_ending

    else:
        show fear smile
        fear "{b}АХАХАХА Я ТЕБЯ ПОГЛОЩУ{/b}"
        jump bad
        

        
label bad:
    scene bg white with fade
    pause 1.0
    jump bad_ending     



screen space_invaders:
    default game = SpaceInvaders()

    add game
    



