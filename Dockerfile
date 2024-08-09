FROM apache/airflow:2.7.1-python3.11

# Copy requirements file
COPY requirements.txt /opt/airflow/

# Switch to root user to install additional packages
USER root

# Install gcc and python3-dev
RUN apt-get update && apt-get install -y gcc python3-dev

# Switch back to airflow user
USER airflow

# Install Python dependencies
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt

# Copy the rest of your application code
COPY . /opt/airflow/

# Set the PYTHONPATH environment variable
ENV PYTHONPATH="/opt/airflow"

# Set the working directory
WORKDIR /opt/airflow