Patients Portal Project Guide

Introduction

The Patients Portal is a basic patient management system designed for receptionists to handle various tasks related to patient records. Key functionalities include listing patients, reading patient details, creating, updating, and deleting patient records.

Prerequisites

Ensure the following prerequisites are met before proceeding:

Install Python (recommended version >= 3.10).
Optional: Install Gitbash.
Downloading

To download the repository, follow these steps:

Forking the Repository:
Fork the Repository: Visit the repository link and click on the "Fork" button. Rename the forked repository to patients-portal.

Clone the Forked Repository:

bash
Copy code
git clone https://github.com/<your-username>/patients-portal.git
Navigate to the Repository:
bash
Copy code
cd patient-portal
Cloning the Repository:
Clone the Repository:
bash
Copy code
git clone https://github.com/gerelee357/patients-portal-for-students
Navigate to the Repository:
bash
Copy code
cd patients-portal-for-students
Building Project Environment

Set up the project environment by following these steps:

Create a Virtual Environment:
bash
Copy code
python -m venv venv
Activate the Virtual Environment:

In Linux (Gitbash):
bash
Copy code
source venv/bin/activate
In Windows:
bash
Copy code
source venv/Scripts/activate
Install Python Packages:
bash
Copy code
python -m pip install -r requirements.txt
Running Server

Start the Flask server by running the API_CONTROLLER (src/api_controller.py) directly or using the provided Linux command:

bash
Copy code
python src/api_controller.py
Completing Function Definitions

In the src/api_controller.py file, replace the placeholder pass statements with appropriate code to fulfill the requirements for each function. Ensure proper exception handling.

Point Allocation: Each function definition is worth 3 points, totaling 15 points.

Once functions are implemented, the Patient Portal application will support various user tasks related to patient records.

Testing the Final Application

After starting the Flask server, open a new terminal and navigate to the testing-api-templates directory. Use provided scripts or web browser to test the application:

Create a patient.
List patients.
List patients with a given name.
Read a patient with a certain ID.
Update patient data.
Delete a patient.
Note

If encountering a port conflict (port 5000 already in use), follow the provided steps to resolve it.

References

Flask Documentation: Flask
Flask Cheatsheet: Flask Cheatsheet
Swagger Editor: Swagger Editor
Python OOP: Python OOP
Feedback

For clarification or assistance, contact the task originator, Aadarsh Mehdi, via LinkedIn.

LinkedIn Profile: Aadarsh Mehdi
