label chapter02:

    "{i}Waking up is such a pain. Maybe something interesting will happen today! That's how I should be thinking, but for some reason…{/i}"
    
    #scene MC house

    "TV" "Another person has gone missing from Asteroth Academy while a missing person in a related case has just been found heavily injured and was recently taken to hospital via helicopter for urgent medical care"
    "{i}I can't let this happen to one of my classmates. I can't handle the regret knowing I could've at least tried to do something. Wait. What time is it? Oh no, I'm going to be late for school! I guess I'll have to skip breakfast to make it there on time.{/i}"

    #scene MC classroom

    mch "That, must be, a new record, for me."
    mch "No one in the class says a word during the lecture, the atmosphere morbid, like a funeral for an insignificant human"

    "outside of classroom" "~Nyofuuuu~"

    menu:

        #if statement (has not met Nyofu i.e. ch111 or ch121 or ch122)
        "{i}What was that? I'm curious to know what kind of animal makes that sound!{/i}":
            jump ch211

        #else statement (has met Nyofu i.e. ch131 or 132)
        "Is that Nyofu? What is she doing here? I should go and talk to her.":
            jump ch211
            #
        #if statement (met Soleil i.e. ch121 or ch122) !!! make sure the statement takes into account the Soleil/(that girl yesterday) part
        #
        "I should try to find Soleil/(that girl yesterday), maybe she knows something useful? It's lunch break so she will probably be at the cafeteria.":
            jump ch221

        #if statement (met Soleil + clue i.e. ch122)
        "{i}I should go and investigate the teachers office afterschool, I don't have enough time right now.{/i}":
            jump ch231

        #if statement (met Nyofu + clue i.e. ch131)
        "{i}Nyofu told me that there was someone suspicious hanging around afterschool at the old school buildings, I'll go and check them out after classes end today.{/i}":
            jump ch241

label ch211:
    #

    #if statement (has not met Nyofu)

    mch "Who are you?"
    "???" "Nyofu is Nyofu!"
    mch "You look so cheerful."
    nyf "Nyofu is only cheerful on the outside. Nyofu wants to help the missing girls like Nyofu!"
    "{i}I'm not sure about the 'like Nyofu' part...{/i}"
    mch "I'm trying to find some clues about the girls that have gone missing as well. Do you know anyplace that I should go and investigate?"
    nyf "Nyofu thinks you are suspicious. Nyofu thinks Nyofu saw someone suspicious around the old school buildings but not as suspicious as you."
    mch "How am I suspicious? I guess I haven't introduced myself. I'm %(name)s."
    nyf "Nyofu will remember suspicious persons name now, bye bye."
    mch "Thank you for the clue Nyofu!"
    mch "Wait! Before you go, what's with the halo on your head?"
    nyf "Nyofu's halo and head is nyofu's secret! Nyofu will tell you when the time is right."
    #else statement (has met Nyofu)

    mch "Hi, Nyofu. What are you doing around here?"
    nyf "Nyofu thinks you've been sleeping too much."
    mch "What?"
    nyf "{i}(Laughing){/i}"
    mch "I feel like I should've asked this yesterday, why do you have a halo on your head?"
    nyf "Nyofu's halo is nyofu's secret! Nyofu will tell you when the time is right."

    #end of the if...else...statement 

    menu:

            "Apologise to Nyofu for asking a personal question":
                jump ch212
            
            "Tell Nyofu that she looks cute with the halo":
                jump ch213
label ch212:
    
    mch "I'm sorry, I didn't realise that was a rude question to ask."
    nyf "Nyofu forgives you! Nyofu thinks we should do something about these missing people!"

    jump ch241

label ch213:

    mch "I think the halo looks cute on Nyofu, no matter what reason you have it for"
    nyf "Nyofu is very happy to hear that but Nyofu is always cute even without the halo!"
    mch "I can't argue with that!"
    nyf "Nyofu thinks we should do something about the missing people! Nyofu was watching TV this morning and it said another person like Nyofu went missing!"
    "{i}“Im not sure about the 'like Nyofu' part…{/i}"
    
label ch231:

#
label ch241:
    "You make your way to the old highschool building."

    scene bg oldschool_entrance    

    "The air is eerie. A dusty wind peaks up as you feel a storm coming."
    "In the distance, a girl leans on one of the pillars at the entrance checking her phone while drinking juice. She looks up and notices you."

    #note: use one of the discarded character designs for this character    
    "(random girl)" "Hey, you!"
    "(random girl)" "Yes, you- the guy looking behind to find someone else."
    "(random girl)" "You are not supposed to be wandering around here. What are you doing here?"
    mch "Why are {i}you{/i} here?"
    "(girl)" "Answering a question with a question— not a bad move."
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


    "You race inside the old school building and make your way upto the fifth floor."

    "{i}Someone was recently here. This place reeks of earth.{/i}"

    jump cha242_b


label cha241_b:
    scene bg oldschool_hallway
    "Roll a d20 to make a perception check."
    python:
        import random
        d20 = random.randrange(0, 20)
    "You rolled a %(d20)s."

    if d20 < 10:
        "Your mind gets overwhelmed by the number of doors you see ahead. With no idea in mind, you check each door one by one."
        $cha241Count = 0
        label cha241Loop:
            if cha241 == 5:
                jump cha242
            else:
                $ cha241Count += 1
                "After trying %(cha241Count+5) doors, you still feel like this is not going anywhere."
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

    "{i}Several doors later..."

    "A HOT KNOB!"

    "Finally."
    "You try to open the knob but it’s locked. You decide to…"

label cha242_a:
    menu: 
        "Kick it down.":
            "The door doesn’t even budge."
            jump cha242_a
        "Use plant spell":
            "You conjure a seed inside the lock, then growing it, the lack of space inside means the plant forces its way outwards, breaking the lock."
            jump cha242_b
        "Use water spell":
            "You conjure some water and move it around the lock randomly until you hear a click, to which you find you have unlocked the door."
            jump cha242_b
        "Use telekinesis":  
            "Using telekinesis, you try to shift some parts until the lock clicks, you put your hand on the door knob and it opens."
            jump cha242_b

label cha242_b:
    scene oldschool_room
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

    ila "..."
    mch "......"
    ila "..............."
    menu:
        ".........................":
            ila "{i}waves her hand and smiles.{\i}"



