FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Set the working directory in the container
# WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

# Copy the rest of the project files to the container
COPY . .

# Expose the port that the application will be running on
#EXPOSE 8000

# Run the application
#CMD ["python", "main.py"]