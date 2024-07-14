# Django API Documentation

## Introduction
Welcome to the Qure API documentation. This API allows you to manage  entities such as persons, practitioners, patients, organizations, subscriptions, patient records, consultations, transfers, and accounts.

**Base URL of the API**: `https://bright-medicals-727e99a79ed2.herokuapp.com/qure/api/`

---

## Endpoints

### Person

- **Create and List Persons**
  - **Endpoint**: `/person/`
  - **HTTP Method**: `GET` and `POST`
  - **Description**: Allows listing all persons and creating new ones.
  - **GET Request Example**:
    ```http
    GET /person/
    ```
  - **POST Request Example**:
    ```json
    POST /person/
    {
        "name": "John",
        "surname": "Doe",
        "sex": "Male",
        "dob": "1990-01-01",
        "address": "123 Main St",
        "email": "john.doe@example.com",
        "tel": "1234567890",
        "country": "USA"
    }
    ```

- **Retrieve, Update, and Delete a Person**
  - **Endpoint**: `/person/<int:pk>/`
  - **HTTP Method**: `GET`, `PUT`, `PATCH`, `DELETE`
  - **Description**: Allows retrieving, partially or fully updating, and deleting a person by ID.
  - **GET Request Example**:
    ```http
    GET /person/1/
    ```
  - **PATCH Request Example**:
    ```json
    PATCH /person/1/
    {
        "address": "456 Main St"
    }
    ```
  - **DELETE Request Example**:
    ```http
    DELETE /person/1/
    ```

### Practician

- **Create and List Practicians**
  - **Endpoint**: `/pratician/`
  - **HTTP Method**: `GET` and `POST`
  - **Description**: Allows listing all practicians and creating new ones.
  - **POST Request Example**:
    ```json
    POST /pratician/
    {
        "person_id": 1,
        "order": "12345",
        "title": "Dr.",
        "occupation": "Cardiologist",
        "speciality": "Heart Surgery"
    }
    ```

- **Retrieve, Update, and Delete a Practician**
  - **Endpoint**: `/pratician/<int:pk>/`
  - **HTTP Method**: `GET`, `PUT`, `PATCH`, `DELETE`
  - **Description**: Allows retrieving, partially or fully updating, and deleting a practician by ID.

### Organization

- **Create and List Organizations**
  - **Endpoint**: `/organization/`
  - **HTTP Method**: `GET` and `POST`
  - **Description**: Allows listing all organizations and creating new ones.
  - **POST Request Example**:
    ```json
    POST /organization/
    {
        "name": "Health Clinic",
        "type_organization": "Hospital",
        "city": "New York",
        "country": "USA"
    }
    ```

- **Retrieve, Update, and Delete an Organization**
  - **Endpoint**: `/organization/<int:pk>/`
  - **HTTP Method**: `GET`, `PUT`, `PATCH`, `DELETE`
  - **Description**: Allows retrieving, partially or fully updating, and deleting an organization by ID.

### Subscription

- **Create and List Subscriptions**
  - **Endpoint**: `/subcription/`
  - **HTTP Method**: `GET` and `POST`
  - **Description**: Allows listing all subscriptions and creating new ones.
  - **POST Request Example**:
    ```json
    POST /subcription/
    {
        "organization_id": 1,
        "dos": "2023-01-01",
        "status": "Active"
    }
    ```

- **Retrieve, Update, and Delete a Subscription**
  - **Endpoint**: `/subcription/<int:pk>/`
  - **HTTP Method**: `GET`, `PUT`, `PATCH`, `DELETE`
  - **Description**: Allows retrieving, partially or fully updating, and deleting a subscription by ID.

### Patient

- **Create and List Patients**
  - **Endpoint**: `/patient/`
  - **HTTP Method**: `GET` and `POST`
  - **Description**: Allows listing all patients and creating new ones.
  - **POST Request Example**:
    ```json
    POST /patient/
    {
        "person_id": 1,
        "abo": "A",
        "rh": "+"
    }
    ```

- **Retrieve, Update, and Delete a Patient**
  - **Endpoint**: `/patient/<int:pk>/`
  - **HTTP Method**: `GET`, `PUT`, `PATCH`, `DELETE`
  - **Description**: Allows retrieving, partially or fully updating, and deleting a patient by ID.

### Consultation

- **Create and List Consultations**
  - **Endpoint**: `/consultation/`
  - **HTTP Method**: `GET` and `POST`
  - **Description**: Allows listing all consultations and creating new ones.
  - **POST Request Example**:
    ```json
    POST /consultation/
    {
        "patient_id": 1,
        "practician_id": 1,
        "reason": "Routine check-up",
        "systolic": 120,
        "diastolic": 80,
        "weight": 70,
        "heart_rate": 70
    }
    ```

- **Retrieve, Update, and Delete a Consultation**
  - **Endpoint**: `/consultation/<int:pk>/`
  - **HTTP Method**: `GET`, `PUT`, `PATCH`, `DELETE`
  - **Description**: Allows retrieving, partially or fully updating, and deleting a consultation by ID.

### PatientRecord

- **Create and List Patient Records**
  - **Endpoint**: `/record/`
  - **HTTP Method**: `GET` and `POST`
  - **Description**: Allows listing all patient records and creating new ones.
  - **POST Request Example**:
    ```json
    POST /record/
    {
        "patient_id": 1,
        "organization_id": 1
    }
    ```

- **Retrieve, Update, and Delete a Patient Record**
  - **Endpoint**: `/record/<int:pk>/`
  - **HTTP Method**: `GET`, `PUT`, `PATCH`, `DELETE`
  - **Description**: Allows retrieving, partially or fully updating, and deleting a patient record by ID.

### Transfert

- **Create and List Transfers**
  - **Endpoint**: `/transfert/`
  - **HTTP Method**: `GET` and `POST`
  - **Description**: Allows listing all transfers and creating new ones.
  - **POST Request Example**:
    ```json
    POST /transfert/
    {
        "patient_record_id": 1,
        "organization_id": 2
    }
    ```

- **Retrieve, Update, and Delete a Transfer**
  - **Endpoint**: `/transfert/<int:pk>/`
  - **HTTP Method**: `GET`, `PUT`, `PATCH`, `DELETE`
  - **Description**: Allows retrieving, partially or fully updating, and deleting a transfer by ID.

### Account

- **Create and List Accounts**
  - **Endpoint**: `/user/`
  - **HTTP Method**: `GET` and `POST`
  - **Description**: Allows listing all accounts and creating new ones.
  - **POST Request Example**:
    ```json
    POST /user/
    {
        "practician_id": 1,
        "organization_id": 1,
        "username": "johndoe",
        "password": "securepassword",
        "is_active": true
    }
    ```

- **Retrieve, Update, and Delete an Account**
  - **Endpoint**: `/user/<int:pk>/`
  - **HTTP Method**: `GET`, `PUT`, `PATCH`, `DELETE`
  - **Description**: Allows retrieving, partially or fully updating, and deleting an account by ID.

---

## Usage Examples

### Create a new Practician
```json
POST /pratician/
{
    "person_id": 1,
    "order": "12345",
    "title": "Dr.",
    "occupation": "Cardiologist",
    "speciality": "Heart Surgery"
}
