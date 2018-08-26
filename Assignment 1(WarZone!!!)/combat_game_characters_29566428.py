#Student Name : Jaimon Thyparambil Thomas
#Student ID : 29566428
#Start Date : 17 - 08 - 2018
#Last modified Date : 24 - 08 - 2018

#This file contains all the details of characters or army units required for basic or extended combat game

#display position constants
head_pos = 0
upper_body_pos = 1
middle_body_pos = 2
lower_body_pos = 3
description_pos = 4
cost_display_pos = 5
health_display_pos = 6
unit_characteristics_ID_divison = 7
unit_ID_display_pos = 8

#Unique Unit IDs
#Note whenever a new unit is been added update max value on basic and extended unit id
archer_ID = 1
soldier_ID = 2
knight_ID = 3
wizard_ID = 4
seige_ID = 5
dead_unit_ID = 6

#Max unit ID values of army units for various game versions
max_basic_unit_ID = 3
max_extended_unit_ID = 5

#unit Advantage
archer_advanage = (soldier_ID,wizard_ID) #Archer has advantage over soldier and wizard
knight_advantage = (archer_ID,seige_ID)
soldier_advantage = (knight_ID)
wizard_advantage = (soldier_ID,knight_ID,seige_ID)
seige_advantage = (archer_ID,soldier_ID)

archer_special_power_str = "If an Archer is at the front of its army but not in battle, " \
                           "\nthey deal their damage to the opposing unit if they are still alive at the end of combat."
knight_special_power_str = "If the Knight is fighting an Archer and the unit behind the Archer is another Archer," \
                           "\nthen the Knight deals its damage to both Archers."

#Army units display characteristics
archer_display = ("  O  \\    "," /|\\--)-> ","  |  /    "," / \\      "," Archer   "," Cost:1$  "," Health:1 "," -------- "," UnitID:"+str(archer_ID)+" ")
soldier_display = ("    O ^   ","   /|\\|   ","    | |   ","   / \\    "," Soldier  "," Cost:1$  "," Health:2 "," -------- "," UnitID:"+str(soldier_ID)+" ")
knight_display = ("  O       "," /X\\-+==> ","  X       "," / \\      "," Knight   "," Cost:1$  "," Health:3 "," -------- "," UnitID:"+str(knight_ID)+" ")
wizard_display = ("  _       "," /O\  .   "," [|]-/    "," / \\      "," Wizard   ", " Cost:2$  "," Health:3 "," -------- "," UnitID:"+str(wizard_ID)+" ")
seige_display = ("   (O     ","  __\\\\__  "," |______| "," (O)  (O) "," Seige    ", " Cost:1$  "," Health:3 "," -------- "," UnitID:"+str(seige_ID)+" ")

#Army units inverse display characteristics
archer_inverse_display = ("    /  O  "," <-(--/|\\ ","    \  |  ","      / \\ ","   Archer ","  Cost:1$ "," Health:1 "," -------- "," UnitID:"+str(archer_ID)+" ")
soldier_inverse_display = ("   ^ O    ","   |/|\\   ","   | |    ","    / \\   ","  Soldier ","  Cost:1$ "," Health:2 "," -------- "," UnitID:"+str(soldier_ID)+" ")
knight_inverse_display = ("       O  "," <==+-/X\\ ","       X  ","      / \\ ","   Knight ","  Cost:1$ "," Health:3 "," -------- "," UnitID:"+str(knight_ID)+" ")
wizard_inverse_display = ("      _   ","  .  /O\  ","    \\-[|] ","      / \\ ","   Wizard ", "  Cost:2$ "," Health:3 "," -------- "," UnitID:"+str(wizard_ID)+" ")
seige_inverse_display = ("     O)   ","  __//__  "," |______| "," (O)  (O) ","    Seige ", "  Cost:1$ "," Health:3 "," -------- "," UnitID:"+str(seige_ID)+" ")

#Extra display characteristcs
vs_display = ("\\\\    // ________ "," \\\\  // //______  ","  \\\\//  \\\\-----\\\\ ","   \\/   _______// "," "*18, " "*18," "*18," "*18," "*18)
dead_unit_display = ("            ","            ","    ____    "," ==|____|+O "," ---DEAD--- "," "*12," Health:0 "," "*12," "*12)
dead_unit_inverse_display = ("            ","            ","    ____    "," O+|____|== "," ---DEAD--- "," "*12," Health:0 "," "*12," "*12)

#Display units required during fighting
basic_unit_display_units = (head_pos, upper_body_pos, middle_body_pos, lower_body_pos, description_pos)
#display units required during Purchasing
unit_purchase_display_units = basic_unit_display_units + (cost_display_pos, health_display_pos,unit_characteristics_ID_divison,unit_ID_display_pos)

#unit spec position constants
unit_Id_pos = 0
unit_name_pos = 1
unit_display_pos = 2
unit_inverse_display_pos = 3
unit_cost_pos = 4
unit_health_pos = 5
unit_advantage_pos = 6

#unit Spec - (unit_Id,unit_display,unit_inverse_display,unit_cost,unit_health,unit advantage)
#Kept as tuple because Not body should be able to edit these details
archer = (archer_ID, "Archer", archer_display, archer_inverse_display, 1, 1, archer_advanage)
soldier = (soldier_ID, "Soldier", soldier_display, soldier_inverse_display, 1, 2, soldier_advantage)
knight = (knight_ID, "Knight", knight_display, knight_inverse_display, 1, 3, knight_advantage)
wizard = (wizard_ID, "Wizard", wizard_display, wizard_inverse_display, 2, 3, wizard_advantage)
seige = (seige_ID, "Seige", seige_display, seige_inverse_display, 1, 3, seige_advantage)
dead_unit = (6,"Dead",dead_unit_display,dead_unit_inverse_display,0,0,())

#Dictionary where details regarding all army units are kept
#kept it as dictionary so that I can search each units details easily
army_units = {
    archer_ID: archer,
    soldier_ID: soldier,
    knight_ID: knight,
    wizard_ID: wizard,
    seige_ID: seige
}

#basic games army units
army_units_tuple = (archer, soldier, knight)
#Extended games army units
extended_army_units_tuple = army_units_tuple + (wizard, seige)

basic_army_units_ids = (archer_ID,soldier_ID,knight_ID)
exended_army_unit_ids = (basic_army_units_ids + (wizard_ID, seige_ID))

#max money available for an army
max_army_cost = 10






