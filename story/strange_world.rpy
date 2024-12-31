label strange_world:
    stop music fadeout 1.0
    play music forestmusic fadein 0.2 loop volume 0.3
    scene bg forest with fade
    '''
    Дорога по ужасающему лесу заняла достаточно много времени, 

    но вдруг перед вами появился свет, где-то вдали, вы решили посмотреть что же это такое

    Вы подошли ближе, свет исходил от блокнота и ручки
    '''
    show notebook with dissolve
    pause 1.5
    hide notebook with dissolve
    
    show chara question with dissolve
    chara 'Но зачем мне этот блокнот и ручка? Этот лес хранит огромное количество тайн'

    show chara question:
            linear 0.0 xzoom -1.0 yzoom 1.0

    chara 'Мне кажется или кто-то кричит?'

    chara '''
            Видимо показалось. 

            {b}Стоп!{/b}

            Но.. Почему следы оставленные мной светятся?
        '''

    show chara question:
            linear 0.0 xzoom 1.0 yzoom 1.0

    chara 'Значит я не бесполезен для этого мира, у меня есть какие-то силы, которые заставляют светиться эту траву'
    show chara happy
    chara '''
            Так, я думаю не просто так я нашёл этот блокнот, буду вести свой дневник, 
            
            он поможет мне адекватно оценивать ситуацию и справляться с эмоциями!
        '''

    show chara write
    chara 'Напишу о том, как сильно я хочу домой...'
    play sound fall 
    scene bg house with fade
    show chara amazed at screen_left with dissolve 
    chara 'ААА... Что такое огромное упало??? ДОМ???'
    
    show chara question
    chara 'Значит... этот дневник исполняет желания'

    show chara happy
    chara 'Что же... Домой он меня не отправит, но может сделать моё пребывания здесь немного легче'

    show chara write
    chara 'Сперва, мне определённо нужен фонарик, здесь очень темно, мало ли ещё какие-нибудь предметы на голову будут падать...'

    show chara withlight:
        linear 0.0 xzoom -1.0 yzoom 1.0
    chara 'Впереди ещё три источника света'

    jump farmer
