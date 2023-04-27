FROM python:3.11

COPY . /selenuim
WORKDIR /selenium

# Install dependencies:
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Run the application:
COPY . .
RUN ["pytest", "-v"]
