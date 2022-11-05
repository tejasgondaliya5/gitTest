from time import perf_counter
from django.core.checks import messages
from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
import smtplib
from win10toast import ToastNotifier
import random
import datetime
# Create your views here.


def login(request):
    if request.POST:
        email = request.POST['Email']
        password = request.POST['Password']

        try: 
            chack=UserDetail.objects.get(Email=email)
            if email == chack.Email:
                if password == chack.Password:
                    try:
                        chack_nurse = Addnurse.objects.get(Email=request.session.get('nurselogin'))
                        if chack_nurse:
                            messages.add_message(request,messages.ERROR,'Nurse account befor logout and try after login')
                            return redirect('login')     
                    except:
                        request.session['userlogin']=email
                        return redirect('usersearch')
                else:
                    messages.add_message(request,messages.ERROR,'Worng Password')
        except:
            try:
                print('step6')
                valid_nurse = Addnurse.objects.get(Nurse_email=email)
                print('hii', valid_nurse)
                if email == valid_nurse.Nurse_email:
                    if password == valid_nurse.Nurse_password:
                        try:
                            chack_user = UserDetail.objects.get(Email=request.session.get('userlogin'))
                            if chack_user:
                                print('step7')
                                messages.add_message(request,messages.ERROR, 'your User account is already login. so befor logut your user account and after try to login.')
                        except:
                            request.session['nurselogin']=email
                            return redirect('detail')
                    else:
                        print('step9')
                        messages.add_message(request,messages.ERROR,'Worng Password')
            except:
                print('step10')
                messages.add_message(request,messages.ERROR,'Worng Email_ID')

    if 'userlogin' in request.session:
        return redirect('usersearch')
    elif 'nurselogin' in request.session:
        return redirect('detail')
    else:
        return render(request, 'login.html')

def forget_password(request):
    if request.POST:
        email = request.POST['Email']
        try:
            data = UserDetail.objects.get(Email=email)
            if data:
                request.session['user_email']=email
                try:
                    otp = random.randint(1000,9999)
                    request.session['otp'] = otp
                    print('otp is',otp)
                    s = smtplib.SMTP('smtp.gmail.com', 587)
                    s.starttls()
                    s.login('tejasgondaliya5@gmail.com', 'Tejas@123')
                    s.sendmail('tejasgondaliya5@gmail.com', email, 'Hello , \n your OTP is {otp}.')
                    s.quit()

                    return redirect('otp')
                except:
                    pass
        except:
            try:
                data = Addnurse.objects.get(Nurse_email=email)
                if data:
                    request.session['nurse_email']=email
                    try:
                        otp = random.randint(1000,9999)
                        request.session['otp'] = otp
                        print('otp2 is',otp)
                        s = smtplib.SMTP('smtp.gmail.com', 587)
                        s.starttls()
                        s.login('tejasgondaliya5@gmail.com', 'Tejas@123')
                        print('inside s.login',email)
                        s.sendmail('tejasgondaliya5@gmail.com', email, 'Hello , \n your OTP is {otp}.')
                        print('inside s.sendemail')
                        s.quit()

                        return redirect('otp')
                    except:
                        print('inside expect')
            except:
                messages.add_message(request,messages.ERROR,'You Email Id is Not Match.')
    return render(request, 'forget.html')

def otp(request):
    if request.POST:
        otp = request.POST['OTP']
        if int(otp) == request.session.get('otp'):
            del request.session['otp']
            return redirect('change_password')
    return render(request,'otp.html')

def change_password(request):
    if request.POST:
        password = request.POST['Password']
        confirm_password = request.POST['Confirm_Password']

        if password == confirm_password:
            try:
                data = UserDetail.objects.get(Email=request.session.get('user_email'))
                data.Password = password
                data.Confirm_password = password
                data.save()
                del request.session['user_email']
                return redirect('login')
            except:
                try:
                    data = Addnurse.objects.get(Nurse_email=request.session.get('nurse_email'))
                    data.Nurse_password = password
                    data.save()
                    del request.session['nurse_email']
                    return redirect('login')
                except:
                    pass
        else:
            messages.add_message(request,messages.ERROR,'Your Passwor and Confirm PAssword Is not matched.')
    return render(request,'change_password.html')

