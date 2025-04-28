# Use an ARM64-compatible Python 3.10+ base image
FROM arm64v8/python:3.11  

# Set the working directory
WORKDIR /app

# Copy application files
COPY dist/ /app/
COPY requirements.txt /app/requirements.txt

# Install dependencies (if any)
RUN pip install -r requirements.txt

# Run the application
CMD ["python", "app.py"]


# # Use an ARM64-compatible base image
# FROM arm64v8/python:latest  

# # Set the working directory
# WORKDIR /app

# # Install dependencies required for PyArmor runtime
# RUN apt-get update && apt-get install -y libstdc++6

# # Copy the obfuscated app and runtime explicitly
# COPY dist/app.py /app/app.py
# COPY dist/pyarmor_runtime_000000 /app/pyarmor_runtime_000000
# COPY requirements.txt /app/requirements.txt

# # Install Python dependencies
# RUN pip install -r requirements.txt

# # Set library path for the PyArmor runtime
# ENV LD_LIBRARY_PATH=/app/pyarmor_runtime_000000

# # Run the application
# CMD ["python", "app.py"]



# # Use an ARM64-compatible base image
# FROM arm64v8/python:latest  

# # Set the working directory
# WORKDIR /app

# # Copy application files
# # COPY . .
# COPY dist/ /app/
# # COPY dist/pyarmor_runtime_000000 /app/pyarmor_runtime_000000
# COPY requirements.txt /app/requirements.txt

# # Install dependencies (if any)
# RUN pip install -r requirements.txt

# # Run the application
# CMD ["python", "app.py"]
# # CMD ["python", "pyarmor_runtime.py", "app.py"]
# # CMD ["python", "/app/app.py"]
