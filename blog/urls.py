from django.contrib import admin
from django.urls import path
from feed.views import HomePage, CreateFeed
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomePage.as_view(), name="home"),
    path("create-post/", CreateFeed.as_view(), name="create_post")
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
