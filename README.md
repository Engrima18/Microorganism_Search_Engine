# Microorganism_Search_Engine

Final project for the "Cloud Computing" course at La Sapienza University of Rome.

## Brief description
<img src="https://github.com/Engrima18/Microorganism_Search_Engine/assets/114066138/9a7c4e5c-b6b4-4da5-963b-8a01bbef6698" width=20% height=20% align="left">

The goal of this project is to develop an application that provides a search engine for images of bacteria. The search engine should be able to retrieve the most similar images to a given query image, uploaded by the user. The project will be deployed on Amazon Web Services and the ”algorithmic part” to compute similarity among
images will be done using Weaviate.

<br/>

<img src="https://github.com/Engrima18/Microorganism_Search_Engine/assets/93355495/ee4720e3-8a38-4242-abb6-c797ed4ad519" width=30% height=35%><img src="https://github.com/Engrima18/Microorganism_Search_Engine/assets/93355495/bb7ebf6f-b196-443f-93fd-1a5a2da94fd2" width=30% height=30% ><img src="https://github.com/Engrima18/Microorganism_Search_Engine/assets/93355495/c653b5ae-c998-48be-9fca-f673a52abe22" width=30% height=30%>

<br/>

## Weaviate and the pre-trained NN
<img src="https://github.com/Engrima18/Microorganism_Search_Engine/assets/93355495/8f718d98-37a6-4a8a-95ae-6bbb3226f797" width=35% height=40% align="right">
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
<img src="https://github.com/Engrima18/Microorganism_Search_Engine/assets/93355495/39c0c571-c750-4e3e-a93e-3172a2447215" width=30% height=35% align="right">

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

<img src="https://github.com/Engrima18/FlashLearnChain/assets/93355495/755cd041-6290-46b2-9413-80c6d2479c6b" align="center">

