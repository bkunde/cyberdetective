#Text based game built for 2023 UtahTech PREP CS final project
#Built by Brevin Kunde with description by chatGPT

import random

turn = 0
examine_keywords = ["examine", "look at", "investigate",]
pick_keywords = ["pick up", "take", "grab",]

def officeExam(iItems, computerEmail):
        uin = input().lower()
        #quit
        if uin == "q" or uin == "quit":
            return "quit"

        #test to see if user inputs a examine key word and an item in the room
        for item in iItems:
            for keyword in examine_keywords:
                if keyword in uin:
                    if item in uin:
                        if item == "window":
                            print("""You glance out the window, greeted by a cityscape cloaked in rain and neon. Hovercars whiz by, their trails disappearing into the night. The pulsing lights and shadows hint at the mysteries and dangers lurking within this cyberpunk realm. The window beckons, inviting you to embark on your detective journey through this gritty metropolis.
                            """)
                            return True 
                        elif item == "case files":
                            print("""As you reach for a file, the scent of aged paper fills the air, mingling with the faint traces of ink and determination. Photographs capture frozen moments in time, faces that have seen too much, scenes that hold the key to unraveling the truth. Notes scrawled in your own handwriting, a testament to sleepless nights and relentless pursuit, guide your path.

        The case files speak of corruption, missing persons, corporate conspiracies, and the darker side of technological advancements. So far you haven't been able to crack these cases open, they remain on your desk their scecets staying locked behind a riddle that remains unsolved.
                            """)
                            return True 
                        elif item == "computer":
                            print("""Your weary eyes fixate on the glowing screen of your computer terminal. It hums softly, displaying a torrent of information, messages, and virtual notifications. You swift pass these distractions and log in to your email. An email notification catches your attention. The subject line reads "URGENT: Murder Investigation." With a mix of curiosity and apprehension, you open the email to reveal a message detailing a grisly murder that demands your attention.

The sender remains anonymous, their identity obscured by encrypted digital footprints. The email provides scant details, yet it hints at a carefully orchestrated crime. The email lingers on the screen, its urgency palpable. The city's secrets await your arrival, detective. It's time to uncover the truth behind this murder and bring justice to a city teetering on the edge.
                            """)
                            return False
                        elif item == "pinboard":
                            print("""You scan the pinboard, its cluttered surface adorned with photographs, clippings, and notes. A visual map of mysteries and connections, it beckons you to unravel their secrets. The images and strings hint at a larger conspiracy lurking in the shadows of the cyberpunk city. THe strings connecting to multiple photographs yet you've hit a dead end in that investigation
                            """)
                            return True 
                        elif item == "photos":
                            print("""You examine the array of photographs. Each image captures a moment frozen in time, holding the potential for crucial clues. Faces of suspects, witnesses, and victims gaze back at you, their expressions shrouded in mystery.
                             """)
                            return True 
                        elif item == "notes":
                            print("""You glance at the scattered notes on your desk, a treasure trove of insights and leads. Cryptic symbols, abbreviations, and hastily jotted observations adorn the pages. These notes represent the fragments of your investigative journey.
                            """)
                            return True
        if "leave" in uin or "door" in uin or "go to crime scene" in uin:
            if not computerEmail:
                print("There is more work and investigating to be done.\n")
                return True
            else:
                print("""Leaving your office behind, you step out into the rain-soaked streets of the cyberpunk city, following the leads that have drawn you to the crime scene. The cityscape engulfs you, its neon glow and pulsating energy surrounding your every step.

Navigating through the maze of alleys and bustling thoroughfares, you arrive at the designated location. It's an abandoned warehouse, its decaying facade standing as a haunting reminder of forgotten industries. The rain intensifies, adding an eerie atmosphere to the already ominous setting.

Approaching the entrance, caution takes hold as you step into the dimly lit interior. The sound of dripping water echoes in the empty space, mingling with your footsteps. The scene unfolds before you—an intricate tapestry of evidence and tragedy. The air is heavy with the scent of blood and the lingering presence of violence.
""")
                return "leave"
        else:
            print("Unknown Command.\n")
            return True

