FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /project

# Copiar solo los archivos necesarios para instalar las dependencias
COPY requirements.txt /project/

# Instalar dependencias
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copiar el resto de los archivos
COPY . /project/
