import os

lis = os.listdir(".")
print(lis)

for i in lis:
	os.rename(i, i.replace(' ', ''))

lis = os.listdir(".")
print(lis)