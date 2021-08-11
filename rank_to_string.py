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

print('------------\n')
for i in range(len(arr)) :
	print(arr[i][0].split('/'))
	rank_list.append(arr[i][0].split('/')[0] + '.')

print(rank_list)

pd_data = pd.DataFrame(rank_list)
pd_data.to_excel(excel_writer='./tekken_rank.xlsx')

