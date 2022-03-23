"""D URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from allauth.account.views import LogoutView
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from DD import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('DD.urls')),
    path('', views.login, name='login'),
    path("D/accounts/", include("allauth.urls")),
    path('D/', views.index, name='index'),
    path('D/Subjects/', views.subjects, name='subjects'),
    path('D/Groups/', views.groups, name='groups'),
    path('D/Profile/', views.profile, name='profile'),
    path('D/Practice/', views.practice, name='practice'),
    path('D/Theory/', views.theory, name='theory'),
    path('D/logout/', LogoutView.as_view(), name="logout"),
    path('D/Profile/profile_pic/', views.profile_pic, name="profile_pic"),
    path('D/get_specific_subject/', views.get_specific_subject, name="subject"),
    path('D/Subjects/load_selected_theory/', views.load_selected_theory, name='selected_theory'),
    path('D/Subjects/update_subject/', views.update_subject, name='update_subject'),
    path('D/Subjects/add_new_theory/', views.add_new_theory, name='add_new_theory'),
    path('D/Subjects/add_new_theory/new_theory/', views.new_theory, name='new_theory'),
    path('D/Subjects/load_selected_task/', views.load_selected_task, name='selected_task'),
    path('D/Practice/run_practice/', views.run_practice, name='run_practice'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
