FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install molbloom

WORKDIR /repo
COPY . /repo
