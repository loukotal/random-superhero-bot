FROM ubuntu:16.04

RUN apt-get update -y && apt-get install -y openssl libffi-dev gcc musl python3-pip python3-dev

RUN mkdir /code

RUN pip3 install --upgrade pip

ADD requirements.txt ./

RUN pip3 install -r requirements.txt
RUN pip3 install tensorflow

ADD ./ /code/

WORKDIR /code


CMD ["python3 app/app.py"]
