"""
TODO: Implement the Patient class.
Please import and use the config and db config variables.

The attributes for this class should be the same as the columns in the PATIENTS_TABLE.

The Object Arguments should only be name , gender and age.
Rest of the attributes should be set within the class.

-> for id use uuid4 to generate a unique id for each patient.
-> for checkin and checkout use the current date and time.

There should be a method to update the patient's room and ward. validation should be used.(config is given)

Validation should be done for all of the variables in config and db_config.

There should be a method to commit that patient to the database using the api_controller.
"""
import uuid
from datetime import datetime
from api_controller import PatientAPIController
import config

class Patient:
    def __init__(self, name, gender, age):
        self.patient_id = str(uuid.uuid4())
        self.patient_name = name
        self.patient_gender = gender
        self.patient_age = age
        self.patient_checkin = datetime.now()
        self.patient_checkout = None
        self.patient_room = None
        self.patient_ward = None

    def update_room_and_ward(self, room, ward):
        self.patient_room = room
        self.patient_ward = ward
        self.validate()

    def validate(self):
        if not isinstance(self.patient_name, str):
            raise ValueError('Invalid name')
        if self.patient_gender not in config.GENDERS:
            raise ValueError('Invalid gender')
        if not isinstance(self.patient_age, int) or self.patient_age < 0:
            raise ValueError('Invalid age')
        if self.patient_room and self.patient_room not in sum(config.ROOM_NUMBERS.values(), []):
            raise ValueError('Invalid room')
        if self.patient_ward and self.patient_ward not in config.WARD_NUMBERS:
            raise ValueError('Invalid ward')

    def commit(self):
        self.validate()
        controller = PatientAPIController()
        controller.create_patient(self.__dict__)