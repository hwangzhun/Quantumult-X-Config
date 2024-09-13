import os
from extract_rule import extract_rule

rule_file = "rule_collection/rule_data/Apple.json"
output_rule_file = "rule/ios/Apple.json"

extract_rule(rule_file, output_rule_file)