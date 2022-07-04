init python:
    import classes as f
    player = f.Player("Fang", (10,10,10))
    devlog.info("Player Created")
    boss_miss = 0
    boss_miss_continous = 0

label combat_init:
    
    # Anything to set up the combat will be established in this label

    #Damage Control Variables
    $renpy.block_rollback() #will block going to previous dialogue or exiting out of the combat, useful against cheats and save control
    $ _skipping = False #Need to also make sure players don't just cycle through combat labels and make it skip or softlock anything.

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
    #Since a boss is AI, this will need to become dynamic, either that or we should prepare to hardcode all bosses
    random:
        block:
            $ player.updateVitality(-3)
            $ devlog.info("PLayer lost 3 vitality, now has "+str(player.vitality)+" vitality")
            "[player.vitality]"
            $ boss_miss_continous = 0
        weight 0.5 block: #Need to find a way to make weights, dynamic, TODO: Parser fix
            "The Boss has missed the target."
            $ boss_miss += 1
            $ devlog.info("Boss has missed, total misses: "+str(boss_miss))
            $ boss_miss_continous += 1
            $ devlog.info("Boss has missed consecutively: "+str(boss_miss_continous)+" times.")
    #Check for Player Alive or Not
    #Will always run after the effect is done
    if player.vitality <= 0:
        jump combat_end_player_dead
    
    jump combat_player

label combat_player:
    #Similar to label combat_boss but variable is boss not player.
    "Player Strike"

    jump combat_boss


label combat_end_player_dead:
    "You have Died"
    "Shinoobi Execution"
    "Git Gud"
    $ devlog.critical("--Simulation Ended--")