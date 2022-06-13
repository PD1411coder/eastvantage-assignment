from fastapi import APIRouter

from models.address import Address
from config.db import conn
from schemas.address import addressEntity, addressEntityList
from bson import ObjectId
from getDistance import getDistance

address = APIRouter()

@address.get("/")
async def find_all():
    print(conn.local.user.find())
    print(addressEntityList(conn.local.address.find()))
    return addressEntityList(conn.local.address.find())

@address.post("/")
async def add_new(address: Address):
    if address.lat is None or address.lng is None:
        return {"error": "Latitude and Longitude are required"}
    if address.lat < -90 or address.lat > 90:
        return {"error": "Latitude must be between -90 and 90"}
    if address.lng < -180 or address.lng > 180:
        return {"error": "Longitude must be between -180 and 180"}
    conn.local.address.insert_one(dict(address))
    return addressEntityList(conn.local.address.find())


@address.put("/{id}")
async def update_address(id, address: Address):
    if address.lat is None or address.lng is None:
        return {"error": "Latitude and Longitude are required"}
    if address.lat < -90 or address.lat > 90:
        return {"error": "Latitude must be between -90 and 90"}
    if address.lng < -180 or address.lng > 180:
        return {"error": "Longitude must be between -180 and 180"}
    conn.local.address.find_one_and_update({"_id": ObjectId(id)},{'$set': dict(address)})
    return addressEntity(conn.local.address.find_one({"_id": ObjectId(id)}))


@address.delete("/{id}")
async def update_address(id, address: Address):
    return addressEntity(conn.local.address.find_one_and_delete({"_id": ObjectId(id)}))


@address.get("/range")
async def get_address_range(lat1, lng1, distance):

    lat1 = float(lat1)
    lng1 = float(lng1)
    distance = float(distance)
    if lat1 < -90 or lat1 > 90:
        return {"error": "Latitude must be between -90 and 90"}
    if lng1 < -180 or lng1 > 180:
        return {"error": "Longitude must be between -180 and 180"}
    
    if distance < 0:
        return {"error": "Distance must be greater than 0"}
    
    
    for address in conn.local.address.find():
        if getDistance(lat1, lng1, address["lat"], address["lng"]) <= distance:
            print(addressEntity(address))
            return addressEntity(address)
