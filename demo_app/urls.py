from django.conf.urls import patterns, include, url


urlpatterns = patterns('demo_app.views',
    url(r'','index', {'template':'demo_app/index.html'}, name='index'),
)
