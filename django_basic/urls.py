from django.conf.urls import patterns, include, url

from django.contrib import admin
from fields import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.app_list, name='apps'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
