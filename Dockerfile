FROM python:latest

WORKDIR /app
COPY ./ ./

RUN apt-get update
RUN apt-get install cron -y
# RUN sudo apt-get install python3-pip -y
RUN python -m pip install --upgrade pip
RUN pip install selenium
RUN wget https://chromedriver.storage.googleapis.com/96.0.4664.45/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get update
RUN apt-get install google-chrome-stable -y

CMD [ "python" , "torrentsee.py"]