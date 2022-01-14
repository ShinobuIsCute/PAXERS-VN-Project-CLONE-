# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



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


style ita:
    italic True

label cla_1:

    scene cla
    show silhouettes


    "*Background whispering*""Oh my god did you hear about that girl who went missing yesterday?"
    "*Background whispering*""Are you serious? Another one? How long is this going to go on for"
    "*Background whispering*""Maybe she just felt really sick and left the school?"
    "*Background whispering*""The teachers haven’t been doing anything about this! It’s been going on for weeks now! Isn’t this the third girl who has gone missing?"
    "*Background whispering*""If she was sick wouldn’t the teachers have known by now? They are acting like they don’t know anything."
    "*Background whispering*""That’s right, the teachers would’ve called her parents by now. Maybe she isn’t missing?"
    "*Background whispering*""We won’t know for sure unless we ask the teachers!"
    "*Background whispering*""They always say \”It’s private information.\”"

    hide silhouettes
    show mch thinking

    "{i}I wish I could do something. I know I need to do something about this. I don’t want to regret being weak and unable to help like last time. Last time…{/i}"

    scene bvg

    "{i}I was born and raised in a small village. Well, raised until everyone started to disappear. Many families in the village scattered after almost half the population had gone missing. They left and never came back. No letters, phone calls, text messages, nothing. It was like they vanished into thin air. I always regret not being able to do anything for them, who knows what happened to them. {/i}"
    "{i}I...{/i}"
    "{i}I was too young. I couldn’t do anything. I didn’t understand anything.{/i}"

    scene cla
    show mch thinking
    "{i}But this time...{/i}"

    show mch determined
    "{i}This time I can do something!{/i}"

    show mch speaking at left
    show silhouettes at right

    mch"Tell me more, I will try to find the missing girls. Give me all the information you know!"

    "Laughter erupts"

    "From the crowd""Oh yeah? What are you going to do about it? Cast your that one spell you know?"

    "You don't mention that your magical abilites have only awakened recently, and you haven't had time to learn a single spell as this is your first week at school"

    mch"Come on, I just want to help find these students. What if you guys disappear as well?"

    "From the crowd""Aww, that’s so cute, I didn’t know you cared about us so much."

    "Another wave of laughter erupts, and you feel blood rushing to your face"

    scene ocl

    "Mandatory classes end, and you ponder what to do with your spare time"
    "{i}I could try learning a spell. Prove everyone wrong. Well, they're right, but... anyways{/i}"
    "{i}Or I could look around the school, look for clues. Never fails for scooby-doo.{/i}"
    "{i}Hm.... I guess I could sneak into the teachers office to see if I can find something there.{/i}"
    "{i}But if I get caught...{/i}"

    menu :
        "I will..."

        "Go to afterschool tutoring to learn a spell":
            jump lsp_1
        "Investigate around the school":
            jump sch_1
        "Sneak into the teachers office":
            jump tco_1

label lsp_1:
    "You enter the afterschool practice hall"
    "A large, wide corridor appears before you, the white and gold hall gleaming with reflected lights from the crystal chandeliers"
    "The iconic white and gold has always been part of \"school's name\" prestigious image, but you've always found it \"opinion1\""
    "Either side of the hall are lined with strong, thick doors made of dark oak. They seem strangely strong. You see no sign of activity from behind the door, but whenever a door is opened bright flashes of light and sound from people practising their respective magic could be heard."
    "You walk down the hallway until you find an occupied room. Pushing open the door with some effort, you find yourself in a large rectangular room."
    "The room lies dauntingly empty save for the arcane etchings on the wall and floor."
    "The room appears to be both neverending yet cramped at the same time. You squint, trying to judge how far away the rooms are, only to feel more and more disoriented."
    "{i}Spatial Magic. Perhaps I could learn that first{/i}"
    "Some etching on the floor begin to glow, and water flows from them. The swirl until they form human shaped objects."
    "{i}Training dummies. hmmmmm, water magic isn't bad either.{/i}"

    #IDK what the last spell should be so Ill leave this part until later

    jump day_2

label day_2:
    "{i}I need to find out more about this problem before I can understand how to deal with it!{/i}"

        # ... the game continues here.
    nrd "Ow! Hey, stop blocking the doorway! I’m trying to get to my rock climbing class!"
    mch "Your what? I didn’t know we had a rock climbing club at this school."
    nrd "Are you an idiot? Of course we don’t! I said ‘class’ not ‘club’!"
    mch "You mean it’s not inside the school? Don’t go! It’s too dangerous outside right now!"
    nrd "Stop treating me like a kid! I can burn anyone who tries to get in my way, including you!"
    menu:
        "nrd""Stop treating me like a kid! I can burn anyone who tries to get in my way, including you!"

        "Politely ask her not to go":
            jump ch121

        "Let her go and follow her":
            jump ch122

label ch121:

    mch "Please, I don’t even know your name but I really don’t want you to go missing like the others!"
    nrd "I’m Soleil, but seriously just leave me alone. I think you are being a bit too caring for a stranger."
    mch "I just want you to be safe, that’s all."
    "Soleil shows you a test paper with 100\% written on it."
    mch "Ummm"
    nrd "And that’s why you don’t talk to strangers you don’t know well. Sayonara."
    mch "Soleil, wait! I, uh, I didn’t know you were so intelligent! Please forgive me for being an idiot."
    "Soleil is nowhere to be seen. Only a rolling cactus is there to hear your request."
    "{i}Well, it isn’t a surprise that no one wants to talk to me I guess. Maybe I should just go home for today and rest.{/i}"

    jump day_2

label ch122:
    "mch""Ok, I trust you."
    "You watch her leave, but begin to trail her after she has walked a distance"
