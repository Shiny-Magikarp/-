pokemon_dict ={"妙蛙种子":"草宝可梦，初代御三家，全国编号001",
               "小火龙":"火龙宝可梦，初代御三家，全国编号004",
               "杰尼龟":"水宝可梦，初代御三家，全国编号007",
               "皮卡丘":"黄皮耗子，小智御用宝可梦，全国编号025"}
query = input("请输入您要查询的宝可梦：")
if query in pokemon_dict:
    print("您查询的宝可梦描述如下：")
    print(pokemon_dict[query])
else:
    print("您查询的宝可梦我们暂未收录，敬请谅解")