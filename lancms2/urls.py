from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	
	url ('^(?P<slug>[\w-]+)/$', 'core.views.organization_front', name='organization_front'),
	url ('^(?P<slug>[\w-]+)/\+admin/$', 'core.views.organization_admin', name='organization_admin'),
	url ('^(?P<slug>[\w-]+)/\+admin/event/$', 'core.views.organization_event_create', name='organization_event_create'),
	
	
	url ('^\+accounts/profile/$', 'core.views.selfprofile', name='account_profile'),
	# allauth:
	url ('^\+accounts/', include ('allauth.urls')),
	url ('^$', 'core.views.index', name='index'),
        
	# Examples:
	# url(r'^lancms2/', include('lancms2.foo.urls')),
	# Uncomment the admin/doc line below to enable admin documentation:
	url(r'^\+admin/doc/', include('django.contrib.admindocs.urls')),
	# Uncomment the next line to enable the admin:
	url(r'^\+admin/', include(admin.site.urls)),
)
