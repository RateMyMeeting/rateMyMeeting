from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', StartSurveyView.as_view()),
    url(r'^ps', PsView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
