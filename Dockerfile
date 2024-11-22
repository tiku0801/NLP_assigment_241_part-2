FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN ls
RUN python -m pip install --upgrade pip && \
    pip install -r /app/requirements.txt && \
    rm -rf /root/.cache/pip
CMD ["python","nlp/main.py","docker"]