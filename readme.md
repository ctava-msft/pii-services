# Disclaimer

IMPORTANT: This is just sample code. It is not production quality code. It should not just be taken and deployed to your environments as-is. You are responsible for ensure security and performance requirements and needs are met.

# Setup python environment
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Copy sample.env to .env and enter your language api and endpoint.

# PII Service

Here is a python script to replace text that deemed as PII:

```
python api.py
```


Here is a powershell script to call a language service endpoint using curl:
```

$env:LANGUAGE_ENDPOINT = "https://<redacted>.cognitiveservices.azure.com/"

$env:LANGUAGE_KEY = "<redacted>"

curl.exe -X POST $env:LANGUAGE_ENDPOINT/language/:analyze-text?api-version=2022-05-01 `
-H "Content-Type: application/json" `
-H "Ocp-Apim-Subscription-Key: $env:LANGUAGE_KEY" `
-d "@C:\Users\christava\Documents\src\github.com\ctava-msft\language-services\lang.json"

```



# Presidio

Here is a python script to use the presidio library.

```
python lib.py
```