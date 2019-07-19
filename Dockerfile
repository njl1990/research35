FROM 1stclass/docker-python3-django2-alpine-base
MAINTAINER bowen
RUN ["pip","install","-i","http://mirrors.aliyun.com/pypi/simple/","--trusted-host","mirrors.aliyun.com","pymongo"]
RUN ["mkdir","-p","/usr/local/research35/web"]
COPY ./web /usr/local/research35/web
