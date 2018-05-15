from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'modeling.views.home_page', name="home"),
    url(r'^add/$', 'modeling.views.add_to_db', name="add"),
    url(r'^rewrite/$', 'modeling.views.re_write', name="rewrite"),
    url(r'^results$', 'modeling.views.results', name="results"),
    url(r'^location/$', 'modeling.views.location', name='lcation'),
    url(r'^location_detail$', 'modeling.views.location_detail', name='location_detail'),
    url(r'^location_detail/(\d{1,3})/$', 'modeling.views.page', name='page'),
    url(r'^auto/$', 'modeling.views.auto', name='auto'),
    url(r'^creature-search', 'modeling.views.c_search', name='c_search'),
    url(r'^color$', 'modeling.views.location_count', name='color'),
    url(r'^evaluate$', 'modeling.views.evaluate', name='evaluate'),
    url(r'^evaluate_output$', 'modeling.views.evaluate_output', name='evaluate_output'),
    url(r'^show/(\d{1,})$', 'modeling.views.show_loc', name='show_loc'),
    url(r'^parameter$', 'modeling.views.parameter_count', name='parameter'),
    # Examples:
    # url(r'^$', 'eol.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
