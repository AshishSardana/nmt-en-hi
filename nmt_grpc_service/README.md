## Installation

Make sure to install the libraries, `grpc` and `flask`, using pip:
```
pip install grpcio grpcio-tools flask-cors
```

## Starting the NMT server

Start the server by specifying NMT models (.nemo files) via the `--model` argument:

```
python server.py --model ../model/AAYNBase.nemo
```

Ensure that the above path to the `AAYNBase.nemo` exist.

## Example Text Client

```
python client.py --target_language "hi" --source_language "en" --text “The man is crossing the street”
```