def OfficeItems(pItems):
        uin = input().lower()
        #quit
        if uin == "q" or uin == "quit":
            return "quit"

        #test to see if user inputs a examine key word and an item in the room
        for item in pItems:
            for keyword in examine_keywords:
                if keyword in uin:
                    if item in uin:
                        if item == "electro-magnum":
                            print("""A modified revolver that combines electromagnetic propulsion with traditional bullet ammunition. It delivers substantial stopping power, making it a reliable choice in confrontations where raw firepower is needed.
                            """)
                            return
                        elif item == "notebook":
                            print("""A typical notebook for writing all of your investigation notes
                            """)
                            return
                        elif item == "lockpick set":
                            print("""A collection of specialized tools that assist in bypassing locks and gaining access to restricted areas. It enables the detective to explore places that hold valuable evidence or secrets.
                            """)
                            return
                        elif item == "cyberdeck":
                            print("""Compact device used for hacking into systems, extracting data, or overriding security measures. It allows the detective to access confidential files, uncover digital footprints, and reveal crucial information.
                            """)
                            return
                        elif item == "holorecorder":
                            print("""A handheld device capable of capturing and displaying holographic recordings. It can be used to replay important conversations, examine crime scenes from different angles, or analyze past events.
                            """)
                            return
        for item in pItems:
            for keyword in pick_keywords:
                if keyword in uin:
                    if item in uin:
                        if item == "electro-magnum":
                            print("Electro-magnum added to inventory\n")
                            return  "electro-magnum"
                        elif item == "notebook":
                            print("Notebook added to inventory\n")
                            return "notebook"
                        elif item == "lockpick set":
                            print("Lockpick Set added to inventory\n")
                            return "lockpick set"
                        elif item == "cyberdeck":
                            print("Cyberdeck added to inventory\n")
                            return "cyberdeck"
                        elif item == "holorecorder":
                            print("Holorecorder added to inventory\n")
                            return "holorecorder"


def office(inventory):
    office = True
    computerEmail = False
    #interactable items
    iItems = ["window", "case files", "computer", "pinboard", "photos", "notes",]
    pItems = ["electro-magnum", "notebook", "lockpick set", "cyberdeck", "holorecorder",]
    while office:
        oe = officeExam(iItems, computerEmail)
        #oi = OfficeItems(pItems)
        #inventory.append(oi)
        if oe != True and oe != "leavel":
            computerEmail = True
        if oe == "leave":
            office = False
        if oe == "quit":
            return 'q'


                            



#main game loop
def main():
    print("""
As you step into your cluttered office, a haze of cigarette smoke hangs heavy in the dimly lit room, illuminated only by the flickering neon signs outside your window. The walls, covered in peeling wallpaper, bear the marks of a thousand cases past. The scent ofstale coffee and worn leather permeates the air, mingling with the faint hum of technology that permeates every inch of this cyberpunk metropolis.

Your desk, buried under a mountain of case files, glows softly with the blue light of your computer terminal. The holographic display dances before your weary eyes, showing a constant stream of news updates, virtual notices, and messages from your contacts. The incessant rain beats against the windows, creating a symphony of melancholic rhythms that mirrors the gritty reality of the city outside.

To your left, a dusty old pinboard displays photographs and notes, reminders of unfinished mysteries and unsolved crimes that hauntyour sleepless nights. The flickering fluorescent light above your head buzzes intermittently, casting an eerie glow on the faded linoleum floor beneath your feet.

As you settle into your worn-out leather chair, its creaking protest echoes through the empty office. The city's pulse thrums through the walls, beckoning you to immerse yourself once more in the dangerous underbelly of this neon-lit dystopia. Your intuition tells you that today, like any other day in this cyberpunk maze, holds the promise of adventure, danger, and the elusive truth waitingto be uncovered. The city awaits your next move, detective.
    """)
    inventory = []
    game = True
    while game:
        uin = office(inventory)
        #quit
        if uin == "q" or uin == "quit":
            print("Thanks for playing!")
            game = False
        


if __name__ == '__main__':
    main()
