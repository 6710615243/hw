from django.shortcuts import render,redirect
from .models import RoomData, Booking
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, UserLoginForm


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # ตรวจสอบ user ในฐานข้อมูล
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "เข้าสู่ระบบสำเร็จ", extra_tags="login")
            return redirect('index')  # หรือหน้า dashboard ของคุณ
        else:
            messages.error(request, "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง",  extra_tags="login")
    
    return render(request, 'rooms/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "ออกจากระบบเรียบร้อย")
    return redirect('index')


def index(request):
    rooms = RoomData.objects.all()
    context =  {'rooms' : rooms}
    return render(request, 'rooms/index.html', context)

def room(request,id):
    room = RoomData.objects.get(id=id)
    
    existing_booking = Booking.objects.filter(user=request.user).first()
    if existing_booking:
        messages.error(request, "คุณมีการจองห้องอยู่แล้ว กรุณายกเลิกก่อนจองใหม่")
        return redirect('my_booking')
    
    if room.available_hours > 0:
        Booking.objects.create(user=request.user, room_user=room, hours=1)
        room.available_hours -= 1
        room.save()
        messages.success(request, f'จองห้อง {room.room_name} สำเร็จ!', extra_tags="booking")
    else:
        messages.error(request, f'ห้อง {room.room_name} ไม่สามารถจองได้ เนื่องจากไม่มีชั่วโมงว่างแล้ว!', extra_tags="booking")

    return redirect('index')

def my_booking(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'rooms/my_booking.html', {'bookings': bookings})

def cancel_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id, user=request.user)
    room = booking.room_user
    room.available_hours += booking.hours
    room.save()
    booking.delete()
    messages.success(request, f'ยกเลิกการจอง {room.room_name} เรียบร้อยแล้ว')
    return redirect('my_booking')


def login_admin(request):
    return redirect('admin')

