init:
    image effects pool:
        'ripple1'
        pause 1.0
        'ripple2'
        pause 1.0
        repeat

    # XXX: for some reason, not equivalent to image bg pool = Tile('tile pool', size=(2200, 1097 * 2))
    image bg pool = im.Tile('cg/pool/tile pool.png', size=(2200, 1097 * 2))

init:
    $ screen_left = Position(xalign=0.1, yalign=1.0)
    $ screen_right = Position(xalign=0.9, yalign=1.0)
    $ more_right = Position(xalign=1.1, yalign=1.0)
    $ character_right = Position(xalign=0.7, yalign=1.0)
    $ character_left = Position(xalign=0.3, yalign=1.0)
    $ image_place = Position(xalign=1.0, yalign=0.4)
    $ puddle = Position(xalign=1.0, yalign=0.7)

