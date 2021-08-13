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
import operator
import random

def input_rawfile_name() :
	print('엑셀 파일은 이 프로그램의 위치와 동일한 위치에 존재해야합니다.\n')
	file_name = input('파일 이름을 확장자(.xlsx)를 제외하고 적어주세요 : ')
	print('\n');
	return (file_name)

def input_member_per_team() :
	mpt = input('한 조에 팀원 몇명? : ')
	print('\n')
	return (mpt)

def input_is_rank_word() :
	is_rank_word = input('계급이 숫자로 되어있으면 1, 계급이 Vindicator, 1st처럼 영어면 2를 입력해주세요')
	print('\n')
	return (int(is_rank_word) == 2)

def create_arr_by_rank(num_per_draw , lst = []) :
	new_list = []
	competitor_count = len(lst)
	member_per_team = num_per_draw
	team_count = int((competitor_count + member_per_team - 1) / member_per_team)
	temp_competitor_count = competitor_count - team_count

	for i in range(team_count) :
		new_list.append(lst[i])
	lst.reverse()
	for i in range(temp_competitor_count) :
		new_list.append(lst[i])
	return (new_list)

# make random list
def	create_arr_by_random(lst = []) :
	new_list = []
	competitor_count = len(lst)

	random_list = random.sample(lst, competitor_count)
	print(random_list)
	return (random_list)

def make_dataframe_list(num_per_draw, lst = []) :
	df_list = []
	competitor_count = len(lst)
	member_per_team = num_per_draw
	team_count = int((competitor_count + member_per_team - 1) / member_per_team)


	row_name = []
	column_name = ['순번', '갤닉', '스팀닉', '계급명', '계급', '계급합평균', '조']

	# dataframe의 배열에서 뭔가 문제가 생긴것같아도, 문제가 생긴게 아님.
	# TODO : df_list를 리턴받은 뒤, df_list의 수만큼 엑셀에 데이터를 입력시키기
	# https://better-than-alone.tistory.com/71
	for i in range(int(competitor_count / member_per_team)) :
		team_list = []
		for j in range(member_per_team) :
			team_list.append(lst[team_count * j + i])
		df_list.append(pd.DataFrame(team_list, columns=column_name))

	if competitor_count % member_per_team != 0 :
		team_list = []
		for i in range(competitor_count % member_per_team) :
			team_list.append(lst[team_count * i + (team_count - 1)])
		df_list.append(pd.DataFrame(team_list, columns=column_name))
	return (df_list)

def append_sumof_rank(member_per_team, lst = []) :
	team_num = 0
	competitor_count = len(lst)
	team_count = int((competitor_count + member_per_team - 1) / member_per_team)

	for i in range(int(competitor_count / member_per_team)) :
		sum = 0
		for j in range(member_per_team) :
			sum += lst[team_count * j + i][4]
		for j in range(member_per_team) :
			lst[team_count * j + i].append(round(sum / member_per_team, 1))
			lst[team_count * j + i].append(str(team_num) + '조')
		team_num += 1

	if competitor_count % member_per_team != 0 :
		sum = 0
		for i in range(competitor_count % member_per_team) :
			sum += lst[team_count * i + (team_count - 1)][4]
		for i in range(competitor_count % member_per_team) :
			lst[team_count * i + (team_count - 1)].append(round(sum / (competitor_count % member_per_team), 1))
			lst[team_count * i + (team_count - 1)].append(str(team_num) + '조')
	return (lst)

def df_list_to_excel(lst = []) :
	new_df = pd.concat(lst)
	new_df.to_excel('./tekken7_draw_complete.xlsx', index=False)





member_per_team = int(input_member_per_team())
df = pd.read_excel(input_rawfile_name() + '.xlsx')
is_rank_word = input_is_rank_word()

# making dict with tekken7 rank. keys : 0 to 36
rank = '1th, 2th, 3th, Initiate, Mentor, Expert, Grand Master, Brawler, Marauder, Fighter, Vanguard, Warrior, Vindicator, Juggernaut, Usurper, Vanquisher, Destroyer, Savior, Overlord, Genbu, Byakko, Seiryu, Suzaku, Mighty Ruler, Revered Ruler, Divine Ruler, Eternal Ruler, Fujin, Raijin, Yaksa, Ryujin, Emperor, Tekken King, Tekken God, True Tekken God, Tekken God Prime, Tekken God Omega'
rank_splited = rank.split(', ')
rank_num = []
for i in range(len(rank_splited)) :
	rank_num.append(i);
rank_dict = dict(zip(rank_splited, rank_num))

arr = df.to_numpy().tolist()

# if rank data is valid, individual's rank data conversion to integer
# else, give all rank's integer data 0

is_draw_type_ranked = (len(arr[0]) == 4)

if is_draw_type_ranked == False:
	for i in range(len(arr)) :
		arr[i].append(0)
else :
	if is_rank_word == True :
		for i in range(len(arr)) :
			arr[i].append(rank_dict[(arr[i][3])])
	else :
		for i in range(len(arr)) :
			arr[i].append(int(arr[i][3]))

sorted_arr = sorted(arr, key=lambda x: x[4], reverse=True)
print('\n\n')
print(sorted_arr)

####################################

rank_list = create_arr_by_rank(member_per_team, sorted_arr)
print(rank_list)

final_draw_list = append_sumof_rank(member_per_team, rank_list)
df_list = make_dataframe_list(member_per_team, final_draw_list)

for i in range(len(df_list)) :
	print(df_list[i])

df_list_to_excel(df_list)
