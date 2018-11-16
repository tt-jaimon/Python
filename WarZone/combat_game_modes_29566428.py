#Student Name : Jaimon Thyparambil Thomas
#Student ID : 29566428
#Start Date : 17 - 08 - 2018
#Last modified Date : 24 - 08 - 2018

#This file contains all the details and various methods regarding the various game modes
#Which is been used in both basic and extended combat game versions

import combat_game_display_utilities_29566428 as display_utilities
import combat_game_utilities_29566428 as utilities
import combat_game_characters_29566428 as unit
import extended_combat_game_features_29566428 as extended_features

#Various Display modes during Fighting
regular_fight_mode = 0 #Each time user is been prompted for continue
instant_result_mode = 1 #Winner is displayed instantly
fight_summary_mode = 2 #Entire fight summary is displayed

#Function for Single Player Fight
#ie Player fight with the computer
def single_player():
    display_utilities.game_menu_title()
    player_details = utilities.set_player_details()
    comp_name = input("Please Enter the name of your opponent : ")
    comp_details = utilities.random_army_selection(comp_name,[],unit.max_army_cost)
    utilities.game_fighting_menu(player_details, comp_details)
    return

#Function for Multiplayer Fight
#That is player fights with another player
def battle_mode():
    display_utilities.game_menu_title()
    player_1_details = utilities.set_player_details(1)
    player_2_details = utilities.set_player_details(2)
    utilities.game_fighting_menu(player_1_details, player_2_details)
    return

#Function for Game Settings
def game_settings():
    display_utilities.game_menu_title()
    print("\n Game Settings")
    print(" --------------\n\n")
    print_status("1.Health Mode",extended_features.health_mode_enabled)
    print_status("2.Improved Combat Mode",extended_features.improved_combat_mode_enabled)
    print_status("3.Medics Mode",extended_features.medics_mode_enabled)
    print_status("4.User Prompt Medics Mode",extended_features.user_prompt_medics_enabled)
    print_status("5.Extended Army Mode",extended_features.extended_army_mode_enabled)
    print("")
    print("6.Help")
    print("7.Go back to previous menu")
    print("8.Exit")
    choice = input("Choose any of the above options to continue:")
    while(not choice.isdigit() or (int(choice) < 1 and int(choice) > 8)):
        choice = input("Invalid Input!!!. Please Enter a valid choice : ")
    choice = int(choice)

    if (choice == 1):
        extended_features.health_mode_enabled = get_game_settings_updated_status("Health",extended_features.health_mode_enabled)
        game_settings()
    elif (choice == 2):
        extended_features.improved_combat_mode_enabled = get_game_settings_updated_status("Improved Combat",extended_features.improved_combat_mode_enabled)
        game_settings()
    elif (choice == 3):
        extended_features.medics_mode_enabled = get_game_settings_updated_status("Medics",extended_features.medics_mode_enabled)
        game_settings()
    elif ( choice == 4):
        extended_features.user_prompt_medics_enabled = get_game_settings_updated_status("User Prompt Medics",extended_features.user_prompt_medics_enabled)
        game_settings()
    elif ( choice == 5):
        extended_features.extended_army_mode_enabled = get_game_settings_updated_status("Extended Army",extended_features.extended_army_mode_enabled)
        game_settings()
    elif (choice == 6):
        display_utilities.print_file("Game_Settings_Help_29566428.txt")
        game_settings()
    elif ( choice == 7):
        display_utilities.main_menu()
    else:
        print(display_utilities.exit_msg)
    return

#Function used to print if a mode is Enabled or not
def print_status(mode_name = "", is_mode_enabled=False):
    if (is_mode_enabled):
        print(mode_name + " : Enabled")
    else:
        print(mode_name + " : Disabled")
    return

#Function used for editing a game settings
def get_game_settings_updated_status(settings_name = "", previous_status = False):
    print("\n")
    print("Press e to enable " + settings_name + " Mode.")
    print("Press d to disable " + settings_name + " Mode.")
    print("Press l to leave " + settings_name + " Mode as it is.")
    choice = input("\nChoose any of the above options : ")
    while (choice != 'e' and choice != 'd' and choice != 'l'):
        choice = input("Invalid Input!!!. Please Enter a valid choice (e/d/l): ")

    if (choice == 'e'):
        return True
    elif (choice == 'd'):
        return False
    return previous_status
