from flowycart.resources import Resource


class Order(Resource):

    @staticmethod
    def create(api_key, items, currency, success_url, cancel_url, ref_id=None, customer=None, metadata=None, currency_value=None, intent=False, language='en'):
        """
        Creates an order
        :param api_key: The API key
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
                    status
                    id
                }
            }
        """

        variables = {
            'refId': ref_id,
            'items': items,
            'metadata': metadata,
            'currency': currency,
            'currencyValue': currency_value,
            'customerId': customer,
            'successUrl': success_url,
            'cancelUrl': cancel_url,
            'language': language,
            'intent': intent
        }

        response = Resource.request(
            api_key,
            query=query,
            variables={'order': variables},
            operation='createOrder'
        )

        return response.json()
