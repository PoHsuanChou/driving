country = input('你是哪國人？')
age  = input('請問你幾歲？')
age = int(age)
if country == '台灣':
	if age >=18:
		print('你可以考駕照')
	else:
		print('你不能腦駕照')
elif country == '美國':
	if age >= 16:
		print('你可以開車')
	else:
		print('你不能開車')
