import requests
from django.http import HttpResponse

# Create your views here.
def get_api_data(request):
    response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
    api_data = response.json()
    return HttpResponse(api_data['joke'])