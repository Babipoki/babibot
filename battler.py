import asyncio

items = {
    0: {
        "name": "balloon",
        "plural": "balloons",
        "sellPrice": 3,
        "sellable": True,
        "tradable": True,
        "spawnRate": 40.5,
        "spawnMin": 1,
        "spawnMax": 8
    },
    1: {
        "name": "dollar",
        "plural": "dollars",
        "sellPrice": 1,
        "sellable": False,
        "tradable": True,
        "spawnRate": 14.5,
        "spawnMin": 1,
        "spawnMax": 20,
        "craft": {

        }
    },
    2: {
        "name" : "bucket of latex",
        "plural" : "buckets of latex",
        "sellPrice": 1,
        "sellable": True,
        "tradable": True,
        "spawnRate": 32.15,
        "spawnMin": 1,
        "spawnMax": 2,
        "craft": {
            "bucket of latex":{
                "result": "balloon",
                "resultQuantity": 1,
                "inputQuantity": [1, 1],
                "itemsLost": ["bucket of latex", "bucket of latex"]
            }
        },
    },
    3: {
        "name": "oak log",
        "plural": "oak logs",
        "sellPrice": 1,
        "sellable": True,
        "tradable": True,
        "spawnRate": 11.45,
        "spawnMin": 1,
        "spawnMax": 3,
        "craft": {
            "saw": {
                "result": "oak plank",
                "resultQuantity": 3,
                "inputQuantity": [1, 1],
                "itemsLost": ["oak log"]
            }
        }
    },
    4: {
        "name": "oak plank",
        "plural": "oak planks",
        "sellPrice": 2,
        "sellable": True,
        "tradable": True,
        "spawnRate": 2.45,
        "spawnMin": 1,
        "spawnMax": 3,
        "craft": {

        }
    },
    5: {
        "name": "saw",
        "plural": "saws",
        "sellPrice": 2,
        "sellable": True,
        "tradable": True,
        "spawnRate": 0.45,
        "spawnMin": 1,
        "spawnMax": 3,
        "craft": {
            "oak log": {
                "result": "oak plank",
                "resultQuantity": 3,
                "inputQuantity": [1, 1],
                "itemsLost": ["oak log"]
            }
        }
    }
}