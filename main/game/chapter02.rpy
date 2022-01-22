label chapter02:

    scene bg black_screen

    "{i}Waking up is such a pain. Maybe something interesting will happen today! That's how I should be thinking, but for some reason…{/i}"
    
    #scene MC house

    "TV" "Another person has gone missing from Asteroth Academy while a missing person in a related case has just been found heavily injured and was recently taken to hospital via helicopter for urgent medical care"
    "{i}I can't let this happen to one of my classmates. I can't handle the regret knowing I could've at least tried to do something. Wait. What time is it? Oh no, I'm going to be late for school! I guess I'll have to skip breakfast to make it there on time.{/i}"

    scene bg classroom with dissolve

    mch "That, must be, a new record, for me."
    mch "No one in the class says a word during the lecture, the atmosphere morbid, like a funeral for an insignificant human"

    "outside of classroom" "~Nyofuuuu~"

    if met_nyf and d1_nyf_clue:
        menu:
            
            "{i}Is that Nyofu? What is she doing here? I should go and talk to her.{/i}":
                jump ch211
            
            "{i}Nyofu told me that there was someone suspicious hanging around afterschool at the old school buildings, I'll go and check them out after classes end today.{/i}":
                jump ch241

    elif met_nyf:
        menu:
            
            "{i}Is that Nyofu? What is she doing here? I should go and talk to her.{/i}":
                jump ch211

    elif met_sol and d1_sol_clue:
        menu:
            
            "{i}What was that? I'm curious to know what kind of animal makes that sound!{/i}":
                jump ch211

            "{i}I should try to find that girl yesterday, maybe she knows something useful? It's lunch break so she will probably be at the cafeteria.{/i}":
                jump ch221
            
            "{i}I should go and investigate the teachers office afterschool, I don't have enough time right now.{/i}":
                jump ch231

    elif met_sol:
        menu:
            
            "{i}What was that? I'm curious to know what kind of animal makes that sound!{/i}":
                jump ch211
                
            "{i}I should try to find that girl yesterday, maybe she knows something useful? It's lunch break so she will probably be at the cafeteria.{/i}":
                jump ch221

    else:
        menu:
            
            "{i}What was that? I'm curious to know what kind of animal makes that sound!{/i}":
                jump ch211
        
label ch211:
    
    scene bg hallway1 with dissolve
    #if statement (has not met Nyofu)
    if not(met_nyf):

        show nyofu cute at center with dissolve:
            zoom 1.5

        mch "Who are you?"
        "???" "Nyofu is Nyofu!"
        mch "You look so cheerful."

        show nyofu sad at center with dissolve:
            zoom 0.75

        nyf "Nyofu is only cheerful on the outside. Nyofu wants to help the missing girls like Nyofu!"
        "{i}I'm not sure about the 'like Nyofu' part...{/i}"
        mch "I'm trying to find some clues about the girls that have gone missing as well. Do you know anyplace that I should go and investigate?"
        nyf "Nyofu thinks you are suspicious. Nyofu thinks Nyofu saw someone suspicious around the old school buildings but not as suspicious as you."
        mch "How am I suspicious? I guess I haven't introduced myself. I'm %(name)s."
        
        show nyofu cute at center with dissolve:
            zoom 1.5
        
        nyf "Nyofu will remember suspicious persons name now, bye bye."
        mch "Thank you for the clue Nyofu!"
        #I could add a zoom out here maybe?? - Pranav
        mch "Wait! Before you go, what's with the halo on your head?"

        show nyofu angry at center:
            zoom 0.75

        nyf "Nyofu's halo and head is Nyofu's secret! Nyofu will tell you when the time is right."

        menu:

            "Apologise to Nyofu for asking a personal question":
                jump ch212
            
            "Tell Nyofu that she looks cute with the halo":
                jump ch213

    #else statement (has met Nyofu)
    else:

        show nyofu cute at center with dissolve:
            zoom 1.5

        mch "Hi, Nyofu. What are you doing around here?"
        nyf "Nyofu thinks you've been sleeping too much."
        mch "What?"
        nyf "{i}(Laughing){/i}"
        mch "I feel like I should've asked this yesterday, why do you have a halo on your head?"

        show nyofu angry at center:
            zoom 0.75

        nyf "Nyofu's halo is Nyofu's secret! Nyofu will tell you when the time is right."

    #end of the if...else...statement 

        menu:

            "Apologise to Nyofu for asking a personal question":
                jump ch212
            
            "Tell Nyofu that she looks cute with the halo":
                jump ch213
label ch212:
    
    mch "I'm sorry, I didn't realise that was a rude question to ask."

    show nyofu cute at center with dissolve:
        zoom 1.5

    nyf "Nyofu forgives you! Nyofu thinks we should do something about these missing people!"

    hide nyofu cute with dissolve

    jump ch241

