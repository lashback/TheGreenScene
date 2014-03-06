from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from tastypie.api import Api
from apps.Unofficial.api import TweetResource

v1_api = Api(api_name='v1')
v1_api.register(TweetResource())

admin.autodiscover()

urlpatterns = patterns('',
    # Admin
    (r'^admin/', admin.site.urls),

    # Project URLs go here
    (r'^api/', include(v1_api.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),

)