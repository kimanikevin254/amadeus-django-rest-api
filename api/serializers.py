from rest_framework import serializers

class CitySearchResultSerializer(serializers.Serializer):
    """Serializer for Amadeus city search results"""
    type = serializers.CharField()
    subType = serializers.CharField()
    name = serializers.CharField()
    iataCode = serializers.CharField(required=False, allow_null=True)
    address = serializers.DictField()
    geoCode = serializers.DictField()

    class Meta:
        fields = [
            'type', 'subType', 'name', 'iataCode',
            'address', 'geoCode'
        ]