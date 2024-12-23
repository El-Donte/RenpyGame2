label bus:
    scene bg buswindow with fade
    
    show chara calm at screen_left with easeinleft
    chara '''
        Как же хорошо и беззаботно в деревне...

        Я увижусь со старыми друзьями, с которыми провёл своё детство. 

        Всё это так странно, будто ещё вчера я писал увлекательные сценарии для летних концертов в этом забытом Богом местечке...
        '''
    show chara idea:
            zoom 1.2
    chara "{b}А ведь я правда неплох в этом!{/b}"

    show chara calm:
            zoom 1.0
    chara "Пейзаж за окном значительно изменился, мне кажется или я сел не в тот автобус?"
    extend "Куда делись все люди, почему я здесь один?"

    menu:
        "1.Спросить водителя, правильный ли это автобус":
            jump bus_driver

        "2.Попытаться отвлечься от плохих мыслей и уснуть":
            jump bus_distract

    

label bus_driver:

    # scene bg busdriver
    show bg businter with dissolve
    show chara calm at screen_left with easeinleft
    show skelet at right with easeinright
    chara "Извините, этот автобус идёт до деревни Париж?"

    
    skelet "Нет, мальчик, тебе пока рано знать в какое место доставит тебя этот автобус"
    show skelet smilechair with dissolve
    show chara scared with dissolve
    skelet "И вообще, правильно люди говорят: «Меньше знаешь, крепче спишь»"
    
    scene bg businter with fade
    '''
    Вы доковыляли дрожащими ногами. От увиденного и услышанного оставшуюся часть поездки вы провели в страхе,

    вас пугали мысли о будущем, и правда куда же ведёт этот автобус, пока остаётся загадкой
    '''

    show skelet smile at screen_right with easeinright:
            linear 0.0 xzoom -1.0 yzoom 1.0
            zoom 1.2
        
    show chara scared at screen_left with easeinleft
    skelet "Парень, твоя остановочка"

    chara "Что это за место? Что мне тут делать?"

    skelet  '''
            Наслаждайся, это место особенное, ты сам должен понять, что тебе нужно сделать,

            покажи свои лучшие черты, прояви фантазию, может и получится вернуться обратно живым
            '''

    chara "Где я? Почему уезжает автобус? Стой! Не бросай меня Здесь!"

    jump strange_world

label bus_distract:

    scene black with fade
    '''
    Вы спали до конца поездки, думаете это не представляет никакой опасности? 

    Как же вы ошибаетесь... Ведь последняя остановка этого автобуса ужасающий лес, 

    из которого вам и придётся выбираться.
    '''
    scene bg businter with fade

    show skelet fury at center:
            linear 0.0 xzoom -1.0 yzoom 1.0
            zoom 1.2
    skelet 'Доброе утро, выспался?'

    show skelet smile at center:
            linear 0.0 xzoom -1.0 yzoom 1.0
            
    extend  '''
            Молодец, конечно, что уснул в незнакомом загадочном месте, тебя же этому мама учила?  

            Твоя остановочка ужасающий лес, отдыхай, кайфуй, можешь ещё поспать
            '''

    jump strange_world