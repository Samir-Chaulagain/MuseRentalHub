from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact_us, name="contact"),
    path('post/<str:pk>', views.post, name='post'), 
    path('send-email/', views.send_email, name='send_email'),
    
   
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)