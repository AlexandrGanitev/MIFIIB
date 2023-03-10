FROM python:3.9
WORKDIR /app
LABEL Author=A.Ganitev
LABEL module=7.10
COPY ./app /code/requirements
# folder /code belongs to the inner structure of this Docker container
RUN pip install --no-cache-dir /code/requirement.txt
EXPOSE 3009
ENTRYPOINT ["python", "sanner_ag.py"]