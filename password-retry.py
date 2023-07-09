cnt = 3
password = 'a123456'
while cnt > 0 :
	tmp = input('請輸入密碼：')
	if tmp != password:
		cnt -= 1
		if cnt == 0:
			break
		print('密碼錯誤！還有', cnt,'次機會')
		continue
	else:
		print('登入成功！')
		break