
from django.urls import path
from .import views #same module both url and views so .
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.userlogout,name='logout'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)