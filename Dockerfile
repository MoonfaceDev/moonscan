FROM python:3.10
RUN apt-get update && apt-get install -y iputils-ping
RUN pip install git+https://github.com/MoonfaceDev/moonscan.git
ADD https://svn.nmap.org/nmap/nmap-services nmap-services
ENTRYPOINT moonscan