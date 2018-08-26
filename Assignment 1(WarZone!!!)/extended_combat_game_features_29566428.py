#Student Name : Jaimon Thyparambil Thomas
#Student ID : 29566428
#Start Date : 17 - 08 - 2018
#Last modified Date : 24 - 08 - 2018

#This file contains all the details and utility methods required for handling extended combat game

import combat_game_characters_29566428 as unit
import combat_game_utilities_29566428 as utilities
import combat_game_modes_29566428 as modes
import combat_game_display_utilities_29566428 as display_utilities

#Default Extended Game Settings Constants
health_mode_enabled = False
improved_combat_mode_enabled = False
medics_mode_enabled = False
user_prompt_medics_enabled = False
extended_army_mode_enabled = False
is_extended_combat_mode = False

#Damage modes For Handling Health
damage_advantage = 3
damage_retaliation = 1
damage_tie = 2
damage_extra_Archer = 3


# This function is used for checking wheather player wishes to revive his dead unit
def revive_unit_handling(player_name,player_money,player_army,current_unit,display_mode):
    #If player has any money left and enbled the various medics mode the only he should be able to revive a unit
    if(player_money > 0 and (medics_mode_enabled or user_prompt_medics_enabled)):
        save = ""
        if (display_mode == modes.regular_fight_mode and user_prompt_medics_enabled):
            #only in regular fight mode user will be asked for actions.
            #so in rest of the modes medics using prompt is disabled  and acts as normal medics mode
            save = input("Do you wish to revive "+player_name+"'s last dead unit (y/n):")
            while (save != "y" and save != "n"):
                save = input("Invalid Input!!!. Please Enter a valid choice(y/n) : ")
        else:
            save = "y"
        if (save == "y"):
            #revived unit is been appended to the end of the army
            if(display_mode != modes.instant_result_mode):
                print(player_name + "'s last dead unit has been successfully revived and added to back of the army.")
            player_army.append(current_unit[utilities.current_unit_ID_pos])
            player_money -= 1
    return [player_army,player_money]

#In this Function various validations of extended combat is been handled
#like improved combat mode, medics, health mode etc
def extended_combat_handling(player_1_details,player_2_details,display_mode,is_display_inverse=False):
    #intializing player 1 and player 2 details
    player_1_name = player_1_details[utilities.improved_combat_disp_name_pos]
    player_2_name = player_2_details[utilities.improved_combat_disp_name_pos]
    player_1_unit_health = player_1_details[utilities.improved_combat_disp_health_pos]
    player_2_unit_health = player_2_details[utilities.improved_combat_disp_health_pos]
    current_player_1_unit = player_1_details[utilities.improved_combat_disp_current_unit_pos]
    current_player_2_unit = player_2_details[utilities.improved_combat_disp_current_unit_pos]
    player_1_army = player_1_details[utilities.improved_combat_disp_army_pos]
    player_1_money = player_1_details[utilities.improved_combat_disp_money_pos]

    if (player_1_unit_health < 1):
        # If player 1's unit is Dead
        #checking wheather player 1 wishes to revive his dead unit
        is_last_unit = len(player_1_army) < 1
        temp = revive_unit_handling(player_1_name,player_1_money, player_1_army, current_player_1_unit, display_mode)
        player_1_army = temp[0]
        player_1_money = temp[1]
        if ((not is_last_unit) and improved_combat_mode_enabled and (player_2_unit_health > 0)):
            dead_units = []
            dead_units.append(unit.dead_unit)

            # If improved combat mode is enabled and player 2 is still alive
            if (current_player_2_unit[unit.unit_Id_pos] == unit.knight[unit.unit_Id_pos]):
                #If player 2's unit which is still alive is a knight
                if (current_player_1_unit[utilities.current_unit_ID_pos] == unit.archer[unit.unit_Id_pos]
                        and len(player_1_army) > 0 and player_1_army[0] == unit.archer[unit.unit_Id_pos]):
                    #If improved combat mode is enabled and player 2's unit is still alive and it is a knight then
                    #If the unit which has been died and next unit is an Archer then
                    #knight can kill both of them with a single strike
                    dead_units.append(unit.dead_unit)
                    if(display_mode != modes.instant_result_mode):
                        print("Archer in the behind is also been killed due to knights special ability")
                    temp = revive_unit_handling(player_1_name,player_1_money, player_1_army, current_player_1_unit,display_mode)
                    player_1_army = temp[0]
                    player_1_money = temp[1]
                    player_1_army.pop(0)

            if (len(player_1_army) > 0 and player_1_army[0] == unit.archer[unit.unit_Id_pos]):
                # If unit behind my dead unit is an Archer and if the opponent unit is still alive then my
                # Archer can kill the opponent unit
                if (health_mode_enabled):
                    player_2_unit_health -= damage_extra_Archer
                else:
                    player_2_unit_health = 0  # player 2 unit Dies

                player_2_unit_name = current_player_2_unit[utilities.current_unit_details_pos][unit.unit_name_pos]
                player_1_current_units = []
                #Since we know that current player 1 unit will always be archer in this case we can directly append archer
                if(is_display_inverse):
                    player_1_current_units = dead_units + [unit.archer]
                else:
                    player_1_current_units = [unit.archer] + dead_units
                if (display_mode != modes.instant_result_mode):
                    #In instant result mode all the match details is been skipped.
                    #Displaying the current fighting units
                    if(is_display_inverse):
                        display_utilities.display_current_fighting_units([current_player_2_unit[utilities.current_unit_details_pos]]
                                                                      ,player_1_current_units)
                    else:
                        display_utilities.display_current_fighting_units(player_1_current_units
                                                                  ,[current_player_2_unit[utilities.current_unit_details_pos]])
                    print("Here "+player_1_name + "'s Archer attacks "+player_2_name+"'s "+player_2_unit_name+" from behind the dead units ")
                    if(player_2_unit_health < 1):
                        print("Thus "+player_2_name+"'s "+player_2_unit_name +" also dies.")

    player_1_details[utilities.improved_combat_disp_health_pos] = player_1_unit_health
    player_2_details[utilities.improved_combat_disp_health_pos] = player_2_unit_health
    player_1_details[utilities.improved_combat_disp_army_pos] = player_1_army
    player_1_details[utilities.improved_combat_disp_money_pos] = player_1_money
    return [player_1_details,player_2_details]

