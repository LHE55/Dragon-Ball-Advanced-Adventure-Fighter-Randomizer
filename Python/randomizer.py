# This is a randomizer file for the Simple Randomizer Maker.
# This file must be named randomizer.py in order to work.

from inspect import Attribute
from random import Random, shuffle, randint, normalvariate
from classes import *

def value(name):
	for att in Attributes:
		if att.name == name:
			return att
	print("This attribute does not exist: "+name)
	return None

########################
# EDIT BELOW THIS LINE #
########################

Program_Name = "Dragon Ball Advance Adventure Fighter Randomizer"
Rom_Name = "Dragon Ball Advance Adventure ROM (EU)"
Rom_File_Format = "gba" # File format (nes, gba, etc.)
Rom_Hash = None
About_Page_Text = "V: 1.0 Made by LHE "
Timeout = 100
Slow_Mode = False



Attributes = [

# Requirements for Level Loading and Stuff

	Attribute(
		name="Flying_Level_For_Everyone", #All Character can do Flying Level and load correct in Levels with start Cutscene
		addresses=[0x016ECB],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		
	Attribute(
		name="All_Characters_Load", #All Characters Load correct, no matter if unlocked
		addresses=[0x011E96],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		
	Attribute(
		name="All_Characters_Start_Cutscene", #All Characters have start Cutscene
		addresses=[0x011996],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0045], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		
	Attribute(
		name="Mid Cutscenes", #All Characters have Mid Cutscenes
		addresses=[0x0271f6],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0045], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		
	Attribute(
		name="All_Characters_End_Cutscene", #All Characters have End Cutscene
		addresses=[0x0271AA],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0045], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
	Attribute(
		name="Krillin_Does_Not_Start_own_Fight", #All Characters have End Cutscene
		addresses=[0x0270EE],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0045], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		
	Attribute(
		name="Always_Load_Map_Goku_1", #Always load the normal Story Mode Map no matter the charakter part 1
		addresses=[0x0FF2AA],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0045], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		
	Attribute(
		name="Always_Load_Map_Goku_2", #Always load the normal Story Mode Map no matter the charakter part 2
		addresses=[0x0FF28C],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0045], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		
	Attribute(
		name="Map_Icon_Goku", #Set the Map Icon to Goku no matter the charakter
		addresses=[0x0FF232],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0045], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		
	Attribute(
		name="Map_Unlocked", #Unlocks the whole map 
		addresses=[0x0FF19C],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x1128], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled="Levels_Unlocked",
                ),
		
	Attribute(
		name="Progress Assumed", #Does not start level 1 directly
		addresses=[0x0F2578],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0xFF], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		
		
		# Character per Cutscenes START
	Attribute(
		name="Change_Char_Per_Cutscene_Preperation_1", #Prepares to Set the Character based on the Level Start Cutscenes
		addresses=[0x0C864E],
		number_of_bytes=4,
		is_little_endian=False,
		possible_values=[0xD6F214FA], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		
	Attribute(
		name="Change_Char_Per_Cutscene_Preperation_2", #Prepares to Set the Character based on the Level Start Cutscenes
		addresses=[0x101FE2],
		number_of_bytes=34,
		is_little_endian=False,
		possible_values=[0x012D08D09CF26DFDECF84CE00000309F020275F70F080348CA30002501709CF260FD], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		
	Attribute(
		name="Change_Char_Per_Cutscene_Preperation_3", #Prepares to Set the Character based on the Level Start Cutscenes
		addresses=[0x39EB34],
		number_of_bytes=96,
		is_little_endian=False,
		possible_values=[0x01210125C2E702210125BFE703210125BCE704210125B9E705210125B6E706210125B3E707210125B0E708210125ADE709210125AAE70A210125A7E70B210125A4E70C210125A1E70D2101259EE70E2101259BE70F21012598E72021012595E7], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		
	Attribute(
		name="Change_Char_Per_Cutscene_Preperation_4", #Prepares to Set the Character based on the Level Start Cutscenes
		addresses=[0x39EA7A],
		number_of_bytes=82,
		is_little_endian=False,
		possible_values=[0x474680B48146012857D01E2858D0042859D021285AD025285BD029285CD02F285DD04A285ED037285FD0382860D03B2861D0522862D03E2863D0412864D0432865D0542866D063F58FFA48464D4629F5C3FD], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		
		#Char Changes
		
	Attribute(
		name="Change_Char_Cutscene_1", #Change Char Gokus House
		addresses=[0x39EB34],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		
	Attribute(
		name="Change_Char_Cutscene_2", #Change Char Oolong
		addresses=[0x39EB3A],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0,1,2,3,4,5,6,7,8,9,10,12,14,15,16,17,18,19,20,21,22,24,25,26,27,29], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name="Change_Char_Cutscene_3", #Change Char Yamcha
		addresses=[0x39EB40],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name="Change_Char_Cutscene_4", #Change Char based on Cutscene
		addresses=[0x39EB46],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name="Change_Char_Cutscene_5", #Change Char based on Cutscene
		addresses=[0x39EB4C],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name="Change_Char_Cutscene_6", #Change Char based on Cutscene
		addresses=[0x39EB52],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name="Change_Char_Cutscene_7", #Change Char based on Cutscene
		addresses=[0x39EB58],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name="Change_Char_Cutscene_8", #Change Char Korin Minigame (No Bear Thief, No Krillin)
		addresses=[0x39EB5E],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name="Change_Char_Cutscene_9", #Change Char based on Cutscene
		addresses=[0x39EB64],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0,1,2,3,4,5,6,7,8,9,10,12,14,15,16,17,18,19,20,21,22,24,25,26,27,29], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name="Change_Char_Cutscene_10", #Change Char based on Cutscene
		addresses=[0x39EB6A],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name="Change_Char_Cutscene_11", #Change Char based on Cutscene
		addresses=[0x39EB70],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name="Change_Char_Cutscene_12", #Change Char based on Cutscene
		addresses=[0x39EB76],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name="Change_Char_Cutscene_13", #Change Char Above City
		addresses=[0x39EB7C],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0,1,2,3,4,5,6,7,8,9,10,12,14,15,16,17,18,19,20,21,22,24,25,26,27,29], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name="Change_Char_Cutscene_14", #Change Char Yajirobies Prairie
		addresses=[0x39EB82],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name="Change_Char_Cutscene_15", #Change Char Chow Castle
		addresses=[0x39EB88],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name="Change_Char_Cutscene_16", #Change Char based on Cutscene Fire Mountain
		addresses=[0x39EB8E],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0,1,2,3,7,9,13,14,15,16,17,18,19,20,25,27], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		
		# Gerade nur Regular Difficulty, kann man auf alle ausweiten!
		Attribute(
		name="Own_Char_Battle_01", #Change Own Char in the 21st World Tournament all difficulties
		addresses=[0XE896BC,0xE896CC,0xE896DC,0xE8997C,0xE8998C,0xE8999C,0xE89C3C,0xE89C4C,0xE89C5C],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0,1,2,3,4,5,6,7,8,9,10], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name="Own_Char_Battle_02", #Change Own Char in the Tao Fights
		addresses=[0xE896EC, 0xE899AC, 0xE89C6C, 0xE896FC, 0xE899BC, 0xE89C7C],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0,1,2,3,4,5,6,7,8,9,10], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name="Own_Char_Battle_03", #Change Own Char in the Gohan Fight
		addresses=[0xE8970C, 0xE899CC, 0xE89C8C],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0,1,2,3,4,5,6,7,8,9,10], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name="Own_Char_Battle_04", #Change Own Char in the 22nd
		addresses=[0xE8971C, 0xE899DC, 0xE89C9C, 0xE8972C, 0xE899EC, 0xE89CAC, 0xE8973C, 0xE899FC, 0xE89CBC],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0,1,2,3,4,5,6,7,8,9,10], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name="Own_Char_Battle_05", #Change Own Char in Piccolo Fights
		addresses=[0xE8974C, 0xE89A0C, 0xE89CCC, 0xE8975C, 0xE89A1C, 0xE89CDC],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0,1,2,3,4,5,6,7,8,9,10], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name="Own_Char_Battle_06", #Change Own Char in the Training
		addresses=[0xE896AC, 0xE8996C, 0xE89C2C, 0xE8993C, 0xE89BFC, 0xE89EBC, 0xE8994C, 0xE89C0C, 0xE89ECC, 0xE8995C, 0xE89C1C, 0xE89EDC],
		number_of_bytes=1,
		is_little_endian=False,
		possible_values=[0,1,2,3,4,5,6,7,10], # unused since min_value and max_value are used
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),

				# Level Change Highjump bei 1_2
		Attribute(
		name= "Level_Change_1_2_A", #Level Change if not Goku
		addresses=[0x91ACD8],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0100,0x0800], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_B", #Level Change if not Goku
		addresses=[0x91ABE8],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0100,0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_C", #Level Change if not Goku
		addresses=[0x91AAF8],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0100,0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_D", #Level Change if not Goku
		addresses=[0x91ACDA],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0100,0x0801], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_E", #Level Change if not Goku
		addresses=[0x91ABEA],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0100,0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_F", #Level Change if not Goku
		addresses=[0x91AAFA],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0100,0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_G", #Level Change if not Goku
		addresses=[0x91AA0A],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0100,0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_H", #Level Change if not Goku
		addresses=[0x91A91A],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0100,0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_I", #Level Change if not Goku
		addresses=[0x91A82A],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0100,0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_J", #Level Change if not Goku
		addresses=[0x91A55C],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000,0x0100], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_K", #Level Change if not Goku
		addresses=[0x919568],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x7F01,0x0F01], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_L", #Level Change if not Goku
		addresses=[0x91956A],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x7F01,0x3C01], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_M", #Level Change if not Goku
		addresses=[0x919476],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x1101,0x1201], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_N", #Level Change if not Goku
		addresses=[0x919478],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x7F01,0x0300], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_O", #Level Change if not Goku
		addresses=[0x91947A],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x7F01,0x1101], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_P", #Level Change if not Goku
		addresses=[0x919386],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0901,0x3F01], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_Q", #Level Change if not Goku
		addresses=[0x919388],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x5E01,0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_R", #Level Change if not Goku
		addresses=[0x91938A],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x7F01,0x6101], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_S", #Level Change if not Goku
		addresses=[0x919296],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x2F00,0x3F01], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_T", #Level Change if not Goku
		addresses=[0x919298],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x2E00,0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_U", #Level Change if not Goku
		addresses=[0x91929A],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x7F01,0x6101], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_V", #Level Change if not Goku
		addresses=[0x9191A8],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x6101,0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_W", #Level Change if not Goku
		addresses=[0x9191AA],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x7F01,0x3401], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_X", #Level Change if not Goku
		addresses=[0x9190B8],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0901,0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_Y", #Level Change if not Goku
		addresses=[0x9190BA],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x5E01,0x3401], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_Z", #Level Change if not Goku
		addresses=[0x918FC8],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x2F00,0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_AA", #Level Change if not Goku
		addresses=[0x918FCA],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x2E00,0x3401], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_AB", #Level Change if not Goku
		addresses=[0x918CFA],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000,0x2F00], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_AC", #Level Change if not Goku
		addresses=[0x918CFC],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000,0x1901], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_AD", #Level Change if not Goku
		addresses=[0x918DEA],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000,0x0901], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_AE", #Level Change if not Goku
		addresses=[0x918EDC],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x5E01,0x7F01], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_1_2_AF", #Level Change if not Goku
		addresses=[0x918DEC],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x2E00,0x5801], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
