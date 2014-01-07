from django.shortcuts import render_to_response
from django.template import RequestContext

def prtr (template, dict, request):
    return render_to_response (template, dict, context_instance=RequestContext(request))
