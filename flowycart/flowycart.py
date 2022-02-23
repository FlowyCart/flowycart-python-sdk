from dataclasses import dataclass
from functools import lru_cache
from typing import List

from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport


@dataclass
class FlowyCart:
    api_url: str = "https://api.flowycart.com/api/graphql"
    api_key: str = None
    transport: AIOHTTPTransport = None
    client: Client = None

    def __post_init__(self):
        self.transport: AIOHTTPTransport = AIOHTTPTransport(
            url=self.api_url,
            headers={"content-type": "application/json", "authorization": self.api_key},
        )
        self.client: Client = Client(
            transport=self.transport,
            fetch_schema_from_transport=True,
        )

    def connect(self, vendor: str, base_url: str = None) -> dict:
        """
        An order
        :param vendor: The merchant name, for example "OpenCart"
        :param base_url: The vendor's API base URL, if any
        """
        query = gql(
            """
            mutation connectMerchant($vendor: String!, $baseUrl: String!) {
                connectMerchant(vendor: $vendor, baseUrl: $baseUrl) {
                    status
                    token
                }
            }
            """
        )
        variables = {"vendor": vendor, "baseUrl": base_url}
        result = self.client.execute(query, variable_values=variables)
        return result

    @lru_cache
    def get_countries(self) -> dict:
        """
        Get list of FlowyCart countries
        """

        query = gql(
            """
            query countries{
                countries{
                    id
                    name
                    codeIso2
                    codeIso3
                }
            }
        """
        )
        result = self.client.execute(query)
        return result

    def get_zones(self, country_id: int) -> dict:
        """
        Get list of FlowyCart zones for a specified country
        :param country_id: The customer id from the store or e-commerce site
        """

        query = gql(
            """
            query zones($countryId: String!){
                zones(countryId: $countryId){
                    id
                    name
                    code
                }
            }
        """
        )
        result = self.client.execute(query, variable_values={"countryId": country_id})
        return result

    def create_customer(
        self,
        ref_id: str,
        first_name: str,
        lastname: str,
        email: str,
        addresses: List[dict],
    ) -> dict:
        """
        Creates an order
        :param ref_id: The customer id from the store or e-commerce site
        :param first_name: Customer first name
        :param lastname: Customer lastname
        :param email: Customer email
        :param addresses: Customer addresses
        """

        query = gql(
            """
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
        )

        variables = {
            "refId": ref_id,
            "firstName": first_name,
            "lastName": lastname,
            "email": email,
            "addresses": addresses,
        }

        result = self.client.execute(query, variable_values=variables)
        return result

    def create_order(
        self,
        items: List[dict],
        currency: str,
        success_url: str,
        cancel_url: str,
        ref_id: str = None,
        customer: int = None,
        metadata: List[dict] = None,
        currency_value: float = None,
        intent: bool = False,
        language: str = "en",
    ) -> dict:
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

        query = gql(
            """
            mutation createOrder($order: OrderInputType!) {
                createOrder(order: $order) {
                    order {
                        id
                        refId
                        uuid
                        status
                    }
                }
            }
        """
        )

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

        result = self.client.execute(query, variable_values=variables)
        return result
