from vibora import Vibora, client
from vibora.responses import JsonResponse
from aiocache import cached, MemcachedCache

app = Vibora()


@cached()
async def fetch_currency_data():
    response = await client.get('https://google.com/')


def convert_currency(sourceCurrency, destinationCurrency):
    return {'result': result}


@app.route('/')
def handle_conversion_request():
    data = fetch_currency_data()
    return JsonResponse(convert_currency(data["sourceCurrency"], data["destinationCurrency"]))


if __name__ == '__main__':
    app.run(debug=True)
