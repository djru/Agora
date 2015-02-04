from django.conf.urls import patterns, include, url
from views import display_page

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'agora.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', display_page),
)