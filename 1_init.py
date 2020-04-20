import time
import requests
from ray.serve.utils import pformat_color_json

import ray
from ray import serve
ray.init(address="auto")
serve.init()


def my_func(flask_request):
    return "Hello world, the url is {}".format(flask_request.url)


serve.create_endpoint(endpoint_name="my_func", route="/my_func")
serve.create_backend(my_func, "my_func:v1")
serve.link(endpoint_name="my_func", backend_tag="my_func:v1")

while True:
    routes = requests.get("http://localhost:8000/-/routes").json()
    print("Current Routes: \n{}".format(list(routes.keys())))
    time.sleep(5)
