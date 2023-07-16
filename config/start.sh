#!/bin/bash

# update and install docker
sudo yum update -y
sudo yum install -y docker
sudo service docker start
sudo usermod -a -G docker ec2-user

# install docker-compose
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# download YAML
cd /home/ec2-user
curl -o docker-compose.yml "https://configuration.weaviate.io/v2/docker-compose/docker-compose.yml?generative_cohere=false&generative_palm=false&image_neural_model=keras-resnet50&media_type=image&modules=modules&ref2vec_centroid=true&reranker_cohere=false&runtime=docker-compose&weaviate_version=v1.20.1"

sudo docker-compose up 