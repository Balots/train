FROM python:3.9-slim 

WORKDIR /model           
COPY /AppFiles ./

RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirements.txt

EXPOSE 3000

CMD ["python", "main.py"] 
