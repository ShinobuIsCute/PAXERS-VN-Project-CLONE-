label chapter01:

    scene bg classroom with dissolve
    show silhouettes

    play music normalDaySchool
    "*Background whispering*""Oh my god did you hear about that girl who went missing yesterday?"
    "*Background whispering*""Are you serious? Another one? How long is this going to go on for?"
    "*Background whispering*""Maybe she just felt really sick and left school?"
    "*Background whispering*""The teachers haven’t been doing anything about this! It’s been going on for weeks now! Isn’t this the third girl who has gone missing?"
    "*Background whispering*""If she was sick, wouldn’t the teachers have known by now? They are acting like they don’t know anything."
    "*Background whispering*""That’s right, the teachers would’ve called her parents by now. Maybe she isn’t missing?"
    "*Background whispering*""We won’t know for sure unless we ask the teachers!"
    "*Background whispering*""I tried many teachers. They always say \”It’s private information.\”"

    hide silhouettes
    show mch thinking

    stop music fadeout 1.0

    "{i}I wish I could do something. I need to do something about this. I don’t want to regret being weak and unable to help like last time. Last time…{/i}"

    scene bg village with flash
    play music flashback

    "{i}I was born and raised in a small village. Well, raised until everyone started to disappear. Many families in the village scattered after almost half the population had gone missing. They left and never came back. No letters, phone calls, text messages, nothing.{/i}"
    "{i}It was like they vanished into thin air. I always regret not being able to do anything for them, who knows what happened to them. {/i}"
    "{i}I...{/i}"
    "{i}I was too young. I couldn’t do anything. I didn’t understand anything.{/i}"

    scene bg classroom with flash
    show mch thinking

    stop music fadeout 1.0
    play music normalDaySchool
    "{i}But this time...{/i}"

    show mch determined
    "{i}This time I can do something!{/i}"

    show mch speaking at left
    show silhouettes at right

    mch"Tell me more, I will try to find the missing girls. Give me all the information you know!"

    play sound "audio/cat.mp3"
    "Laughter erupts"

    "From the crowd""Oh yeah? What are you going to do about it? Cast the only spell that you know?"

    "You don't mention that your magical abilites have only awakened recently, and you haven't had time to learn a single spell as this is your first week at school"

    mch"Come on, I just want to help find these students. What if you guys disappear as well?"

    "From the crowd""Aww, that’s so cute, I didn’t know you cared about us so much."

    "Another wave of laughter erupts, and you feel blood rushing to your face"

    scene bg hallway1 with dissolve

    "Mandatory classes end, and you ponder what to do with your spare time"
    "{i}I could try learning a spell. Prove everyone wrong. Well, they're right, but... anyways{/i}"
    "{i}Or I could look around the school, look for clues. Never fails for scooby-doo.{/i}"
    "{i}Hm.... I guess I could sneak into the teachers office to see if I can find something there.{/i}"
    "{i}But if I get caught...{/i}"

    menu:
        "I will..."

        "Go to afterschool tutoring to learn a spell":
            jump lsp_1
        "Investigate around the school":
            jump sch_1
        "Sneak into the teachers office":
            jump tco_1

label lsp_1:
    scene bg hallway2 with dissolve
    stop music fadeout 1.0
    play music trainingRoomTheme
    "You enter the afterschool practice hall"
    "A long, narrow corridor appears before you, the white and gold hall gleaming with reflected lights from the high-ceiling lamps."
    "The iconic white and gold has always been part of Asteroth Academy's prestigious image, yet you've always found it ugly."
    "One side of the hall is lined with strong, thick doors made of dark oak. They seem strangely strong."
    "You see no sign of activity in the corridor, but whenever a door is opened bright flashes of light and sound from people practising their respective magic can be heard."

    scene bg training_room with dissolve
    "You walk down the hallway until you find an unoccupied room. Pushing open the door with some effort, you find yourself in a large rectangular room."
    "The room lies dauntingly empty save for the arcane etchings on the wall and floor."
    "The room appears to be both neverending yet cramped at the same time. You squint, trying to judge how far away the rooms are, only to feel more and more disoriented."
    "{i}Spatial Magic. Perhaps I could learn that first{/i}"
    "Some etching on the floor begin to glow, and water flows from them. The swirl until they form human shaped objects."
    "{i}Training dummies. hmmmmm, not bad. Not bad at all.{/i}"

    #IDK what the last spell should be so Ill leave this part until later

    jump chapter02

label sch_1:

    #flag
    $ met_sol = True

    "{i}I need to find out more about this problem before I can understand how to deal with it!{/i}"

        # ... the game continues here.
    show soleil angry at center:
        zoom 1.7

    "???" "Ow! Hey, stop blocking the doorway! I’m trying to get to my rock climbing class!"
    mch "Your what? I didn’t know we had a rock climbing club at this school."
    "???" "Are you an idiot? Of course we don’t! I said ‘class’ not ‘club’!"
    mch "You mean it’s not inside the school? Don’t go! It’s too dangerous outside right now!"
    "???" "Stop treating me like a kid! I can burn anyone who tries to get in my way, including you!"
    
    menu:
        "???""Stop treating me like a kid! I can burn anyone who tries to get in my way, including you!"

        "Politely ask her not to go":
            jump ch121

        "Let her go and follow her":
            jump ch122

