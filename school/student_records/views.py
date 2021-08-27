from django.shortcuts import render,redirect
from .models import *


def index(request):
    return render(request, 'index.html', {})


def student_details(request):
    if request.method == 'POST':
        stud_name = request.POST['Student_name']
        roll_no = request.POST['Student_roll_number']
        date_of_birth = request.POST['dob']
        data = StudentDetails(student_name=stud_name, roll_number=roll_no, DOB=date_of_birth)
        data.save()
    return render(request, 'student_details.html', {})


def stud_data_show(request):
    stud_data = StudentDetails.objects.all()
    stud_count = StudentDetails.objects.all().count()
    return render(request, 'student_data_show.html', {'data': stud_data, 'no_of_students': stud_count})


def student_marks(request):
    if request.method == 'POST':
        stud_name = request.POST['student_name']
        roll_no = request.POST['stud_roll_no']
        tamil = request.POST['Tamil']
        english = request.POST['English']
        maths = request.POST['Mathematical']
        science = request.POST['Science']
        social_science = request.POST['Social_science']
        total = int(tamil) + int(english) + int(maths) + int(science) + int(social_science)
        print(total)
        add_details = StudentMarkDetails(stud_name=stud_name, stud_roll_no=roll_no, Tamil=tamil, English=english, Mathematical=maths, Science=science, Social_science=social_science, Total=total)
        add_details.save()
    return render(request, 'stud_mark_entry.html', {})


def student_result(request):
    if request.method == "POST":
        roll_no = request.POST['stud_roll_no']
        result = StudentMarkDetails.objects.filter(stud_roll_no=roll_no)
        stud_filter_mark = StudentMarkDetails.objects.filter(Science='23').count()
        print(stud_filter_mark)
    return render(request, 'stud_result.html', {'result': result})


def student_result_login(request):
    return render(request, 'student_result_login.html', {})


def payment_index(request):
    return render(request, 'online_payment_index.html', {})


def pay_login(request):
    if request.method == "POST":
        name = request.POST['username']
        user_password = request.POST['password']
        OnlinePayment.objects.filter(username=name, password=user_password)
        return render(request, 'payment.html')
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        mail = request.POST['email']
        phone = request.POST['phone_number']
        a = OnlinePayment(username=name, password=password, email=mail, phone=phone)
        a.save()
    return render(request, 'signup.html')


def payment(request):
    if request.method == "POST":
        amount = request.POST['amount']
        password = request.POST['password']
        OnlinePayment.objects.filter(password=password)
        data = AmountBalance(bal_amount=amount)
        data.save()
    return render(request, 'payment.html')

