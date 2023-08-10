from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name='home'),
    path('login', views.loginPage, name='login'),
    #path('thankyou/', views.thankyou, name='thankyou'),
    path('signupPage', views.signupPage, name='signup'),
    path('create_event', views.create_event, name='create_event'),
    path('logout', views.logoutPage, name='logout'),
    path('like', views.like_post),
    path('event_detail/<int:id>', views.event_detail, name='event_detail'),
    path('delete/<int:id>', views.delete, name="delete"),
    path('edit/<int:id>', views.edit, name="edit"),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
