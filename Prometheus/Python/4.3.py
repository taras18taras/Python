import sys

arg="())()(()())(()"
p={parentheses1: "(", parentheses2: ")"}
s1=''
s2=''
if len(arg)%2 != 0:
	print('NO')
	exit(0)
elif arg[0] == ")" or arg[-1] == "(":
	print("NO")
	exit(0)
for i in arg:
	if i == "(":
		s1+=i
	elif i == ")":
		s2+=i
if len(s2) == len(s1):
	print("YES")
else:
	print("NO")