label ch121:

    #flag
    $ know_sol_name = True

    show soleil angry at center with dissolve:
        zoom 1.7

    mch "Please, I don’t even know your name but I really don’t want you to go missing like the others!"
    "???" "I’m Soleil, but seriously just leave me alone. I think you are being a bit too caring for a stranger."
    mch "I just want you to be safe, that’s all."
    "Soleil shows you a test paper with 100\% written on it."
    mch "Ummm"
    nrd "And that’s why you don’t talk to strangers you don’t know well. Sayonara."
    mch "Soleil, wait! I, uh, I didn’t know you were so intelligent! Please forgive me for being an idiot."

    hide soleil angry with dissolve

    "Soleil is nowhere to be seen. Only a rolling cactus is there to hear your request."
    "{i}Well, it isn’t a surprise that no one wants to talk to me I guess. Maybe I should just go home for today and rest.{/i}"

    jump chapter02

label ch122:

    #flag
    $ d1_sol_clue = True

    show soleil angry at center:
        zoom 1.7

    mch "Ok, I trust you."

    hide soleil angry with dissolve

    "You follow her to the rock climbing class"
    "You watch her leave, but begin to trail her after she has walked a distance"
    "While following the girl, you hear other students talking about suspicious activity"
    "{i}Wait, what are they talking about? A suspicious person lurking around the school?{/i}"
    "{i}I need to find this person and interrogate them! They said this person hangs around afterschool near the teachers office?{/i}"
    "{i}Guess I’ll go and investigate that tomorrow.{/i}"

    show soleil angry at center with dissolve:
        zoom 1.7

    mch "WAIT, ITS NOT WHAT YOU THINK!"
    "{i}I found myself staring at that girl's face once again. She found out I had been following her.{/i}"
    "???" "Disgusting. Repulsive. Abhorrent."
    mch "I just want to find out more about these girls going missing, and it just so happened that I was following you."
    "???" "Who would believe such a xxxxx story"
    mch "I promise! I just found out that there is a suspicious person who hangs around the teachers office afterschool!"
    "???" "Well either way, you admitted to be following me. You’re lucky I’m also interested in finding out who is behind all the missing girls. Thanks for the information. I hope it’s not who I think it is though."
    mch "Uh, you’re welcome?"
    "???" "Can’t you tell when someone is being sarcastic!"

    hide soleil angry with dissolve

    "The girl scurries off into the distance."
    "{i}I got a good amount of information today, I think we can call that a success!{/i}"
    #Who tf added this line??? " You know there is a suspicious person, and you have met a love interest, Soleil!"
    jump chapter02

label tco_1:
    
    #flag
    $ met_nyf = True

    "{i}Maybe I can get some information if I listen to what the teachers are talking about.{/i}"
    "You go closer to the door and crouch down next to it"

    scene bg teacher with dissolve

    "{i}I can’t hear much from here. Maybe I should sneak inside and try to find something relevant in the teachers office.{/i}"
    "Someone falls onto you!"

    show nyofu sad at center with hpunch:
        zoom 0.75

    "???" "Ahhh! Errr, uhh, eeeeeeee!"
    mch "Shhhhh!"
    "You look at the perpetrator, a girl who looks like she is at the verge of tears"
    mch "Let’s whisper here, ok?"

    show nyofu cute:
        zoom 1.5

    "???" "Shh! Ok, Nyofu understand!"
    mch "Well you are clearly being too loud..."
    "Background" "Is someone there?"
    "You take Nyofu’s hand and run down the hallway"

    scene bg hallway1 with dissolve
    
    mch "Um, sorry about before, I’m %(name)s. What's your name?"
    nyf "Nyofu! Nyofu think’s your hand is warm. Nyofu think’s your hand is a bit sweaty."

    menu :
        "Try to explain the situation to Nyofu":
            jump ch131

        "Tell Nyofu your hand wasn’t sweaty!":
            jump ch132

label ch131:

    #flag
    $ d1_nyf_clue = True

    scene bg hallway1 with dissolve

    show nyofu cute at center:
        zoom 1.5

    mch "Nyofu, I’m sure you know about the girls that are going missing. I’m here to try and get some information so I can find out where to look for these girls, or maybe something about the suspects."
    nyf "Nyofu thinks you are doing the right thing! Nyofu still doesn’t know why %(name)s's hand was sweaty..."
    mch "Uh, that was um..."
    nyf "Nyofu thinks %(name)s has tried very hard today! Maybe that's why %(name)s's hand was sweaty."
    mch "Wow! Nyofu you are so smart!"
    "{i}Wow, how can a girl be this dense? Well, I guess it’s for the better.{/i}"
    mch "I still need to get some more information, I haven’t found enough for today!"
    nyf "Nyofu thinks there might be a suspicious person in the school. Nyofu has seen this suspicious person trespassing on the old school buildings immediately afterschool more than once!"
    mch "You think it might be someone from the school? I guess I will take a look around the old school buildings tomorrow."

    hide nyofu cute
    show nyofu angry at center:
        zoom 0.75

    nyf "Nyofu thinks you would have to be trespassing to get to the old school buildings..."
    mch "Nyofu, you are right. Unfortunately, I have to do this. I can’t let my past demons keep me locked up in their grasp for my lifetime, I have to do as much as I can, so I don’t regret anything afterwards."
    nyf "Nyofu thinks you might be the suspicious person..."
    mch "What? How? I’m not suspicious!"
    
    hide nyofu angry
    show nyofu cute at center:
        zoom 1.5

    "You and Nyofu start laughing."

    jump chapter02

label ch132:

    scene bg hallway1 with dissolve
    
    show nyofu_cute at center:
        zoom 1.5

    mch "My hand wasn’t sweaty at all!"
    nyf "....."
    mch "Anyway, I need information on the girls that have recently gone missing from this school."
    nyf "Nyofu thinks %(name)s is a philanderer."
    mch "No, no, Nyofu I just want to help them. I should try and become better at my magic skills! Nyofu, can you teach me your magic spell?"
    nyf "Nyofu can help you learn a new magic spell!"

    #MC LEARNS A NEW ICE SPELL HERE!!!

    scene bg training_room with dissolve

    jump chapter02