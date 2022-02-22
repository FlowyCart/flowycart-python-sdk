import requests


class FlowyCart:

    api_url = "https://api.flowycart.com/api/graphql"

    api_key = None

    def __init__(self, api_key, api_url=None):
        self.api_key = api_key
        self.api_url = api_url if api_url else self.api_url

    def _request(self, query, variables=None, operation=None):
        data = {"query": query, "variables": variables, "operation": operation}

        return requests.post(
            url=self.api_url,
            json=data,
            headers={"content-type": "application/json", "authorization": self.api_key},
        )

    def connect(self, vendor, base_url=None):
        """
        An order
        :param vendor: The merchant name, for example "OpenCart"
        :param base_url: The vendor's API base URL, if any
        """

        query = """
            mutation connectMerchant($vendor: String!, $baseUrl: String!) {
                connectMerchant(vendor: $vendor, baseUrl: $baseUrl) {
                    status
                    token
                }
            }
        """

        variables = {"vendor": vendor, "baseUrl": base_url}

        response = self._request(
            query=query, variables=variables, operation="connectMerchant"
        )

        return response.json()

    def create_order(
        self,
        items,
        currency,
        success_url,
        cancel_url,
        ref_id=None,
        customer=None,
        metadata=None,
        currency_value=None,
        intent=False,
        language="en",
    ):
        """
        Creates an order
        :param items: The order items, expressed as an array
        :param currency: The currency
        :param success_url: The success URL to redirect the user to when the order processes
        :param cancel_url: The cancel URL to redirect the user to when it cancels the order
        :param ref_id: The order id from the store or e-commerce site
        :param customer: The customer, represented by its id
        :param metadata: The metadata, expressed as an array
        :param currency_value: The currency value
        :param intent: Defines whether the order is created to redirect your customer to the FlowyCart checkout page
        :param language: The order language
        """

        query = """
            mutation createOrder($order: OrderInputType!) {
                createOrder(order: $order) {
                    id
                    refId
                    uuid
                    status
                }
            }
        """

        variables = {
            "refId": ref_id,
            "items": items,
            "metadata": metadata,
            "currency": currency,
            "currencyValue": currency_value,
            "customerId": customer,
            "successUrl": success_url,
            "cancelUrl": cancel_url,
            "language": language,
            "intent": intent,
        }

        response = self._request(
            query=query, variables={"order": variables}, operation="createOrder"
        )

        return response.json()

    def create_customer(self, ref_id, first_name, lastname, email, addresses):
        """
        Creates an order
        :param ref_id: The customer id from the store or e-commerce site
        :param first_name: Customer first name
        :param lastname: Customer lastname
        :param email: Customer email
        :param addresses: Customer addresses
        """

        query = """
            mutation createCustomer($customer: CustomerInputType!){
              createCustomer(customer: $customer){
                customer{
                  id
                  refId
                }
                status
              }
            }
        """

        variables = {
            "refId": ref_id,
            "firstName": first_name,
            "lastName": lastname,
            "email": email,
            "addresses": addresses,
        }

        response = self._request(
            query=query, variables={"order": variables}, operation="createOrder"
        )

        return response.json()

    def get_countries(self):
        """
        Get list of FlowyCart countries
        """

        query = """
            query countries{
              countries{
                id
                name
                codeIso2
                codeIso3
              }
            }
        """

        response = self._request(query=query, operation="createOrder")

        return response.json()

    def get_zones(self, country_id):
        """
        Get list of FlowyCart zones for a specified country
        :param country_id: The customer id from the store or e-commerce site
        """

        query = """
            query zones($countryId: String!){
              zones(countryId: $countryId){
                id
                name
                code
              }
            }
        """

        response = self._request(
            query=query, variables={"countryId": country_id}, operation="createOrder"
        )

        return response.json()
