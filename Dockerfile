FROM bentoml/model-server:0.11.0-py312
MAINTAINER ersilia

RUN pip install molbloom==2.3.4

WORKDIR /repo
COPY . /repo
