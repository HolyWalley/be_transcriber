FROM python:3.10.12-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libsndfile1 \
    ffmpeg

RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip3 install Cython
RUN pip3 install nemo_toolkit['all']

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0"]
