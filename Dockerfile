FROM jenkins/inbound-agent

USER root

RUN apt-get update && apt-get install -y python3

USER jenkins