# FordVJ
  #Create the project folder:
    mkdir sensor_streaming_backend
    cd sensor_streaming_backend

  #Install Flask and Redis libraries:
    pip install Flask redis

#Set Up Docker
  #Create a Dockerfile for the Flask app:
    # Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]

#Create a requirements.txt file:
  Flask
  redis

#Create a docker-compose.yml file:

    version: '3'services:  web:    build: .    ports:      - "5000:5000"    depends_on:      - redis  redis:    image: "redis:alpine"

#Build and Run the Containers
  #Build and start the containers:

    docker-compose up --build
#Test the API
  #Use Postman or curl to test the endpoints:
  *To record a new temperature:

  curl -X POST http://localhost:5000/record -H "Content-Type: application/json" -d '{"temperature": 75}'

  *To collect the average temperature:

  curl http://localhost:5000/collect
#Monitor and Maintain

  Regularly check the logs for both the Flask app and Redis to ensure everything is functioning correctly. You can access the logs using:

  docker-compose logs

#Collaborate with the Mobile Team
  Share API documentation and endpoint details with the mobile development team to ensure they can integrate seamlessly.


  
