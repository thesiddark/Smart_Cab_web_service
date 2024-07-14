from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from myapp.models import *



def login (request):
    return render(request,'login_index.html')


def login_Post(request):
    uname=request.POST['textfield']
    password=request.POST['textfield2']
    log=Login.objects.filter(username=uname,password=password)
    if log.exists():
        obj=Login.objects.get(username=uname,password=password)
        request.session['lid']=obj.id
        if obj.type == 'admin':
            return HttpResponse('''<script> alert('Login Successfull');window.location="/myapp/Admin_home/"</script>''')

        else:
            return HttpResponse('''<script> alert('Invalid username or Password');window.location="/myapp/login/"</script>''')
    else:
        return HttpResponse(
            '''<script> alert('Invalid username or Password');window.location="/myapp/login/"</script>''')

def logout(request):
    return redirect('/myapp/login/')

def home(request):
    if request.session['lid'] =="":
        return HttpResponse("You Are Logged Out..")
    return render(request,'home_index.html')

def Admin_change_password(request):
    return render(request,'change password.html')

def Admin_change_password_post(request):
    current_password=request.POST['textfield']
    new_password=request.POST['textfield2']
    confirm_password=request.POST['textfield3']
    lid=request.session['lid']
    log=Login.objects.get(id=lid)
    if log.password==current_password:
        if new_password==confirm_password:
            log.password=confirm_password
            log.save()
            return HttpResponse('''<script> alert('Password changed successfully');window.location="/myapp/login/"</script>''')
        else:
            return HttpResponse('''<script> alert('Password does not match');window.location="/myapp/Admin_change_password/"</script>''')
    else:
        return HttpResponse('''<script> alert('Password does not match');window.location="/myapp/Admin_change_password/"</script>''')

def view_approved_Drivers(request):
    var = Driver.objects.filter(status='approved')
    return render(request, 'view approved drivers.html', {'data': var})

def Search_Approved_driver_post(request):
    pname = request.POST['textfield']
    var = Driver.objects.filter(name__icontains=pname, status='approved')

    return render(request, 'view approved drivers.html', {'data': var})

def view_pending_Drivers(request):
    var = Driver.objects.filter(status='pending')
    return render(request, 'view pending drivers.html', {'data': var})

def driver_pending_post(request):
    Search = request.POST['textfield']
    var = Driver.objects.filter(name__icontains=Search, status='pending')
    return render(request, 'view pending drivers.html', {'data': var})

def approve_Driver(request, id):
    var = Driver.objects.filter(LOGIN=id).update(status='approved')
    varr = Login.objects.filter(pk=id).update(type='driver')
    return HttpResponse(
        '''<script> alert('Approved..');window.location="/myapp/view_pending_Drivers/"</script>''')

def reject_Driver(request,id):
    var = Driver.objects.filter(LOGIN=id).update(status='rejected')
    varr = Login.objects.filter(pk=id).update(type='Rejected')
    return HttpResponse('''<script>alert('Rejected..');window.location="/myapp/view_pending_Drivers/"</script>''')

def view_rejected_Drivers(request):
    var = Driver.objects.filter(status='rejected')
    return render(request, 'view rejected drivers.html', {'data': var})

def Search_rejected_pg_post(request):
    s = request.POST['textfield']
    var = Driver.objects.filter(name__icontains=s, status='rejected')
    return render(request, 'view rejected drivers.html', {'data': var})

def adm_view_ambulance(request):
    res=Ambulance_Driver.objects.filter(status='pending')
    return render(request,'view pending ambulance.html',{'data':res})

def adm_view_ambulance_post(request):
    s=request.POST['textfield']
    res = Ambulance_Driver.objects.filter(name__icontains=s,status='pending')
    return render(request, 'view pending ambulance.html', {'data': res})


def adm_approve_ambulance(request,id):
    var = Ambulance_Driver.objects.filter(LOGIN=id).update(status='approved')
    varr = Login.objects.filter(pk=id).update(type='ambulance')
    return HttpResponse(
        '''<script> alert('Approved..');window.location="/myapp/adm_view_ambulance/"</script>''')

def adm_reject_ambulance(request,id):
    var = Ambulance_Driver.objects.filter(LOGIN=id).update(status='rejected')
    varr = Login.objects.filter(pk=id).update(type='rejected')
    return HttpResponse(
        '''<script> alert('Rejected..');window.location="/myapp/adm_view_ambulance/"</script>''')


def adm_view_approved_ambulance(request):
    res=Ambulance_Driver.objects.filter(status='approved')
    return render(request,'view approved ambulance.html',{'data':res})

