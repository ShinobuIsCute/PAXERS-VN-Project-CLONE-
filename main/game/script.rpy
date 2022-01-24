# The script of the game goes in this file.
#randomcomment
#Attempting to add the images
image nyofu cute = "nyofu_cute.png"
image nyofu sad = "nyofu_sad.png"
image nyofu angry = "nyofu_angry.png"

image soleil happy = "soleil_happy.png"
image soleil sad = "soleil_sad.png"
image soleil angry = "soleil_angry.png"

image ilana happy = "ilana_happy.png"
image ilana sad = "ilana_sad.png"
image ilana angry = "ilana_angry.png"

#Fixing the image issues + custom transitions stuff will go here
#defining custom flash transition
define flash = Fade(0.1, 0.0, 0.5, color='#fff')

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg black_screen = "black screen.jpg"
image bg classroom = "bg classroom.jpg"
image bg canteen = "bg canteen.jpg"
image bg hallway1 = "bg hallway 2.5.jpg"
image bg hallway2 = "bg hallway narrow.jpg"
image bg teacher = "bg teacher's door.jpg"
image bg village = "bg village.jpg"
image bg oldschool_entrance = "bg old school entrance.jpg"
image bg training_room = "bg training room.jpg"
image bg oldschool_hallway = "bg old school hallway.jpg"
image bg oldschool_room = "bg old school room.jpg"

init:

    define mch = Character("[name]", color = "#808080")
    define tch = Character("Mr Jaffa", color = "#0000ff")
    define nrd = Character("Soleil", color = "#ff0000")
    define nyf = Character("Nyofu", color = "#ffffff")
    define ila = Character("Ilana", color="#9339cf")

    define normalDaySchool = "audio/music/normal day in the school.mp3"
    define insideTeacherOffice = "audio/music/inside the teachers office.mp3"
    define oldSchoolBuilding = "audio/music/old school buildings.mp3"
    define trainingRoomTheme = "audio/music/training room theme.mp3"
    define flashback = "audio/music/flashback.mp3"
    define sadatFav = "audio/music/main menu.mp3"
    
    #initialising flags
    default met_nyf = False 
    default met_sol = False
    default d1_nyf_clue = False
    default d1_sol_clue = False
    default know_sol_name = False

label start:
    python:
        spells = [0] * 10
        for i in range(10):
            print(spells[i])
    python:
        name = renpy.input("What is your name?")
        name = name.strip() or "The Nameless One"

    jump chapter01