import ray
from ray import serve

ray.init(address="auto")
serve.init()


def load_dataset():
    import tensorflow as tf
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    return x_test


def perform_prediction(model, dataset, input_index):
    input_tensor = dataset[input_index:input_index + 1]
    prediction = model(input_tensor).numpy().tolist()
    return prediction


class TFMnistModel:
    def __init__(self, model_path):
        import tensorflow as tf
        self.model_path = model_path
        self.model = tf.keras.models.load_model(model_path)
        self.dataset = load_dataset()

    def __call__(self, flask_request):
        # Transform HTTP request -> business logic
        index = int(flask_request.args.get("index", 0))
        # Transform business logic -> prediction output
        prediction = perform_prediction(self.model, self.dataset, index)

        return {"prediction": prediction, "file": self.model_path}


serve.create_endpoint(endpoint_name="tf_classifier", route="/mnist")
serve.create_backend(TFMnistModel, "tf:v1", "./mnist_model.h5")
serve.link(endpoint_name="tf_classifier", backend_tag="tf:v1")

# curl localhost:8000/mnist\?index=3