from core.common import prtr
# Create your views here.

def index (request):
    c = {}
    return prtr ('index.html', c, request) 
