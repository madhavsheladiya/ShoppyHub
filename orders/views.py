from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum

MERCHANT_KEY = '<Enter your paytm merchant-key>'


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            param_dict = {

                'MID': '<Enter your paytm  merchant id>',
                'ORDER_ID': str(order.id),
                'TXN_AMOUNT': str(cart.get_total_price()),
                'CUST_ID': order.email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL': 'http://127.0.0.1:8000/orders/order/handlerequest/'

            }
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'orders/order/paytm.html', {'order': order, 'param_dict': param_dict})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})


@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print("order successful")
        else:
            print("order was not successful because" + response_dict['RESPMSG'])
    return render(request, 'orders/order/paymentstatus.html', {'response': response_dict})
