## RayServe + TensorFlow

### How to run?

1. Install ray 0.8.4:

```python
pip install ray==0.8.4
```

2. Start the ray cluster

```bash
ray start --head
```

3. Run the training scrip to generate model file.

```bash
python 3_train_tf_model.py
```

4. Run the deployment scripts to deploy to the running cluster.

Open two terminal, in one terminal:

```bash
python 1_init.py # deploys a hello world function, and queries available routes in while True loop
```

In the other terminal:

```bash
python 2_counter.py # deploys a counter
python 4_serve_tf_model.py # deploys a TF model
python 5_serve_tf_model_v2.py # deploys the second TF model sharing the same /mnist route
```
