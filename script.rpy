define flash = Fade(.25, 0, .75, color="#fff")
define menudissolve = Dissolve(1.0)
define slowdissolve = Dissolve(2.0)
define mc = Character("[name]")
define skill = Character("Skill")
define gender = ("")
# The game starts here.

label start:

    stop music

    scene black
    with menudissolve
    pause 1.0

python:
#    name = renpy.input("What's your name?")
#    name = name.strip()

#    if not name:
#        name = "MC"

#    menu gender:

#        "Are you male or female?"

#        "Male":
#            jump gender_m

#        "Female":
#            jump gender_f

#    label gender_m:
#        $ gender = "male"

#        jump gender_done

#    label gender_f:
#        $ gender = "male"

#        jump gender_done:

#    menu:

#        "Are you [gender]?"

#        "Yes":
#            "Cool."

#        "No":
#            jump gender

    pause 1.0

    play sound "audio/alarm.ogg"

    pause 2.0

    "I wake up, groaning and checking my alarm clock."

    stop sound

    pause 0.2

    "It's 7:40."

    scene bedroom
    with slowdissolve

    pause 0.5

    "Ugh... 5 minutes more can't hurt anybody..."

    pause 0.3

    "Yea... Just 5 minutes more..."

    scene black
    with slowdissolve

    pause 1.0

    play sound "audio/phone_vibrate.ogg"

    pause 2.0

    scene bedroom
    with slowdissolve

    "Checking again the clock"

    stop sound

    "its 8:00"

    "Fuck my god damn life, at this rate i'll be late on my first day."

    pause 0.2

    mc "Man..."

    menu:

        "I really should..."

        "Sleep 5 minutes more.":
            jump choice1_sleep

        "Get up.":
            jump choice1_get_up

        "This bed is...":
            jump choice1_poland

    label choice1_sleep:

        $ choice1_sleep = "true"

        mc "Who needs to study anyways..."

        scene black
        with slowdissolve

        pause 3.0

        play sound"audio/you_died.ogg"
        show youdied:
            xalign 0.5
            yalign 0.5
        with slowdissolve
        pause 3.0
        hide youdied
        with slowdissolve
        pause 2.0
        stop sound

        "I'm the one who's gonna be dead if i can't make it at time to school."

        pause 2.0

        mc "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

        scene bedroom
        with dissolve

        play sound"audio/blanket.ogg"

        "Painfully i get up and starts preparing myself."

        pause 0.5
        stop sound

        scene bedroom
        with fade

        pause 0.5

        mc "It's 8:15 already? Fuck my life."

        jump choice1_done

    label choice1_get_up:

        $ choice1_get_up = "true"

        mc "Yea i should do that..."

        pause 0.5

        play sound"audio/blanket.ogg"

        pause 0.5

        mc "Being up this early is such a pain, it shouldn't be allowed."

        stop sound

        scene bedroom
        with fade

        pause 0.5

        play sound "audio/jacket_lock.ogg"

        "Alright, i'm heading out then."

        pause 1.0

        stop sound

        jump choice1_done

    label choice1_poland:

        $ choice1_poland = "true"

        "After a moment of consideration while laying in my very comfy... very..."

        mc "Wow, holy shit, is it just me or does it feel more comfortable than usual...?"

        mc "{cps=15}I think I'm-{nw}{/cps=15}"

        play sound "audio/bedjump.ogg"
        with dissolve

        scene black
        with dissolve

        pause 1.0
        stop sound

        "I doze off, going to a very peaceful sleep, when all of a sudden..."

        scene germanroom
        with slowdissolve
        play sound "audio/basement.ogg" loop

        "I'm sitting at a desk with a big red button and a letter that says {b}Invade Poland{/b}."

        mc "How did... Why am I..."

        "I stare at the button. I'm in an empty room, surrounded by nothing, except for this chair, the table, some documents and the button in front of me."

        mc "Why would I invade Poland? I'm not German, or anything, in fact, I don't know what my nationality is. I was never told that for some reason."

        "But... there's nothing here. Except for that button right there. No doors, no vents, nothing. Just me, the table and chair, the documents and this button."

        mc "I guess... What's the worst that could happen?"

        "I hover my finger over the button, inching it closer and closer to the button."

        scene germanroomzoom

        mc "Well, guess I'm invading Poland."

        stop sound
        play sound "audio/button.ogg"
        pause 0.3
        play music "audio/siren.ogg" fadein 1 fadeout 1

        "I press the button, and as soon as I do, I hear what sounds like a siren going off"

        scene white
        with flash

        play sound "audio/wall.ogg"
        "And the walls all drop to reveal a massive German army surrounding me."

        scene german
        with dissolve

        play sound "audio/german_speech.ogg"

        "They start shouting in German and they run off to... somewhere."

        "I can only guess is Poland."

        scene white
        with flash



        stop music fadeout 1
        stop sound fadeout 1

        pause 0.3

        play sound "audio/catapult.ogg"
        pause 0.3

        "Suddenly the chair flings me into the air, allowing me to see what's going on."
        play sound "audio/wind.ogg" loop
        play music "audio/war.ogg" fadeout 2

        scene germanwar
        with dissolve

        pause 2.0

        mc "It's the Invasion of Poland."

        "Again."

        pause 2.0

        mc "And I just started it."

        "And I'm also now plummetting to the ground."
        "{cps=15}Huh, I wonder what'll happen when I l-{/cps=15}{nw}"

        stop music
        stop sound

        play sound "audio/body_fall.ogg"

        scene black
        pause 4.0

        play sound "audio/phone_vibrate.ogg" loop

        pause 1.0

        mc "Mmmhh, what time is it...?"

        scene bedroom
        with slowdissolve

        "I turn over to my right side and see my alarm clock displaying 2:46 PM, my eyes widening."

        stop sound

        mc "Holy shit, I skipped school."

        "I grab my phone from the end table and check my notifications, scrolling through the list of calls from the school."

        mc "Huh."

        mc "Oh well. This can't possibly come back to bite me in the ass."

        "Right?"

        play sound "audio/hungry.ogg"

        "As I sit up in my bed, my stomach rumbles like a fuckin' lion, clearly telling me {i}u should eat somethin{/i} dipshit."

        "I get up and go to my fridge to find any food and..."

        mc "I forgot to get food again?? Damn, that's the second time this month."

        mc "Well, might as well get some clothes on and head out to the store."

        play sound "audio/jacket_lock.ogg"

        "I prep to go out, and lock my door, starting my short trek for food."

        pause 1.0
        stop sound

        scene street
        with fade

        play music "audio/street.ogg"

        play sound "audio/walk.ogg" loop fadeout 1

        pause 1.5

        play sound "audio/hungry2.ogg"

        "A few minutes later down the block, I'm nearing the store, my stomach still raging for sustanance."

        pause 1.0
        stop sound

        play sound "audio/bomb_far.ogg"

        pause 0.5

        mc "What the fuck was that?"

        play sound "audio/bomb_far.ogg"

        pause 0.5

        "{i}A small explosion can be heard to your right, down a strangely dark alleyway.{/i}"

        scene city
        with fade

        "I turn to my right and see nothing but pitch darkness..."

        mc "Darkness? In the afternoon? That's crazy."

        play sound "audio/hungry.ogg"

        "I try to look into the alleyway, but my gut's telling me {b}food{/b}."

        mc "Screw it, curiosity never killed the cat. I think?"

        "Shit, maybe I shouldn'tve skipped school..."

        "Eh, whatever."

        scene hallway
        with fade

        play sound "audio/walk.ogg" loop fadeout 1

        "I walk into the alleyway, surrounded by darkness."

        "..."

        "Okay that sounds pretty edgy, uhhh..."

        "I walk into the very poggers alleyway, surrounded by a very light darkness."

        "Alright that makes no sense whatsoever."

        mc "{cps=15}Maybe if I we-{nw}{/cps=15}"

        stop sound

        skill "Hey"

        with vpunch

        mc "{cps=20}HOLY SHI-{/cps=20}{nw}"

        skill "Yuo wanna"

        skill "mini pipe bomb"

        "..."

        mc "What?"

        show pipebomb:
            xalign 0.5
            yalign 0.5
        with dissolve

        "The strange girl hands me... a mini pipe bomb. It's very tiny. Almost cute, if it wasn't destructive."

        hide pipebomb
        with dissolve

        skill "Pipe bobms are cool"

        mc "Uhhh... sure... who are you?"

        skill "Skill issue"

        "That's..."

        mc "That's not a name though"

        skill "Its mine"

        mc "Um, alright. Can I just call you Skill for short?"

        skill "Throw the bomb"

        mc "...Can't you answer my question first?"

        skill "Bomb now"

        mc "Okay fine, but where? I'm not throwing it if someone's gonna ge-"

        play sound "audio/bomb_near.ogg"

        "Skill takes out a mini pipe bomb from their pocket and throws it at a wall, creating a mini-explosion and leaving a small mark on the wall."

        mc "Oh. I thought that would've exploded a lot... bigger."

        mc "But hey, small expectations for small packages."

        mc "Thank god I don't have a small package."

        skill "throw the bomb now"

        "Skill points to the wall, just below where she threw hers."

        play sound "audio/bomb_near.ogg"

        "I slightly wind my arm back, and toss the bomb at the wall, watching it explode."

        mc "Huh. That was neat."

        skill "Bombs are neat. Throw another?"

        mc "... Sure, why not."

        play sound "audio/bomb_near.ogg"

        "Skill hands me another, and I throw it at the wall again."

        pause 1.5

        "Something about it is just... kinda satisfying."

        pause 1.0

        scene hallway
        with fade

        "An hour passes without me knowing and I've thrown countless bombs at the wall with Skill. The wall is covered in black and crumbled brick-parts litter the ground."

        mc "Hey, that was fun, but I gotta get going. I've got food to eat, since I'm starving."

        skill "Ok. Come back to throw more bombs?"

        mc "Yeah, absolutely. Catch you later."

        play sound "audio/hungry2.ogg"

        "I wave goodbye to Skill and walk out of the alleyway and get back on track, my stomach punching the shit out of me for taking longer with the food."

        #termine el script de lie
        scene black
        with slowdissolve

        "End of actual skill script"

        jump choice1_done

    label choice1_done:

        with dissolve

        pause 0.5

        scene city
        with fade

        pause 1.0

        "act 1?"
    return
