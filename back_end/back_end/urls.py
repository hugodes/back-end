from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'back_end.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^get_json/', include('shelf_json_manager.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
