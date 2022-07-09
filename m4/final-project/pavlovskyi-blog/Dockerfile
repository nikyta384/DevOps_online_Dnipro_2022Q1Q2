FROM python:slim-buster
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install flask
WORKDIR /usr/myapp
ENV FLASK_APP=app
COPY . .
#RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
