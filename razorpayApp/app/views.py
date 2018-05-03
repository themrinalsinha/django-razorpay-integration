from django.shortcuts import render
from django.conf      import settings

from .razorpay        import create_order

# Create your views here.
def home(request):
    payment_id = ''
    if request.POST.get('razorpay_payment_id', '/'):
        payment_id = request.POST.get('razorpay_payment_id')

    order_id    = 'O1234' # will change everytime.
    rp_order_id = create_order(order_id)['id']
    print("===============", rp_order_id)


    data = { 'COMPANY' : 'Warlock Inc.',
             'NAME'    : 'Mrinal Sinha',
             'EMAIL'   : 'mail@themrinalsinha.com',
             'MOBILE'  : '9099477241',
             'AMOUNT'  : '1000',
             'RP_ORDER_ID' : rp_order_id,
             'RKEY'    : 'rzp_test_lfhUO5Xn2ZIA86', }
    return render(request, 'index.html', {'data' : data, 'payment_id' : payment_id})
