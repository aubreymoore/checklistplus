from django.shortcuts import render_to_response, RequestContext
from taxonomy.models import Taxon

def show_taxa(request):
    return render_to_response("taxa.html", {'nodes':Taxon.objects.all()}, context_instance=RequestContext(request))
