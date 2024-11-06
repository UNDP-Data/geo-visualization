FROM giswqs/leafmap:latest

ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1
# Set the working directory
WORKDIR /usr/src/app


COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Make port 8888 available to the world outside this container
EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
