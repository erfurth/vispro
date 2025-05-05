# FROM ubuntu:latest

# ENV DEBIAN_FRONTEND=noninteractive
# ENV DISPLAY=:0

# RUN apt-get update && apt-get install -y \
#     wine-stable \
#     x11-apps \
#     x11vnc \
#     xvfb \
#     fluxbox \
#     xterm && \
#     rm -rf /var/lib/apt/lists/*

# RUN dpkg --add-architecture i386 && \
#     apt-get update && \
#     apt-get install -y wine32

# RUN mkdir -p ~/.vnc
# RUN x11vnc -storepasswd 1234 ~/.vnc/passwd

FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive
ENV DISPLAY=:0

# 1. Architektur und Basispakete installieren
RUN dpkg --add-architecture i386 && \
    apt update && \
    apt install -y wget gnupg2 software-properties-common

# 2. WineHQ GPG-Key & Paketquellen hinzufügen
RUN wget -O - https://dl.winehq.org/wine-builds/winehq.key | apt-key add -
RUN  add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ jammy main'

# 3. Wine 10 + GUI-Tools installieren
RUN apt update && \
    apt install -y --install-recommends \
    winehq-stable \
    x11-apps \
    x11vnc \
    xvfb \
    fluxbox \
    xterm

# Optional: Wine 32-bit Support (häufig schon durch winehq-devel abgedeckt)
RUN apt-get install -y wine32

# VNC Passwort setzen
RUN mkdir -p ~/.vnc && \
    x11vnc -storepasswd 1234 ~/.vnc/passwd

COPY . /com-opcua-bridge

EXPOSE 3010 4841 5900 21 30000-30009

CMD Xvfb :0 -screen 0 1024x768x24 & \
    fluxbox & \
    x11vnc -display :0 -passwd 1234 -forever

