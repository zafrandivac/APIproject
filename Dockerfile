FROM python:3.10.7-slim
WORKDIR /APIproject
COPY requirements.txt /APIproject/requirements.txt
RUN pip install -r requirements.txt
COPY . /APIproject
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]