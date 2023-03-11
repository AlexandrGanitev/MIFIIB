FROM python:3.9
WORKDIR /app
LABEL Author=A.Ganitev
LABEL module=7.10
COPY . /app
RUN pip install --no-cache-dir /code/requirement.txt
EXPOSE 3009
ENTRYPOINT ["python3"]
CMD ["main.py"]