# A MySQL container.
FROM python:3.6

# Place app in container.
COPY . /opt/client
WORKDIR /opt/client

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["/bin/bash", "entrypoint.sh"]