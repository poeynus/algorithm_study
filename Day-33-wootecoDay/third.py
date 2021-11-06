def solution(ings, menu, sell):

    ings_dict = {}
    menu_dict = {}
    sell_dict = {}
    answer = 0
    for i in ings:
        a, b = i.split()
        ings_dict[a] = b

    for i in menu:
        a, b, c = i.split()
        me_result = 0
        for k, v in ings_dict.items():
            tmp = b.count(k)
            me_result = me_result + tmp * int(v)
        me_result -= int(c)
        menu_dict[a] = me_result
    for i in sell:
        a, b = i.split()
        sell_dict[a] = b

    for k,v in sell_dict.items():
        for jk, jv in menu_dict.items():
            if k in jk:
                answer += jv * int(v)

    return answer * -1

solution(["r 10", "a 23", "t 124", "k 9"],	["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"],	["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"])

# ["r 10", "a 23", "t 124", "k 9"],	["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"],	["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]	1161
# ["x 25", "y 20", "z 1000"],	["AAAA xyxy 15", "TTT yy 30", "BBBB xx 30"],	["BBBB 3", "TTT 2"]	-80