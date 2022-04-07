FROM python:3
WORKDIR /usr/app/
COPY . .
#########
#########
RUN apt-get clean
##########
RUN pip3 install pandas
CMD ["p.py"]
