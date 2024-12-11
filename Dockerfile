# Step 1: Use the official Python image from Docker Hub
FROM python:3.9-slim

# Step 2: Set environment variables
# This prevents Python from writing .pyc files to disc and ensures output is logged directly to the terminal
ENV PYTHONUNBUFFERED 1

# Step 3: Set the working directory inside the container
WORKDIR /app

# Step 4: Copy the requirements file into the container
COPY requirements.txt /app/

# Step 5: Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Copy the Django project files into the container
COPY . /app/

# Step 7: Expose the port the app will run on
EXPOSE 8000

# Step 8: Define the command to run the Django app using Gunicorn (WSGI server)
CMD ["gunicorn", "BLOG.wsgi:application", "--bind", "0.0.0.0:8000"]