def adm_view_approved_ambulance_post(request):
    s=request.POST['textfield']
    res=Ambulance_Driver.objects.filter(name__icontains=s,status='approved')
    return render(request,'view approved ambulance.html',{'data':res})

def adm_view_rejected_ambulance(request):
    res=Ambulance_Driver.objects.filter(status='rejected')
    return render(request,'view rejected ambulance.html',{'data':res})

def adm_view_rejected_ambulance_post(request):
    s=request.POST['textfield']
    res = Ambulance_Driver.objects.filter(name__icontains=s,status='rejected')
    return render(request, 'view rejected ambulance.html', {'data': res})

def adm_view_users(request):
    res=User.objects.all()
    return render(request,'view users.html',{'data':res})

def adm_view_users_post(request):
    s=request.POST['textfield']
    res = User.objects.filter(name__icontains=s)
    return render(request, 'view users.html', {'data': res})


def adm_view_complaint(request):
    res=Complaint.objects.all()
    return render(request,'view_user_complaint.html',{'data':res})

def adm_view_complaint_post(request):
    fdate=request.POST['textfield']
    tdate=request.POST['textfield2']
    res = Complaint.objects.filter(date__range=[fdate,tdate])
    return render(request, 'view_user_complaint.html', {'data': res})

def adm_send_reply(request,id):
    return render(request,'send reply.html',{'id':id})

def adm_send_reply_post(request):
    id=request.POST['id']
    rep=request.POST['ureply']
    res=Complaint.objects.filter(pk=id).update(status='replied',reply=rep)
    return HttpResponse('''<script> alert('Replied..');window.location="/myapp/adm_view_complaint/"</script>''')

def adm_view_feedback(request):
    res=Feedback.objects.all()
    return render(request,'view reviews.html',{'data':res})

def adm_view_feedback_post(request):
    fdate = request.POST['textfield']
    tdate = request.POST['textfield2']
    res = Feedback.objects.filter(date__range=[fdate,tdate])
    return render(request, 'view reviews.html',{'data': res})


#===Driver====================

def and_login(request):
    user = request.POST['username']
    password = request.POST['password']
    res = Login.objects.filter(username=user, password=password)
    print(request.POST)
    if res.exists():
        ress = Login.objects.get(username=user, password=password)
        lid = ress.id
        if ress.type == "driver":
            return JsonResponse({'status': 'ok', 'lid': str(lid),'type':ress.type})
        elif ress.type == "user":
            return JsonResponse({'status': 'ok', 'lid': str(lid),'type':ress.type})
        elif ress.type == "ambulance":
            return JsonResponse({'status': 'ok', 'lid': str(lid),'type':ress.type})
        else:
            return JsonResponse({'status': 'no'})
    else:
        return JsonResponse({'status': 'no'})




def driver_signup_post(request):
    name=request.POST['name']
    dob=request.POST['dob']
    gender=request.POST['gender']
    email=request.POST['email']
    phone=request.POST['phone']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    district=request.POST['district']
    reg=request.POST['regno']
    photo=request.POST['photo']

    import datetime
    import base64
    #
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    a = base64.b64decode(photo)
    fh = open("F:\\project\\web\\smart cab\\media\\driver\\photo\\" + date + ".jpg", "wb")
    # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
    path = "/media/driver/photo/" + date + ".jpg"
    fh.write(a)
    fh.close()

    vproof=request.POST['vproof']
    date1 = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    a1 = base64.b64decode(vproof)
    fh = open("F:\\project\\web\\smart cab\\media\\driver\\proof\\" + date1 + "1.jpg", "wb")
    # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
    path1 = "/media/driver/proof/" + date1 + "1.jpg"
    fh.write(a1)
    fh.close()

    vphoto = request.POST['vphoto']
    date1 = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    a1 = base64.b64decode(vphoto)
    fh = open("F:\\project\\web\\smart cab\\media\\driver\\vphoto\\" + date1 + "2.jpg", "wb")
    # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
    path2 = "/media/driver/vphoto/" + date1 + "2.jpg"
    fh.write(a1)
    fh.close()



    # fs=FileSystemStorage()
    # fn=fs.save(date,photo)
    # path=fs.url(date)
    password = request.POST['password']
    cpassword = request.POST['cpassword']
    lobj = Login()
    lobj.username = email
    lobj.password = cpassword
    lobj.type = 'pending'
    lobj.save()

    uobj = Driver()
    uobj.name = name
    uobj.email = email
    uobj.gender = gender
    uobj.phone = phone
    uobj.email = email
    uobj.dob = dob
    uobj.photo = path
    uobj.proof = path1
    uobj.vphoto = path2
    uobj.place = place
    uobj.post = post
    uobj.pin = pin
    uobj.district = district
    uobj.vnumber = reg
    uobj.LOGIN = lobj
    uobj.status = 'pending'
    uobj.save()
    return JsonResponse({'status': 'ok'})



