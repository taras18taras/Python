import sys, math
s1=int(input())
s2=int(input())

l=[]; ll=[]

while s1 < s2+1:
	l.insert(-1,str(s1))
	s1+=1

for i in l:
	if len(i) < 6:
		while len(i) < 6:
			i='0'+i;
	ll.insert(-1, i);
del l[0:]

for i in ll:
	if (int(i[0])+int(i[1])+int(i[2])) == (int(i[3])+int(i[4])+int(i[5])):
		l.append(i)

print(len(l))