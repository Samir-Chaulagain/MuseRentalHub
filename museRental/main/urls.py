from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signup, name="signup"),
    path("blog", views.blog, name="blog"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
     path('post/<str:pk>', views.post, name='post'),
]

# Serve media files only during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

