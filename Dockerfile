FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y ca-certificates curl git && rm -rf /var/lib/apt/lists/*
WORKDIR /app
CMD [ "bash" ]
