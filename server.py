from sanic import Sanic, response
from managers.mongo import Mongo

app = Sanic("Earn_burn")

@app.get("/")
async def hello(request):
    return response.json({"data":"Hello world!"})

@app.post("/consume_webhook")
async def consume_webhook(request):
    payload = request.json
    print(Mongo.push_queue(payload))
    return response.json({"data":'success'})