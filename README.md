Objective:

Develop a set of APIs for user registration, login, linking an ID, and implementing joins and chain delete functionality using Python and MongoDB.

Requirements:
            
1. Framework and Libraries:
   - Utilize FastAPI for the web framework.
   - Use PyMongo for interacting with MongoDB.

2. API Endpoints:
   - Registration API: Endpoint to register a new user.
   - Login API: Endpoint to authenticate an existing user.
   - Linking ID API: Endpoint to link an ID to a user's account.
   - Joins: Implement functionality to join data from multiple collections.
   - Chain Delete: Implement functionality to delete a user and all associated data across collections.

3. Database:
   - Use MongoDB to store user information.

instructions:

1. Setup FASTAPI and PyMongo:
   - Create a new Flask application.
   - Configure PyMongo to connect to your MongoDB instance.

2. Registration API:
   - Create an endpoint that allows users to register by providing necessary details such as username, email, and password.
   - Ensure that passwords are securely hashed before storing them in the database.

3. Login API:
   - Create an endpoint that allows users to log in by verifying their credentials (email and password).
   - Implement appropriate error handling.

4. Linking ID API:
   - Create an endpoint that allows users to link an ID to their account.
   - Ensure that the ID is stored securely and associated with the correct user.

5. Joins:
   - Implement functionality to join data from multiple collections, enabling complex queries that involve multiple data sources.

6. Chain Delete:
   - Implement functionality to delete a user and all associated data across collections, ensuring that all related records are properly removed.



Implementation:

STEP1: pip install -r requirements.txt

STEP2: cd app/

STEP3: RUN command "uvicorn main:app --reload"

STEP4: Testing the API:

4.1 Test the Registration API
      
![image](https://github.com/user-attachments/assets/ef435ead-16e8-4cec-9991-dad763edb189)

![image](https://github.com/user-attachments/assets/8b6a87cc-d79e-4ed1-9aea-a48bda7035e5)

![image](https://github.com/user-attachments/assets/1ead41ce-9123-4a09-a212-e97e95449b38)


4.2 Test the Login API 
![image](https://github.com/user-attachments/assets/23599f63-be9a-4a35-b75b-270334cdfabe)

4.3 Test the Linking ID API
![image](https://github.com/user-attachments/assets/e59864bf-aa1a-480d-8cf2-fe1502e05cdb)

4.4 Test the Joins API
![image](https://github.com/user-attachments/assets/d52e81de-d8f5-49a0-af85-cd84dcdf0004)

![image](https://github.com/user-attachments/assets/dc2be8bf-0ce3-4d8f-86a0-db5157642ff7)

4.5 Test the Chain Delete API
![image](https://github.com/user-attachments/assets/d0720295-9124-4b1d-9027-edbc7fa3b578)

