FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /project

# Copy only the files necessary to install dependencies
COPY requirements.txt /project/

# Install dependencies
RUN pip install --upgrade pip \
    && apt-get update \
    && apt-get install -y dos2unix \
    && pip install -r /project/requirements.txt

# Copy the rest of the files
COPY . /project/

# Make sure the build script is executable
RUN dos2unix /project/build_files.sh \
    && chmod +x /project/build_files.sh
