FROM ubuntu:jammy

RUN export DEBIANFRONTEND=noninteractive
RUN apt-get update
RUN apt-get update && apt-get install -y locales
ENV LANG en_US.utf8
RUN apt-get install pandoc -y
RUN apt-get install make
RUN apt-get install zip -y
RUN apt-get install python3 -y
RUN cp bin/python3 bin/python
RUN mkdir youtube-dl
COPY ./ ./youtube-dl
RUN cd youtube-dl && make install

