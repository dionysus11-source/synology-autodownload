FROM python:latest

WORKDIR /app
COPY ./ ./

RUN apt-get update
RUN apt-get install cron -y
RUN python -m pip install --upgrade pip
RUN pip install selenium
RUN pip install requests
RUN pip install schedule
RUN wget https://chromedriver.storage.googleapis.com/97.0.4692.71/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
#RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get update
RUN apt-get install google-chrome-stable -y
RUN useradd -ms /bin/bash newuser
RUN chown -R newuser:newuser /app
USER newuser
#CMD [ "python", "torrent_see.py" , "놀면"]
CMD [ "python", "CronManager.py"]
#CMD [ "/bin/bash"]