def driver_view_profile(request):
    lid = request.POST['lid']
    res = Driver.objects.get(LOGIN=lid)
    print(res)
    return JsonResponse({'status': 'ok', 'name': res.name, 'email': res.email, 'phone': res.phone,'gender':res.gender, 'vphoto': res.vphoto,
                         'dob': res.dob, 'photo': res.photo, 'proof': res.proof,'place': res.place,'post': res.post,
                         'pin': res.pin,'vnumber': res.vnumber, 'district': res.district})

def driver_edit_profile(request):
    lid = request.POST['lid']
    name = request.POST['name']
    dob = request.POST['dob']
    gender = request.POST['gender']
    email = request.POST['email']
    phone = request.POST['phone']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    district = request.POST['district']
    reg = request.POST['regno']
    photo = request.POST['photo']
    vproof = request.POST['vproof']
    vphoto = request.POST['vphoto']


    uobj = Driver.objects.get(LOGIN=lid)
    uobj.name = name
    uobj.email = email
    uobj.gender = gender
    uobj.phone = phone
    uobj.email = email
    uobj.dob = dob
    if len(photo)!=0:
        import datetime
        import base64
        #
        date =  datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        a = base64.b64decode(photo)
        fh = open("F:\\project\\web\\smart cab\\media\\driver\\photo\\" + date + ".jpg", "wb")
        # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
        path = "/media/driver/photo/" + date + ".jpg"
        fh.write(a)
        fh.close()
        uobj.photo = path

    if len(vproof)!=0:
        import datetime
        import base64
        date1 =  datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        a1 = base64.b64decode(vproof)
        fh = open("F:\\project\\web\\smart cab\\media\\driver\\proof\\" + date1 + "1.jpg", "wb")
        # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
        path1 = "/media/driver/proof/" + date1 + "1.jpg"
        fh.write(a1)
        fh.close()
        uobj.proof = path1
    if len(vphoto)!=0:
        import datetime
        import base64
        date1 = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        a1 = base64.b64decode(vphoto)
        fh = open("F:\\project\\web\\smart cab\\media\\driver\\vphoto\\" + date1 + "2.jpg", "wb")
        # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
        path2 = "/media/driver/vphoto/" + date1 + "2.jpg"
        fh.write(a1)
        fh.close()
        uobj.vphoto = path2

    uobj.place = place
    uobj.post = post
    uobj.pin = pin
    uobj.district = district
    uobj.vnumber = reg
    uobj.save()
    return JsonResponse({'status': 'ok'})

def driver_view_request(request):
    lid=request.POST['lid']
    res=Driver_Request.objects.filter(DRIVER__LOGIN_id=lid,status="pending")
    l=[]
    print(res)
    for i in res:
        l.append({'id':i.id,'datee':str(i.date),'source':i.source,'destination':i.destination,'uname':i.USER.name,'uphone':i.USER.phone,'uemail':i.USER.email,})
    print(l)
    return JsonResponse({'status':"ok","data":l})

def driver_view_approved_request(request):
    lid = request.POST['lid']
    res = Driver_Request.objects.filter(DRIVER__LOGIN_id=lid,status="approved")
    l = []
    for i in res:
        l.append({'id': i.id, 'datee': str(i.date), 'source': i.source, 'destination': i.destination,'uid':i.USER.id, 'uname': i.USER.name,
                  'uphone': i.USER.phone, 'uemail': i.USER.email,'ulid':i.USER.id })
    print(l)
    return JsonResponse({'status': "ok", "data": l})

def driver_get_user_location(request):
    id=request.POST['id']
    res = User.objects.get(pk=id).LOGIN_id
    print(res)
    var = {'latitude':'', 'longitude':''}
    if Location.objects.filter(LOGIN_id=res).exists():
        var=Location.objects.get(LOGIN_id=res)
        print(var)
        return JsonResponse({'status': 'ok', 'lati': var.latitude, 'longi': var.longitude})
    else:
        return JsonResponse({'status':'not ok'})



def driver_view_rejected_request(request):
    lid = request.POST['lid']
    res = Driver_Request.objects.filter(DRIVER__LOGIN_id=lid, status="rejected")
    l = []
    for i in res:
        l.append({'id': i.id, 'datee': str(i.date), 'source': i.source, 'destination': i.destination, 'uname': i.USER.name,
                  'uphone': i.USER.phone, 'uemail': i.USER.email, })
    return JsonResponse({'status': "ok", "data": l})

