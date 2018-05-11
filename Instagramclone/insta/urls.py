from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns=[
    url(r'^$',views.landing,name='landing'),
    url(r'^accounts/profile/$',views.profile,name='profile')
   ]
