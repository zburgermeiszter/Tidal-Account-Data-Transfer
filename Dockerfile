FROM python:3-alpine

RUN pip install --upgrade pip

RUN adduser -D user
USER user

ENV PATH="/home/user/.local/bin:${PATH}"

RUN mkdir -p /home/user/app
WORKDIR /home/user/app

COPY --chown=user:user requirements.txt .
RUN pip install -r requirements.txt

COPY --chown=user:user . .

# CMD [ "python3" ]