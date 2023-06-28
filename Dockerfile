FROM python:3

WORKDIR /usr/src/app

RUN apt update; apt install -y libgl1

COPY ./ ./
RUN pip install -r requirements.txt

CMD ["python3", "./image_processing.py"]

