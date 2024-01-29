from django.shortcuts import render,redirect
from ecomapp.models import Product, Categories,Filter_Price,Color,Brand, Contact_us,Order,OrderItem
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
import razorpay

client=razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def BASE(request):
    return render(request, 'main/base.html')

def Home(request):
    product = Product.objects.filter(status='PUBLISH')

    context= {
        'product':product,
    }
    return render(request,'main/index.html',context)


def PRODUCT(request):
    product = Product.objects.filter(status='PUBLISH')
    categories= Categories.objects.all()
    filter_price=Filter_Price.objects.all()
    color=Color.objects.all()
    brand=Brand.objects.all()

    CATID=request.GET.get('categories')
    PRICE_FILTER_ID=request.GET.get('filter_price')
    COLOR_ID=request.GET.get('color')
    BRAND_ID=request.GET.get('brand')
    ATOZID=request.GET.get('ATOZ')
    ZTOAID=request.GET.get('ZTOA')
    PRICE_LOWTOHIGHID=request.GET.get('PRICE_LOWTOHIGH')
    PRICE_HIGHTOLOWID=request.GET.get('PRICE_HIGHTOLOW')
    SORT_NEWID=request.GET.get('SORTBY_NEW')
    SORT_OLDID=request.GET.get('SORTBY_OLD')
    if CATID:
        product = Product.objects.filter(categories=CATID, status='PUBLISH')
    elif PRICE_FILTER_ID:
        product=Product.objects.filter(filter_price=PRICE_FILTER_ID, status='PUBLISH')
    
    elif COLOR_ID:
        product=Product.objects.filter(color=COLOR_ID, status='PUBLISH')
    elif BRAND_ID:
        product=Product.objects.filter(brand=BRAND_ID,status='PUBLISH')
    elif ATOZID:
        product=Product.objects.filter(status='PUBLISH').order_by('name')
    elif ZTOAID:
        product=Product.objects.filter(status='PUBLISH').order_by('-name')
    elif PRICE_LOWTOHIGHID:
        product=Product.objects.filter(status='PUBLISH').order_by('price')
    elif PRICE_HIGHTOLOWID:
        product=Product.objects.filter(status='PUBLISH').order_by('-price')
    elif SORT_NEWID:
        product=Product.objects.filter(status='PUBLISH', condition='NEW').order_by('id')
    elif SORT_OLDID:
        product=Product.objects.filter(status='PUBLISH', condition='OLD').order_by('-id')   
    else:
        product = Product.objects.filter(status='PUBLISH')
    

    context= {
        'product':product,
        'categories':categories,
        'filter_price':filter_price,
        'color':color,
        'brand':brand,
    }
    return render(request, 'main/product.html', context)

def SEARCH(request):
    query=request.GET.get('query')
    product=Product.objects.filter(name__icontains= query)
    context={
        'product':product,
    }
    return render(request, 'main/search.html',context)

def PRODUCT_DETAIL_PAGE(request,id):
    prod=Product.objects.filter(id=id).first()

    context={
        'prod':prod,
    }

    return render(request,'main/product_single.html',context)

def Contact_Page(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        contact=Contact_us(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
       
        subject=subject
        message=message
        email_from= settings.EMAIL_HOST_USER
        try:
            send_mail(subject,message,email_from,['rahul.sharma@codeclouds.co.in'])
            contact.save()
            return redirect('Home')
        except:
            return redirect('contact')

    return render(request,'main/contact.html')


def HandleRegister(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get(' pass2')

        customer=User.objects.create_user(username,email,pass1)
        customer.first_name=first_name
        customer.last_name=last_name
        customer.save()
        return redirect('login')
    return render(request, 'main/registration/auth.html')

def HandleLogin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')


        user=authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            return redirect('login')
    return render(request, 'main/registration/auth.html')

def HandleLogout(request):
    logout(request)
    
    return redirect('Home')



@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("Home")


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')

def Checkout(request):
    
    return render(request,'cart/checkout.html')


def PLACE_ORDER(request):
    if request.method=='POST':
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(id=uid)
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        country=request.POST.get('country')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        postcode=request.POST.get('postcode')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        order_id=request.POST.get('order_id')
        payment=request.POST.get('paymnet')
        amount=request.POST.get('amount')
        print(uid,user,firstname, lastname,country,address,city,state)
        order=Order(
            user=user,
            firstname=firstname,
            lastname=lastname,
            country=country,
            address=address,
            city=city,
            state=state,
            postcode=postcode,
            phone=phone,
            email=email,
            payment_id=order_id,
            amount=amount,
        )
        
    return render(request,'cart/placeorder.html')

def THANKS(request):
    
    return render(request,'cart/thank_you.html')