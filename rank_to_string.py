# ************************************************************************************************************************* #
#   UTC Header                                                                                                              #
#                                                         ::::::::::::::::::::       :::    ::: :::::::::::  ::::::::       #
#      rank_to_string.py                                  ::::::::::::::::::::       :+:    :+:     :+:     :+:    :+:      #
#                                                         ::::::::::::::+++#####+++  +:+    +:+     +:+     +:+             #
#      By: chemicat53 <daumtto53@gmail.com>               ::+++##############+++     +:+    +:+     +:+     +:+             #
#      daumtto53@gmail.com                            +++##############+++::::       +#+    +:+     +#+     +#+             #
#                                                       +++##+++::::::::::::::       +#+    +:+     +#+     +#+             #
#                                                         ::::::::::::::::::::       +#+    +#+     +#+     +#+             #
#                                                         ::::::::::::::::::::       #+#    #+#     #+#     #+#    #+#      #
#      Update: 2021/08/11 20:11:08 by chemicat53          ::::::::::::::::::::        ########      ###      ######## .fr   #
#                                                                                                                           #
# ************************************************************************************************************************* #

import pandas as pd
import numpy as np

df = pd.read_excel("./Rank.xlsx")

arr = df.to_numpy()
print(arr)
print(len(arr))

string_list = arr.tolist()

rank_list = ['1th, 2th, 3th, Initiate, Mentor, Expert, Grand Master, Brawler, Marauder, Fighter, Vanguard, Warrior, Vindicator, Juggernaut, Usurper, Vanquisher, Destroyer, Savior, Overlord, Genbu, Byakko, Seiryu, Suzaku, Mighty Ruler, Revered Ruler, Divine Ruler, Eternal Ruler, Fujin, Raijin, Yaksa, Ryujin, Emperor, Tekken King, Tekken God, True Tekken God, Tekken God Prime, Tekken God Omega']
rank_list
print('------------\n')
for i in range(len(arr)) :
	print(arr[i][0].split('/'))
	rank_list.append(arr[i][0].split('/')[0] + '.')

print(rank_list)

pd_data = pd.DataFrame(rank_list)
pd_data.to_excel(excel_writer='./tekken_rank.xlsx')

