from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .services import AmadeusService
from .serializers import CitySearchResultSerializer

class CitySearchAPIView(APIView):
    """
    API view for searching cities using the Amadeus API
    """
    permission_classes = [AllowAny]  # Allow public access to this endpoint

    def get(self, request, format=None):
        # Extract query parameters
        keyword = request.query_params.get('keyword')
        country_code = request.query_params.get('country_code')
        max_results = request.query_params.get('max_results', 10)

        # Validate required parameters
        if not keyword:
            return Response(
                {"error": "The 'keyword' parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            max_results = int(max_results)
        except ValueError:
            return Response(
                {"error": "The 'max_results' parameter must be a valid integer"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Call Amadeus API
        amadeus_service = AmadeusService()
        results = amadeus_service.search_city(
            keyword=keyword,
            country_code=country_code,
            max_results=max_results
        )

        # Check if there was an error
        if "error" in results:
            return Response(results, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Serialize the results
        serializer = CitySearchResultSerializer(results, many=True)
        return Response(serializer.data)