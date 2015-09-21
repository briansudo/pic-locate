from django.shortcuts import render
from django.http import HttpResponse
import requests
import utils
from models import *
import json

def index(request):
    return render(request, "index.html", {})

def image_search(request):
    print request
    if request.method == 'GET':

        utils.get_tags(request.GET.get('image_url'))
        classification = utils.run_nmf()
        response = {"id": classification}
        return HttpResponse(json.dumps(response), content_type="application/json")
    return None

def flight_search(request):
    print request
    if request.method == 'GET':
        origin = request.GET.get('origin')
        dst = request.GET.get('destination')
        dpt_date = request.GET.get('departure_date')
        return_date = request.GET.get('return_date')
        params = {"origin": origin, "destination": dst, "departure_date": dpt_date, "return_date": return_date, "apikey": "GpGMcG9JY8FPrmcxYyJ84kml0cQFRKMk"}
        url = "https://api.sandbox.amadeus.com/v1.2/flights/extensive-search"
        r = requests.get(url, params)
        print r.json()
        return HttpResponse(json.dumps(r.json()), content_type="application/json")
    return None

def search_result(request, classification):
    class_model = Landmark.objects.get(classification_id=classification)
    pages = requests.get(class_model.summary_url).json()
    print pages
    pages = pages["query"]["pages"]
    first_key = pages.keys()[0]

    extract =  pages[first_key]["extract"]
    return render(request, "search_result.html", {'landmark': class_model, "summary": extract})
