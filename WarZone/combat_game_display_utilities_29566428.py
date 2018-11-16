#Student Name : Jaimon Thyparambil Thomas
#Student ID : 29566428
#Start Date : 17 - 08 - 2018
#Last modified Date : 24 - 08 - 2018

#This file contains all the details and methods required for
#displaying various things required for basic or extended combat game

import combat_game_characters_29566428 as unit
import combat_game_utilities_29566428 as utilities
import combat_game_modes_29566428 as modes
import extended_combat_game_features_29566428 as extended_features

exit_msg = "\nBye Bye See You Later"
continue_msg = "\n Press Enter to continue"

#Function to print padding spaces
def print_space(padding = 1):
    return(" "*padding)

#function to clear current screen
def clear_screen( n = 100):
    print("\n"*n)
    return

#function to display game menu title
def game_menu_title():
    clear_screen()
    print_game_name()
    print("\n")
    return

#Function used for displaying current fighting units
def display_current_fighting_units(player_1_units=[],player_2_units=[]):
    print()
    for feature in unit.basic_unit_display_units:
        temp_string = ""
        for each in player_1_units:
                temp_string += each[unit.unit_display_pos][feature]
        temp_string +="  "+unit.vs_display[feature] + "  "
        for each in player_2_units:
                temp_string += each[unit.unit_inverse_display_pos][feature]
        print(temp_string)
    print()
    return

#Funtion used to display player details like name, money, army etc
def display_player_details(player_name, player_army_Ids, player_money, is_inverse=False):
    print("Player Details")
    print("--------------")
    print("Player Name : " + player_name)
    print("Money Left : $" + str(player_money))
    print("Player Army : ")
    print_all_units(get_army_units(player_army_Ids), is_inverse, False)
    return

#Function to display all Army units fighting sequence
def display_army_fighting_sequence(player_1_details,player_2_details):
    game_menu_title()
    display_army_fighting_sequence_without_title(player_1_details,player_2_details)
    return

#Function used to display fighting sequence of army units without game title
def display_army_fighting_sequence_without_title(player_1_details,player_2_details):
    print("\nCurrent Army Status of Players")
    print()
    display_player_details(player_1_details[utilities.player_name_pos], player_1_details[utilities.player_army_pos],
                         player_1_details[utilities.player_money_pos])
    print("\n")
    display_player_details(player_2_details[utilities.player_name_pos], player_2_details[utilities.player_army_pos],
                         player_2_details[utilities.player_money_pos])
    return

#print Welcome
def print_welcome(padding = 0):
    print(print_space(padding)+" \\\\  /\\  // ||==== ||      //==  //\\\\   /\\ /\\   ||====")
    print(print_space(padding)+"  \\\\//\\\\//  ||===  ||     ((    ((  )) //\\//\\\\  ||===")
    print(print_space(padding)+"   \\/  \\/   ||==== ||====  \\\\==  \\\\// //     \\\\ ||====")
    return

#Print TO
def print_to(padding = 0):
    print(print_space(padding)+" ======  //\\\\")
    print(print_space(padding)+"   ||   ((  ))")
    print(print_space(padding)+"   ||    \\\\//")
    return

#Function to Print Game's Name
def print_game_name(padding = 0):
    print(print_space(padding)+"==================================>>")
    print(print_space(padding)+" \\\\  /\\  //  //\\\\   ||-\\\\      //   //\\\\   /\\  // ||==== | | |")
    print(print_space(padding)+"  \\\\//\\\\//  // _\\\\  ||-//     //   ((  )) //\\\\//  ||===  | | |")
    print(print_space(padding)+"   \\/  \\/  //    \\\\ || \\\\    //     \\\\// //  \\/   ||==== @ @ @")
    if(extended_features.is_extended_combat_mode):
        print(print_space(padding) + "                          <<==========Extended Version=========== ")
    else:
        print(print_space(padding) + "                          <<=============Basic Version========== ")
    return

#Function to print welcome screen
def welcome_screen(padding = 0):
    clear_screen()
    print_welcome(padding+3)
    print()
    print_to(padding+23)
    print()
    print_game_name(padding)
    print("\n")
    input(print_space(padding)+print_space(15)+"Press ENTER to continue")
    return

