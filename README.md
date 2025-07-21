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

<img width="263" height="316" alt="image" src="https://github.com/user-attachments/assets/5d78111b-61f3-4afe-95ce-4df412565072" />



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






