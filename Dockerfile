FROM ubuntu:16.04

RUN apt update -y
RUN apt -y install python3
RUN apt  -y install  python3-pip
RUN pip3 install flask

COPY . .

EXPOSE 5000

CMD [flask runflask run --host=0.0.0.0]


