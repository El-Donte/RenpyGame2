

label farmer:
    stop music fadeout 1.0
    play music farmermusic fadein 0.2 loop volume 0.4
    $ farmerBool = False
    scene bg farm2 with fade

    show chara question at screen_left with easeinleft
    chara 'От чего же исходит загадочный свет?'

    show bg farm with dissolve
    show farmer calm at screen_right with easeinright:
        zoom 1.2
    farmer 'Привет, я фермер Маша! Мой сад кормит жителей ужасающего леса уже много лет.'

    show chara happy
    chara 'Приятно познакомиться, Маша, я Саша. Я случайным образом здесь оказался, теперь пытаюсь попасть обратно домой'
    
    
    show farmer scared
    farmer 'Саша, прячься!'
    play sound crows 
    hide chara
    hide farmer

    show bg ravens with vpunch
    $ quick_menu = False
    pause 2.0
    $ quick_menu = True
    #убрать менюшку и звук ворон
    

    show chara scared at screen_left with dissolve
    chara 'Это вороны?'

    show farmer sad at screen_right with dissolve
    farmer 'Да, они вечно меня досаждают, если бы не они урожая было бы в два раза больше! '

    hide chara
    hide farmer

    menu:
        'Приятно было пообщаться, я пойду дальше':
            pass
        'Я помогу тебе, Маша, у меня чёрный пояс по борьбе с воронами, я каждой клюв снесу!':
            
            '''
            У вас не получилось разогнать ворон, может из-за того, что их количество близится к бесконечности, 

            а может из-за того, что просмотр сериала «Слово пацана» не равно умению драться
            '''
            pass

        'Я думаю, можно сделать пугало, и вороны улетят, я могу помочь, Маша!':

            centered "Loading data...{nw}"

            $ farmerBool = True
            $ grid_width = 5
            $ grid_height = 5
            $ chosen_img = "scarecrow.png"

            
            call puzzle from _call_puzzle    

            scene bg farmscarecrow with fade
            show chara happy at screen_left with easeinleft
            show farmer calm at screen_right with easeinright
            
            play sound ypee
            farmer 'Спасибо большое, Саша, моя проблема решена! Возьми в знак благодарности золотое зачарованное яблоко, оно сделает тебя неуязвимым!'

            chara 'Я был рад помочь, Маша, мне пора идти дальше, надеюсь, ещё повстречаемся'
            pass

    jump developer

