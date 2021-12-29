FROM python:3.7-alpine
RUN mkdir /app
COPY Scores.txt , MainScores.py /app
EXPOSE 5000
RUN pip install flask
CMD python /app/MainScores.py