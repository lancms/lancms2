from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	
	url ('^(?P<slug>[\w-]+)/$', 'core.views.organization_front', name='organization_front'),
	url ('^(?P<slug>[\w-]+)/\+admin/$', 'core.views.organization_admin', name='organization_admin'),
	url ('^(?P<slug>[\w-]+)/\+admin/event/$', 'core.views.organization_event_create', name='organization_event_create'),
	

	url ('^(?P<orgslug>[\w-]+)/(?P<eventslug>[\w-]+)/$', 'core.views.event_front', name='event_front'),
	url ('^(?P<orgslug>[\w-]+)/(?P<eventslug>[\w-]+)/\+addowner/$', 'core.views.event_owner_add', name='event_owner_add'),
	url ('^(?P<orgslug>[\w-]+)/(?P<eventslug>[\w-]+)/\+admin/$', 'core.views.event_admin', name='event_admin'),
	url ('^(?P<orgslug>[\w-]+)/(?P<eventslug>[\w-]+)/\+settings/$', 'core.views.event_settings', name='event_settings'),

	url ('^(?P<orgslug>[\w-]+)/(?P<eventslug>[\w-]+)/\+crews/$', 'crew.views.crew_front', name='crew_front'),
	#url ('^(?P<orgslug>[\w-]+)/(?P<eventslug>[\w-]+)/\+crews/apply$', 'crew.views.apply_form', name='apply_form'),
	url ('^(?P<orgslug>[\w-]+)/(?P<eventslug>[\w-]+)/\+crew/(?P<crewslug>[\w-]+)$', 'crew.views.crew_view', name='crew_view'),
	
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
