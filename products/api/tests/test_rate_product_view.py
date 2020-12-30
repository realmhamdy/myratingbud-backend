from urllib.parse import urlencode

from core.test_base import PlusAPITestCase


class TestRateProductView(PlusAPITestCase):

    def test_rate_product(self):
        product_url = "http://example.com/product1"
        url_params = urlencode({"url": product_url})

        response = self.client.get(self.reverse("products:api:rate_product") + f"?{url_params}")

        self.assertJSONEqual(response.content, {
            "type": "Phone",
            "name": "IPhone 11 Pro Max",
            "images": ["/images/iphone-large.png"],
            "rating": 70,
            "ratingDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmodtempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam.",
            "condition": "Second Hand",
            "timeLeft": "3d 13h Friday",
            "priceNoDiscount": 1200,
            "totalPrice": 1000
        })

        # make the request a second time
        response = self.client.get(self.reverse("products:api:rate_product") + f"?{url_params}")

        self.assertJSONEqual(response.content, {
            "type": "Phone",
            "name": "IPhone 11 Pro Max",
            "images": ["/images/iphone-1.png", "/images/iphone-2.png", "/images/iphone-3.png", "/images/iphone-4.png", "/images/iphone-3.png", "/images/iphone-4.png"],
            "rating": 70,
            "ratingDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmodtempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam.",
            "condition": "Second Hand",
            "timeLeft": "3d 13h Friday",
            "priceNoDiscount": 1200,
            "totalPrice": 1000
        })
