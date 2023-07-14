#!/bin/bash
yum update -y
yum install docker python3-pip
usermod -a -G docker ec2-user
pip3 install docker-compose
systemctl enable docker.service
systemctl start docker.service

pip3 install docker-compose --user

curl -o docker-compose.yml "https://configuration.weaviate.io/v2/docker-compose/docker-compose.yml?generative_cohere=false&generative_palm=false&image_neural_model=keras-resnet50&media_type=image&modules=modules&ref2vec_centroid=true&reranker_cohere=false&runtime=docker-compose&weaviate_version=v1.20.1"
docker-compose up