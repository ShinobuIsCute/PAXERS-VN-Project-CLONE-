# The script of the game goes in this file.
#test

#Attempting to add the images
image nyofu cute = "nyofu_cute.png"
image nyofu sad = "nyofu_sad.png"
image nyofu angry = "nyofu_angry.png"
image soleil happy = "soleil_happy.png"
image soleil sad = "soleil_sad.png"
image soleil angry = "soleil_angry.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg classroom = "bg classroom.jpg"
image bg canteen = "bg canteen.jpg"
image bg hallway1 = "bg hallway 2.5.jpg"
image bg hallway2 = "bg hallway narrow.jpg"
image bg teacher = "bg teacher's door.jpg"
image bg village = "bg village.jpg"


init:

    define mch = Character("[name]", color = "#808080")
    define tch = Character("Mr Jaffa", color = "#0000ff")
    define nrd = Character("Soleil", color = "#ff0000")
    define nyf = Character("Nyofu", color = "ffffff")

label start:
    python:
        spells = [0] * 10
        for i in range(10):
            print(spells[i])
    python:
        name = renpy.input("What is your name?")
        name = name.strip() or "The Nameless One"

    jump chapter01

