# Microorganism_Search_Engine

Final project for the "Cloud Computing" course at La Sapienza University of Rome.

## Brief description
<img src="https://github.com/Engrima18/Microorganism_Search_Engine/assets/114066138/9a7c4e5c-b6b4-4da5-963b-8a01bbef6698" width=20% height=20% align="left">

The goal of this project is to develop an application that provides a search engine for images of bacteria. The search engine should be able to retrieve the most similar images to a given query image, uploaded by the user. The project will be deployed on Amazon Web Services and the ”algorithmic part” to compute similarity among
images will be done using Weaviate.

<br/>
<br/>

## Weaviate and the pre-trained NN

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

In order to allow the scaling of our application we would like to implement it through
a set of microservices such that the single functions can be scaled individually. But
identifying the set of microservices in which an application can be split in isn’t a trivial
task, however we identified three main components of our application:
>- A web user interface from which our user can interact with the application;
>- An API call for querying the database;
>- The vector database itself.
