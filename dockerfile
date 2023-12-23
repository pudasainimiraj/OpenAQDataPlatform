# Parent Image : python:3.9-slim
FROM python:3.9-slim

#working directory for application
WORKDIR /app

#installing requirements
RUN pip install --upgrade pip


#copying requirements.txt to working directory
COPY ./requirements.txt ./requirements.txt
COPY ./OpenAQDataPlatform ./OpenAQDataPlatform
COPY ./api_utilities ./api_utilities

RUN pip install --no-cache-dir -r requirements.txt
# set up application gateway
ENTRYPOINT [ "python" ]

