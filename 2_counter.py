import ray
from ray import serve

ray.init(address="auto")
serve.init()


class Counter:
    def __init__(self):
        self.count = 1

    def __call__(self, flask_request):
        self.count += 1
        return "My current number is {}".format(self.count)


serve.create_endpoint(endpoint_name="my_counter", route="/my_counter")
serve.create_backend(Counter, "my_counter:v1")
serve.link(endpoint_name="my_counter", backend_tag="my_counter:v1")

# curl localhost:8000/my_counter