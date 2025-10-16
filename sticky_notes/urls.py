from django.contrib import admin
from django.urls import path, include

app_name = 'posts'

urlpatterns = [
    # Admin Url pattern for accessing the Django admin interface
    path("admin/", admin.site.urls),

    # Include the URLs from the posts app
    path("", include(("posts.urls"), namespace='posts')),

]
