from django.urls import path
from . import views

# Define a list of URLs patterns
urlpatterns = [
   
    path('', views.index, name = 'index'),
    path('room/', views.room, name='room'),
    path('book/<int:id>/', views.room, name='book_room'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),

    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),

    path('admin/', views.login_admin, name='admin')
]