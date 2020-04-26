FROM centos:7

RUN yum update -y \
 && yum -y install yum-utils \
 && yum -y install https://centos7.iuscommunity.org/ius-release.rpm \
 && yum -y install python36u \
 && yum -y install python36u-pip \
 && yum -y install python-devel \
 && yum -y install git-core \
 && yum -y install gcc-c++

RUN pip3.6 install --upgrade pip

COPY ./src /src

ENV PYTHONPATH="$PYTHONPATH:/src"

RUN mkdir /logs
RUN chmod 777 /logs
RUN chmod 777 /src

COPY requirements.txt /src
RUN pip3.6 install --trusted-host pypi.python.org -r /src/requirements.txt

WORKDIR /src

EXPOSE 8011

#CMD ["python3.6", "predict_ticket.py"]