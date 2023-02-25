from django.shortcuts import render,redirect
#from django.contrib.import messages
from .models import Course,Student,Amount
import datetime
def index(request):
    if request.method=='POST':
        s=Student()
        s.sname=request.POST['sname']
        s.email=request.POST['email']
        s.mob=request.POST['mob']
        s.branch=request.POST['branch']
        cr=request.POST.getlist('course')
        s.status=request.POST['status']
        s.date=datetime.datetime.now()
        s.address=request.POST['address']
        s.qualification=request.POST['qualification']
        s.sem=request.POST['sem']
        p=request.POST['passout']
        s.passout=int(p)
        for i in cr: 
            s.course=Course.objects.get(id=i)
            s.save()
        messages.info(request,'student added sucessfully')
        return redirect('/')
    else:
        cr=Course.objects.all()
        return render(request,'index.html',{'cr':cr})
def addcourse(request):
    if request.method=='POST':
        c=Course()
        c.cname=request.POST['cname']
        c.duration=request.POST['duration']
        c.details=request.POST['details']
        f=request.POST['fees']
        c.fees=int(f)
        c.save()
        messages.info(request,'course added sucessfully')
        return redirect('/')
    else:
        return render(request,'addcourse.html')
def showcourse(request):
    cr=Course.objects.all()
    return render(request,'showcourse.html',{'cr':cr})
def showstudents(request):
    st=Student.objects.all()
    return render(request,'showstudents.html',{'st':st})
def payamount(request):
    if request.method=='POST':
        a=Amount()
        id=request.POST['student']
        st=Student.objects.get(id=id)
        a.student=st
        tf=request.POST['total_fee']
        a.total_fee=int(tf)
        submitamount=request.POST['submitamount']
        sb=Amount.objects.filter(student_id=id).all()
        if len(sb)>0:
            a.submitdate=sb[0].submitdate+','+str(datetime.datetime.now())
            sb=sb[0].submitamount
            a.submitamount=sb+','+submitamount
            tt=sb.split(",")
            ss=0
            for i in tt:
                ss=ss+int(i)
            a.remaining=int(tf)-ss-int(submitamount)
        else:
            a.submitamount=submitamount
            a.remaining=int(tf)-int(submitamount)
            a.submitdate=datetime.datetime.now()
        a.nextpaydate=request.POST['nextpaydate']
        a.save()
        st=Student.objects.all()
        return render(request,'payamount.html',{'st':st})
    else:
        st=Student.objects.all()
        return render(request,'payamount.html',{'st':st})
def showam(request):
    id=request.GET['val']
    t=Student.objects.get(id=id)
    s=Amount.objects.filter(student=t).all()
    rm=0
    his=[['no','records found']]
    if len(s)>0:
        rm=s[0].remaining
        l1=s[0].submitamount.split(",")
        l2=s[0].submitdate.split(",")
        his=list(zip(l1,l2))
    else:
        rm=t.course.fees
    return render(request,'showajax.html',{'totalfee':t.course.fees,'rm':rm,'his':his})
def searchenquiry(request):
    if request.method=='POST':
        cid=request.POST['course']
        status=request.POST['status']
        sname=request.POST['sname']
        fdt=request.POST['fdt']
        tdt=request.POST['tdt']
        st=Student.objects.all()
        if fdt and tdt is not '':
            st=st.filter(doe__range=(fdt, tdt))
        if sname is not '':
            st=st.filter(sname=sname)
        if status is not '':
            st=st.filter(status=status)
        if cid is not '':
            st=st.filter(course=cid)
        return render(request,'showstudents.html',{'st':st})
    else:
        cr=Course.objects.all()
        return render(request,'searchenquiry.html',{'cr':cr})
    