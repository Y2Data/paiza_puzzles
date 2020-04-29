import sys
dimensions = int(input())

line = sys.stdin.readlines()
table = []
for i in line:
	new_line_lst = i.rstrip().split(" ")
	dot_list = []
	for j in new_line_lst:
		dot = int(j)
		dot_list.append(dot)
	table.append(dot_list)

def get_zero_index(table):
	zero_index = []
	dot1_line, dot2_line = 0, 0
	dot1_col, dot2_col = 0, 0
	for line_i, line in enumerate(table):
		for dot_i, dot in enumerate(line):
			if dot == 0:
				zero_index.append([line_i, dot_i])
	dot1_line, dot2_line = zero_index[0][0], zero_index[1][0]
	dot1_col, dot2_col = zero_index[0][1], zero_index[1][1]
	return dot1_line, dot2_line, dot1_col, dot2_col

dot1_line, dot2_line, dot1_col, dot2_col = get_zero_index(table) #2,1,2,2
zero_dot_1, zero_dot_2 = [dot1_line, dot1_col], [dot2_line, dot2_col]
def get_target(table):
	for line_i, line in enumerate(table):
		for dot_i, dot in enumerate(line):
			if line_i != dot1_line and line_i != dot2_line and dot_i != dot1_col and dot_i != dot2_col:
				return sum(line)
target = get_target(table)

if dot1_col != dot2_col:
	res1, res2 = target, target
	for line in table:
		res1 -= line[dot1_col]
		res2 -= line[dot2_col]
	table[dot1_line][dot1_col] = res1
	table[dot2_line][dot2_col] = res2
	
	

for line in table:
	line_result = ""
	line = str(line)
	for dot in line:
		if dot != "," and dot != "[" and dot != "]":
			line_result += dot
	print(line_result)
	
"""
3

"""