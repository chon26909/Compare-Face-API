FROM python:3.9

WORKDIR /

COPY requirements.txt . 

RUN pip install -r requirements.txt

COPY main.py .
COPY compare_image.py .

CMD ["python", "main.py"]