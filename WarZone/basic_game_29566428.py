#Student Name : Jaimon Thyparambil Thomas
#Student ID : 29566428
#Start Date : 17 - 08 - 2018
#Last modified Date : 24 - 08 - 2018

#In this File Basic combat game is implemented with 3 units (Archer , Soldier and Knight)

import extended_combat_game_features_29566428 as extended_features
import combat_game_display_utilities_29566428 as display_utilities

def main():
    # initializing game settings
    extended_features.health_mode_enabled = False
    extended_features.improved_combat_mode_enabled = False
    extended_features.medics_mode_enabled = False
    extended_features.user_prompt_medics_enabled = False
    extended_features.extended_army_mode_enabled = False
    extended_features.is_extended_combat_mode = False

    display_utilities.welcome_screen()
    display_utilities.main_menu()
    return

if(__name__ == "__main__"):
    main()