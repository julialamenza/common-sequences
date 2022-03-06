FROM python:latest
ADD solution.py /
WORKDIR /nr-test

COPY . .

CMD [ "python", "./solution.py", "moby-dick.txt" ]