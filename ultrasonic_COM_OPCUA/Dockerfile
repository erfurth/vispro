FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive
ENV DISPLAY=:0

RUN apt-get update && apt-get install -y \
    wine-stable \
    x11-apps \
    x11vnc \
    xvfb \
    fluxbox \
    xterm && \
    rm -rf /var/lib/apt/lists/*

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y wine32

RUN mkdir -p ~/.vnc
RUN x11vnc -storepasswd 1234 ~/.vnc/passwd

COPY . /com-opcua-bridge

EXPOSE 3010 4841

CMD Xvfb :0 -screen 0 1024x768x24 & \
    fluxbox & \
    x11vnc -display :0 -passwd 1234 -forever

