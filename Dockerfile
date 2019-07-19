FROM 1stclass/docker-python3-django2-alpine-base
MAINTAINER bowen
RUN ["mkdir","-p","/usr/local/research35/web"]
COPY ./web /usr/local/research35/web
COPY ./35research.cloud.key /usr/local/research35/35research.cloud.key
COPY ./35research.cloud.pem /usr/local/research35/35research.cloud.pem
RUN ["pip","install","-i","http://mirrors.aliyun.com/pypi/simple/","--trusted-host","mirrors.aliyun.com","pymongo"]
RUN ["pip","install","-i","http://mirrors.aliyun.com/pypi/simple/","--trusted-host","mirrors.aliyun.com","django-extensions"]
RUN ["pip","install","-i","http://mirrors.aliyun.com/pypi/simple/","--trusted-host","mirrors.aliyun.com","django-werkzeug-debugger-runserver"]
RUN ["pip","install","-i","http://mirrors.aliyun.com/pypi/simple/","--trusted-host","mirrors.aliyun.com","pyOpenSSL"]