FROM python:3.11
WORKDIR /app
EXPOSE 5000
RUN pip install flask
COPY . .
CMD [ "flask", "run", "--host", "0.0.0.0"]
