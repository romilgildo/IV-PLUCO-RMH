FROM ubuntu:14.04
MAINTAINER Ruben Martin Hidalgo <rubenmartin1991@gmail.com>

RUN sudo apt-get update
RUN sudo apt-get install -y git
RUN sudo apt-get install -y build-essential
RUN sudo git clone https://github.com/romilgildo/IV-PLUCO-RMH.git
RUN cd IV-PLUCO-RMH && make install
