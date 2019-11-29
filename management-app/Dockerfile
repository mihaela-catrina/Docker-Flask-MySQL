# specify the image you want to use build docker image

FROM python:3.6

# Maintainer name to let people know who made this image.

MAINTAINER Mihaela <catrina.mihaela20@gmail.com>

#apt is the ubuntu command line tool for advanced packaging tool(APT) for sw upgrade '''

RUN apt update && \
    apt install -y netcat-openbsd

# Place app in container.
COPY . /opt/www
WORKDIR /opt/www

# Copy in the application code from your work station at the current directory
# over to the working directory.

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


CMD ["/bin/bash", "management_app_entrypoint.sh"]