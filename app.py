from fastapi import FastAPI, Path
from typing import List
from pydantic import BaseModel


app = FastAPI()

products = [

    {
        "id": 1,
        "name": "MR-Blue",
        "details": "10 ml • 1400 mAh • Mesh coil • Up to 4000 Puffs • 20mg Salt Nicotine",
        "price": "18",
        "image": "https://i.ibb.co/D72yZmS/MR-Blue.png",
        "undefined": ""
    },
    {
        "id": 2,
        "name": "Peach-Ice",
        "details": "10 ml • 1400 mAh • Mesh coil • Up to 4000 Puffs • 20mg Salt Nicotine",
        "price": "18",
        "image": "https://i.ibb.co/Gp0DpTt/Peach-Ice.png",
        "undefined": ""
    },
    {
        "id": 3,
        "name": "Pink-Lemonade",
        "details": "10 ml • 1400 mAh • Mesh coil • Up to 4000 Puffs • 20mg Salt Nicotine",
        "price": "18",
        "image": "https://i.ibb.co/5sdrj0c/Pink-Lemonade.png",
        "undefined": ""
    },
    {
        "id": 4,
        "name": "Sour-Apple",
        "details": "10 ml • 1400 mAh • Mesh coil • Up to 4000 Puffs • 20mg Salt Nicotine",
        "price": "18",
        "image": "https://i.ibb.co/NS71Q75/Sour-Apple.png",
        "undefined": ""
    },
    {
        "id": 5,
        "name": "Strawberry-Banana",
        "details": "10 ml • 1400 mAh • Mesh coil • Up to 4000 Puffs • 20mg Salt Nicotine",
        "price": "18",
        "image": "https://i.ibb.co/rfXXJHD/Strawberry-Banana.png",
        "undefined": ""
    },
    {
        "id": 6,
        "name": "Apple-Strawberry-Lemon",
        "details": "10 ml • 1400 mAh • Mesh coil • Up to 4000 Puffs • 20mg Salt Nicotine",
        "price": "18",
        "image": "https://i.ibb.co/hmrqPwX/Apple-Strawberry-Lemon.png",
        "undefined": ""
    },
    {
        "id": 7,
        "name": "Strawberry-Raspberry",
        "details": "10 ml • 1400 mAh • Mesh coil • Up to 4000 Puffs • 20mg Salt Nicotine",
        "price": "18",
        "image": "https://i.ibb.co/H4g2ypm/Strawberry-Raspberry.png",
        "undefined": ""
    },
    {
        "id": 8,
        "name": "Watermelon-Ice",
        "details": "10 ml • 1400 mAh • Mesh coil • Up to 4000 Puffs • 20mg Salt Nicotine",
        "price": "18",
        "image": "https://i.ibb.co/6DmSC6V/Watermelon-Ice.png",
        "undefined": ""
    },
    {
        "id": 9,
        "name": "banana-ice",
        "details": "10 ml • 1400 mAh • Mesh coil • Up to 4000 Puffs • 20mg Salt Nicotine",
        "price": "18",
        "image": "https://i.ibb.co/Ns0c1k9/banana-ice.png",
        "undefined": ""
    },
    {
        "id": 10,
        "name": "Berry-Ice",
        "details": "10 ml • 1400 mAh • Mesh coil • Up to 4000 Puffs • 20mg Salt Nicotine",
        "price": "18",
        "image": "https://i.ibb.co/HD2q1wN/Berry-Ice.png",
        "undefined": ""
    },
    {
        "id": 11,
        "name": "Blue-Razz-Cherry",
        "details": "10 ml • 1400 mAh • Mesh coil • Up to 4000 Puffs • 20mg Salt Nicotine",
        "price": "18",
        "image": "https://i.ibb.co/m6LCTnW/Blue-Razz-Cherry.png",
        "undefined": ""
    },
    {
        "id": 12,
        "name": "Blueberry-Raspberry",
        "details": "10 ml • 1400 mAh • Mesh coil • Up to 4000 Puffs • 20mg Salt Nicotine",
        "price": "18",
        "image": "https://i.ibb.co/xDjpVNt/Blueberry-Raspberry.png",
        "undefined": ""
    },
    {
        "id": 13,
        "name": "Gummy-Bear",
        "details": "10 ml • 1400 mAh • Mesh coil • Up to 4000 Puffs • 20mg Salt Nicotine",
        "price": "18",
        "image": "https://i.ibb.co/1L86n18/Gummy-Bear.png",
        "undefined": ""
    },
    {
        "id": 14,
        "name": "Kiwi-Passion-Fruit-Guava",
        "details": "10 ml • 1400 mAh • Mesh coil • Up to 4000 Puffs • 20mg Salt Nicotine",
        "price": "18",
        "image": "https://i.ibb.co/pbtgFdb/Kiwi-Passion-Fruit-Guava.png",
        "undefined": ""
    },
    {
        "id": 15,
        "name": "Lemon-Lime",
        "details": "10 ml • 1400 mAh • Mesh coil • Up to 4000 Puffs • 20mg Salt Nicotine",
        "price": "18",
        "image": "https://i.ibb.co/Q9M9Tn8/Lemon-Lime.png",
        "undefined": ""
    },
    {
        "id": 16,
        "name": "Fresh-Mint",
        "details": "10 ml • 1400 mAh • Mesh coil • Up to 4000 Puffs • 20mg Salt Nicotine",
        "price": "18",
        "image": "https://i.ibb.co/tLM9S1V/Fresh-Mint.png",
        "undefined": ""
    },
    {
        "id": 17,
        "name": "Cola-Ice",
        "details": "10 ml • 1400 mAh • Mesh coil • Up to 4000 Puffs • 20mg Salt Nicotine",
        "price": "18",
        "image": "https://i.ibb.co/Y21v62Z/Cola-Ice.png",
        "undefined": ""
    },
    {
        "id": 18,
        "name": "Bull-Ice",
        "details": "10 ml • 1400 mAh • Mesh coil • Up to 4000 Puffs • 20mg Salt Nicotine",
        "price": "18",
        "image": "https://i.ibb.co/RCTQn1b/Bull-Ice.png",
        "undefined": ""
    }

]


class Student(BaseModel):
    id: int
    name: str
    details: str
    price: int


@app.get("/")
async def root():
    return {
        'example': 'this is an example', 'data': 0}


@app.get("/products/", response_model=List[dict])
def get_products():
    return products
