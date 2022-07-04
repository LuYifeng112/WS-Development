init python:
    import classes as f
    player = f.Player("Fang", (10,10,10))

label combat_init:
    
    # Anything to set up the combat will be established in this label
    $renpy.block_rollback() #will block going to previous dialogue or exiting out of the combat, useful against cheats and save control

    jump combat_startup_probability


label combat_startup_probability:
    #This label will randomly select who starts first
    random: #Random Parser, see code in vscode://game/WS_defines/CDD-Apperance.rpy:87:4
        block: #Block Parser, see code in vscode://game/WS_defines/CDD-Apperance.rpy:135:4
            "The Boss Goes First"
            jump combat_boss
        block:
            "You Go First!"
            jump combat_player


label combat_boss:
    "Boss Strike"
    random:
        block:
            $ player.updateVitality(-3)
            "[player.vitality]"
        block:
            "The Boss has missed the target."

label combat_player:
    "Player Strike"
