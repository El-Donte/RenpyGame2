$ developerBool = False

label developer:
    scene bg forest2

    show chara withligth at screen_left with easeinleft
    chara 'Свет всё ближе и ближе, здесь кто-нибудь есть?'

    show terminal light at screen_right with easeinright:
        linear 0.0 xzoom -1.0 yzoom 1.0
        zoom 1.2
    
    show chara question
    chara "Это терминал?"

    extend "Стоит ли нажимать кнопку на терминале?"

    menu:
        "1. Да":
            scene bg comp2 with fade

            chara "Где я? Здесь кто-нибудь есть?"
            show chara sad at screen_left with easeinleft
            chara "У меня от яркости сейчас глаза выпадут. Я что в раю?"
            show chara angry
            chara "Видимо зря я нажал кнопку на том автомате, мне теперь не выбраться отсюда!"

            show bg comp with dissolve
            show dev calm at screen_right with easeinright:
                zoom 1.1

            dev 'Не думал, что кто-нибудь найдёт меня в этой глуши, как твоё имя?'

            show chara calm
            chara 'Ты меня нупагал, Я Саша, попал в этот ужасающий лес из-за случайных обстоятельств'

            show dev tired
            dev '''
                Здравствуй, Саша, я программист Никита. 

                Не вовремя ты меня встретил, конечно, я разрабатываю игру и третий день уже пытаюсь подобрать эмоции персонажа под реплики. 

                Я уже просто не справляюсь, путаница какая-то...
                '''
            

            menu:
                'Могу ли я взглянуть на эту задачу и помочь тебе?':
                    $ developerBool = True

                    #мини игра
                    show chara happy at screen_left with easeinleft
                    show dev happy at screen_right with easeinright

                    dev 'Спасибо тебе за помощь! Раз уж я теперь освободился, давай я присоединюсь к твоему путешествию, может и я тебе помогу!'

                    chara 'Давай вместе отправимся в путь, следующий источник свете недалеко!'

                    scene bg forest
                    show chara happy at screen_left with easeinleft
                    show dev assend at screen_right with easeinright:
                            linear 0.0 xzoom -1.0 yzoom 1.0
                            zoom 1.2
                    dev "{b}Наконец-то свобода{/b}"
                    show chara question
                    chara "Что ?"
                    show dev love
                    dev "Ничего)"

                    jump knight_dev

                'Пока, Никита, я дольше пошёл, ты мне не сможешь помочь, поэтому тебе я помогать тоже не буду!':
                    jump kinght

        "2. Нет":
            chara "Не буду лучше рисковать, пойду дальше на свет"
            jump kinght
    
           

    