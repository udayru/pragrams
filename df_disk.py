import subprocess
a = subprocess.run(['df','-h'],shell=True,capture_output=True)
value = a.stdout.decode('utf-8')
value = [i for i in value.split('\n')]
s=[]
for i in range(1,len(value)-1):
	l=[]
	for j in value[i].split(' '):
		if j != '':
			print(j,end=' ')
			l.append(j)
	print()
	s.append(l)
	l=[]
y=[]	
t=0
for i in range(len(s)):
	for j in s:
		if int(s[i][2]) >= t:
			t=int(s[i][2])
			y=[]
			y.append(s[i])
print(f'the more momery used is : {y}')
