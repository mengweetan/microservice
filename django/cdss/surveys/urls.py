from django.conf.urls import url

#from django.views.decorators.cache import cache_page, never_cache

from django.urls import path, include
import surveys.views as Views

app_name = 'surveys'

urlpatterns = [


    path('d2d/<pk>', Views.Prep_data.as_view(), name='prep_data'),


]
