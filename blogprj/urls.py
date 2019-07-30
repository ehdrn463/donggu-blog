"""blogprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import blogapp.views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blogapp.views.index,name='index'),
    path('send/',blogapp.views.send, name='send'),
    path('question/',blogapp.views.question, name='question'),
    path('question_detail/<int:posting_id>', blogapp.views.question_detail, name='question_detail'),
    path('aboutdonggu/',blogapp.views.aboutMe, name='aboutMe'),
    path('portfolio/',blogapp.views.portfolio, name='portfolio'),
    path('heeburndeuk/', blogapp.views.heeburndeuk, name='heeburndeuk'),
    path('our_school/', blogapp.views.our_school, name='our_school'),
    path('news_crawling/', blogapp.views.news_crawling, name='news_crawling'),
]