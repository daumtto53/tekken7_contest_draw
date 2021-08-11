# ************************************************************************************************************************* #
#   UTC Header                                                                                                              #
#                                                         ::::::::::::::::::::       :::    ::: :::::::::::  ::::::::       #
#      tekken.py                                          ::::::::::::::::::::       :+:    :+:     :+:     :+:    :+:      #
#                                                         ::::::::::::::+++#####+++  +:+    +:+     +:+     +:+             #
#      By: chemicat53 <daumtto53@gmail.com>               ::+++##############+++     +:+    +:+     +:+     +:+             #
#      daumtto53@gmail.com                            +++##############+++::::       +#+    +:+     +#+     +#+             #
#                                                       +++##+++::::::::::::::       +#+    +:+     +#+     +#+             #
#                                                         ::::::::::::::::::::       +#+    +#+     +#+     +#+             #
#                                                         ::::::::::::::::::::       #+#    #+#     #+#     #+#    #+#      #
#      Update: 2021/08/11 20:11:01 by chemicat53          ::::::::::::::::::::        ########      ###      ######## .fr   #
#                                                                                                                           #
# ************************************************************************************************************************* #

import pandas as pd
import numpy as np

df = pd.read_excel("./tekken.xlsx")



# making dict with tekken7 rank. keys : 0 to 36
rank = '1th, 2th, 3th, Initiate, Mentor, Expert, Grand Master, Brawler, Marauder, Fighter, Vanguard, Warrior, Vindicator, Juggernaut, Usurper, Vanquisher, Destroyer, Savior, Overlord, Genbu, Byakko, Seiryu, Suzaku, Mighty Ruler, Revered Ruler, Divine Ruler, Eternal Ruler, Fujin, Raijin, Yaksa, Ryujin, Emperor, Tekken King, Tekken God, True Tekken God, Tekken God Prime, Tekken God Omega'
rank_splited = rank.split(', ')
rank_num = []
for i in range(len(rank_splited)) :
	rank_num.append(i);
rank_dict = dict(zip(rank_splited, rank_num))
print(rank_dict)

temp_list = []
arr = df.to_numpy().tolist()

# individual's rank data conversion to integer
for i in range(len(arr)) :
	print(rank_dict[(arr[i][3])])
	arr[i].append(rank_dict[(arr[i][3])])
print(arr)
