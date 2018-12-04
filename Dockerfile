FROM python:3.6

WORKDIR /smi-slave

COPY . /smi-slave

RUN pip install --no-cache-dir -r requirements.txt

CMD ["flask", "run", "--host", "0.0.0.0"]