#!/bin/bash

request_payload_path="payloads/update_patient.json"

payload=$(cat "$request_payload_path")
patient_id="d638356b-c015-4586-81ad-e6980568f76d"

curl -X PUT -H "Content-Type: application/json" -d "$payload" "127.0.0.1:5000/patient/$patient_id"