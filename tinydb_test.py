from tinydb import TinyDB


db = TinyDB("data2.json")
table = db.table("Infos")
index = table.insert_multiple([
    {
        "title": "Atarayo",
        "description": ["A J-Pop Band","招募鼓手"],
        "type": "线下",
        "province": "上海市",
        "city": "上海市",
        "district": "不限",
        "insts": ["架子鼓"]
    },
    {
        "title": "Mygo",
        "description": ["A J-Punk Band","招募键盘手"],
        "type": "线下",
        "province": "上海市",
        "city": "上海市",
        "district": "不限",
        "insts": ["键盘"]
    },
    {
        "title": "OnlineBand",
        "description": ["一个线上乐队","除了吉他，所有乐手都缺"],
        "type": "线上",
        "province": "",
        "city": "",
        "district": "",
        "insts": ["键盘","电贝斯","架子鼓"]
    }])
print("添加索引：", index)
