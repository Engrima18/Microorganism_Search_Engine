# Microorganism_Search_Engine

Final project for the "Cloud Computing" course at La Sapienza University of Rome.

## Brief description
<img src="https://github.com/Engrima18/Microorganism_Search_Engine/assets/93355495/f1c13eea-9130-4ad5-bee5-6579bc8ec452" width=20% height=20% align="left">

The goal of this project is to develop an application that provides a search engine for images of bacteria. The search engine should be able to retrieve the most similar images to a given query image, uploaded by the user. The project will be deployed on Amazon Web Services and the ”algorithmic part” to compute similarity among
images will be done using Weaviate.

<br/>

Upload the image           |     Search the most similar bacterias     | Analyze the specs
:-------------------------:|:-------------------------: |:-------------------------:
<img src="https://github.com/Engrima18/Microorganism_Search_Engine/assets/93355495/c83ea911-0a5f-46f5-a69d-fbe81d056aac"> | <img src="https://github.com/Engrima18/Microorganism_Search_Engine/assets/93355495/cd7485c2-0d25-45c7-8369-e50695a1b5cd"> | <img src="https://github.com/Engrima18/Microorganism_Search_Engine/assets/93355495/f2367f00-a650-4aaa-9a9f-e65e76df494f">



## Weaviate and the pre-trained NN
<img src="https://github.com/Engrima18/Microorganism_Search_Engine/assets/93355495/a598a9d7-663e-4780-a097-eae0c638e081" width=35% height=40% align="right">
We will use a
tool like Weaviate pre-trained neural network to extract features from the images
and create a fast index of reference items.
When a query image is provided, the search engine will compare the features of the
query image with the features of the reference items in the index and return the most
similar images.
The key point of the Weaviate usage is the embedding of images in a vectorial databese.
When the user add an image (or any other data object) to Weaviate, the vector
database computes a vector embedding for that image using a given model. This
vector is then placed into an index, allowing the database to quickly perform searches
by finding the most similar vectors in the database to a given query vector.

## Microservices architecture
<img src="https://github.com/Engrima18/Microorganism_Search_Engine/assets/93355495/3f9b13c6-d5d0-43f7-ae30-79b664911891" width=30% height=35% align="right">

In order to allow the scaling of our application we would like to implement it through
a set of microservices such that the single functions can be scaled individually. But
identifying the set of microservices in which an application can be split in isn’t a trivial
task, however we identified three main components of our application:
>- A web user interface from which our user can interact with the application;
>- An API call for querying the database;
>- The vector database itself.

## Scaling with AWS
The implementative solution involves the use of an EC2 instance on which to directly upload
the already containerized application. In this first, fairly trivial example, a call to
lambda function via a specific event on the web page (in an S3 bucket) is then always
expected, and the lambda code will then provide for using the EC2 computational
resource to launch the two docker images. Finally, the computed output will be
returned dynamically and asynchronously (with respect to the request from the client).
The following steps then power to good scalability performance:
1. Set up an Auto Scaling group: we create an Auto Scaling group using our Launch
Configuration. We specify the desired capacity, minimum and maximum number
of instances, and scaling policy. The Auto Scaling group will automatically
launch and terminate instances based on the defined criteria.
2. Configure a load balancer: we set up an Elastic Load Balancer (ELB), in particular
an Application Load Balancer (ALB) to distribute incoming traffic across our
EC2 instances. We configure the load balancer to listen on the appropriate ports
and protocols for our web app, i.e. port 80 for the HTTP protocol.
3. Add instances to the load balancer: we associate the instances launched by the
Auto Scaling group with our load balancer. This ensures that traffic is evenly
distributed among the instances (fairness performance).
4. Monitor and adjust scaling: finally we can monitor the performance of our web
app and adjust the scaling policies as needed.

<img src="https://github.com/Engrima18/Microorganism_Search_Engine/assets/93355495/2f0f8bc4-98e7-4c22-8379-8d949f22346d" align="center">

## Team:
"GanziManzi" team

>- [Matteo Migliarini](https://github.com/Mamiglia)
>- [Giuseppe Di Poce](https://github.com/giuseppedipoce)
>- [Enrico Grimaldi](https://github.com/Engrima18)

## Used technologies
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![ESLint](https://img.shields.io/badge/ESLint-4B3263?style=for-the-badge&logo=eslint&logoColor=white)
![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D)
![LaTeX](https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