# Level 7-3 High Jump
		Attribute(
		name= "Level_Change_7_3_A", #Level Change if not Goku
		addresses=[0x9D03CC],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0100], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_7_3_B", #Level Change if not Goku
		addresses=[0x9D02DC],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0100], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_7_3_C", #Level Change if not Goku
		addresses=[0x9CF10C],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0A00], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_7_3_D", #Level Change if not Goku
		addresses=[0x9CF01C],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0A00], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_7_3_E", #Level Change if not Goku
		addresses=[0x9CEF2C],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x8702], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
# Level 7-2 Chokepoint
		Attribute(
		name= "Level_Change_7_2_A", #Level Change if not Goku
		addresses=[0x9BFE5E],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_7_2_B", #Level Change if not Goku
		addresses=[0x9BFFC6],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x3900], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_7_2_C", #Level Change if not Goku
		addresses=[0x9BF4FA],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x3900], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_7_2_D", #Level Change if not Goku
		addresses=[0x9BE2F2],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_7_2_E", #Level Change if not Goku
		addresses=[0x9BE3A4],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_7_2_F", #Level Change if not Goku
		addresses=[0x9BE3A6],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0xF900], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_7_2_G", #Level Change if not Goku
		addresses=[0x9BE45A],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x3700], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_7_2_H", #Level Change if not Goku
		addresses=[0x9BE50E],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x5300], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_7_2_I", #Level Change if not Goku
		addresses=[0x9BDA42],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x5300], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_7_2_J", #Level Change if not Goku
		addresses=[0x9BD98E],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x3700], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),

