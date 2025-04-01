# Use the official Python image as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR ./

# Install build-essential and other necessary system packages
RUN apt update && apt install -y build-essential

# Install Python dependencies
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . ./

# Expose the port the app runs on
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
