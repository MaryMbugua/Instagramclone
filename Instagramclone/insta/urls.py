from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns=[
    url(r'^$',views.landing,name='landing'),
    url(r'^profile/(?P<profile_id>\d+)/$',views.profile,name='profile'),
    url(r'^accounts/profile/edit/$',views.edit,name='edit'),
    url(r'^search/$',views.search,name='search')
   ]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)