label ch213:

    mch "I think the halo looks cute on Nyofu, no matter what reason you have it for"
    nyf "Nyofu is very happy to hear that but Nyofu is always cute even without the halo!"
    mch "I can't argue with that!"

    show nyofu sad at center with dissolve:
        zoom 0.75

    nyf "Nyofu thinks we should do something about the missing people! Nyofu was watching TV this morning and it said another person like Nyofu went missing!"
    "{i}“Im not sure about the 'like Nyofu' part…{/i}"
    
    hide nyofu sad with dissolve

    jump ch241

label ch221:

    scene bg canteen with dissolve

    "{i}I look around the canteen and see a slim female figure eating while … reading a book?{/i}"
    
    show soleil happy at center with dissolve:
        zoom 1.7

    if know_sol_name:

        nrd "Ah, the exile from yesterday? Sorry, I've just finished eating."
        mch "Wait! I don’t mind if you don’t want to talk to me, just tell me if you know anything else about the missing girls!"

        show soleil sad at center with dissolve:
            zoom 1.7

        nrd "You do realise you are a very suspicious person? Well whatever, I could see you were earnestly trying to find clues yesterday. Go to the teachers office afterschool, I’ve heard that they occasionally discuss things in regards to missing girls."
        mch "Wait you, you were stalking me? Thank you for the clue anyway, you should tell me where to find you if you want me report back to you."
        
        show soleil happy at center with dissolve:
            zoom 1.7

        nrd "You’ll find me here at lunchtime everyday. Feel free to come and get lectured if you are a masochist."
        "{i}Wow, this girl has a twisted personality.{/i}"
        
        show soleil angry at center with dissolve:
            zoom 1.7

        nrd "You better come back with good information! Otherwise you’ll see me come after you…"
        "Soleil glares angrily at the MC, scaring him into submission."

        hide soleil angry with dissolve

        jump ch231

    #else statement (if MC doesn't know Soleil's name i.e. ch121)
    else:
    
        "???" "Ah, the exile from yesterday? Or should I say stalker? Sorry, I've just finished eating."
        mch "Wait! I don’t mind if you don’t want to talk to me, just tell me if you know anything else about the missing girls!"

        show soleil sad at center with dissolve:
            zoom 1.7

        "???" "You do realise you are a very suspicious person? Well whatever, I could see you were earnestly trying to find clues yesterday. Go to the teachers office afterschool, I’ve heard that they occasionally discuss things in regards to missing girls."
        mch "Wait you, you knew I was following you the whole time? Thank you for the clue anyway, you should tell me your name if you want me to find you again and report back to you."
        
        show soleil happy at center with dissolve:
            zoom 1.7

        "???" "I’m Soleil, part of the arcana class. You’ll find me here at lunchtime everyday. Feel free to come and get lectured if you are a masochist."
        "{i}Wow, this girl has a twisted personality.{/i}"
        
        show soleil angry at center with dissolve:
            zoom 1.7
        
        nrd "You better come back with good information! Otherwise you’ll see me come after you…"
        "Soleil glares angrily at the MC, scaring him into submission."

        hide soleil angry with dissolve

        jump ch231

label ch231:

    scene bg classroom with dissolve

    "As the bell for the final period of the school ends, you casually walk outside the class …"
    
    scene bg hallway1 with dissolve

    "...into the hallway…"

    scene bg teacher with dissolve

    "...and then stand outside the teachers office."

    #scene of inside of teachers office

    "{i}I’ll sneak inside and try to find some clues - maybe a document that hasn’t been shred yet? I’d assume something like that would be near the shredder.{/i}"
    "You sneak inside the teachers office, surprised to notice that there are only two teachers inside."

    "???" "...I’m surprised their meeting is taking so long…"
    "???" "....yes, maybe they are talking about the next…."
    "???" "...I’ve heard from the others…"
    "???" "...there might be an experiment tomorrow after school…"
    "???" "...oh I’ve heard of that too…"
    "???" "...it was going to be in the chem…"
    "???" "...age room if I remember correctly…"

    "{i}I need to make sure I don’t get found, that was definitely confidential information. From what I heard, I would deduce that something is going to happen in the chemistry storage room after school?{/i}"

    menu:
        "Look around the shredder for documents":
            jump ch232
        "Leave the teachers office":
            jump ch233

label ch232:
    "You slowly make your way towards the shredder, as silently as you can. Now that you are next to it, you can see a document with some interesting information written on it."
    "{i}What on earth is this! Another experiment the day after tomorrow in the gym? It’s written here that it will be the first time something like this has ever happened in the school’s history! I have to get out of here and go and train for this.{/i}"
    
    # MC learns a new spell here
    
    jump chapter03

label ch233:

    "{i}I can’t risk getting caught here, otherwise who knows what they’ll do to me! I should get out while they don’t know anything.{/i}"

    scene bg teacher with dissolve
    
    mch "I should go and train for tomorrow, I can’t afford losing this battle!"

    # MC learns a new spell here

    jump chapter03
