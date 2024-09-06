from presidio_analyzer import AnalyzerEngine, PatternRecognizer
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig
import json
from pprint import pprint

text_to_anonymize = "His name is Mr. Jones and his phone number is 212-555-5555"

analyzer = AnalyzerEngine()
analyzer_results = analyzer.analyze(text=text_to_anonymize, entities=["PHONE_NUMBER"], language='en')

print(analyzer_results)