from rest_framework import views, response


MANY_SMALL_IMAGES = [
    "/images/iphone-1.png", "/images/iphone-2.png", "/images/iphone-3.png",
    "/images/iphone-4.png", "/images/iphone-3.png", "/images/iphone-4.png"]
ONE_LARGE_IMAGE = ["/images/iphone-large.png"]

PRODUCT_DATA = {
    "type": "Phone",
    "name": "IPhone 11 Pro Max",
    "images": MANY_SMALL_IMAGES,
    "rating": 70,
    "ratingDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod"\
        "tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam.",
    "condition": "Second Hand",
    "timeLeft": "3d 13h Friday",
    "priceNoDiscount": 1200,
    "totalPrice": 1000
}

DISPLAY_LARGE_IMAGE = True


class RateProductView(views.APIView):

    def get(self, request, **kwargs):
        product_url = self.request.query_params["url"]
        product_data = PRODUCT_DATA
        global DISPLAY_LARGE_IMAGE
        if DISPLAY_LARGE_IMAGE:
            product_data = product_data.copy()
            product_data["images"] = ONE_LARGE_IMAGE
            DISPLAY_LARGE_IMAGE = False
        else:
            DISPLAY_LARGE_IMAGE = True
        return response.Response(product_data)


class CompareProductsView(views.APIView):

    def get(self, request, **kwargs):
        product_urls = self.request.query_params["urls"]
        compared_products = [PRODUCT_DATA for _ in range(6)]
        return response.Response(compared_products)
