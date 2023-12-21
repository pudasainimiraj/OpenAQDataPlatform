# Parent Image : python:3.9-slim
FROM python:3.9-slim

#working directory for application
WORKDIR /app

#copying requirements.txt to working directory
COPY requirements.txt /app

#installing requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# set up application gateway
ENTRYPOINT [ "python" ]

