#Student Name : Jaimon Thyparambil Thomas
#Student ID : 29566428
#Start Date : 17 - 08 - 2018
#Last modified Date : 24 - 08 - 2018

#This file contains all the details and utility methods required required for basic or extended combat game

from random import randint as randomInt
import combat_game_display_utilities_29566428 as display_utilities
import combat_game_characters_29566428 as unit
import combat_game_modes_29566428 as modes
import extended_combat_game_features_29566428 as extended_features

#Constants for Player Details postions
player_name_pos = 0
player_army_pos = 1
player_money_pos = 2

#current unit Details Nodes pos
current_unit_ID_pos = 0
current_unit_health_pos = 1
current_unit_details_pos = 2

#Improved combats Display Nodes pos
improved_combat_disp_name_pos = 0
improved_combat_disp_health_pos = 1
improved_combat_disp_current_unit_pos = 2
improved_combat_disp_army_pos = 3
improved_combat_disp_money_pos = 4

#Function used for setting values of improved combat's display nodes
def improve_combat_display_nodes(player_name,health,current_unit,army,money):
    result = []
    #appending various display nodes as per the respective sequence in Improved combats Display Nodes pos
    result.append(player_name)
    result.append(health)
    result.append(current_unit)
    result.append(army)
    result.append(money)
    return result

#Function used for displaying the current unit details
def set_current_unit_details(unit_ID):
    current_unit =[]
    army_unit = unit.army_units[unit_ID]
    #appending various current unit details as per the respective sequence in current unit Details Nodes pos
    current_unit.append(army_unit[unit.unit_Id_pos])
    current_unit.append(army_unit[unit.unit_health_pos])
    current_unit.append(army_unit)
    return current_unit

#Function used to set player details like Name, money, Army etc
def set_player_details(player_no = 0):
    display_utilities.game_menu_title()
    player_money = 10
    player_army_ids = []
    player_no_str = " "
    if(player_no != 0 and type(player_no) == int):
        player_no_str += (str(player_no) + " ")
    print("\nEnter Player" + player_no_str + " Details")
    player_name = input("Player Name : ")
    res = player_army_selection(player_name, player_army_ids, player_money)
    return res

#Function used for selecting army units for player
def player_army_selection(player_name = "", player_army_ids = [], player_money = 0):
    choice = 1
    while (choice != "q" and player_money > 0):
        #printing players current Army Details
        display_utilities.game_menu_title()
        display_utilities.display_player_details(player_name,player_army_ids,player_money)
        print("\nAvailable Army Units Are")
        if(extended_features.extended_army_mode_enabled):
            display_utilities.print_all_units(display_units = unit.extended_army_units_tuple, is_purchase_version = True)
        else:
            display_utilities.print_all_units(is_purchase_version = True)

        print("\nPress q if you are done with all the purchasing")
        print("Press h for help regarding units")
        if(len(player_army_ids) > 0):
            print("Press r to remove last unit")
        choice = input("\nEnter the desired army unit ID that you wish to purchase:")

        if (choice.isdigit()):
            choice = int(choice)
        #processing if the choice entered by the player is a valid choice or not
        while ((((not extended_features.extended_army_mode_enabled) and choice not in unit.basic_army_units_ids)
                or (extended_features.extended_army_mode_enabled and choice not in unit.exended_army_unit_ids))
               and choice != "q" and choice != "h" and ((choice == "r" and len(player_army_ids) < 1) or choice != "r")):
            print("\nInvalid Input!!!")
            print("Enter q if you are done with all the purchasing")
            print("Enter army unit ID for purchasing the unit")
            choice = input("Enter your choice: ")
            if (choice.isdigit()):
                choice = int(choice)

        #Appending the unit into players Army as per the choice entered by the player
        if ((choice in unit.basic_army_units_ids) or (extended_features.extended_army_mode_enabled and choice in unit.exended_army_unit_ids)):
            if(unit.army_units[choice][unit.unit_cost_pos] > player_money):
                print("Sorry you don't have enough money to purchase the unit")
            else:
                player_money -= unit.army_units[choice][unit.unit_cost_pos]
                player_army_ids.append(choice)
        elif choice == "h":
            display_utilities.print_units_help()
        elif choice == "r" and len(player_army_ids) > 0:
            player_army_ids.pop()
            player_money +=1
        elif choice == "q":
            break

        #Handling edge case when player is out of money
        if(player_money < 1):
            print("\nGreat Job!!! You have used up all you money\n")
        #returning players details along with name, new Army, left over player money
    return get_player_details(player_name, player_army_ids, player_money)

