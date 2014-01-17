from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	
	url ('^org/(?P<slug>[\w-]+)/$', 'core.views.organization_front', name='organization_front'),
	
	
	url ('^accounts/profile/$', 'core.views.selfprofile', name='account_profile'),
	# allauth:
	url ('^accounts/', include ('allauth.urls')),
	url ('^$', 'core.views.index', name='index'),
        
	# Examples:
	# url(r'^lancms2/', include('lancms2.foo.urls')),
	# Uncomment the admin/doc line below to enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
)
