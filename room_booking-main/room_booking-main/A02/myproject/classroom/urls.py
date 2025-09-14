from django.contrib import admin
from django.urls import path, include
# from django.contrib.auth import views as auth_views
from . import views

# Define a list of URLs patterns
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('', include('classroom.urls')),

    path('', views.index, name = 'index'),
    path('room/', views.room, name='room'),
    path('book/<int:id>/', views.room, name='book_room'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),

]