def driver_approve_request(request):
    id=request.POST['rid']
    res=Driver_Request.objects.filter(id=id).update(status="approved")
    return JsonResponse({'status': 'ok'})



def driver_reject_request(request):
    id=request.POST['rid']
    res=Driver_Request.objects.filter(id=id).update(status="rejected")
    return JsonResponse({'status': 'ok'})

# def driver_view_user_location(request):
#     id=request.POST['uid']
#     res=

def driver_view_user_payment(request):
    lid=request.POST['lid']
    print(lid,"login...")
    res=Payment_to_cab.objects.filter(REQUEST__DRIVER__LOGIN_id=lid,status='paid')
    l=[]
    print(res)
    for i in res:
        l.append({'id':i.id,'amount':i.amount,'date':i.date,'source':i.REQUEST.source,'destination':i.REQUEST.destination,'username':i.USER.name,'email':i.USER.email,'phone':i.USER.phone})
    print(l)
    return JsonResponse({'status': 'ok', 'data': l})


def driver_view_payments(request):
    id=request.POST['rid']
    res=Payment_to_cab.objects.get(REQUEST=id)
    return JsonResponse({'status': 'ok','date':res.date,'uname':res.USER.name,'amnt':res.amount,'statuss':res.status})

def driver_change_password(request):
    lid=request.POST['lid']
    oldp=request.POST['old']
    newp=request.POST['new']
    conp=request.POST['confirm']
    log=Login.objects.filter(id=lid,password=oldp)
    if log.exists():
        log = Login.objects.filter(id=lid, password=oldp).update(password=newp)
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'no'})



#===Ambulance===========

def ambulance_driver_signup_post(request):
    name=request.POST['name']
    dob=request.POST['dob']
    gender=request.POST['gender']
    email=request.POST['email']
    phone=request.POST['phone']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    district=request.POST['district']
    reg=request.POST['regno']
    import datetime
    import base64
    vphoto=request.POST['vphoto']
    date2 = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    a = base64.b64decode(vphoto)
    fh = open("F:\\project\\web\\smart cab\\media\\ambulance\\vphoto\\" + date2 + ".jpg", "wb")
    # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
    path2 = "/media/ambulance/vphoto/" + date2 + ".jpg"
    fh.write(a)
    fh.close()

    photo=request.POST['photo']
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    a2 = base64.b64decode(photo)
    fh = open("F:\\project\\web\\smart cab\\media\\ambulance\\photo\\" + date + ".jpg", "wb")
    # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
    path = "/media/ambulance/photo/" + date + ".jpg"
    fh.write(a2)
    fh.close()

    vproof=request.POST['vproof']
    date1 = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    a1 = base64.b64decode(vproof)
    fh = open("F:\\project\\web\\smart cab\\media\\ambulance\\proof\\" + date1 + "1.jpg", "wb")
    # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
    path1 = "/media/ambulance/proof/" + date1 + "1.jpg"
    fh.write(a1)
    fh.close()

    password = request.POST['password']
    cpassword = request.POST['cpassword']
    lobj = Login()
    lobj.username = email
    lobj.password = cpassword
    lobj.type = 'pending'
    lobj.save()

    uobj = Ambulance_Driver()
    uobj.name = name
    uobj.email = email
    uobj.gender = gender
    uobj.phone = phone
    uobj.email = email
    uobj.dob = dob
    uobj.photo = path
    uobj.proof = path1
    uobj.place = place
    uobj.post = post
    uobj.pin = pin
    uobj.district = district
    uobj.vphoto = path2
    uobj.vreg_no = reg
    uobj.LOGIN = lobj
    uobj.status = 'pending'

    uobj.save()
    return JsonResponse({'status': 'ok'})

def ambulance_view_profile(request):
    lid = request.POST['lid']
    res = Ambulance_Driver.objects.get(LOGIN_id=lid)
    print(res)
    return JsonResponse({'status': 'ok', 'name': res.name, 'email': res.email, 'phone': res.phone,'gender':res.gender,
                         'dob': res.dob, 'photo': res.photo, 'proof': res.proof,'vphoto':res.vphoto,'place': res.place,'post': res.post,
                         'pin': res.pin,'vnumber': res.vreg_no, 'district': res.district, 'statuss': res.status})

