import os
from vibora import Vibora, client
from vibora.responses import JsonResponse
from aiocache import cached, MemcachedCache
from aiocache.serializers import JsonSerializer
app = Vibora()

FIXER_URI = "https://data.fixer.io/api/latest?access_key={}&base=USD"
API_KEY = os.environ("FIXER_API_KEY")

URI = FIXER_URI.format(API_KEY)


@cached(ttl=86500, cache=MemcachedCache, serializer=JsonSerializer(), namespace="wocc")
async def fetch_currency_data():
    return await client.get(URI)


def convert_currency(sourceCurrency, destinationCurrency):
    return {'result': 245}


@app.route('/')
async def handle_conversion_request():
    data = await fetch_currency_data()
    return JsonResponse(convert_currency(data["sourceCurrency"], data["destinationCurrency"]))


if __name__ == '__main__':
    app.run(debug=True)
