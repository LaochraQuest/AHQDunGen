#-*-coding:utf8;-*-
#################
#import libraries
import random as rd
#################


#############
#Roll d12
def d12():
    return rd.choice(range(1, 13))
#############

###Use Terror in the Dark Finding Quest Rooms
##Terror = True
##
###################
###Global variables
##chars = []
##room_counter = 0
##################

def passages():
##    text = "Passage:\n"
    
    #Passage Length
    pass_length = d12()
    text = "Passage Length: ("+str(pass_length)+")\n"
    if pass_length <=2:
        text += "1 Section\n"
    if 2 < pass_length < 9:
        text += "2 Sections\n"
    if pass_length >= 9:
        text += "3 Sections\n"
    
    #Passage Features
    pass_feat = d12()+d12()
    text += "\nPassage Features: ("+str(pass_feat)+")\n"
    if pass_feat <= 4:
        text += "Wandering Monsters\n"
    if 5 <= pass_feat <= 15:
        text += "Nothing\n"
    if 16 <= pass_feat <= 19:
        text += "1 Door\n"
    if 20 <= pass_feat <= 21:
        text += "2 Doors\n"
    if pass_feat >= 22:
        text += "Wandering Monsters\n"
              
    #Passage End
    pass_end = d12()+d12()
    text += "\nPassage End: ("+str(pass_end)+")\n"
    if pass_end <= 3:
        text += "T-Junction\n"
    if 4 <= pass_end <= 8:
        text += "Dead End\n"
    if 9 <= pass_end <= 11:
        text += "Right Turn\n"
    if 12 <= pass_end <= 14:
        text += "T-Junction\n"
    if 15 <= pass_end <= 17:
        text += "Left Turn\n"
    if 18 <= pass_end <= 19:
        text += "Stairs Down\n"
    if 20 <= pass_end <= 22:
        text += "Stairs Out\n"
    if pass_end >= 23:
        text += "T-Junction\n"

    return text

############

def rooms(room_count, skip=False, terror=True, chars=set(),furniture=True):
    
##    text = ''
##    if skip == False:
##        text = "[b]Rooms[/b]\n\n"
    
    #Room Type
    room_type = d12()
    text = "Room Type: ("+str(room_type)+")\n"
    if terror == True:
        #Room count 0,1 2
        if room_count < 3:
            if room_type <= 6:
                text += "Normal Room\n"
            if 7 <= room_type <= 9:
                haz = d12()
                text += "Hazard ("+str(haz)+")\n"
                #for now i have kept this global
                hz = hazard(chars, haz=haz, furniture=furniture)
##                print(hz[0])
                chars = chars.union(hz[0])
                text += hz[1]
                furniture = hz[2]
            if 10 <= room_type <= 12:
                text += "Lair\n" 
        #Room count 3-5
        if 3 <= room_count <= 5:
            if room_type <= 5:
                text += "Normal Room\n"
            if 6 <= room_type <= 8:
                haz = d12()
                text += "Hazard ("+str(haz)+")\n"
                #for now i have kept this global
                hz = hazard(chars, haz=haz, furniture=furniture)
                chars = chars.union(hz[0])
                text += hz[1]
                furniture = hz[2]
            if 9 <= room_type <= 11:
                text += "Lair\n" 
            if room_type == 12:
                text += "Quest\n"
        #Room count 6-7
        if 6 <= room_count <= 7:
            if room_type <= 4:
                text += "Normal Room\n"
            if 5 <= room_type <= 6:
                haz = d12()
                text += "Hazard ("+str(haz)+")\n"
                #for now i have kept this global
                hz = hazard(chars, haz=haz, furniture=furniture)
                chars = chars.union(hz[0])
                text += hz[1]
                furniture = hz[2]
            if 7 <= room_type <= 8:
                text += "Lair\n" 
            if 9 <= room_type <= 12:
                text += "Quest\n"
        #Room count > 8
        if room_count >= 8:
            if room_type <= 3:
                text += "Normal Room\n"
            if 4 <= room_type <= 5:
                haz = d12()
                text += "Hazard ("+str(haz)+")\n"
                #for now i have kept this global
                hz = hazard(chars, haz=haz, furniture=furniture)
                chars = chars.union(hz[0])
                text += hz[1]
                furniture = hz[2]
            if 6 <= room_type <= 7:
                text += "Lair\n" 
            if 8 <= room_type <= 12:
                text += "Quest\n"
            
    else:
        if room_type <= 6:
            text += "Normal Room\n"
        if 7 <= room_type <= 8:
            haz = d12()
            text += "Hazard ("+str(haz)+")\n"
            #for now i have kept this global
            hz = hazard(chars, haz=haz, furniture=furniture)
            chars = chars.union(hz[0])
            text += hz[1]
            furniture = hz[2]
        if 9 <= room_type <= 10:
            text += "Lair\n" 
        if 11 <= room_type <= 12:
            text += "Quest\n"

    #Furniture
    if furniture == True:
        furn = d12()
        text += '\nFurniture: ('+str(furn)+')\n'
        if furn <= 6:
            text += 'Nothing\n'
        if furn == 7:
            text += 'Weapons Rack\n'
        if furn == 8:
            text += 'Cupboard\n'
        if furn == 9:
            text += 'Table\n'
        if furn == 10:
            text += 'Fireplace\n'
        if furn == 11:
            text += 'Bookcase\n'
        if furn == 12:
            text += 'Torture Rack\n'
        
    
       
    #Doors
    doors = d12()
    text += "\nRoom Doors: ("+str(doors)+")\n"
    if doors <= 4:
        text += "None"
    if 5 <= doors <= 8:
        text += "1 Door"
    if 9 <= doors <= 12:
        text += "2 Doors"
    

    return 1, text

