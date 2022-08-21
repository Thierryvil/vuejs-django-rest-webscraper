import requests
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from drogasil.serializers import ProductSerializer

DROGASIL_API_SEARCH_URL = 'https://api-gateway-prod.drogasil.com.br/search/v2/store/DROGASIL/channel/SITE/product/search/live?term={term}&sort_by=relevance:desc&origin=searchSuggestion'


def get_search_url(url_api: str, term: str) -> str:
    return url_api.format(term=term.lower().strip())

@api_view(['GET',])
def search(request: Request) -> dict:
    # Verify if the request has the term parameter
    term = request.query_params.get('term', None)
    if not term:
        raise Exception('Term is required')
    # Get the search url
    url = get_search_url(DROGASIL_API_SEARCH_URL, term)
    response = requests.get(url)
    if not response.status_code == 200:
        raise Exception('Error loading products from Drogasil.')
    # Check response
    products = response.json()['results']['products']
    serializer = ProductSerializer(data=products, many=True)
    if not serializer.is_valid(raise_exception=True):
        raise Exception('Response from Drogasil is not valid.')
    # Return response
    return Response(serializer.data)