# Level 4-B Chokepoint
		Attribute(
		name= "Level_Change_4_B_A", #Level Change if not Goku
		addresses=[0x959A7A],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_B_B", #Level Change if not Goku
		addresses=[0x959A7C],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_B_C", #Level Change if not Goku
		addresses=[0x959C80],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x3900], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_B_D", #Level Change if not Goku
		addresses=[0x959D80],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x3900], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_B_E", #Level Change if not Goku
		addresses=[0x9586FA],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0xAC00], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_B_F", #Level Change if not Goku
		addresses=[0x9586FC],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0xAC00], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_B_G", #Level Change if not Goku
		addresses=[0x958880],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0xE001], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_B_H", #Level Change if not Goku
		addresses=[0x958900],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x2302], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_B_I", #Level Change if not Goku
		addresses=[0x958980],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0xE001], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_B_J", #Level Change if not Goku
		addresses=[0x958A00],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x2302], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),

# Level 4-3
		Attribute(
		name= "Level_Change_4_3_A", #Level Change if not Goku
		addresses=[0x956AA0],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x3900], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_3_B", #Level Change if not Goku
		addresses=[0x956AA2],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x3900], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_3_C", #Level Change if not Goku
		addresses=[0x956AA4],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x3900], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_3_D", #Level Change if not Goku
		addresses=[0x9552E8],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x2302], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_3_E", #Level Change if not Goku
		addresses=[0x9552EA],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x2302], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_3_F", #Level Change if not Goku
		addresses=[0x9552EC],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x2302], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_3_G", #Level Change if not Goku
		addresses=[0x956772],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_3_H", #Level Change if not Goku
		addresses=[0x956774],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_3_I", #Level Change if not Goku
		addresses=[0x956776],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_3_J", #Level Change if not Goku
		addresses=[0x956778],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_3_K", #Level Change if not Goku
		addresses=[0x95677A],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_3_L", #Level Change if not Goku
		addresses=[0x95677C],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_3_M", #Level Change if not Goku
		addresses=[0x95677E],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_3_N", #Level Change if not Goku
		addresses=[0x954EBA],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0xAC00], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_3_O", #Level Change if not Goku
		addresses=[0x954EBC],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0xAC00], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_3_P", #Level Change if not Goku
		addresses=[0x954EBE],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0xAC00], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_3_Q", #Level Change if not Goku
		addresses=[0x954EC0],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0xAC00], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_3_R", #Level Change if not Goku
		addresses=[0x954EC2],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0xAC00], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_3_S", #Level Change if not Goku
		addresses=[0x954EC4],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0xAC00], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_3_T", #Level Change if not Goku
		addresses=[0x954EC6],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0xAC00], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),

