FROM python:3.11
LABEL maintainer='hellengoll@gmail.com'

WORKDIR /selenium
COPY . .

# Chrome
RUN apt-get update; apt-get clean
RUN apt-get install -y wget
RUN apt-get install -y gnupg
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get -y install google-chrome-stable

COPY requirements.txt ./
RUN pip install -r requirements.txt

CMD pytest -v
