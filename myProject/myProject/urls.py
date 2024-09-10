from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',index,name="index"),
    path('listportfolio/',listportfolio,name="listportfolio"),
    path('portfolio/<str:myid>',portfolio,name="portfolio"),
    path('profile/',profile,name="profile"),
    path('editprofile/',editprofile,name="editprofile"),
    path('signin/',signin,name="signin"),
    path('signup/',signup,name="signup"),
    path('signout/',signout,name="signout"),
    
    path('portfolio/<int:myid>/contact/', contact_user, name='contact_user'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)