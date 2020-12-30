from urllib.parse import urlencode

from core.test_base import APITestCase


class TestCompareProductsView(APITestCase):

    def test_compare_products_view(self):
        product_urls = ["http://example.com/product1", "http://example.com/product2"]
        url_params = urlencode({"urls": product_urls})

        response = self.client.get(self.reverse("products:api:compare_products") + f"?{url_params}")

        self.assertJSONEqual(response.content, [{
            "type": "Phone",
            "name": "IPhone 11 Pro Max",
            "images": ["/images/iphone-1.png", "/images/iphone-2.png", "/images/iphone-3.png", "/images/iphone-4.png", "/images/iphone-3.png", "/images/iphone-4.png"],
            "rating": 70,
            "ratingDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmodtempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam.",
            "condition": "Second Hand",
            "timeLeft": "3d 13h Friday",
            "priceNoDiscount": 1200,
            "totalPrice": 1000
        }] * 6)
