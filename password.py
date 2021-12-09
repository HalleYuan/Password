password = 'a123456'
i = 3 #定義i的次數，剩餘可輸入錯誤的機會
while True:
    pwd = input('請輸入密碼') 
    if pwd == password:
        print('登入成功!')
        break #逃出迴圈
    else:
        i = i - 1 
        print('密碼錯誤! 還有' , i  ,'次機會')
        if i == 0: 
            break #如果嘗試了3次，就會終止程式