def ambulance_edit_profile_post(request):
    lid=request.POST['lid']
    name = request.POST['name']
    dob = request.POST['dob']
    gender = request.POST['gender']
    email = request.POST['email']
    phone = request.POST['phone']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    district = request.POST['district']
    reg = request.POST['regno']
    import datetime
    import base64
    vphoto = request.POST['vphoto']

    photo = request.POST['photo']


    vproof = request.POST['vproof']


    uobj = Ambulance_Driver.objects.get(LOGIN=lid)
    if len(photo)>0:
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        a2 = base64.b64decode(photo)
        fh = open("F:\\project\\web\\smart cab\\media\\ambulance\\photo\\" + date + ".jpg", "wb")
        # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
        path = "/media/ambulance/photo/" + date + ".jpg"
        fh.write(a2)
        fh.close()
        uobj.photo = path
    if len(vphoto)>0:
        date2 = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        a = base64.b64decode(vphoto)
        fh = open("F:\\project\\web\\smart cab\\media\\ambulance\\vphoto\\" + date2 + ".jpg", "wb")
        # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
        path2 = "/media/ambulance/vphoto/" + date2 + ".jpg"
        fh.write(a)
        fh.close()
        uobj.vphoto = path2
    if len(vproof)>0:
        date1 = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        a1 = base64.b64decode(vproof)
        fh = open("F:\\project\\web\\smart cab\\media\\ambulance\\proof\\" + date1 + "1.jpg", "wb")
        # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
        path1 = "/media/ambulance/proof/" + date1 + "1.jpg"
        fh.write(a1)
        fh.close()
        uobj.proof = path1

    uobj.name = name
    uobj.email = email
    uobj.gender = gender
    uobj.phone = phone
    uobj.email = email
    uobj.dob = dob
    uobj.place = place
    uobj.post = post
    uobj.pin = pin
    uobj.district = district
    uobj.vreg_no = reg

    uobj.save()
    return JsonResponse({'status': 'ok'})

def ambulance_change_password(request):
    lid=request.POST['lid']
    oldp=request.POST['old']
    newp=request.POST['new']
    conp=request.POST['confirm']
    log=Login.objects.filter(id=lid,password=oldp)
    if log.exists():
        log = Login.objects.filter(id=lid, password=oldp).update(password=newp)
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'no'})

def ambulance_view_request(request):
    lid = request.POST['lid']
    res = Ambulance_request.objects.filter(AMBULANCE_DRIVER__LOGIN_id=lid, status="pending")
    l = []
    print(res)
    for i in res:
        l.append({'id': i.id, 'datee': str(i.date), 'source': i.source, 'destination': i.destination,
                  'uname': i.USER.name, 'uphone': i.USER.phone, 'uemail': i.USER.email, })
    print(l)
    return JsonResponse({'status': "ok", "data": l})


def ambulance_approve_request(request):
    id=request.POST['rid']
    res=Ambulance_request.objects.filter(id=id).update(status="approved")
    return JsonResponse({'status': 'ok'})

def ambulance_reject_request(request):
    id=request.POST['rid']
    res=Ambulance_request.objects.filter(id=id).update(status="rejected")
    return JsonResponse({'status': 'ok'})

def ambulance_view_approved_request(request):
    lid = request.POST['lid']
    res = Ambulance_request.objects.filter(AMBULANCE_DRIVER__LOGIN_id=lid,status="approved")
    l = []
    for i in res:
        l.append({'id': i.id, 'datee': str(i.date), 'source': i.source, 'destination': i.destination,'uid':i.USER.id, 'uname': i.USER.name,
                  'uphone': i.USER.phone, 'uemail': i.USER.email })
    return JsonResponse({'status': "ok", "data": l})


def ambulance_get_user_location(request):
    id=request.POST['id']
    res = User.objects.get(pk=id).LOGIN_id
    print(res)
    var = {'latitude':'', 'longitude':''}
    if Location.objects.filter(LOGIN_id=res).exists():
        var=Location.objects.get(LOGIN_id=res)
        print(var)
        return JsonResponse({'status': 'ok', 'lati': var.latitude, 'longi': var.longitude})
    else:
        return JsonResponse({'status':'not ok'})




def ambulance_view_rejected_request(request):
    lid = request.POST['lid']
    res = Ambulance_request.objects.filter(AMBULANCE_DRIVER__LOGIN_id=lid, status="rejected")
    l = []
    for i in res:
        l.append({'id': i.id, 'datee': str(i.date), 'source': i.source, 'destination': i.destination, 'uname': i.USER.name,
                  'uphone': i.USER.phone, 'uemail': i.USER.email, })
    return JsonResponse({'status': "ok", "data": l})

