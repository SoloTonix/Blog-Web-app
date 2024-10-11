from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('create/', create, name='create'),
    path('update/<int:pk>/', update, name='update'),
    path('personal/', personal, name='personal'),
    path('personal_2/', personal_2, name='personal_2'),
    path('unpublish/<int:pk>/', unpublish, name='unpublish'),
    path('republish/<int:pk>/', republish, name='republish'),
    path('delete/<int:pk>/', delete, name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 