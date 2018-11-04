# Title
Judging a book by its cover

# Abstract
In many situations, people will choose products based on first hand impressions or personal rule of thumbs. As an example, studies show that people choose wine based on the etiquette. Originally, this problem was posed as whether the reviews would be affected by the book covers, but we thought it was unrealistic that any correlation from this question could be due to an actual causation, since a review require you to actually read the book, whereas it only takes one click to buy. 
Instead, we will In this project examine whether people tend to buy books on Amazon based on the book covers, and in relation to this we will try to find specific good and bad practices of book covers. Furthermore, we will examine whether the ratings are correlated with the book covers. 
As a comparison, we will examine the correlation between author/publicor and the sales score, and extract information about what is the most important factor for the internet buyers. 

Ultimately, we would like to answer the overall question of whether people are impulse-buying based on visual appearance or basing their choice on content or author.

# Research questions
Do visual features of book covers affect book sales?

- Is it possible to find semantically meaningful features of book covers that affect sales? 
- Do book covers affect the ratings?
- Does author/publisher have a stronger correlation with sales compared to book cover design?	
- Does the importance of a book cover design depend on the genre?
- Are there “good cover pratices” and “bad cover pratices” we can find? 

# Dataset
The dataset we have chosen to work with is the amazon dataset (http://jmcauley.ucsd.edu/data/amazon/). Originally, this dataset is focused on reviews of the items, whereas we have chosen to focus mainly on the meta-data explaining the different products. 

The dataset is 20GB and available on the EPFL cluster. The dataset includes information on several categories, but we will throughout this project focus on books. Variables as the ID, the price, the title, and the category are available and will be used. An important variable is the Sales rank, which is a popularity measure within the main category, and it is based on the number of times the book has been bought. Furthermore, the dataset includes around 4000 visual features of the book covers already extracted using a deep convolutional neural network. First, we will try to answer the above research question using semantically meaningful features extracted by ourselves. This result will be compared with the 4000 features extracted from the CNN.


# A list of internal milestones up until project milestone 2
Add here a sketch of your planning for the next project milestone.

# Questions for TAa
Add here some questions you have for us, in general or project-specific.
