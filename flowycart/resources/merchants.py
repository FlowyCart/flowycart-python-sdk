from flowycart.resources import Resource


class Merchant(Resource):

    @staticmethod
    def connect(api_key, vendor, base_url=None):
        """
        An order
        :param api_key: The API key
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

        variables = {
            'vendor': vendor,
            'baseUrl': base_url
        }

        response = Resource.request(
            api_key,
            query=query,
            variables=variables,
            operation='connectMerchant'
        )

        return response.json()
