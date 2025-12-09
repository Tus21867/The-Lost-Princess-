# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define g = Character("ghost child")
define a = Character("King Angelo")
define p = Character ("Prince carlos")
define r = Character("Random voice")
define y = Character("Y/N")
image window:
    "bg window view.jpg"
    zoom 1.5

image annoyed king angelo:
    "the king annoyed.png"
    zoom 1.0
image frowning king angelo:
    "the king frowning.png"
    zoom 1.0

image smiling king angelo:
    "the king smiling.png"
    zoom 1.0

image annoyed prince:
    "the prince annoyed.png"
    zoom 1.0

image frowning prince:
    "the prince frowning.png"
    zoom 1.0

image smiling prince:
    "the prince grinning.png"
    zoom 1.0

image ghost child frowning:
    "ghost child frowning.png"
    zoom 1.0

image ghost child talking:
    "ghost child.png"
    zoom 1.0

image glitch child frowning:
    "frowning glitch.png"
    zoom 1.0

image glitch child talking:
    "ghost child glitch.png"
    zoom 1.0
image family portrait:
    "family portrait.png"
    zoom 1.0
image bedroom:
    "bg bedroom.png"
    zoom 2.0

image black screen:
    "black screen.webp"
    zoom 2.0

image castle hallway:
    "bg castle hallway.png"
    zoom 2.0

image rain:
    "bg rain.png"
    zoom 2.0
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg black screen 

    #show smiling prince 


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy
    #show angelo smiling

    # These display lines of dialogue.

    # This ends the game.
    y"ugh..another day out at sea and still no sign of land.."

    y "its been what? three months since I left those worn docks behind in search for something new?"

    y "I know being an archaeologist isn't exactly the most glamorous job..but I didn't think it would be this bad. I've already reached my late twenties and what is there to show for it?"
    y "no discoveries, no fame..just me and my thoughts and failures stuck on this tiny ship with nothing but the endless ocean surrounding us.."
    y"why didn't I just stay home? I guess being stuck at sea is better than being stuck at some dead-end office job but this isn't exactly life-changing either"


    y" *sigh* and with water and food supplies running low? That office job wouldn't have been so bad."
    y"it's raining out, maybe I could catch some water to drink.."
    
    scene bg rain 
    with fade 
    y"shit..this rain is worse than I thought.. everything is sliding around and slippery..its making me sick " 
    scene bg rain 
    with vpunch 
    y"Woah! christ..this is worse than i thought.. i better finish this up this jug before i fall off"
    scene bg rain
    with vpunch 
    y"crap these waves are getting worse-"
    scene bg rain
    with vpunch
    y"aAAHH-"

    scene bg black screen
    with fade

    r"what is that in me waters?..."
    y"'i cant breathe..my body feels so numb..its so cold..'"
    r"is that?..no it cant be..boy get me the net!"
    y"'help me..please..it hurts..'"
    r"help me pull boy! whatever this is isnt light"
    y"'is this the end? its suffocating ..'"
    r"its a human..boy start the engine turn the sails..the king won't be happy about this.."
    y"'the..king?..' my mind goes blank as the siren calls of fatige and slumber call me..it doesnt hurt anymore.."

    

    a"how did this..thing get across the boarder? a boarder mde by the gods no less "
    p"i dont know father.. the sea merchaints found it floating in the water.. barely alive.."
    y"'who is that?..where am I? those voices..they sound so distant..so deep almost demonic..'"
    y"'father?..a father and son? is that who is by my bedside? i can feel their precense but they dont sound too friendly they seem angry that im here..'"
    y"'the older sounding one..what is he ranting on about? a boarder? gods? this has to be a joke..'"
    scene bg bedroom
    with fade
    y" as my eyes adjust to the dim light of the room i can make out two figures standing over me.. one older with a stern look on his face and the other younger looking more curious than anything else.. but both faces are almost filled with..disgust?"
    show annoyed king angelo at right
    show annoyed prince at left
    p" father this thing is awake.."
    a"so it lives? how shameful..these gods must be mocking me.. bringing this..creature to my kingdom.. i mean look at this sack of meat and bones? it couldnt even satisfy scylla if given the chance"
    y"upon looking up i see two men both figures tall muscular rough apperences the room smells if incense and old wood as they peer down at me i notice one of them was wearing a dark blue blindfold one made of silk.."
    y"where..am I?"
    show frowning king angelo 
    a"tch.. and its not house trained either .."
    r"his voice filled with disgust and anger as he glares down at me"

    menu:
        a"how did you get here little mortal?"
        "where am i?":
            jump where am i 
            y"where am i?"
            a"a place you shouldnt be tell me mere mortal how did something as tiny as you get here?"
            y"mortal?..is that some sort of joke? why are you grey?! where is my boat?!"
            p"so you got here by boat? thats a first.."
         return
    
    "remain silent":
            jump silent
            y" ..."
            show annoyed king angelo at right
            show grinning prince at left
            a"tch I asked you a question you little meat bag is that mouth of yours no longer working?"
            p"im sure we can make use of its bones father especially those of the teeth a mute wont need them"
            y"'teeth? these creeps are crazy! i need to get out of here and fast..'"
          return
label after_choice:
        y"Y/N..my name is Y/N..where am I? who are you guys?"
        a"Y/N? what kind of name is that? you are in our kingdom a place no mortal should have access to and yet here you are.."
        p"I am prince carlos and this is my father king Angelo we are the rulers of this land of monsters.."
        y"'monsters? is this some kind of joke? monsters arent real..'"
        a"careful now mortal staring at royalty like that is considered rather rude here"
    #show ghost child sad 
    
    return
