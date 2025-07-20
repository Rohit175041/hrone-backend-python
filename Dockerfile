FROM python:3.11

# Set work directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the app port
EXPOSE 3000

# Start server using Uvicorn and hrone_backend.main:app
CMD ["uvicorn", "hrone_backend.main:app", "--host", "0.0.0.0", "--port", "3000"]
