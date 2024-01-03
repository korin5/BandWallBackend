from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from tinydb import TinyDB,Query

class Filter(BaseModel):
    type: str
    province: str|None = None
    city: str|None = None
    district: str|None = None
    insts: List[str]

class Info(BaseModel):
    type: str
    province: str|None = None
    city: str|None = None
    district: str|None = None
    insts: List[str]
    title: str
    description: str

db = TinyDB("data2.json")
table = db.table("Infos")
app = FastAPI()

@app.post("/bandinfos")
async def get_infos(filter:Filter):
    Info = Query()
    # query_data = table.search(Info.type==filter.type and Info.province==filter.province and Info.city==filter.city and Info.district==filter.district and Info.insts.any(filter.insts))
    query_data = table.search((Info.type==filter.type) & (Info.province==filter.province) & (Info.city==filter.city) & (Info.district==filter.district) & (Info.insts.any(filter.insts)))
    search_result = query_data
    return search_result

@app.post("/upload")
async def upload_infos(info:Info):

    description_list = info.description.split("\n")

    index = table.insert({
        "title": info.title,
        "description": description_list,
        "type": info.type,
        "province": info.province,
        "city": info.city,
        "district": info.district,
        "insts": info.insts
    })
    print("添加索引：", index)
