# from django.shortcuts import render, redirect
# from django.conf import settings
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse
# from user_payments.models import UserPayment
# import stripe
# import time
# from store.models.products import Products 


# from django.http import JsonResponse
# from django.views.decorators.http import require_POST

# # Initialize Stripe with your API keys
# stripe.api_key = settings.STRIPE_SECRET_KEY

# @require_POST
# @csrf_exempt
# def checkout(request):
#     try:
#         # Create a new Stripe Checkout Session
#         session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=[
#                 {
#                     'price_data': {
#                         'currency': 'usd',
#                         'unit_amount': int(products|total_cart_price:request.session.cart * 100),  # Amount in cents
#                         'product_data': {
#                             'name': 'Your Product Name',  # Replace with your product name
#                         },
#                     },
#                     'quantity': 1,
#                 },
#             ],
#             mode='payment',
#             success_url=settings.STRIPE_SUCCESS_URL,
#             cancel_url=settings.STRIPE_CANCEL_URL,
#         )

#         return JsonResponse({'sessionId': session.id})
#     except Exception as e:
#         return JsonResponse({'error': str(e)})

# # This view handles the payment successful redirect (settings.STRIPE_SUCCESS_URL)
# def payment_successful(request):
#     return render(request, 'payment_successful.html')

# # This view handles the payment canceled redirect (settings.STRIPE_CANCEL_URL)
# def payment_cancelled(request):
#     return render(request, 'payment_cancelled.html')



# # # Create your views here.
# # @login_required(login_url='login')

# # class Cart(View):
# #     def get(self , request):
# #         ids = list(request.session.get('cart').keys())
# #         products = Products.get_products_by_id(ids)
# #         print(products)
# #         return render(request , 'cart.html' , {'products' : products} )
		
# # 		def post(self,request):
					
# # 		mode = Stripe.Product.all()
# #     # def post(self,request):
# #     #     ids = list(request.session.get('cart').keys())
# #     #     products = Products.get_products_by_id(ids)
# #     #     checkout_session = stripe.checkout.Session.create
# # 		# 		(
# #     #       payment_method_types = ['card'],
          
# #     #       p_price = products
# #     #       print(products)
# #     #       line_items = [
# #     #         {
# #     #           'price': settings.PRODUCT_PRICE,
# #     #           'quantity':1,
# #     #         },
# #     #       ],
# #     #       mode = 'payment',
# #     #       customer_creation = 'always',
# #     #       success_url = settings.REDIRECT_DOMAIN + '/payment_successful?session_id={CHECKOUT_SESSION_ID}',
# #     #       cancel_url =settings.REDIRECT_DOMAIN + '/payment_cancelled',
# #     #     )
# #     #     return redirect(checkout_session.url,code=303)
		
# #     #   return render(request,'user_payment/product_page.html')

# # def payment_successful(request):
# #   stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
# #   checkout_session_id = request.GET.get('session_id',None)
# #   session = stripe.checkout.Session.retrive(checkout_session_id)
# #   customer = stripe.Customer.retrive(session.customer)
# #   user_id = request.user.user_id
# #   user_payment = UserPayment.objects.get(app_user=user_id)
# #   user_payment.stripe_checkout_id = checkout_session_id
# #   user_payment.save()
# #   return render(request,'user_payments/payment_successful.html',{'customer:',customer})


# # def payment_cancelled(request):
# # 	stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
# # 	return render(request, 'user_payment/payment_cancelled.html')


# # @csrf_exempt
# # def stripe_webhook(request):
# # 	stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
# # 	time.sleep(10)
# # 	payload = request.body
# # 	signature_header = request.META['HTTP_STRIPE_SIGNATURE']
# # 	event = None
# # 	try:
# # 		event = stripe.Webhook.construct_event(
# # 			payload, signature_header, settings.STRIPE_WEBHOOK_SECRET_TEST
# # 		)
# # 	except ValueError as e:
# # 		return HttpResponse(status=400)
# # 	except stripe.error.SignatureVerificationError as e:
# # 		return HttpResponse(status=400)
# # 	if event['type'] == 'checkout.session.completed':
# # 		session = event['data']['object']
# # 		session_id = session.get('id', None)
# # 		time.sleep(15)
# # 		user_payment = UserPayment.objects.get(stripe_checkout_id=session_id)
# # 		user_payment.payment_bool = True
# # 		user_payment.save()
# # 	return HttpResponse(status=200)