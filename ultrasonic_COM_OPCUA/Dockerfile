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

# Architekturen und Grundpakete installieren
RUN dpkg --add-architecture i386 && \
    apt-get update && apt-get install -y \
    wget gnupg2 software-properties-common

# WineHQ Key & Repo hinzufügen
RUN mkdir -pm755 /etc/apt/keyrings && \
    wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key && \
    wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/ubuntu/dists/jammy/winehq-jammy.sources

# Wine 10 + GUI-Tools installieren
RUN apt-get update && apt-get install -y \
    winehq-devel \
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

