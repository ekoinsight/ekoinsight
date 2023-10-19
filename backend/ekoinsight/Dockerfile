FROM python:3.9



WORKDIR /app

COPY . /app



RUN apt-get update
RUN apt-get install  -y libgl1 cmake
RUN pip install --upgrade setuptools
RUN pip install --upgrade pip
RUN pip install cmake
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu


EXPOSE 8000

# Run app.py when the container launches
CMD ["python", "app.py"]