def logout(request):
    try:
        if 'userlogin' in request.session:
            if 'cart' in request.session:
                del request.session['cart']
            del request.session['userlogin']

            return redirect('login')
        
        elif 'nurselogin' in request.session:
            del request.session['nurselogin']
            return redirect('login')

    except:
        pass
def signup(request):
    if request.POST:
        name = request.POST['Name']
        email = request.POST['Email']
        number = request.POST['Number']
        password = request.POST['Password']
        confirm_password = request.POST['Confirm_password']
    
        obj = UserDetail()
        obj.Name = name
        obj.Email = email
        obj.Number = number
        obj.Password = password
        obj.Confirm_password = confirm_password

        if password == confirm_password:
            obj.save()
            return redirect(login)  

        else:
            messages.add_message(request,messages.ERROR,'Your Password and Confirm_Password is Not Match.')
    return render(request, 'signup.html')

def usersearch(request):
    # agar session create hu to
    if 'Dentist' in request.session:
        del request.session['Dentist']
        
    elif 'Orthopedic' in request.session:
        del request.session['Orthopedic']

    elif 'Homeyopethic' in request.session:
        del request.session['Homeyopethic']

    # first time he to
    if request.POST:
        Specialist = request.POST['Specialist']

        if Specialist=='Dentist':
            request.session['Dentist'] = spacialist
            return redirect('applynurse')
        
        elif Specialist=='Homeyopethic':
            request.session['Homeyopethic'] = spacialist
            return redirect('applynurse')
        
        elif Specialist=='Orthopedic':
            request.session['Orthopedic'] = spacialist
            return redirect('applynurse')
        
        else:
            messages.add_message(request,messages.ERROR,'Plese select any option.')
        
    name = UserDetail.objects.get(Email=request.session.get('userlogin'))
    request.session['cart']="tejasgondaliya0@gmail.com"
    return render(request, 'user/usersearch.html',{'data':name})

def applynurse(request):
    name = UserDetail.objects.get(Email=request.session.get('userlogin'))
    if 'Dentist' in request.session:
        data = Addnurse.objects.filter(Nurse_specialist='Dentist')
        k = 0
        List = []
        try:
            for i in data:
                print('id is',data[k])
                data1 = Addnurse.objects.get(Nurse_name = data[k])
                data2 = Setshedule.objects.get(join_N=data1)
                List.append(data2)
                k+=1
        except:
            if list:
                pass
            else:
                messages.add_message(request,messages.ERROR,'Nurse Is Not Available')
        
        return render(request, 'user/applynurse.html',{'data':data, 'time':List, 'name':name})

    elif 'Homeyopethic' in request.session:
        data = Addnurse.objects.filter(Nurse_specialist='Homeyopethic')
        k = 0
        List = []
        try:
            for i in data:
                print('id is',data[k])
                data1 = Addnurse.objects.get(Nurse_name = data[k])
                data2 = Setshedule.objects.get(join_N=data1)
                List.append(data2)
                k+=1
        except:
            messages.add_message(request,messages.ERROR,'Nurse Is Not Available')

        return render(request, 'user/applynurse.html',{'data':data, 'time':List, 'name':name})

    elif 'Orthopedic' in request.session:
        data = Addnurse.objects.filter(Nurse_specialist='Orthopedic')
        k = 0
        List = []
        try:
            for i in data:
                print('id is',data[k])
                data1 = Addnurse.objects.get(Nurse_name = data[k])
                data2 = Setshedule.objects.get(join_N=data1)
                List.append(data2)
                k+=1
        except:
            messages.add_message(request,messages.ERROR,'Nurse Is Not Available')
            
        return render(request, 'user/applynurse.html',{'data':data, 'time':List, 'name':name})

