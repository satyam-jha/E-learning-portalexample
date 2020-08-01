
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="homepage"),
    path('answer/<uuid:pk>', views.ans, name="ans"),
    path('question/', views.askquestion, name="qus"),
    path('answering/<uuid:pk>', views.edit_answer, name="edit"),
    path('login/', admin.site.login, name='login'),
    path('logout/', admin.site.logout, name='logout'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