#Function used for returing players details as a list
def get_player_details(player_name,player_army,player_money):
    result = []
    #Appending is done as per the order in nodes of Constants for Player Details postions
    result.append(player_name)
    result.append(player_army)
    result.append(player_money)
    return result

#Function used to randomly select an army
def random_army_selection(player_name = "Comp", player_army_Ids = [], player_money = unit.max_army_cost):
    if(player_money < 1):
        return

    #Here the max no of army units that he can get is as myuch money he has leftover. Since min amount is 1$
    number_of_army_units = randomInt(1, player_money)
    while(player_money > 0 and number_of_army_units > 0):
        #There can be cases where number of units may not reach max number of army unit the player can have
        #Since the max cost per unit is greater than 1$
        if(extended_features.extended_army_mode_enabled and player_money > 1):
            #because max cost of a unit in extended army is greater than 1
            random_unit_ID = randomInt(1, unit.max_extended_unit_ID)
        else:
            random_unit_ID = randomInt(1,unit.max_basic_unit_ID)

        player_army_Ids.append(random_unit_ID)
        army_unit = unit.army_units[random_unit_ID]
        player_money -= army_unit[unit.unit_cost_pos]
        number_of_army_units -= 1

    display_utilities.game_menu_title()
    display_utilities.display_player_details(player_name, player_army_Ids, player_money)
    return get_player_details(player_name,player_army_Ids,player_money)

#Function used for displaying the fighting menu
def game_fighting_menu(player_1_details,player_2_details):
    display_utilities.display_army_fighting_sequence(player_1_details, player_2_details)
    print("-" * 20)
    print("\n Match Menu ")
    print("------------")
    print("1.Start Fight")
    print("2.Instant Result")
    print("3.Fight Summary")
    print("4.Go back to Previous menu")
    print("5.Exit")
    choice = input("Please select Any of the above choices: ")
    while (not choice.isdigit() or (int(choice) < 1 and int(choice) > 5)):
        choice = input("Invalid Input!!! Please select Any of the above choices: ")
    choice = int(choice)
    if (choice == 1):
        armyFighting(player_1_details, player_2_details, modes.regular_fight_mode)
    elif (choice == 2):
        armyFighting(player_1_details, player_2_details, modes.instant_result_mode)
    elif (choice == 3):
        armyFighting(player_1_details, player_2_details, modes.fight_summary_mode)
    elif (choice == 4):
        display_utilities.main_menu()
    else:
        print(display_utilities.exit_msg)
    return

def display_current_fighting_units(current_player_1_unit, current_player_2_unit,player_1_army,player_2_army, display_mode):
    if (display_mode != modes.instant_result_mode):
        player_1_current_display = []
        player_1_current_display.append(current_player_1_unit[current_unit_details_pos])
        player_2_current_display = []
        player_2_current_display.append(current_player_2_unit[current_unit_details_pos])
        if (extended_features.improved_combat_mode_enabled):
            #If one players current unit is a knight and opposite players units next two units are archers
            #Then we have to display both archers and knight as fighting
            #As knight can kill two consecutive archers if improved combat is been enabled
            if (current_player_1_unit[current_unit_ID_pos] == unit.knight_ID and
                    current_player_2_unit[current_unit_ID_pos] == unit.archer_ID and
                    len(player_2_army) > 0 and player_2_army[0] == unit.archer_ID):
                # Since current unit is already an archer we can append that itself
                player_2_current_display.append(current_player_2_unit[current_unit_details_pos])
            elif (current_player_2_unit[current_unit_ID_pos] == unit.knight_ID and
                  current_player_1_unit[current_unit_ID_pos] == unit.archer_ID and
                  len(player_1_army) > 0 and player_1_army[0] == unit.archer_ID):
                # Since current unit is already an archer we can append that itself
                player_1_current_display.append(current_player_1_unit[current_unit_details_pos])

        display_utilities.display_current_fighting_units(player_1_current_display, player_2_current_display)
    return

