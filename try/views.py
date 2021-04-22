from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Customer,Transfer
from django.utils.timezone import datetime 
# Create your views here.
#data=Customer()
#data1=Customer()

GLOBAL_Entry=None

def home(request):
	return render(request,'home.html')
def customers(request):
	data=Customer.objects.all().order_by('emp_id')
	return render(request,'customers.html',{'stu':data})
def history(request):
	data=Transfer.objects.all().order_by('date_trans')
	return render(request,'history.html',{'stu':data})
@csrf_protect
@csrf_exempt
def valid(request):
	#global send,rec,GLOBAL_Entry
	
	send= int(request.POST.get('send',False))
	rec= int(request.POST.get('receive',False))
	request.session['sen']=send
	request.session['re']=rec
	if send==rec:
		return HttpResponse("sender andd receiver cannot be same<br><a href='../home'>Go to home page</a>")
	data=Customer.objects.get(emp_id=send)
	data1=Customer.objects.get(emp_id=rec)
	
	#s=send
	#r=rec
	return render(request,'check.html',{'c':data,'d':data1})
	
def transfer(request):
	return render(request,'transfer.html')
#def create():


@csrf_protect
@csrf_exempt
def check(request):
	#send= int(request.GET.get('id1'))
	#amount=int(request.GET.get('amount'))
	#global send,rec
	#global s
	#send =
	send=request.session['sen']
	rec=request.session['re']
	data=Customer.objects.get(emp_id=send)
	data1=Customer.objects.get(emp_id=rec)
	amount=int(request.POST.get('amount',False))
	#for d in data:
	#	if send==d.emp_id:
	if data.currentbal<amount:
		return HttpResponse("Amount entered is greater than balance<br><a href='../home'>Go to home page</a>")
	x=str(send)
	x=x.zfill(1)
	y=str(rec)
	y=y.zfill(1)
	zz=str(datetime.today().day) 
	z=x+y+zz
	z=z.ljust(7,'0')
	x=int(x)
	y=int(y)
	z=int(z)
	inc=0
	his=Transfer.objects.all()
	for h in his:
		if h.emp_id==send and h.receiver==rec:
			inc=inc+1
	for h in his:
		if h.transid==z:
			z=z+inc
	
	Customer.objects.filter(emp_id=send).update(currentbal=data.currentbal-amount)
	Customer.objects.filter(emp_id=rec).update(currentbal=data1.currentbal+amount)
	updatedbal=data.currentbal-amount
	Transfer.objects.create(emp_id=x,receiver=y,sender=data.emp_name,recname=data1.emp_name,amount=amount,date_trans=datetime.today(),transid=z)
	return render(request,'success.html',{'amo':updatedbal,'send':data})	