from django.conf.urls import patterns, include, url

from django.contrib import admin
from fields import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.AppList.as_view(), name='apps'),
    url(r'^$', views.AppDetail.as_view(), name='app-detail'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
