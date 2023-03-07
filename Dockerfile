FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 80 443
CMD ["python3","bot.py"]