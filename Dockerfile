FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents
COPY . .

# Setting the environment variable
ENV INPUT_DIR=/app/input_files
ENV OUTPUT_DIR=/app/output_files

# Run task.py
CMD ["python", "task.py"]