FROM docker.io/library/ubuntu:24.04

# run linux commands
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# copy Makefile and source to container
COPY 590MakefileLab/ /app/590MakefileLab/

# set 590MakefileLab as the working directory
WORKDIR /app/590MakefileLab

# run make command to compile source code
RUN make

# run unit tests
CMD ["make", "test"]