# Level 13-1
		Attribute(
		name= "Level_Change_13_1_A", #Level Change if not Goku
		addresses=[0xA45ADE],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_13_1_B", #Level Change if not Goku
		addresses=[0xA45AE0],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_13_1_C", #Level Change if not Goku
		addresses=[0xA4436C],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_13_1_D", #Level Change if not Goku
		addresses=[0xA4436E],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_13_1_E", #Level Change if not Goku
		addresses=[0xA44370],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_13_1_F", #Level Change if not Goku
		addresses=[0xA44372],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_13_1_G", #Level Change if not Goku
		addresses=[0xA44404],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_13_1_H", #Level Change if not Goku
		addresses=[0xA44406],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),

# Level 14-1

		Attribute(
		name= "Level_Change_14_1_A", #Level Change if not Goku
		addresses=[0xA34D8E],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0100], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_14_1_B", #Level Change if not Goku
		addresses=[0xA34E44],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0100], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_14_1_C", #Level Change if not Goku
		addresses=[0xA34E46],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0100], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_14_1_D", #Level Change if not Goku
		addresses=[0xA33DBC],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x2F01], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_14_1_E", #Level Change if not Goku
		addresses=[0xA33DBE],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x2F01], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_14_1_F", #Level Change if not Goku
		addresses=[0xA33D06],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x2F01], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),

