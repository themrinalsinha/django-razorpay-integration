from django.conf import settings
from requests    import post
from json        import loads

def create_order(order):
    response = post(settings.API_URL + 'orders',
                data = {'amount'   : '1000',
                        'currency' : 'INR',
                        'receipt'  : order,
                        'payment_capture' : '1'})
    response = loads(response.text)
    return response