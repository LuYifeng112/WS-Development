# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define var = 1

# The game starts here.

label start:
    e "[test]"
    $ var += 1
    e "[var]"
    jump combat_init #see code in vscode://game/WS_defines/combat.rpy.rpy:87:4

    return