# Level 14-2
		Attribute(
		name= "Level_Change_14_2_A", #Level Change if not Goku
		addresses=[0xA3867E],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0100], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_14_2_B", #Level Change if not Goku
		addresses=[0xA38680],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0100], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_14_2_C", #Level Change if not Goku
		addresses=[0xA385C8],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0100], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_14_2_D", #Level Change if not Goku
		addresses=[0xA3839E],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0100], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_14_2_E", #Level Change if not Goku
		addresses=[0xA375F6],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x2F01], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_14_2_F", #Level Change if not Goku
		addresses=[0xA375F8],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x2F01], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_14_2_G", #Level Change if not Goku
		addresses=[0xA37540],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x2F01], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_14_2_H", #Level Change if not Goku
		addresses=[0xA37316],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x2F01], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_14_3_A", #Level Change if not Goku
		addresses=[0xA3BC6A],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0100], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_14_3_B", #Level Change if not Goku
		addresses=[0xA3BC6C],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0100], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_14_3_C", #Level Change if not Goku
		addresses=[0xA3ABE2],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x2F01], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_14_3_D", #Level Change if not Goku
		addresses=[0xA3ABE4],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x2F01], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_14_C_A", #Level Change if not Goku
		addresses=[0xA3E312],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_14_C_B", #Level Change if not Goku
		addresses=[0xA3E31C],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_13_Ball_A", #Level Change if not Goku
		addresses=[0xA46E00],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x3900], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_13_Ball_B", #Level Change if not Goku
		addresses=[0xA45690],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x4301], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_13_Ball_C", #Level Change if not Goku
		addresses=[0xA455FA],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0xCB00], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_9_After_Item_A", #Level Change if not Goku
		addresses=[0xA16C0C],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0100], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_9_After_Item_B", #Level Change if not Goku
		addresses=[0xA150B4],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0300], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),

		Attribute(
		name= "Level_Change_4_2_Down_Jump_A", #Level Change if not Goku
		addresses=[0x95314A],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x3A00], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_2_Down_Jump_B", #Level Change if not Goku
		addresses=[0x951A16],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0xCE00], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_4_2_Down_Jump_C", #Level Change if not Goku
		addresses=[0x951ACA],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x2202], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),

		Attribute(
		name= "Level_Change_9_2_Pitescape_A", #Level Change if not Goku
		addresses=[0xA1297C],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0100], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_9_2_Pitescape_B", #Level Change if not Goku
		addresses=[0xA1120C],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x0300], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_13_1_Robojump_A", #Level Change if not Goku
		addresses=[0xA45DF4],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x3900], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_13_1_Robojump_B", #Level Change if not Goku
		addresses=[0xA44684],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0x4301], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),
		Attribute(
		name= "Level_Change_13_1_Robojump_C", #Level Change if not Goku
		addresses=[0xA445EE],
		number_of_bytes=2,
		is_little_endian=False,
		possible_values=[0xCB00], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),

		Attribute(
		name= "Level_Change_4_3_Chokepoint_Extension", #Level Change if not Goku
		addresses=[0x956670],
		number_of_bytes=16,
		is_little_endian=False,
		possible_values=[0x00000000000000000000000000000000], # First Not Goku, Second Goku
		min_value=None,
		max_value=None,
		lock_if_enabled=None,
		lock_unless_enabled=None,
                ),


]



