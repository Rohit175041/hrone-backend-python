# 🛒 HROne Backend Intern Hiring Task

## ✅ Features

- Create Product
- List Products with filters (name, size, pagination)
- Create Order
- List Orders by User ID with pagination
- Dockerized setup
- Manual and Script-Based API Testing
- ✅ Logger support (file and console)

---

## 💻 Tech Stack

- **Backend:** FastAPI (Python 3.11)
- **Database:** MongoDB (MongoDB Atlas or local)
- **ODM/Driver:** PyMongo
- **API Testing:** Postman, Python `requests`
- **Logging:** Python `logging` (`logs/hrone.log`)
- **Containerization:** Docker

---

## 📁 Project Structure

hrone-backend-python/
├── Dockerfile
├── .env
├── requirements.txt
├── hrone_backend/
│ ├── init.py
│ ├── main.py
│ ├── db.py
│ ├── utils.py
│ ├── logger.py ✅ Logger config
│ ├── models/
│ │ └── order_model.py
│ ├── controllers/
│ │ └── order_controller.py
│ └── routes/
│ └── order_routes.py
├── logs/
│ └── hrone.log ✅ Log output file
├── test_runner.py ✅ Manual test script

----

## ⚙️ Environment Setup

1. Clone the project

```bash
git clone https://github.com/Rohit175041/hrone-backend-python.git
cd hrone-backend-python

----
Build Docker image:
docker build -t image_name .
docker run --env-file .env -p 3000:3000 image_name

----

To view logs inside container:
docker exec -it <container_id> tail -f logs/hrone.log
tail -f logs/hrone.log



#****************** .env file *********************************##
MONGO_URI=mogodb_atls_url
DB_NAME=hrone_db
PORT=3000
#
##************************************************************##
Run From DockerHub
docker pull rohit175041/hrone-backend-python
docker run --env-file .env -p 3000:3000 rohit175041/hrone-backend-python

#*******************************************************************#






