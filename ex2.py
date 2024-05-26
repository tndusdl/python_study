while True:
    print('음료목록 1.오렌지주스(100원), 2.커피(200원), 3.콜라(300원)')
    coin = int(input('동전을 넣으세요: '))
    drink = int(input('음료를 고르세요: '))
    
    if drink == 1:
        # 오렌지주스 100원
        if coin >= 100:
            remain = coin - 100
            print('오렌지주스가 곧 제공됩니다.')
            print('거스름돈은 {}원입니다.'.format(remain))
        else:
            print('잔액이 부족합니다.')
    elif drink == 2:
        # 커피 200원
        if coin >= 200:
            remain = coin - 200
            print('커피가 곧 제공됩니다.')
            print('거스름돈은 {}원입니다.'.format(remain))
        else:
            print('잔액이 부족합니다.')
    elif drink == 3:
        # 콜라 300원
        if coin >= 300:
            remain = coin - 300
            print('콜라가 곧 제공됩니다.')
            print('거스름돈은 {}원입니다.'.format(remain))
        else:
            print('잔액이 부족합니다.')
    else:
        # 없는번호
        print('없는 메뉴입니다. 다시 입력해 주세요.')