def booknurse(request,A):
    name = UserDetail.objects.get(Email=request.session.get('userlogin'))
    getid = Addnurse.objects.get(id=A)
    print('passing value is',getid)
    if request.POST:
        Name = request.POST['Book_name']
        specialist = request.POST['Book_specialist']
        Email = request.POST['Book_email']
        Expirence  = request.POST['Book_expirence']
        Fees = request.POST['Book_fees']
        message = request.POST['Message1']
        username = UserDetail.objects.get(Email=request.session.get('userlogin'))
        nurse_object = Addnurse.objects.get(Nurse_email = Email)
        shedule_object = Setshedule.objects.get(join_N = nurse_object)

        obj = Cart()
        obj.joinuser = username
        obj.joinNurse = nurse_object
        obj.joinshedule = shedule_object
        obj.Message = message

        obj.save()

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('tejasgondaliya5@gmail.com', 'Tejas@123')
        s.sendmail('tejasgondaliya5@gmail.com', Email, f'Dear {Name}, \n you have one Noification From {name.Name}. So you have Accept this Pationt Request So open Nursing Home Website And Accept Request.')
        s.quit()
        return redirect ('status')
        
    return render(request, 'user/booknurse.html',{'data':getid, 'name':name})

def status(request):
    show_user = UserDetail.objects.get(Email = request.session.get('userlogin'))
    show_cart = Cart.objects.filter(joinuser=show_user)
    show_date = Setshedule.objects.all()
    date = datetime.date.today()
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")
    for i in show_date:
        print('time is', time)
        print('date is', date)
        print('time database is',i.Start_time)
        print('date database is',i.Date)
        if date >= i.Date:
            if time >= str(i.Start_time):
                show_date.delete()
        else:
            pass
    return render(request, 'user/status.html', {'name': show_user, 'data':show_cart})
    
def deleteshedule(request,B):
    d1 = Cart.objects.get(id=B)
    d1.delete()
    if 'cart' in request.session:
        del request.session['cart']
        return redirect('status')
    else:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('tejasgondaliya5@gmail.com', 'Tejas@123')
        s.sendmail('tejasgondaliya5@gmail.com', d1.joinuser.Email, f'Dear {d1.joinuser.Name}, \n you have one Noification From {d1.joinNurse.Nurse_name}. Your have Sent Request from {d1.joinNurse.Nurse_specialist} Nurse. But {d1.joinNurse.Nurse_name} is cancel Your request. So We Suggest you have look Another Nurse. \n Thanks.')
        s.quit()
        return redirect('chackShedule')

def addnurse(request):
    if request.POST:
        Name = request.POST['Nurse_name']
        Specialist = request.POST['Nurse_specialist']
        Email = request.POST['Nurse_email']
        Number = request.POST['Nurse_number']
        Expirence  = request.POST['Nurse_expirence']
        Fees = request.POST['Nurse_fees']
        Password = request.POST['Nurse_password']

        obj = Addnurse()
        obj.Nurse_name = Name
        obj.Nurse_specialist = Specialist
        obj.Nurse_email = Email
        obj.Nurse_number = Number
        obj.Nurse_expirence = Expirence
        obj.Nurse_fees = Fees
        obj.Nurse_password = Password

        obj.save()
        print(Specialist)
        return redirect('login')
    return render(request, 'owner/owner.html',{'active1':'active'})

def nursedatabase(request):
    list_nurse = Addnurse.objects.all()
    return render(request, 'owner/nurse_database.html',{'data': list_nurse,'active1':'active'})

def userdatabase(request):
    list_user = UserDetail.objects.all()
    return render(request, 'owner/user_database.html',{'data': list_user,'active1':'active'})

