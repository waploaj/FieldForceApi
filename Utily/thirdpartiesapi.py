import googlemaps
import requests
import jsonify
from Utily.keys import GOOGLEMAPS_KEY, USERNAME, PASSWORD, LOGIN_URL


class CustomerApi:
    """

    """
    #TODO: add more functionality
    gmaps = googlemaps.Client(key = GOOGLEMAPS_KEY)

    def __init__(self, source, customer_id):
        """

        """
        self.source = source
        self.customer_id = customer_id

    def customer_distance(self):
        """
       #TODO: Calculate distance from source to  customer
        """

        pass

    def customer_navigation(self):
        """
        #TODO: provide navigation to customer address
        """
        pass

    def customer_address(self):
        """
        """
        #TODO: get customer city, street, ward -->
        pass


class EmployeeApi:
    """

    """
    #TODO: add more functionaliyt to employee api
    @staticmethod
    def login():
        """
        login
        """

        parameter = {"username": USERNAME, "password": PASSWORD}
        try:
            req = requests.post(LOGIN_URL, data = parameter)
        except Exception as e:
            return e

        return req

    def check_person_id(self, person_id):
        """

        """
        #TODO: add more functionality
        pass

    def get_all_person_id(self):
        """
        #TODO: come back later to retrive employee info
        """