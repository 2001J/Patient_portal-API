"""Patient API Controller"""

from flask import Flask, request, jsonify # type: ignore
from patient_db import PatientDB
import uuid


class PatientAPIController:
    def __init__(self):
        self.app = Flask(__name__)
        self.patient_db = PatientDB()
        self.setup_routes()
        self.run()

    def setup_routes(self):
        """
        Sets up the routes for the API endpoints.
        """
        self.app.route("/patients", methods=["GET"])(self.get_patients)
        self.app.route("/patients/<patient_id>", methods=["GET"])(self.get_patient)
        self.app.route("/patients", methods=["POST"])(self.create_patient)
        self.app.route("/patient/<patient_id>", methods=["PUT"])(self.update_patient)
        self.app.route("/patient/<patient_id>", methods=["DELETE"])(self.delete_patient)


    """
    TODO:
    Implement the following methods,
    use the self.patient_db object to interact with the database.

    Every method in this class should return a JSON response with status code
    Status code should be 200 if the operation was successful,
    Status code should be 400 if there was a client error,
    """

    def create_patient(self):
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No data provided'}), 400
        patient_id = str(uuid.uuid4())
        data['patient_id'] = patient_id
        patient_row = self.patient_db.insert_patient(data)
        if patient_row is None:
            return jsonify({'message': 'Failed to create patient'}), 400
        return jsonify({'message': 'Patient created successfully', 'patient_id': patient_id}), 200

    def get_patients(self):
        patients = self.patient_db.select_all_patients()
        return jsonify({'patients': patients}), 200

    def get_patient(self, patient_id):
        patient = self.patient_db.select_patient(patient_id)
        if patient is None:
            return jsonify({'message': 'Patient not found'}), 400
        return jsonify({'patient': patient}), 200

    def update_patient(self, patient_id):
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No input data provided'}), 400
        updated = self.patient_db.update_patient(patient_id, data)
        if not updated:
            return jsonify({'message': 'Failed to update patient'}), 400
        return jsonify({'message': 'Patient updated successfully', 'patient_id': patient_id, 'data': data}), 200

    def delete_patient(self, patient_id):
        deleted = self.patient_db.delete_patient(patient_id)
        if not deleted:
            return jsonify({'message': 'Failed to delete patient'}), 400
        return jsonify({'message': 'Patient deleted successfully', 'patient_id': patient_id}), 200

    def run(self):
        """
        Runs the Flask application.
        """
        self.app.run()


PatientAPIController()