#Funtion to print main menu
def main_menu():
    game_menu_title()
    i = 1
    c_single_player = i
    print(str(c_single_player)+".Single Player")
    i += 1
    c_battle_mode = i
    print(str(c_battle_mode)+".Battle Mode") #Multiplayer mode
    c_game_settings = -1
    if(extended_features.is_extended_combat_mode):
        #Game settings is available only in extended version
        i += 1
        c_game_settings = i
        print(str(c_game_settings)+".Game Settings")
    i += 1
    c_help = i
    print(str(c_help)+".Help")
    i += 1
    c_exit = i
    print(str(c_exit)+".Exit")
    choice = input("Choose any of these mode to continue:")
    while(not choice.isdigit() or (int(choice) < c_single_player and int(choice) > c_exit)):
        choice = input("Invalid Input!!!. Please Enter a valid choice : ")
    choice = int(choice)

    if (choice == c_single_player):
        modes.single_player()
    elif (choice == c_battle_mode):
        modes.battle_mode()
    elif (extended_features.is_extended_combat_mode and choice == c_game_settings):
        modes.game_settings()
    elif (choice == c_help):
        print_file("Game_Modes_Help_29566428.txt")
        main_menu()
    else:
        print(exit_msg)
    return

#Function used For printing a file
def print_file(file_name = ""):
    game_menu_title()
    game_modes_help_file = open(file_name, "r")
    print(game_modes_help_file.read())
    print("\n")
    input(continue_msg)
    return

#Function used to print All units details
def print_units_help():
    game_menu_title()
    unit_ids = unit.basic_army_units_ids
    if(extended_features.extended_army_mode_enabled):
        unit_ids = unit.exended_army_unit_ids
    for each in unit_ids:
        print_unit_details(each)
    input(continue_msg)
    return

#Function used to print detailed unit description for a particular unit
def print_unit_details(unit_id):
    army_unit = unit.army_units[unit_id]
    #displaying the units basic details like how it looks, cost, health etc
    print_unit(army_unit,unit.unit_purchase_display_units,False)
    print()
    #displaying units against which current unit has an advantage
    temp_string = army_unit[unit.unit_name_pos]+ " has an advantage over "
    advantage_units = army_unit[unit.unit_advantage_pos]
    if (type(advantage_units) == tuple):
        for i in range(0,len(advantage_units)):
            if((not extended_features.extended_army_mode_enabled) and (advantage_units[i] not in unit.basic_army_units_ids)):
                    continue
            if (i == len(advantage_units)-1 ):
                temp_string+=" and "
            elif(i != 0):
                temp_string+=", "
            temp_string += unit.army_units[advantage_units[i]][unit.unit_name_pos]
    else:
        temp_string += unit.army_units[advantage_units][unit.unit_name_pos]
    temp_string +=" units"
    print(temp_string)
    #Displaying special powers in improved combat
    if(extended_features.improved_combat_mode_enabled):
        if(unit_id == unit.archer_ID):
            print("Special Powers : " + unit.archer_special_power_str )
        if(unit_id == unit.knight_ID):
            print("Special Powers : " + unit.knight_special_power_str)
    print("\n")
    return

#Function used to get all army units from their IDs and return it as a list
def get_army_units(army_unit_Ids):
    result_list = []
    for each in army_unit_Ids:
        result_list.append(unit.army_units[each])
    return result_list

#Function used for printing all army units
def print_all_units(display_units = unit.army_units_tuple, is_inverse = False, is_purchase_version = False):
    if len(display_units) == 0:
        return
    if(is_purchase_version):
        print_multiple_units(display_units,unit.unit_purchase_display_units,is_inverse)
    else:
        print_multiple_units(display_units,unit.basic_unit_display_units,is_inverse)
    return

#Function used to print multiple units
def print_multiple_units(units, display_features, is_inverse = False):
    for feature in display_features:
        if((not extended_features.health_mode_enabled) and feature == unit.health_display_pos):
            continue
        temp_string = ""
        for each in units:
            if is_inverse:
                temp_string += each[unit.unit_inverse_display_pos][feature]
            else:
                temp_string += each[unit.unit_display_pos][feature]
        print(temp_string)
    return

#Function used to print a single army unit
def print_unit(army_unit, display_features = unit.basic_unit_display_units, is_inverse = False):
    for feature in display_features:
        if ((not extended_features.health_mode_enabled) and feature == unit.health_display_pos):
            continue
        if is_inverse:
            print(army_unit[unit.unit_inverse_display_pos][feature])
        else:
            print(army_unit[unit.unit_display_pos][feature])
    return
