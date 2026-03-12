# Use an official Python runtime as the base image
FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /app

# Install uv package manager
RUN pip install uv

# Copy the project files into the container
COPY pyproject.toml uv.lock ./

# Install project dependencies using uv
RUN uv sync --frozen --no-dev

# Copy the rest of the application code
COPY main.py ./

# Expose the port the app runs on
EXPOSE 7860

# Define the command to run the application
CMD ["uv", "run", "uvicorn", "main:mcp_app", "--host", "0.0.0.0", "--port", "7860", "--proxy-headers"]