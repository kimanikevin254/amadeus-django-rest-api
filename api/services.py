from django.conf import settings
from amadeus import Client, ResponseError

class AmadeusService:
    def __init__(self):
        self.amadeus = Client(
            client_id=settings.AMADEUS_API_KEY,
            client_secret=settings.AMADEUS_API_SECRET
        )

    def search_city(self, keyword, country_code, max_results):
        """
        Search for cities based on a keyword and country code(optional).

        Args:
            keyword(str): keyword that should represent the start of a word in a city name.
            country_code(str): optional ISO 3166 Alpha-2 code(e.g. "US" United States of America) to filter the search.
            max_results(int): maximum number of results to return.
        """

        try:
            params = {
                'keyword': keyword,
                'max': max_results
            }

            # Add country code if provided
            if country_code:
                params['countryCode'] = country_code

            response = self.amadeus.reference_data.locations.cities.get(**params)

            # Return empty list if result is None
            if response.data is None:
                return []

            return response.data
        except ResponseError as error:
            return {"error": error.response.body}
        except Exception as error:
            return {"error": str(error)}