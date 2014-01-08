from core.common import prtr
from django.contrib.auth.decorators import login_required


def index (request):
    c = {}
    return prtr ('index.html', c, request) 

@login_required()
def selfprofile (request):
	c = {}
	return prtr ('account/profile.html', c, request)

