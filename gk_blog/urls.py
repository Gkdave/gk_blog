
from django.contrib import admin
from django.urls import path,include


admin.site.site_header = "This is Gk_dave Blogs"
admin.site.site_title = "Dave Blogs"
admin.site.index_title = "gajendra dave blog "
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
]
