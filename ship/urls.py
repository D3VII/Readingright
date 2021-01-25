from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('update/<int:id>', views.update, name='update'),
    path('<int:id>', views.delete, name='delete'),
    # path('signup', viwes.signup, name='signup'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)