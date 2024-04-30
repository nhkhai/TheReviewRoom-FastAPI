FROM python:alpine

RUN apt-get -y update

RUN mkdir /home/app
RUN chmod 755 /home/app

COPY ./requirements.txt /home/app
WORKDIR /home/app

USER app

RUN pip install --no-cache-dir --no-warn-script-location -r requirements.txt
ENV PATH="$PATH:/home/app/.local/bin"

COPY . /home/app
WORKDIR /home/app

CMD [  "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]