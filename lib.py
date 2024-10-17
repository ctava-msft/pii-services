from presidio_analyzer import AnalyzerEngine, PatternRecognizer
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import PIIEntity, OperatorConfig
import json
from pprint import pprint
import re

text_to_anonymize = "His name is Mr. Jones , charge this credit card: 5555 5555 5555 4444 cvv: 523 that expires on 08/29 and his phone number is 212-555-5555"

analyzer = AnalyzerEngine()

phone_number = analyzer.analyze(text=text_to_anonymize, entities=["PHONE_NUMBER"], language='en')
print(phone_number)

credit_card = analyzer.analyze(text=text_to_anonymize, entities=["CREDIT_CARD"], language='en')
print(credit_card)

##date_time = analyzer.analyze(text=text_to_anonymize, entities=["DATE_TIME"], language='en')
##print(date_time)

# Using regex to find 3-digit CVV
# cvv_pattern = re.compile(r'\b\d{3}\b')
# cvv_matches = cvv_pattern.findall(text_to_anonymize)
# print("CVV matches:", cvv_matches)

# Using regex to find 3-digit CVV and ensure absence of hyphen
#cvv_pattern = re.compile(r'\b(?!.*-)\d{3}\b')
cvv_pattern = re.compile(r'\b\d{3}\b')
cvv_matches = cvv_pattern.finditer(text_to_anonymize)

# Replace CVV with ***
for match in cvv_matches:
    print(f"CVV match: {match.group()} at position {match.start()} to {match.end()}")
    text_to_anonymize = text_to_anonymize[:match.start()] + '***' + text_to_anonymize[match.end():]


# Using regex to find expiration dates in MM/YY format
expiry_pattern = re.compile(r'\b(0[1-9]|1[0-2])\/\d{2}\b')
expiry_matches = expiry_pattern.finditer(text_to_anonymize)

# Print expiration date matches and their indices
for match in expiry_matches:
    print(f"Expiration date match: {match.group()} at position {match.start()} to {match.end()}")
    text_to_anonymize = text_to_anonymize[:match.start()] + '***' + text_to_anonymize[match.end():]

print("Anonymized text:", text_to_anonymize)
