from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from extractionAPI.models import *	# import the models in the models.py file for the app


@require_http_methods(["GET", "POST"])

# def index(request):
# 	#query_set = Story.object.all()
# 	#data = serializers.serialize("json", query_set)
#     return HttpResponse("<hr/><h3>Hello, world. You're at the poll index.</h3>")
#     #return HttpResponse(data)

def test_api_call(request):
	query_set = Story.objects.all()
	for q in query_set:
		print (q.headline)

	return HttpResponse("<h3>You're at the API Call!</h3>");
