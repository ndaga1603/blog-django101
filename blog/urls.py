from django.contrib import admin
from django.urls import path
from feed.views import HomePage, CreateFeed, Login, Logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomePage.as_view(), name="home"),
    path("create-post/", CreateFeed.as_view(), name="create_post"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
