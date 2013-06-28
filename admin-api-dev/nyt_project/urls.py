from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from extractionAPI import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nyt_project.views.home', name='home'),
    # url(r'^nyt_project/', include('nyt_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # The function inside the app's views
    #url(r'^$', views.index, name='Index Page'),

    url(r'^test', views.test, name='API Page'),
    url(r'^getAllStories', views.get_all_stories, name='Get All Stories'),

)

#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
