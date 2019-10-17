# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Max the Pear")
define angrym = Character("Max the Angry Pear", what_color = "#ffcccc", who_color = "cccffc")

# The game starts here.

label start:
    play music "The Ultimate Showdown of Ultimate Destiny copy.mp3"
    scene bird

    transform slightleft:
        xalign 0.25
        yalign 0.5

    image pear = "pear.jpg"
    show pear at slightleft

    # These display lines of dialogue.

    m "Hey there I am Max the pear."
    m "I bet that {b}you{/b} think you can date me."

    python:
        playerName = renpy.input("But first, you are going to have to tell me your name")
        playerName = playerName.strip() or "Shy boi"
        if (playerName == "Shy boi"):
            flag = True
        else:
            flag = False

    if flag:
        jump shy
    else:
        jump norm
    label shy:
        m "Fine, if you dont want to tell me your name then I'll just call you [playerName]"
        jump continue1
    label norm:
        m "Well thats a weird name [playerName]"
    label continue1:

    m "Well I believe it is time for you to see my true {i}open{/i} form."

    image pear rotated = Transform("pear", rotate=45)
    show pear rotated at slightleft

    angrym "lol u thought I would become human but jk im just rotated"

    return
