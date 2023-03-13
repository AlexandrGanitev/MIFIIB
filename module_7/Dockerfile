FROM python:3.9
WORKDIR /code
LABEL Author=A.Ganitev
LABEL module=7.10
COPY ./requirements.txt /code/requirements.txt
# folder /code belongs to the inner structure of this Docker container
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app /code/app
EXPOSE 3009
ENTRYPOINT ["python3"]
CMD ["app:main", "--host", "0.0.0.0", "--port", "3009"]
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
