#Base Image
FROM python:3.9-slim

#Working Directory
WORKDIR /app

#Copy the code from host to docker container
COPY . /app

#Required Libraries (This step defines the steps to be taken before building the image)
RUN pip install --no-cache-dir -r requirements.txt


# Expose the new port (e.g., 8080)
EXPOSE 5001

# Set the Flask environment variable to allow custom port
ENV FLASK_RUN_PORT=5001

# Run the application on the custom port (This step defines the steps to be taken once the complete image is built and just to run the application)
CMD ["python", "app.py", "--host=0.0.0.0", "--port=8080"]

