DevTrack is a lightweight, backend-only API designed for engineering teams to report bugs, set priorities, and track task statuses. 
It utilizes Object-Oriented Programming (OOP) principles within the Django framework, managing data through local JSON.

## How to Run the Project? ##
1. Clone the Repository
   git clone https://github.com/Namrathabp/DevTrack/new/main
   cd devtrack
2. Set up the Virtual Environment
   python -m venv .venv
3. Activate the Virtual Environment
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate # macOS/Linux
4. Install Django
   pip install django
5. Start the Server: Navigate to the directory containing `manage.py` and run
   python manage.py runserver
6. Server started running in local host of your PC

## API Endpoints ##
### **Reporter Endpoints**
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **POST** | `/api/reporters/` | Creates a new reporter. Requires `id`, `name`, `email`, and `team`. |
| **GET** | `/api/reporters/` | Returns a list of all registered reporters. |
| **GET** | `/api/reporters/?id=1` | Returns a specific reporter by their unique ID. |

### **Issue Endpoints**
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **POST** | `/api/issues/` | Creates a bug report. Logic varies based on `priority`. |
| **GET** | `/api/issues/` | Returns all recorded issues. |
| **GET** | `/api/issues/?id=1` | Returns a specific issue by ID. |
| **GET** | `/api/issues/?status=open` | Returns issues filtered by their current status. |

## Testing using Postman ##

## Reporter
*Reporter Created Successfully [POST Method]
<img width="1577" height="1000" alt="image" src="https://github.com/user-attachments/assets/1ae4c26d-28d2-4201-b28d-a66f9d957fce" />
*Reporter Fetched Successfully through ID [GET Method]
<img width="1577" height="1000" alt="image" src="https://github.com/user-attachments/assets/035bb2de-6ad1-4032-be6d-e5725a6fc2db" />

## Issues
* Issue Fetched Successfully status code: 200
<img width="1577" height="1000" alt="image" src="https://github.com/user-attachments/assets/073e761c-6e43-4a07-8219-abdd1cf161a2" />
* Issue Reported Successfully status code: 201
<img width="1577" height="1000" alt="image" src="https://github.com/user-attachments/assets/f7b7fd28-0a09-4339-86ce-16999f903826" />
* Bad request status code: 400
<img width="1577" height="1000" alt="image" src="https://github.com/user-attachments/assets/07022812-6aa5-46e3-a74e-610fe3304786" />
* Issue not present status code: 404
<img width="1577" height="1000" alt="image" src="https://github.com/user-attachments/assets/aefc92f9-b98e-4d62-9569-31c82e49a358" />
