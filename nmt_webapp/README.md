## Installation

Make sure to install the libraries, `grpc` and `flask`, using pip:
```
pip install grpcio grpcio-tools flask-cors
```

## Steps to run

1. Edit `config.json` file to only contain models you need. Specify the full path to `.nemo` file. <br>
For En-Hi translation model, we've added the following line - 
    ```
    "en-hi": "/workspace/translation/model/AAYNBase.nemo"
    ```

2. Edit `index.html` file and make the following 2 changes:
    1. Change the IP address in the "url" tag. Point it to the IP where the NMT service will run. If the service will run on the same system as the WebApp, then change it to: <br>
        ```
        url: "http://127.0.0.1:5000/translate"
        ```
    
    2. By default, the WebApp is written to showcase 10 NMT models, but we will be using only 1 for English to Hindi translation. Hence, remove the lines corresponding to the models that aren’t required and only add the following lines for our En-Hi translation model: <br>
        ```
        <fieldset>
        <legend>Select translation direction: </legend>
        <table>
        <tr>
            <td>
            <label for="en-hi">English to Hindi</label>
            <input type="radio" name="langpair" id="en-hi">
            </td>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
        </tr>
        </table>
        </fieldset>
        ```

3. After making these 2 changes, we can run the NMT gRPC service using the following python call: <br>
    ```
    python nmt_service.py
    ```
    The script nmt_service.py contains code to load the model from a specified path (in config.json) and deploys it using a Flask server.

4. Finally, launch the webapp using: <br>
    ```
    python -m http.server
    ```