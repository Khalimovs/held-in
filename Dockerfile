# the base image for the python that we are using for the project
FROM python:3.9.0-alpine

ENV PYHTONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# creating a folder.
RUN mkdir -p /home/user

ENV HOME=/home/user
ENV APP_HOME=/home/user/web

WORKDIR ${APP_HOME}

RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/media


RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev zlib zlib-dev jpeg-dev
RUN apk add --no-cache bash python pkgconfig git gcc openldap \
                       libcurl python2-dev gpgme-dev libc-dev \
                        && rm -rf /var/cache/apk/*


RUN pip install --upgrade pip

COPY ./requirements.txt ${APP_HOME}/requirements.txt

RUN pip install -r requirements.txt
COPY entrypoint.sh ${APP_HOME}/entrypoint.sh

RUN addgroup -S user && adduser -S user -G user

COPY . ${APP_HOME}

RUN chown -R user:user $APP_HOME

USER user

ENTRYPOINT [ "/home/user/web/entrypoint.sh" ]
