label final:
    scene black with fade
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
        show chara angry at screen_left with easeinleft
        chara '{b}Достаточно!{/b}'

        show chara apple
        chara '''
            {b}Да{/b}, я не идеален, 
            
            но я стал сильнее, 

            Маша мне дала зачарованное золотое яблоко и оно сделает меня неуязвимым!
            '''

        laziness "{b}НЕЕЕЕТ! НЕ ЕШЬ ЕГО!!!{/b}"

        chara 'Тебе меня не остановить!'

        show chara glow:
            zoom 1.1
        show laziness puddle
        laziness "Ну ничего, мои братья с тобой разберутся!"

    else:
        show chara sleepy at screen_left with easeinleft
        chara "Мне так лень тебе что-то отвечать"
        jump bad

    scene black with dissolve
    show badthoungts at center:
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
        #mini game pacman
    else:
        chara "{b}Прекратите{/b}"
        bad_thoughts "{b}АХАХАХА МЫ ТЕБЯ ПОГЛОТИМ ТЫ НЕУДАЧНИК, У ТЕБЯ НИЧЕГО НЕ ПОЛУЧИТСЯ{/b}"
        jump bad

    
    scene black with dissolve

    show chara tired at screen_left with easeinleft
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

        #звук выстрела 
        show knight cannon at character_left with easeinleft:
            linear 0.0 xzoom -1.0 yzoom 1.0
            zoom 1.2
        kinght "Мне кажется или тебе нужна была моя помощь?"

        show fear shotted with vpunch
        pause 1.5
        hide fear with dissolve

        show chara happy
        chara "Вова, ты победил его!"

        show dev love at screen_right with easeinright:
            zoom 1.1
        
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

        show chara wave
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




    



