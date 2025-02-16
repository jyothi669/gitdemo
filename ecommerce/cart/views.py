
from itertools import product


from django.shortcuts import render, redirect

from shop.models import Product

from cart.models import Cart


# Create your views here.

def addtocart(request,i):
    u=request.user
    p=Product.objects.get(id=i)
    try:
        c=Cart.objects.get(user=u,product=p)
        c.quantity+=1
        c.save()
        p.stock-=1
        p.save()

    except:
        if(p.stock):
            c=Cart.objects.create(user=u,product=p,quantity=1)
            c.save()
            p.stock-=1
            p.save()
    return redirect('cart:cartview')


def cartview(request):
    u=request.user
    c=Cart.objects.filter(user=u)
    total=0
    for i in c:
        total+=i.quantity*i.product.price
    context={'cart':c,'total':total}
    return render(request,'addtocart.html',context)

def cartdecrement(request,i):
    p=Product.objects.get(id=i)
    u=request.user
    try:
        c = Cart.objects.get(user=u, product=p)
        if (c.quantity>1):
            c.quantity -= 1
            c.save()
            p.stock += 1
            p.save()
        else:
            c.delete()
            p.stock+=1
            p.save()

    except:
        pass
    return redirect('cart:cartview')

def cartdelete(request,i):
    p = Product.objects.get(id=i)
    u = request.user
    try:
        c = Cart.objects.get(user=u, product=p)
        c.delete()
        p.stock=p.stock+c.quantity
        p.save()

    except:
        pass
    return redirect('cart:cartview')

from cart.models import Payment,OrderDetails
import razorpay
def order_form(request):
    if(request.method=="POST"):
        a=request.POST['a']
        pn=request.POST['p']
        n=request.POST['n']
        u=request.user
        c=Cart.objects.filter(user=u)
        total=0
        for i in c:
            total+=i.quantity*i.product.price

        total=int(total)

        client=razorpay.Client(auth=('rzp_test_g7R6RTEIfQ1wTm','1wjfzQyh4kELvTrgldIYJlNp'))
        response_payment=client.order.create(dict(amount=total*100,currency='INR'))
        print(response_payment)
        order_id=response_payment['id']
        status=response_payment['status']
        if (status=="created"):
            p=Payment.objects.create(name=u.username,amount=total,order_id=order_id)
            p.save()
            for i in c:
                o=OrderDetails.objects.create(product=i.product,user=i.user,phone=pn,pin=n,address=a,order_id=order_id,no_of_items=i.quantity)
                o.save()
            context={'payment':response_payment,'name':u.username}
            return render(request,"payment.html",context)
    return render(request,'orderform.html')

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login

@csrf_exempt
def payment_status(request,p):
    user=User.objects.get(username=p)
    login(request,user)

    response=request.POST
    print(response)

    param_dict={
        'razorpay_order_id':response['razorpay_order_id'],
        'razorpay_payment_id':response['razorpay_payment_id'],
        'razorpay_signature':response['razorpay_signature']

    }
    client=razorpay.Client(auth=('rzp_test_g7R6RTEIfQ1wTm','1wjfzQyh4kELvTrgldIYJlNp'))
    try:
        status=client.utility.verify_payment_signature(param_dict)
        print(status)
        p=Payment.objects.get(order_id=response['razorpay_order_id'])
        print(p)
        p.paid=True
        p.razorpay_payment_id=response['razorpay_payment_id']
        p.save()

        o=OrderDetails.objects.filter(order_id=response['razorpay_order_id'])
        print(o)
        for i in o:
            i.payment_status="completed"
            i.save()

        c=Cart.objects.filter(user=user)
        c.delete()

    except:
        pass

    return render(request,'payment_status.html')

def your_orders(request):
    u=request.user
    o=OrderDetails.objects.filter(user=u,payment_status="completed")
    context={'orders':o}

    return render(request,'your_orders.html')