################
#Opening Room Door    

def door_leads():#room_count):
#Where the door leads to
    text = ""#Room door\n"
    leads = d12()
    text += "\nDoor leads to ("+str(leads)+")\n\n"
    if leads % 2 == 0:
        text += "a passage\n"
        #inp = input("a passage (Press r to reveal)\n")
        #if inp=='r':
        #    passages()
    else:
        text += "another room\n"
    #    room_count = rooms(room_count,skip=text)

    #return room_count, text
    return text


#################
#Hazards

def hazard(chars, furniture, haz=False):
    text = ''
    if haz== False:
        haz = d12()
    if haz == 1:
        text += "\nWandering Monsters\n"
    if haz == 2:
        text += "\nNon-player Character:\n"
        npc = d12()
        if 1 <= npc <= 3:
            if "maiden" in chars:
                text += "Wandering Monsters\n"
            else:
                text += "Maiden\n"
                chars.add("maiden")
        if 4 <= npc <= 6:
            if "witch" in chars:
                text += "Wandering Monsters\n"
            else:
                text += "Witch\n"
                chars.add("witch")
        if 7 <= npc <= 9:
            if "henchman" in chars:
                text += "Wandering Monsters\n"
            else:
                text += "Man-at-Arms\n"
                chars.add("henchman")
        if 10 <= npc <= 12:
            if "rogue" in chars:
                text += "Wandering Monsters\n"
            else:
                text += "Rogue\n"
                chars.add("rogue")
    if haz == 3:
        text += "Chasm\n"
        furniture = False
    if haz == 4:
        text += "Statue\n"
    if haz == 5:
        ratbat = d12()
        if ratbat % 2 == 0:
            text += "Rats\n"
        else:
            text += "Bats\n"
    if haz == 6:
        text += "Mould\n"
        furniture = False
    if haz == 7:
        text += "Mushrooms\n"
        furniture = False
    if haz == 8:
        text += "Grate\n"
    if haz == 9:
        text += "Pool\n"
        furniture = False
    if haz == 10:
        text += "Magic Circle\n"
        furniture = False
    if haz == 11:
        text += "Trapdoor\n"
    if haz == 12:
        text += "Throne\n"


    
    return chars, text, furniture
#################
#Treasure

def treasure():
    treas = d12()
    text = "Treasure ("+ str(treas) +")\n\n\n"
    if treas == 1:
        text += "Treasure Map\n"
    if treas == 2:
        text += "6 arrows and \n20 gold crowns"
    if treas == 3:
        text += "10 feet of rope and \n30 gold crowns"
    if treas == 4:
        text += "2 flasks of Greek Fire\n"
    if treas == 5:
        text += "50 gold crowns\n"
    if treas == 6:
        text += "100 gold crowns\n"
    if treas == 7:
        text += "150 gold crowns\n"
    if treas == 8:
        text += "Screech Bug and \n50 gold crowns"
    if treas == 9:
        text += "Rat Poison and \n50 gold crowns"
    if treas == 10:
        text += "200 gold crowns\n"
    if treas == 11:
        potion = d12()
        if potion % 2 == 0:
            text += "Strength potion and \n50 gold crowns"
        else:
            text += "Healing potion and \n50 gold crowns"
    if treas == 12:
        text += "Magic Treasure\n"


    return text

#################
#run

##def run(room_count):
##    choice = input("\n--------------\nSelect table (q to quit)\n1. Passage\n2. Room\n3. Room Door\n4. Treasure\n\n")
##    print()
##    #print('rooms:',room_count)
##    
##    if choice == '1':
##        print(passages())
##    if choice == '2':
##        rms = rooms(room_count)
##        room_count = rms[0]
##        print(rms[1])
##    if choice == '3':
##        dl = door_leads()#room_count)
##        print(dl)
##        if 'room' in dl:
##            rms = rooms(room_count, skip=True)
##            room_count = rms[0]
##            print(rms[1])           
##        
##    if choice == '4':
##        print(treasure())
##       
##    if choice != 'q':
##        run(room_count)
##
##
###################
###Run
##        
##run(room_counter)
