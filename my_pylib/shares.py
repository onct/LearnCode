def marry(age, appearance, money):
    if age < 25 and appearance > 90 and money > 1000000:
        print('我要嫁给你！')
    elif age >= 25 and appearance <= 90 and money <= 1000000:
        print('不嫁!')
    else:
        print('哎！嫁了吧！')


def attack(one_life, one_attack, two_life, two_attack):
    while one_life > 0 and two_life > 0:
        one_life -= two_attack
        two_life -= one_attack
    if one_life > 0:
        print('亚瑟胜利')
    elif two_life > 0:
        print('阿珂胜利')
    elif two_life <= 0 and one_life <= 0:
        4
        print('同归于尽')


if __name__ == "__main__":
    dage = 12
    dappearance = 2
    dmoney = 3
    marry(dage, dappearance, dmoney)
    yase_life = 150
    yase_attack = 12
    ake_life = 100
    ake_attack = 15
    attack(yase_life, yase_attack, ake_life, ake_attack)
    starts = '王一博 李现 杨紫 肖战 易烊千玺 关晓彤 李现 杨紫 肖战 易烊千玺 王一博 关晓彤 肖战 李现'
    line = starts.split()
    time = 0
    for i in line:
        if i == '肖战':
            time += 1
    print(time)
    infos = {'哈登': '123456', '詹姆斯': '456789', '字母哥': '666666'}
    print('回车后输入密码')
    name = input()
    passwd = input()
    if infos.get(name):
        if(infos.get(name) == passwd):
            print('login success')
        else:
            print('login failed,password is error')
    else:
        print('no user')
