from django.shortcuts import render,redirect
from .models import RoomData, Booking
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.decorators import login_required

#from django.http import HttpResponse

# Create your views here.
# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST) #ต้องส่งคำขอเข้ามา
#         if form.is_valid():
#             return redirect("posts:list")
#     else:
#         form = AuthenticationForm()
#     return render(request, "user/login.html", {"form" : form}) #ตรวจสอบสิทธิ์

# def home(request):
#     if request.user.is_staff:  # ถ้าเป็น Admin
#         return redirect('/admin/')
#     else:
#         return redirect('room_list')

def index(request):
    rooms = RoomData.objects.all()
    context =  {'rooms' : rooms}
    return render(request, 'rooms/index.html', context)

def room(request,id):
    room = RoomData.objects.get(id=id)
    if room.available_hours > 0:
        Booking.objects.create(user=request.user, room_user=room, hours=1)
        room.available_hours -= 1
        room.save()
        messages.success(request, f'จองห้อง {room.room_name} สำเร็จ!')
    else:
        messages.error(request, f'ห้อง {room.room_name} ไม่สามารถจองได้ เนื่องจากไม่มีชั่วโมงว่างแล้ว!')
    return redirect('index')

def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'classroom/my_bookings.html', {'bookings': bookings})

def cancel_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id, user=request.user)
    room = booking.room_user
    room.available_hours += booking.hours
    room.save()
    booking.delete()
    messages.success(request, f'ยกเลิกการจอง {room.room_name} เรียบร้อยแล้ว')
    return redirect('my_bookings')

