FROM python:3.7.3-alpine

ARG APP_SRC

WORKDIR $APP_SRC
COPY . $APP_SRC

RUN pip install --no-cache-dir -r requirements.txt
RUN ln -s $(pwd)/bruteforcer.sh /usr/bin/bruteforcer

CMD tail -f /dev/null
