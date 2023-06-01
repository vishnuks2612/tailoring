from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import sessions, messages



# Create your views here.
from django.db.models import Max

from .models import *


def index(request):
    products = Product.objects.all()
    context = {'details': products}
    return render(request,'myapp/index.html', context)



def admin_home(request):
    if 'admin_id' in request.session:
        return render(request,'myapp/admin_home.html')
    else:
        return redirect('admin_login')


def contact_us(request):
    return render(request, 'myapp/contact_us.html')




def user_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')
        try:
            ul = user_login.objects.get(uname=uname, passwd=passwd, u_type='user')
            request.session['user_id'] = ul.id
            request.session['user_name'] = ul.uname
            return     redirect('user_home')
        except user_login.DoesNotExists:
            messages.error(request, 'Invalid Credentials')
            return redirect('user_login')
    else:
        return render(request, 'myapp/user_login.html')




def user_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        uname=email
        


        ul = user_login(uname=uname, passwd=password, u_type='user')


        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = user_details(user_id=user_id,fname=fname, lname=lname,addr=addr, pin=pin, contact=contact, email=email )
        ud.save()

        print(user_id)
        context = {'msg': 'User Registered'}
        return render(request, 'myapp/user_login.html',context)

    else:
        return render(request, 'myapp/user_details_add.html')


def user_home(request, slug=None):

    if 'user_id' in request.session:

        if slug != None:
            category = get_object_or_404(Category, slug=slug)
            products = Product.objects.filter(category=category).order_by('-id')
        
        else:
            products = Product.objects.all().order_by('-id')
            
            
            
        context = {'details': products}
        return render(request,'myapp/user_home.html',context)
    
    else:
        return redirect('user_login')


def user_feedback(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            user = request.POST.get('user')
            message = request.POST.get('message')

            feed = Feedback(user=user, message=message)
            feed.save()

            return render(request, 'myapp/user_feedback.html')
        else:
            return render(request, 'myapp/user_feedback.html')
    else:
        return redirect('user_login')



def view_feedback(request):
    if 'admin_id' in request.session:
        feedbacks = Feedback.objects.all()
        context = {'feedbacks':feedbacks}

        return render(request, 'myapp/admin_view_feedback.html', context)
    else:
        return redirect('admin_login')


def admin_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        try:
            ul = user_login.objects.get(uname=un, passwd=pwd, u_type='admin')
            request.session['user_name'] = ul.uname
            request.session['admin_id'] = ul.id
            return redirect('admin_home')
        except user_login.DoesNotExist:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, 'myapp/admin_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, 'myapp/admin_login.html',context)



def user_details_update(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            user_id = request.session['user_id']
            up = user_details.objects.get(user_id=int(user_id))

            fname = request.POST.get('fname')
            lname = request.POST.get('lname')

            addr = request.POST.get('addr')
            pin = request.POST.get('pin')
            contact = request.POST.get('contact')


            up.fname = fname
            up.lname = lname
            up.addr = addr
            up.pin = pin
            up.contact = contact

            up.save()


            context = {'msg': 'User Details Updated','up':up}
            return render(request, 'myapp/user_details_update.html',context)

        else:
            user_id = request.session['user_id']
            up = user_details.objects.get(user_id=int(user_id))
            context={'up':up}
            return render(request, 'myapp/user_details_update.html',context)
    else:
        return redirect('user_login')
    


def admin_logout(request):
    try:
        del request.session['user_name']
        del request.session['admin_id']
    except:
        return admin_login(request)
    else:
        return admin_login(request)
    
    

def user_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return user_login_check(request)
    else:
        return user_login_check(request)






def admin_user_details(request):
    if 'admin_id' in request.session:
        jm_l = user_details.objects.all()
        context = {'user_list': jm_l}
        return render(request, 'myapp/admin_userdetails_view.html', context)
    else:
        return redirect('admin_login')





def user_changepassword(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            uname = request.session['user_name']
            new_password = request.POST.get('new_password')
            current_password = request.POST.get('current_password')
            print("username:::" + uname)
            print("current_password" + str(current_password))

            try:

                ul = user_login.objects.get(uname=uname, passwd=current_password)

                if ul is not None:
                    ul.passwd = new_password  # change field
                    ul.save()
                    context = {'msg':'Password Changed Successfully'}
                    return render(request, 'myapp/user_changepassword.html',context)
                else:
                    context = {'msg': 'Password Not Changed'}
                    return render(request, 'myapp/user_changepassword.html', context)
            except user_login.DoesNotExist:
                context = {'msg': 'Password Not Changed'}
                return render(request, 'myapp/user_changepassword.html', context)
        else:
            return render(request, 'myapp/user_changepassword.html')
    else:
        return redirect('user_login')


def product_add(request):
    if 'admin_id' in request.session:
        if request.method == 'POST':

            u_file = request.FILES['img']
            

            p = request.POST.get('title')
            d = request.POST.get('desc')
            pr = request.POST.get('price')
            slug = request.POST.get('category')

            category = get_object_or_404(Category, slug=slug)

            pd = Product(product_name=p, desc=d, price=pr, image=u_file, category=category)
            pd.save()

            context = {'msg': 'product added'}
            return render(request, 'myapp/admin_product_add.html', context)

        else:
            categories = Category.objects.all()
            context = {'categories': categories}
            return render(request, 'myapp/admin_product_add.html', context)
    else:
        return redirect('admin_login')


def admin_product_details_view(request):
    if 'admin_id' in request.session:
        products = Product.objects.all()
        context = {'details': products}
        return render(request, 'myapp/admin_product_details_view.html', context)
    else:
        return redirect('admin_login')


def admin_purchase_view(request):
    if 'admin_id' in request.session:
        view_purchase = purchase.objects.all()
        context = {'details': view_purchase}
        return render(request, 'myapp/admin_purcahse_details_view.html', context)
    else:
        return redirect('admin_login')


def admin_product_update(request):
    if 'admin_id' in request.session:
        if request.method == 'POST':

            id = request.POST.get('id')
            up = Product.objects.get(id=int(id))

            product_name = request.POST.get('product_name')
            desc = request.POST.get('desc')
            price = request.POST.get('price')
            

            up.product_name = product_name
            up.desc = desc
            up.price = price
            up.save()

            msg = 'Product updated'
            up_l = Product.objects.all()
            context = {'details': up_l, 'msg': msg}
            return render(request, 'myapp/admin_product_details_view.html', context)

        else:
            id = request.GET.get('id')
            up = Product.objects.get(id=int(id))
            context = {'up': up}
            return render(request, 'myapp/admin_product_update.html', context)
    else:
        return redirect('admin_login')


def user_add_cart(request, id):
    if 'user_id' in request.session:
        if request.method == 'POST':
            size = request.POST.get('size')
            card = request.POST.get('card')
            number = request.POST.get('number')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            address = request.POST.get('address')
            cvv = request.POST.get('cvv')
            product = get_object_or_404(Product, id=id)
            


            pm = purchase(size=size, card=card, number=number, email=email,mobile=mobile, address=address, cvv=cvv, product=product)
            pm.save()

            context = {'plan_id':pm,'msg':'Record added'}
            return render(request, 'myapp/user_home.html', context)

        else:
            return render(request, 'myapp/user_add_cart.html',{'id':id})
    else:
        return redirect('user_login')






 