def ambulance_view_user_payment(request):
    lid=request.POST['lid']
    print(lid,"login...")
    res=Payment_to_ambulance.objects.filter(REQUEST__AMBULANCE_DRIVER__LOGIN_id=lid,status='paid')
    l=[]
    print(res)
    for i in res:
        l.append({'id':i.id,'amount':i.amount,'date':i.date,'source':i.REQUEST.source,'destination':i.REQUEST.destination,'username':i.USER.name,'email':i.USER.email,'phone':i.USER.phone})
    print(l)
    return JsonResponse({'status': 'ok', 'data': l})





#=====User==========

def user_signup_post(request):
    name=request.POST['name']
    dob=request.POST['dob']
    gender=request.POST['gender']
    email=request.POST['email']
    phone=request.POST['phone']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    district=request.POST['district']
    # from datetime import datetime
    # date=datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
    photo=request.POST['photo']

    import datetime
    import base64
    #
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    a = base64.b64decode(photo)
    fh = open("F:\\project\\web\\smart cab\\media\\user\\" + date + ".jpg", "wb")
    # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
    path = "/media/user/" + date + ".jpg"
    fh.write(a)
    fh.close()
    password = request.POST['password']
    cpassword = request.POST['cpassword']

    lobj = Login()
    lobj.username = email
    lobj.password = cpassword
    lobj.type = 'user'
    lobj.save()

    uobj = User()
    uobj.name = name
    uobj.dob = dob
    uobj.gender = gender
    uobj.phone = phone
    uobj.email = email
    uobj.photo = path
    uobj.place = place
    uobj.post = post
    uobj.pin = pin
    uobj.district = district
    uobj.LOGIN = lobj
    uobj.save()
    return JsonResponse({'status': 'ok'})


def user_view_profile(request):
    lid = request.POST['lid']
    res = User.objects.get(LOGIN=lid)
    print(res)
    return JsonResponse({'status': 'ok', 'name': res.name, 'email': res.email, 'phone': res.phone,
                         'dob': res.dob,'gender':res.gender, 'photo': res.photo,'place': res.place,'post': res.post,
                         'pin': res.pin, 'district': res.district})

def user_edit_profile(request):
    lid=request.POST['lid']
    name = request.POST['name']
    dob = request.POST['dob']
    gender = request.POST['gender']
    email = request.POST['email']
    phone = request.POST['phone']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    district = request.POST['district']
    photo = request.POST['photo']
    uobj = User.objects.get(LOGIN=lid)
    uobj.name = name
    uobj.dob = dob
    uobj.gender = gender
    uobj.phone = phone
    uobj.email = email
    if len(photo)>0:
        import datetime
        import base64
        #
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        a = base64.b64decode(photo)
        fh = open("F:\\project\\web\\smart cab\\media\\user\\" + date + ".jpg", "wb")
        # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
        path = "/media/user/" + date + ".jpg"
        fh.write(a)
        fh.close()
        uobj.photo = path
    uobj.place = place
    uobj.post = post
    uobj.pin = pin
    uobj.district = district
    uobj.save()
    return JsonResponse({'status': 'ok'})


def user_change_password(request):
    lid = request.POST['lid']
    oldp = request.POST['old']
    newp = request.POST['new']
    conp = request.POST['confirm']
    log = Login.objects.filter(id=lid, password=oldp)
    if log.exists():
        log = Login.objects.filter(id=lid, password=oldp).update(password=newp)
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'no'})

def user_view_cab(request):
    res=Driver.objects.filter(status="approved")
    l=[]
    for i in res:
        l.append({'id':i.id,'dname':i.name,'vnumber': i.vnumber,'phone':i.phone,'place':i.place,'vphoto':i.vphoto})
    return JsonResponse({'status': 'ok','data':l})

def user_view_cab_more(request):
    id=request.POST['id']
    res = Driver.objects.get(pk=id)
    print(res)
    return JsonResponse({'status': 'ok', 'name': res.name, 'email': res.email, 'phone': res.phone, 'gender': res.gender,
                         'vphoto': res.vphoto,'photo':res.photo,
                         'dob': res.dob,'place': res.place, 'post': res.post,
                         'pin': res.pin, 'vnumber': res.vnumber, 'district': res.district})




def user_send_request(request):
    id=request.POST['did']
    lid=request.POST['lid']
    sour=request.POST['source']
    desti=request.POST['destination']
    uu=User.objects.get(LOGIN=lid)
    dobj=Driver_Request()
    dobj.USER=uu
    dobj.DRIVER=Driver.objects.get(pk=id)
    dobj.destination=desti
    dobj.source=sour
    dobj.status='pending'
    from datetime import datetime
    datee = datetime.now().strftime("%Y-%m-%d")
    dobj.date=datee
    dobj.save()
    return JsonResponse({'status':'ok'})

