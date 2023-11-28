FROM python:3.8
WORKDIR /app
COPY . /app
EXPOSE 8081
CMD ["python", "todo.py"]