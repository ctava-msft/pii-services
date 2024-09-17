# Disclaimer

IMPORTANT: This is just sample code. It is not production quality code. It should not just be taken and deployed to your environments as-is. You are responsible for ensure security and performance requirements and needs are met. You may install and use the sample code included in this repository. The sample code is licensed "as is" and is excluded from any service level agreements or support services. You bear the risk of using it.
Microsoft gives no express warranties, guarantees, or conditions and excludes all implied warranties, including merchantability, fitness for a particular purpose, and non-infringement.


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
