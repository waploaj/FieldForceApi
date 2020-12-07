import googlemaps
import requests
import urllib
import jsonify

class CustomerUtility:
    """

    """
    gmaps = googlemaps.Client(key = "AIzaSyBMfcFjv2xwcnyLoAmpv9W5XhNI-4LqyDA")
    def customeraddress( self, param ):
        """
        takein json param with latitude and longitude
        return: customer ward, street, city and navigation in json
        """
        latiude:str = param["latitude"]
        longitude:str = param["longitude"]