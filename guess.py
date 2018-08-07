import random

b = input('請決定數字範圍開始值:')
b = int(b)

e = input('請決定數字範圍結束值:')
e = int(e)
r = random.randint(b, e)
counter = 0
while True :
	num = input('請猜數字: ')
	num = int(num)
	if r == num :
		print('第',counter,'次 終於猜對了 YYY')
		break
	else :
		if num < r :
			b = num
		else :
			e = num 
		print('第',counter,'次 猜錯了 Orz，再猜一次!!(',b,'~',e,')')
	counter += 1