def nursedetail(request):
    data = Addnurse.objects.get(Nurse_email=request.session.get('nurselogin'))

    if request.POST:
        name = request.POST['Name']
        date = request.POST['Date']
        root = request.POST['Root']
        start_time = request.POST['Start_time']
        end_time = request.POST['End_time']

        nursedetail = Addnurse.objects.get(Nurse_email=request.session.get('nurselogin'))
        obj = Setshedule()
        obj.join_N = nursedetail

        obj.Date = date
        obj.Root = root
        obj.Start_time = start_time
        obj.End_time = end_time

        obj.save()
        return redirect('detail')
    return render(request, 'nurse/detail.html',{'active1':'active', 'data':data})

def changeShedule(request):
    name = Addnurse.objects.get(Nurse_email=request.session.get('nurselogin'))
    data = Setshedule.objects.filter(join_N=name)
    return render(request, 'nurse/change_shedule.html',{'name':name, 'data':data})

def changedetail(request, D):
    data = Setshedule.objects.get(id=D)
    if request.POST:
        name = request.POST['Name']
        date = request.POST['Date']
        root = request.POST['Root']
        start_time = request.POST['Start_time']
        end_time = request.POST['End_time']

        nursedetail = Addnurse.objects.get(Nurse_email=request.session.get('nurselogin'))
        
        data.join_N = nursedetail

        data.Date = date
        data.Root = root
        data.Start_time = start_time
        data.End_time = end_time

        data.save()
        return redirect('changeShedule')
    return render(request, 'nurse/change_detail.html',{'data':data})

def deletenurse(request,E):
    data = Setshedule.objects.get(id=E)
    data.delete()
    return redirect('changeShedule')

def pationtnotify(request):
    if 'nurselogin' in request.session:
        data = Addnurse.objects.get(Nurse_email = request.session.get('nurselogin'))
        data1 = Cart.objects.filter(joinNurse = data, Trigger=0)
        # msg = messages.add_message(request,messages.SUCCESS, 'You Have Success Fully Accepted.')
    return render(request,'nurse/pationt_notify.html',{'active1':'active','name':data, 'data':data1})

def show(request, C):
    data = Addnurse.objects.get(Nurse_email=request.session.get('nurselogin'))
    # data1 = UserDetail.objects.get(id=C)
    data2 = Cart.objects.get(id=C)
    print(data2)
    if 'Delete' in request.POST:
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login('tejasgondaliya5@gmail.com', 'Tejas@123')
            s.sendmail('tejasgondaliya5@gmail.com', data2.joinuser.Email, f'Dear {data2.joinuser.Name}, \n you have one Noification From {data2.joinNurse.Nurse_name}. Your have Sent Request from {data2.joinNurse.Nurse_specialist} Nurse. But {data2.joinNurse.Nurse_name} is cancel Your request. So We Suggest you have look Another Nurse. \n Thanks.')
            s.quit()
            data2.delete()
            return redirect('alert')
        except:
            messages.add_message(request,messages.ERROR,'Please Chack Youe InterNet Connection.')
    
    if 'Accept' in request.POST:
        print('Accept')
        try:
            data = Addnurse.objects.get(Nurse_email=request.session.get('nurselogin'))
            data2.Trigger = 1
            data2.save()
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login('tejasgondaliya5@gmail.com', 'Tejas@123')
            s.sendmail('tejasgondaliya5@gmail.com', data2.joinuser.Email, f'Dear {data2.joinuser.Name}, \n you have one Noification From {data2.joinNurse.Nurse_name}. Your have Sent Request from {data2.joinNurse.Nurse_specialist} Nurse. And {data2.joinNurse.Nurse_name} is Accept Your request. So Nurse is contect Coming soon... \n Thanks.')
            s.quit()
            return redirect('chackShedule')
        
        except:
            messages.add_message(request,messages.ERROR,'Please chack your Internet Connection')

    return render(request, 'nurse/show.html',{'active1':'active', 'data':data2 ,'name':data})

def chack_shedule(request):
    data = Addnurse.objects.get(Nurse_email=request.session.get('nurselogin'))
    data1 = Cart.objects.filter(joinNurse=data,Trigger=1)

    return render(request, 'nurse/chack_shedule.html', {'active1':'active','name':data, 'data':data1})