def user_view_request_status(request):
    lid=request.POST['lid']
    res=Driver_Request.objects.filter(USER__LOGIN_id=lid)
    l=[]
    for i in res:
        paid="no"
        if Payment_to_cab.objects.filter(REQUEST=i).exists():
            paid='yes'
        l.append({'id':i.id,'date':i.date,
                  'did':i.DRIVER.id,'number':i.DRIVER.vnumber,
                  'vphoto':i.DRIVER.vphoto,
                  'statuss':i.status,
                  'selfno':i.USER.phone,
                  'driverno':i.DRIVER.phone,
                  'source':i.source,'destination':i.destination,'paid':paid})
    return JsonResponse({'status':"ok",'data':l})


def user_send_cab_payment(request):
    lid=request.POST['lid']
    c=request.POST['cid']
    print(c,"gggg")
    amnt=request.POST['amount']
    cp=Payment_to_cab()
    cp.amount=amnt
    from datetime import datetime
    cp.date=datetime.now().today()
    cp.USER=User.objects.get(LOGIN_id=lid)
    cp.REQUEST=Driver_Request.objects.get(pk=c)
    cp.status='paid'
    cp.save()
    return JsonResponse({'status':"ok"})

def user_view_cab_payment(request):
    lid=request.POST['lid']
    res=Payment_to_cab.objects.filter(USER__LOGIN_id=lid,status='paid')
    l=[]
    for i in res:
        l.append({'id':i.id,'amount':i.amount,'date':i.date,'source':i.REQUEST.source,'destination':i.REQUEST.destination,'vehicle':i.REQUEST.DRIVER.vnumber})
    print(l)
    return JsonResponse({'status': 'ok', 'data': l})







def user_view_request_status_more(request):
    id=request.POST['rid']
    res=Driver_Request.objects.get(id=id)
    print(res)
    return JsonResponse({'status': 'ok', 'name': res.DRIVER.name, 'email': res.DRIVER.email, 'phone': res.DRIVER.phone, 'gender': res.DRIVER.gender,
                          'photo': res.DRIVER.photo,'dob': res.DRIVER.dob, 'place': res.DRIVER.place, 'post': res.DRIVER.post,
                         'pin': res.DRIVER.pin,'district': res.DRIVER.district})



def user_view_ambulance(request):
    res=Ambulance_Driver.objects.filter(status="approved")
    print(res)
    l=[]
    for i in res:
        l.append(
            {'id': i.id, 'dname': i.name, 'vnumber': i.vreg_no, 'phone': i.phone, 'place': i.place, 'vphoto': i.photo})
    # print(l)
    return JsonResponse({'status': 'ok', 'data': l})

def user_view_ambulance_more(request):
    id=request.POST['id']
    res = Ambulance_Driver.objects.get(pk=id)
    print(res)
    return JsonResponse({'status': 'ok', 'name': res.name, 'email': res.email, 'phone': res.phone, 'gender': res.gender,
                         'photo':res.photo,
                         'dob': res.dob,'place': res.place, 'post': res.post,
                         'pin': res.pin, 'vnumber': res.vreg_no, 'district': res.district})
def user_get_driver_location(request):
    id=request.POST['id']
    res = Driver.objects.get(pk=id).LOGIN_id
    print(res)
    var = {'latitude':'', 'longitude':''}
    if Location.objects.filter(LOGIN_id=res).exists():
        var=Location.objects.get(LOGIN_id=res)
    print(var)
    return JsonResponse({'status': 'ok', 'lati': var.latitude, 'longi': var.longitude})


def user_view_ambulance_status(request):
    lid = request.POST['lid']
    res = Ambulance_request.objects.filter(USER__LOGIN_id=lid)
    print(res)
    l = []
    for i in res:
        paid = "no"
        if Payment_to_ambulance.objects.filter(REQUEST=i).exists():
            paid = 'yes'
        l.append(
            {'id': i.id, 'date': i.date,
             'aid':i.AMBULANCE_DRIVER.id,
             'number': i.AMBULANCE_DRIVER.vreg_no,
             'vphoto': i.AMBULANCE_DRIVER.photo,
             'statuss': i.status,
             'selfno': i.USER.phone,
             'driverno': i.AMBULANCE_DRIVER.phone,
             'source': i.source, 'destination': i.destination,'paid':paid})
    return JsonResponse({'status': "ok", 'data': l})


def user_send_ambu_payment(request):
    lid=request.POST['lid']
    c=request.POST['cid']
    print(c,"iii")
    amnt=request.POST['amount']
    cp=Payment_to_ambulance()
    cp.amount=amnt
    from datetime import datetime
    cp.date=datetime.now().today()
    cp.USER=User.objects.get(LOGIN_id=lid)
    cp.REQUEST=Ambulance_request.objects.get(pk=c)
    cp.status='paid'
    cp.save()
    return JsonResponse({'status':"ok"})