#Function where fighting between two armies is been handled
def armyFighting(player_1_details = [], player_2_details = [], display_mode = modes.regular_fight_mode):
    if (display_mode != modes.instant_result_mode):
        print("\n--------------------------Fighting Begins Here --------------------------\n")

    # Initiazing Variables
    player_1_army = player_1_details[player_army_pos].copy()
    player_2_army = player_2_details[player_army_pos].copy()
    player_1_money = player_1_details[player_money_pos]
    player_2_money = player_2_details[player_money_pos]
    player_1_name = player_1_details[player_name_pos]
    player_2_name = player_2_details[player_name_pos]
    current_player_1_unit = []
    current_player_2_unit = []
    player_1_unit_health = 0
    player_2_unit_health = 0

    while ((len(player_1_army) > 0 or len(current_player_1_unit) != 0) and (
            len(player_2_army) > 0 or len(current_player_2_unit) != 0)):
        #Cases when when both the army units are not over are handled below

        #If current unit which had been fighting is dead then new unit should enter into the battle field
        if (len(current_player_1_unit) == 0):
            current_player_1_unit = set_current_unit_details(player_1_army[0])
            player_1_unit_health = current_player_1_unit[current_unit_health_pos]
            player_1_army.pop(0)
        if (len(current_player_2_unit) == 0):
            current_player_2_unit = set_current_unit_details(player_2_army[0])
            player_2_unit_health = current_player_2_unit[current_unit_health_pos]
            player_2_army.pop(0)

        #initializing Current units details in variables
        player_1_unit_advantage = current_player_1_unit[current_unit_details_pos][unit.unit_advantage_pos]
        player_2_unit_advantage = current_player_2_unit[current_unit_details_pos][unit.unit_advantage_pos]
        player_1_unit_name = current_player_1_unit[current_unit_details_pos][unit.unit_name_pos]
        player_2_unit_name = current_player_2_unit[current_unit_details_pos][unit.unit_name_pos]
        player_1_unit_id = current_player_1_unit[current_unit_ID_pos]
        player_2_unit_id = current_player_2_unit[current_unit_ID_pos]

        if (display_mode != modes.instant_result_mode):
            #Current Army fleet of both the players is been displayed
            player_1_display_details = (player_1_details[player_name_pos], [player_1_unit_id] + player_1_army ,
                                        player_1_money)
            player_2_display_details = ( player_2_details[player_name_pos],[player_2_unit_id] + player_2_army,
                                         player_2_money)

            display_utilities.display_army_fighting_sequence_without_title(player_1_display_details,
                                                                          player_2_display_details)
            #Current fighting units is been displayed
            display_current_fighting_units(current_player_1_unit, current_player_2_unit, player_1_army, player_2_army,
                                           display_mode)
            #displaying current health details if health mode is been enabled
            if(extended_features.health_mode_enabled):
                print(player_1_name + "'s " + player_1_unit_name + " has health - " + str(player_1_unit_health)+" left")
                print(player_2_name + "'s " + player_2_unit_name + " has health - " + str(player_2_unit_health)+" left")

        if ((type(player_1_unit_advantage) == tuple and current_player_2_unit[
            current_unit_ID_pos] in player_1_unit_advantage)
                or (player_1_unit_advantage == current_player_2_unit[current_unit_ID_pos])):
            # Case when Player 1 unit has an advantage over player 2 unit
            if (extended_features.health_mode_enabled):
                if (not extended_features.improved_combat_mode_enabled):
                    # player 1 unit gets affected by the retaliation damage by player 2 unit
                    player_1_unit_health -= extended_features.damage_retaliation
                # player 2 unit gets affected by player 1's advantage damage
                player_2_unit_health -= extended_features.damage_advantage
            else:
                # since player 1 unit has advantage over player 2 unit. Player 2 unit dies
                player_2_unit_health = 0

            if (display_mode != modes.instant_result_mode):
                print("Since " + player_1_unit_name + " has an advantage over " + player_2_unit_name)
                if (player_2_unit_health < 1):
                    print(player_1_name + "'s " + player_1_unit_name + " kills "
                          + player_2_name + "'s " + player_2_unit_name)
                    if(extended_features.health_mode_enabled and not extended_features.improved_combat_mode_enabled):
                        print("But still "+player_2_name + "'s " + player_2_unit_name+" gives a retaliation damage "+
                              "of "+str(extended_features.damage_retaliation) +" unit to "+ player_1_name + "'s " + player_1_unit_name +"'s health.")
                        if (player_1_unit_health < 1):
                            print("Thus " + player_1_name + "'s " + player_1_unit_name + " also dies due to low health")
        elif ((type(player_2_unit_advantage) == tuple and current_player_1_unit[
            current_unit_ID_pos] in player_2_unit_advantage)
              or (player_2_unit_advantage == current_player_1_unit[current_unit_ID_pos])):

            if (extended_features.health_mode_enabled):
                if (not extended_features.improved_combat_mode_enabled):
                    # player 2 unit gets affected by the retaliation damage by player 1 unit
                    player_2_unit_health -= extended_features.damage_retaliation
                # player 1 unit gets affected by player 2's advantage damage
                player_1_unit_health -= extended_features.damage_advantage
            else:
                # since player 2 unit has advantage over player 1 unit. Player 1 unit dies
                player_1_unit_health = 0

            if (display_mode != modes.instant_result_mode):
                print("Since " + player_2_unit_name + " has an advantage over " + player_1_unit_name)
                if (player_1_unit_health < 1):
                    print(player_2_name + "'s " + player_2_unit_name + " kills "
                          + player_1_name + "'s " + player_1_unit_name)
                    if (extended_features.health_mode_enabled and not extended_features.improved_combat_mode_enabled):
                        print(
                            "But still " + player_1_name + "'s " + player_1_unit_name + " gives a retaliation damage " +
                            "of " + str(extended_features.damage_retaliation) + " unit to " + player_2_name + "'s " + player_2_unit_name +"'s health.")
                        if(player_2_unit_health < 1):
                            print("Thus "+player_2_name + "'s " + player_2_unit_name+" also dies due to low health")
        else:
            # Since both units doesnt have an advantage or disadvantage
            if (extended_features.health_mode_enabled):
                # Both units gets affeted by damage during tie
                player_1_unit_health -= extended_features.damage_tie
                player_2_unit_health -= extended_features.damage_tie
            else:
                # Both units dies
                player_1_unit_health = 0  # player 1 unit Dies
                player_2_unit_health = 0  # player 2 unit Dies
            if (display_mode != modes.instant_result_mode):
                print(
                    "Here since both of the units are " + player_2_unit_name + ". None of the units has a clear advantage.")
                if (player_1_unit_health < 1 and player_2_unit_health < 1):
                    print("So both of them dies")
                elif (player_1_unit_health < 1):
                    print("But still only " + player_1_name + "'s" + player_1_unit_name + " dies due to low health.")
                elif (player_2_unit_health < 1):
                    print("But still only " + player_2_name + "'s" + player_2_unit_name + " dies due to low health.")
                else:
                    print("Both of them goes for another round as both of them has more health left out")

        improved_combat_player_1_details = improve_combat_display_nodes(player_1_name, player_1_unit_health,
                                                                      current_player_1_unit, player_1_army, player_1_money)
        improved_combat_player_2_details = improve_combat_display_nodes(player_2_name, player_2_unit_health,
                                                                      current_player_2_unit, player_2_army, player_2_money)

        #here Improved combat validations are handled below
        temp = extended_features.extended_combat_handling(improved_combat_player_1_details, improved_combat_player_2_details, display_mode)
        improved_combat_player_1_details = temp[0]
        improved_combat_player_2_details = temp[1]

        temp = extended_features.extended_combat_handling(improved_combat_player_2_details, improved_combat_player_1_details, display_mode,True)
        improved_combat_player_2_details = temp[0]
        improved_combat_player_1_details = temp[1]

        player_1_unit_health = improved_combat_player_1_details[improved_combat_disp_health_pos]
        player_1_army = improved_combat_player_1_details[improved_combat_disp_army_pos]
        player_1_money = improved_combat_player_1_details[improved_combat_disp_money_pos]

        player_2_unit_health = improved_combat_player_2_details[improved_combat_disp_health_pos]
        player_2_army = improved_combat_player_2_details[improved_combat_disp_army_pos]
        player_2_money = improved_combat_player_2_details[improved_combat_disp_money_pos]

        #reseting current unit details when current unit is dead
        if (player_1_unit_health < 1):
            current_player_1_unit = []
        if (player_2_unit_health < 1):
            current_player_2_unit = []

        if(display_mode == modes.regular_fight_mode):
            input(display_utilities.continue_msg)

    #Inorder to insert the last unit back to the army once fight is over
    if (len(current_player_1_unit) != 0):
        player_1_army.insert(0, current_player_1_unit[current_unit_ID_pos])
    if (len(current_player_2_unit) != 0):
        player_2_army.insert(0, current_player_2_unit[current_unit_ID_pos])

    if (len(player_1_army) > 0):
        print("\nPlayer "+player_1_name + " Wins!!!")
    elif (len(player_2_army) > 0):
        print("\nPlayer "+player_2_name + " Wins!!!")
    else:
        print("\nBoth Players Units Dies Neither of them Wins!!!")
    print("\n")
    input(display_utilities.continue_msg)
    return game_fighting_menu(player_1_details,player_2_details)