#
label ch241:
    "You make your way to the old highschool building."

    scene bg oldschool_entrance with dissolve

    "The air is eerie. A dusty wind peaks up as you feel a storm coming."
    "In the distance, a girl leans on one of the pillars at the entrance checking her phone while drinking juice. She looks up and notices you."

    #note: use one of the discarded character designs for this character
    
    show ilana angry at center with dissolve:
        zoom 1.5

    "???" "Hey, you!"
    "???" "Yes, you- the guy looking behind to find someone else."
    "???" "You're not supposed to be wandering around here. What are you doing here?"
    mch "Why are {i}you{/i} here?"
    
    show ilana happy with dissolve:
        zoom 1.5
    
    "???" "Answering a question with a question— not a bad move."
    ila "Name’s Ilana. What’s yours?"

    menu:
        "%(name)s.":
            ila "Nice to meet you, %(name)s. My name is— oh. Nevermind."
            jump ch241_a
        "James. James Bo-":
            ila "Nice try, %(name)s. Even though you don’t know me, I have known about you for a long time."
            "You smile as you find yourself a stalker."
            jump ch241_a

label ch241_a:
    mch "Do you usually hang around here, Ilana?"
    ila "Yeah, mostly."
    mch "Have you seen anything suspicious going around here then?"
    ila "No, not really. Even though this is a huge building, barely anyone comes around these parts."
    ila "I bet you and I are the only ones in this part of the campus right now–"

    #*SWISH/FOOTSTEPS SOUND* 
    """
    A Dark figure dashes through one of the windows on the 5th floor.
    Note: can do a pan-in too.
    Make it short like 0.5 seconds
    """

    mch "Did you see that?"

    ila "What? I didn’t see anything."

    mch "I will talk to you later-"
    ila "…"
    ila "Seeya then!"

    hide ilana happy with dissolve

    "You race inside the old school building and make your way upto the fifth floor."

    "{i}Someone was recently here. This place reeks of earth.{/i}"

    jump cha241_b


label cha241_b:
    scene bg oldschool_hallway with dissolve
    "Roll a d20 to make a perception check."
    python:
        import random
        d20 = random.randrange(0, 20)
    "You rolled a %(d20)s."

    if d20 < 10:
        "Your mind gets overwhelmed by the number of doors you see ahead. With no idea in mind, you check each door one by one."
        $cha241Count = 5
        label cha241Loop:
            if cha241Count == 10:
                jump cha242_HOT
            else:
                $ cha241Count += 1
                "After trying %(cha241Count)s doors, you still feel like this is not going anywhere."
                menu:
                    "Check the next door":
                        jump cha241Loop
                    "Make a plan":
                        "You sit down on the dirty floor and meditate."
                        "Time slows down"
                        "You get up with gleaming eyes."
                        jump cha242

    else:
        jump cha242

    

label cha242:
    "You run along each door gently touching each doorknob you come across with your sensitive elbow."
    "First knob cold. Second knob cold. Third knob also cold…"
    
    "Having studied thermodynamics in your previous school, you know that if a door was recently touched by a living being, one of the bronze knobs should be slightly warmer than the rest."

    "Also with the fact that these knobs are old and the user must have had to hold it for a while before being able to open the door, you are sure that you will find the door that leads to the suspicious person."

    "{i}Several doors later...{/i}"

label cha242_HOT:

    "A HOT KNOB!"

    "Finally."
    "You try to open the knob but it’s locked. You decide to…"

label cha242_a:
    menu: 
        "Kick it down.":
            "The door doesn’t even budge."
            jump cha242_a
        "Use a plant spell":
            "You conjure a seed inside the lock, then growing it, the lack of space inside means the plant forces its way outwards, breaking the lock."
            jump cha242_b
        "Use a water spell":
            "You conjure some water and move it around the lock randomly until you hear a click, to which you find you have unlocked the door."
            jump cha242_b
        "Use telekinesis":  
            "Using telekinesis, you try to shift some parts until the lock clicks, you put your hand on the door knob and it opens."
            jump cha242_b

label cha242_b:
    scene oldschool_room with dissolve
    "The room is mostly dark, except some light that floods in from an open window."
    "All the windows of the room have been boarded up, except one."    
    "Winds swish in and out as papers ruffle on top of table weighted on by a big stone."    
    "Some papers fly off out to the window. You dash in and try to hold the remaining papers left on the table."    
    "With one hand on the papers, you stretch your leg and close the door. The wind stops."    
    "You look carefully onto the papers."    
    "You try to read it but the text is ancient and you can hardly decipher it."    
    "In one of the papers, you can see some instructions, though you don't understand most of it."    
    "Another page has some golem drawings."    
    "From your understanding, the pages tell you how to transmute earth golems out of rock."    
    "You fold the papers and put them in your pocket."    
    "You make your way to the open window."    
    "(inner thought)" "What kind of guy would jump out of a fifth floor just to escape me?"    
    "As you look down through the window, you see Ilana heading off to the main school building."
    "She looks up."

    show ilana sad at left with dissolve:
        zoom 0.8

    ila "..."
    mch "......"
    ila "..............."

    show ilana happy at left with dissolve:
        zoom 0.8

    menu:

        ".........................":    
            ila "{i}waves her hand and smiles.{/i}"

    jump chapter03

