import websockets
import asyncio

async def test_ws():
    async with websockets.connect("ws://127.0.0.1:8000/ws") as websocket:
        print("Connexion réussie !")

asyncio.run(test_ws())
