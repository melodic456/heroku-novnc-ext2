FROM ubuntu:22.04

LABEL AboutImage "Ubuntu22.04_Chromium_NoVNC"

LABEL Maintainer "Apoorv Vyavahare <apoorvvyavahare@pm.me>"

ARG DEBIAN_FRONTEND=noninteractive

#VNC Server Password
ENV	VNC_PASS="samplepass" \
#VNC Server Title(w/o spaces)
	VNC_TITLE="Chromium" \
#VNC Resolution(720p is preferable)
	VNC_RESOLUTION="1280x720" \
#VNC Shared Mode (0=off, 1=on)
	VNC_SHARED=0 \
#Local Display Server Port
	DISPLAY=:0 \
#NoVNC Port
	NOVNC_PORT=$PORT \
	PORT=8080 \
#Locale
	LANG=en_US.UTF-8 \
	LANGUAGE=en_US.UTF-8 \
	LC_ALL=C.UTF-8 \
	TZ="Asia/Kolkata"

COPY rootfs/ /

RUN mkdir /opt/mydir
# Copy zip files to /opt directory
COPY *.gz /opt/mydir/
RUN mkdir /apps
RUN mkdir /apps/python
COPY *.png /apps/python/

SHELL ["/bin/bash", "-c"]

RUN	apt-get update && \
	apt-get install -y  tzdata ca-certificates supervisor curl wget python3 python3-pip sed unzip xvfb x11vnc websockify openbox libnss3 libgbm-dev libasound2 && \
#Chromium
	wget https://commondatastorage.googleapis.com/chromium-browser-snapshots/Linux_x64/1210214/chrome-linux.zip -P /tmp && \
#    mkdir -p /opt/mydir/IAPIFMCEEOKIKOMAJPCCAJHJPACJMIBE_3_4_30_0 && \
#    unzip /opt/mydir/IAPIFMCEEOKIKOMAJPCCAJHJPACJMIBE_3_4_30_0.zip -d /opt/mydir/first && \
#    mkdir -p /opt/mydir/PABJFBCIAEDOMJJFELFAFEJKPPKNJLEH_1_11_4_0 && \
#    unzip /opt/mydir/PABJFBCIAEDOMJJFELFAFEJKPPKNJLEH_1_11_4_0.zip -d /opt/mydir/second && \
#    mkdir -p /opt/mydir/NKBIHFBEOGAEAOEHLEFNKODBEFGPGKNN_11_4_1_0 && \
#    unzip /opt/mydir/NKBIHFBEOGAEAOEHLEFNKODBEFGPGKNN_11_4_1_0.zip -d /opt/mydir/third && \
	tar -zxvf /opt/mydir/first.tar.gz -C /opt/mydir/ && \
    tar -zxvf /opt/mydir/second.tar.gz -C /opt/mydir/ && \
    tar -zxvf /opt/mydir/third.tar.gz -C /opt/mydir/ && \
    unzip /tmp/chrome-linux.zip -d /opt && \
	
#noVNC
	openssl req -new -newkey rsa:4096 -days 36500 -nodes -x509 -subj "/C=IN/ST=Maharastra/L=Private/O=Dis/CN=www.google.com" -keyout /etc/ssl/novnc.key  -out /etc/ssl/novnc.cert && \
#TimeZone
	ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
	echo $TZ > /etc/timezone && \
#Python MOdules
	pip3 install requests && \
#Wipe Temp Files
	rm -rf /var/lib/apt/lists/* && \ 
	apt-get remove -y wget python3-pip unzip && \
	apt-get -y autoremove && \
	apt-get clean && \
	rm -rf /tmp/*

# Create a directory named "mydir" in the Docker image


# Extract each zip file separately

ENTRYPOINT ["supervisord", "-l", "/var/log/supervisord.log", "-c"]

CMD ["/config/supervisord.conf"]