def user_view_ambu_payment(request):
    lid=request.POST['lid']
    res=Payment_to_ambulance.objects.filter(USER__LOGIN_id=lid,status='paid')
    l=[]
    for i in res:
        l.append({'id':i.id,'amount':i.amount,'date':i.date,'source':i.REQUEST.source,'destination':i.REQUEST.destination,'vehicle':i.REQUEST.AMBULANCE_DRIVER.vreg_no})
    print(l)
    return JsonResponse({'status': 'ok', 'data': l})


def user_get_ambulance_location(request):
    id=request.POST['id']
    res = Ambulance_Driver.objects.get(pk=id).LOGIN_id
    print(res)
    var = {'latitude':'', 'longitude':''}
    if Location.objects.filter(LOGIN_id=res).exists():
        var=Location.objects.get(LOGIN_id=res)
    print(var)
    return JsonResponse({'status': 'ok', 'lati': var.latitude, 'longi': var.longitude})


def user_view_ambulance_request_more(request):
    id=request.POST['rid']
    res = Ambulance_request.objects.get(pk=id)
    print(res)
    return JsonResponse({'status': 'ok', 'name': res.AMBULANCE_DRIVER.name, 'email': res.AMBULANCE_DRIVER.email, 'phone': res.AMBULANCE_DRIVER.phone,
                         'gender': res.AMBULANCE_DRIVER.gender,
                         'photo':res.AMBULANCE_DRIVER.photo,'dob': res.AMBULANCE_DRIVER.dob,'place': res.AMBULANCE_DRIVER.place, 'post': res.AMBULANCE_DRIVER.post,
                         'pin': res.AMBULANCE_DRIVER.pin,'district': res.AMBULANCE_DRIVER.district})








def user_send_ambulance_request(request):
    id=request.POST['did']
    lid=request.POST['lid']
    sour=request.POST['source']
    desti=request.POST['destination']
    uu=User.objects.get(LOGIN=lid)
    dobj=Ambulance_request()
    dobj.USER=uu
    dobj.AMBULANCE_DRIVER=Ambulance_Driver.objects.get(pk=id)
    dobj.destination=desti
    dobj.source=sour
    dobj.status='pending'
    from datetime import datetime
    datee = datetime.now().strftime("%Y-%m-%d")
    dobj.date=datee
    dobj.save()
    return JsonResponse({'status':'ok'})

def _update_location(request):
    lid=request.POST['lid']
    lat=request.POST['lat']
    lon=request.POST['lon']
    dobj=Location()
    if Location.objects.filter(LOGIN_id=lid).exists():
        dobj = Location.objects.get(LOGIN_id=lid)
    dobj.latitude=lat
    dobj.longitude=lon
    dobj.LOGIN_id=lid
    dobj.save()
    return JsonResponse({'status':'ok'})




def user_send_complaint(request):
    lid=request.POST['lid']
    complaaint=request.POST['complaint']
    from datetime import datetime
    date=datetime.now().strftime("%Y-%m-%d")
    cc=User.objects.get(LOGIN=lid)
    cobj=Complaint()
    cobj.USER=cc
    cobj.complaint=complaaint
    cobj.date=date
    cobj.status='pending'
    cobj.reply='pending'
    cobj.save()
    return JsonResponse({'status':'ok'})

def user_view_complaint_post(request):
    lid=request.POST['lid']
    cc=User.objects.get(LOGIN=lid)
    obj=Complaint.objects.filter(USER=cc)
    l=[]
    for i in obj:
        l.append({'id':i.id,'comp':i.complaint,'date':i.date,'status':i.status,'reply':i.reply})
    return JsonResponse({'status':'ok','data':l})

def user_feedback_post(request):
    lid=request.POST['lid']
    cc=User.objects.get(LOGIN=lid)
    feedback=request.POST['review']
    # rating=request.POST['rating']
    from datetime import datetime
    date = datetime.now().strftime("%Y-%m-%d")
    fobj=Feedback()
    fobj.USER=cc
    fobj.Feed_back=feedback
    # fobj.rating=rating
    fobj.date=date
    fobj.save()
    return JsonResponse({'status':'ok'})

def user_view_feedback_post(request):
    lid=request.POST['lid']
    cc = User.objects.get(LOGIN=lid)
    res=Feedback.objects.filter(USER=cc)
    l=[]
    for i in res:
        l.append({'id':i.id,'feedback':i.Feed_back,'date':i.date})
    return JsonResponse({'status':'ok','data':l})












