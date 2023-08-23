# Use an official Python runtime as a parent image
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable to set the PostgreSQL connection parameters
ENV PG_HOST=db PG_USER=ryne PG_PASSWORD=secret PG_DB=rynedb

# Run app.py when the container launches
CMD ["python", "app.py"]