Required_Rules = [
	# Kein Level Change Bei Goku
	Rule(
		description="XOR Level Change 1-2 Goku_A",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_A"), "==", 0x0100)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_B",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_B"), "==", 0x0100)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_C",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_C"), "==", 0x0100)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_D",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_D"), "==", 0x0100)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_E",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_E"), "==", 0x0100)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_F",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_F"), "==", 0x0100)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_G",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_G"), "==", 0x0100)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_H",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_H"), "==", 0x0100)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_I",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_I"), "==", 0x0100)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_J",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_J"), "==", 0x0000)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_K",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_K"), "==", 0x7F01)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_L",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_L"), "==", 0x7F01)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_M",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_M"), "==", 0x1101)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_N",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_N"), "==", 0x7F01)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_O",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_O"), "==", 0x7F01)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_P",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_P"), "==", 0x0901)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_Q",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_Q"), "==", 0x5E01)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_R",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_R"), "==", 0x7F01)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_S",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_S"), "==", 0x2F00)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_T",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_T"), "==", 0x2E00)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_U",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_U"), "==", 0x7F01)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_V",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_V"), "==", 0x6101)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_W",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_W"), "==", 0x7F01)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_X",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_X"), "==", 0x0901)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_Y",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_Y"), "==", 0x5E01)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_Z",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_Z"), "==", 0x2F00)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_AA",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_AA"), "==", 0x2E00)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_AB",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_AB"), "==", 0x0000)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_AC",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_AC"), "==", 0x0000)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_AD",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_AD"), "==", 0x0000)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_AE",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_AE"), "==", 0x5E01)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),
	Rule(
		description="XOR Level Change 1-2 Goku_AF",
		left_side=[(value("Change_Char_Cutscene_1"), "==", 0), (value("Level_Change_1_2_AF"), "==", 0x2E00)],
		rule_type="count",
		right_side=("==",True,"==",1)
		),






]

#Palette CHange Stages
#Palette_Stage_Adresses = [0x1744B9, 0x176599, 0x174059, 0x177259, 0x174C19, 0x1777B9, 0x175279, 0x176599, 0x1758D9, 0x17D839, 0x175F39, 0x17DE99, 0x176BF9]
#Palette_Stage_Values = [0xF42D97424C06FF7F524A527F5973FF7F6F12EB05B646F42D, 0x3626B9361C43FF7F524A527F5973FF7FFB3EB215772E141E, 0x3626B9361C43FF7F1C43B2159832141E524A527F5973FF7F, 0xEC3238163146FF7FD74118633146FF7F3816B5563146FF7F, 0x133297422656FB676C5EC449B842F42DCE1A75435973FB67, 0x3626B9361C43FF7F314A527FF762FF7F314AF762FA3AFF7F, 0xF42DB8422656CE1A6C5EC449B842F42DF24B75435973FB67, 0x3626B9361C43FF7F524A527F5973FF7FFB3EB215772E141E, 0xED31E636B2117832324AF03DB6213D2ED125352A99321C43, 0x94297D475622DB25F566527F5973FF7FCB267D475622FF7F, 0x524A527F5973FF7FCE3997428E12FF7FCE39BA3E8E12EB15, 0xF42D97424C06BF7F524A7E7E1E7FFF7F6F12EB05B646F42D, 0xF42D97424C06137F6F12EB05B646F42D524A527F5973FF7F, 0x481C112998310859481C0018003C0859481C481C1129085930]
#for i in range(len(Palette_Stage_Adresses)):
#		curr_sprite_attribute = Attribute(
#			name="Palette Stage: " + str(i),
#			addresses= [Palette_Stage_Adresses[i]],
#			number_of_bytes=24,
#			is_little_endian=False,
#			possible_values=Palette_Stage_Values,
#			min_value=None,
#			max_value=None,
#			lock_if_enabled=None,
#			lock_unless_enabled="Palette Shuffle Stages",
#		)
#		Attributes.append(curr_sprite_attribute)



Optional_Rulesets = [
	Ruleset(
		name="Levels_Unlocked",
		description="Unlocks all levels from the beginning. It is necessary to save once. Best way to do that is to go to kamehouse and then open the map again." ,
		rules = [],
		must_be_enabled=None,
		must_be_disabled=None,
	),

	Ruleset(
		name="Always The Same Character In Beat Em Up Levels",
		description="All beat em up levels use the same characater" ,
		rules = [
			Rule(
				description="Always the same character",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="=",
				right_side=None
			),
		],
		must_be_enabled=None,
		must_be_disabled=None,
	),

	Ruleset(
		name="Always The Same Character In 1 V 1 levels",
		description="All 1 V 1 levels use the same character" ,
		rules = [
			Rule(
				description="Always the same character",
				left_side=[value("Own_Char_Battle_01"),value("Own_Char_Battle_02"),value("Own_Char_Battle_03"),value("Own_Char_Battle_04"),value("Own_Char_Battle_05"),value("Own_Char_Battle_06")],
				rule_type="=",
				right_side=None
			),
		],
		must_be_enabled=None,
		must_be_disabled=None,
	),

	Ruleset(
		name="Exclude Characters Beat Em Up Levels",
		description="Exclude specific characters" ,
		rules = [
		],
		must_be_enabled=None,
		must_be_disabled=None,
	),

	Ruleset(
		name="No Goku (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Goku",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 0
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Krillin (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Krillin",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 1
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Yamcha (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Yamcha",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 2
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Bear Thief (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Bear Thief",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 3
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Major Metallitron (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Major Metallitron",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 4
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Ninja Murasaki (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Ninja Murasaki",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 5
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Pirate Robot (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Pirate Robot",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 6
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No General Blue (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No General Blue",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 7
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Pilaf Machine (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Pilaf Machine",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 8
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Shu Machine (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Shu Machine",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 9
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Star Officer Black (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Star Officer Black",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 10
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Oolong (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Oolong",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 11
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Devilman (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Devilman",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 12
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Tambourine (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Tambourine",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 13
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Drum (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Drum",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 14
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Jackie Chun (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Jackie Chun",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 15
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Tien (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Tien",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 16
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Chiaotzu (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Chiaotzu",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 17
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Grandpa Gohan (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Grandpa Gohan",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 18
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No King Piccolo (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No King Piccolo",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 19
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Mercenary Tao (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Grandpa Gohan",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 20
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Giran (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Giran",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 21
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Nam (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Nam",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 22
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Boar Bandit (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Nam",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 24
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Red Ribbon Army Dog Soldier (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Nam",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 25
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Dog-Wolf (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Dog-Wolf",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 26
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Small Pilaf Machine (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Small Pilaf Machine",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 27
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Flying Camrea(Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Flying Camera",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 28
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Ukulele (Beat Em Up)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Ukulele",
				left_side=[value("Change_Char_Cutscene_1"),value("Change_Char_Cutscene_2"),value("Change_Char_Cutscene_3"),value("Change_Char_Cutscene_4"),value("Change_Char_Cutscene_5"),value("Change_Char_Cutscene_6"),value("Change_Char_Cutscene_7"),value("Change_Char_Cutscene_8"),value("Change_Char_Cutscene_9"),value("Change_Char_Cutscene_10"),value("Change_Char_Cutscene_11"),value("Change_Char_Cutscene_12"),value("Change_Char_Cutscene_13"),value("Change_Char_Cutscene_14"),value("Change_Char_Cutscene_15")],
				rule_type="!=",
				right_side= 29
			),
		],
		must_be_enabled="Exclude Characters Beat Em Up Levels",
		must_be_disabled=None,
	),

	Ruleset(
		name="Exclude Characters 1 V 1 Levels",
		description="Exclude specific characters" ,
		rules = [
		],
		must_be_enabled=None,
		must_be_disabled=None,
	),

	Ruleset(
		name="No Goku (1 V 1)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Goku 1 V 1",
				left_side=[value("Own_Char_Battle_01"),value("Own_Char_Battle_02"),value("Own_Char_Battle_03"),value("Own_Char_Battle_04"),value("Own_Char_Battle_05"),value("Own_Char_Battle_06")],
				rule_type="!=",
				right_side= 0
			),
		],
		must_be_enabled="Exclude Characters 1 V 1 Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Jacky Chun (1 V 1)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Jacky Chun 1 V 1",
				left_side=[value("Own_Char_Battle_01"),value("Own_Char_Battle_02"),value("Own_Char_Battle_03"),value("Own_Char_Battle_04"),value("Own_Char_Battle_05"),value("Own_Char_Battle_06")],
				rule_type="!=",
				right_side= 1
			),
		],
		must_be_enabled="Exclude Characters 1 V 1 Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Tien (1 V 1)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Tien 1 V 1",
				left_side=[value("Own_Char_Battle_01"),value("Own_Char_Battle_02"),value("Own_Char_Battle_03"),value("Own_Char_Battle_04"),value("Own_Char_Battle_05"),value("Own_Char_Battle_06")],
				rule_type="!=",
				right_side= 2
			),
		],
		must_be_enabled="Exclude Characters 1 V 1 Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Mercenary Tao (1 V 1)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Mercenary Tao 1 V 1",
				left_side=[value("Own_Char_Battle_01"),value("Own_Char_Battle_02"),value("Own_Char_Battle_03"),value("Own_Char_Battle_04"),value("Own_Char_Battle_05"),value("Own_Char_Battle_06")],
				rule_type="!=",
				right_side= 3
			),
		],
		must_be_enabled="Exclude Characters 1 V 1 Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Grandpa Gohan (1 V 1)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Grandpa Gohan 1 V 1",
				left_side=[value("Own_Char_Battle_01"),value("Own_Char_Battle_02"),value("Own_Char_Battle_03"),value("Own_Char_Battle_04"),value("Own_Char_Battle_05"),value("Own_Char_Battle_06")],
				rule_type="!=",
				right_side= 4
			),
		],
		must_be_enabled="Exclude Characters 1 V 1 Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Krillin (1 V 1)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Krillin 1 V 1",
				left_side=[value("Own_Char_Battle_01"),value("Own_Char_Battle_02"),value("Own_Char_Battle_03"),value("Own_Char_Battle_04"),value("Own_Char_Battle_05"),value("Own_Char_Battle_06")],
				rule_type="!=",
				right_side= 5
			),
		],
		must_be_enabled="Exclude Characters 1 V 1 Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No King Piccolo (1 V 1)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No King Piccolo 1 V 1",
				left_side=[value("Own_Char_Battle_01"),value("Own_Char_Battle_02"),value("Own_Char_Battle_03"),value("Own_Char_Battle_04"),value("Own_Char_Battle_05"),value("Own_Char_Battle_06")],
				rule_type="!=",
				right_side= 6
			),
		],
		must_be_enabled="Exclude Characters 1 V 1 Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Cyborg Tao (1 V 1)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Cyborg Tao 1 V 1",
				left_side=[value("Own_Char_Battle_01"),value("Own_Char_Battle_02"),value("Own_Char_Battle_03"),value("Own_Char_Battle_04"),value("Own_Char_Battle_05"),value("Own_Char_Battle_06")],
				rule_type="!=",
				right_side= 7
			),
		],
		must_be_enabled="Exclude Characters 1 V 1 Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Giran (1 V 1)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Giran 1 V 1",
				left_side=[value("Own_Char_Battle_01"),value("Own_Char_Battle_02"),value("Own_Char_Battle_03"),value("Own_Char_Battle_04"),value("Own_Char_Battle_05"),value("Own_Char_Battle_06")],
				rule_type="!=",
				right_side= 8
			),
		],
		must_be_enabled="Exclude Characters 1 V 1 Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Nam (1 V 1)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Nam 1 V 1",
				left_side=[value("Own_Char_Battle_01"),value("Own_Char_Battle_02"),value("Own_Char_Battle_03"),value("Own_Char_Battle_04"),value("Own_Char_Battle_05"),value("Own_Char_Battle_06")],
				rule_type="!=",
				right_side= 9
			),
		],
		must_be_enabled="Exclude Characters 1 V 1 Levels",
		must_be_disabled=None,
	),
	Ruleset(
		name="No Chiaotzu (1 V 1)",
		description="Exclude specific characters" ,
		rules = [
			Rule(
				description="No Chiaotzu 1 V 1",
				left_side=[value("Own_Char_Battle_01"),value("Own_Char_Battle_02"),value("Own_Char_Battle_03"),value("Own_Char_Battle_04"),value("Own_Char_Battle_05"),value("Own_Char_Battle_06")],
				rule_type="!=",
				right_side= 10
			),
		],
		must_be_enabled="Exclude Characters 1 V 1 Levels",
		must_be_disabled=None,
	),

]




