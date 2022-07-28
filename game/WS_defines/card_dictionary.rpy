init python:
    #script for assigning id's to card functions
    from cardEffect import draw_one
    
    card_effect_dict = {}
    card_effect_dict[1] = draw_one
    test = card_effect_dict[1]()

    