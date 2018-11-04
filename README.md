# Judging a Book by Its Cover

# Abstract
We would like to judge books by their covers and tell the story of how the aesthetics of a book's cover can influence its reception by the general public, as measured by its sales and reviews.

Originally, this problem was posed as whether the reviews of a book would be affected by the aesthetics of its cover but we decided to expand our investigation to also look into the effects on book sales. To write a review, buyers must first read the book so their reviews will presumably be much more dependent on the many pages of content that they went through, rather than the cover. Whereas while buying a book, one has access to less information that can be used to decide whether to make a purchase or not, and the cover of the book is one of those pieces of information. Hence we hypothesize that we will see a more pronounced correlation between the visual features of the cover of a book and its sales, as opposed to its reviews. We will use the Amazon dataset, which contains information about millions of books, along with their cover images, visual features extracted from those images, and buyer reviews. Through our analysis, we hope to uncover good and bad practices of making book covers and see how important they really are.

# Research questions
How important are the aesthetics of a book cover?
- Is it possible to find semantically meaningful/interpretable features of book covers that affect sales/reviews? 
- Do book covers affect the ratings?
- Does the author/publisher of a book have a stronger correlation with its sales/reviews compared to book cover design?	
- Does the importance of a book cover design depend on the genre?
- Are there “good cover pratices” and “bad cover pratices” we can find? 

# Dataset
The dataset we have chosen to work with is the amazon dataset (http://jmcauley.ucsd.edu/data/amazon/). Originally, this dataset is focused on reviews of the items, whereas we have chosen to focus mainly on the meta-data explaining the different products, though also taking the score of rating into account. 

The dataset is 20GB and available on the EPFL cluster. The dataset includes information on several categories, but we will throughout this project focus on books. Variables as ID, the price, the title, and the category are available and will be used. An important variable is the Sales rank, which is a popularity measure within the main category, and it is based on the number of times the book has been bought. Furthermore, the dataset includes 4096 visual features of the book covers already extracted using a deep convolutional neural network (CNN). First, we will try to answer the above research question using semantically meaningful features extracted by ourselves. This result will be compared with the 4096 features extracted from the CNN.

# A list of internal milestones up until project milestone 2
Week 1 (Nov 11): 
- Check that the relevant data and visual features are available in the cluster, take steps to make it available if necessary.
- Start exploring the data using descriptive statistics and plots.
- Start cleaning the data if necessary.

Week 2 (Nov 18): 
- Finish cleaning and exploration.
- Create semantically meaningful features.
- If needed, update the plan in a reasonable way depending on the findings from the exploration stage.

Week 3 (Nov 25): 
- Comment and debug the code.
- Firmly establish new goals before next milestone. 

# Questions for TAs
- Is it too big of a task to extract interpretable visual features (color, luminance, etc.) from the images ourselves?
