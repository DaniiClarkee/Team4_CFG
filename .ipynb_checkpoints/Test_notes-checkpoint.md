# Rose's notes

## Data inspection

Column 'Unnamed: 32' is an empty column and can be removed with `df_raw.drop('Unnamed: 32', axis=1)`

All other columns contain floats except for 'diagnosis' which contains objects: 357B, 212M.

There are 31 columns and 569 rows after removing 'Unnamed: 32'. That means 30 numerical features and 1 label per datapoint.

Can't really think of any good ways to visualise the data at this stage, except maybe a few histograms to show what some of the data looks like.

**Got this description from a [report](https://rstudio-pubs-static.s3.amazonaws.com/344010_1f4d6691092d4544bfbddb092e7223d2.html):**

"Ten real-valued features are computed for each cell nucleus:

* radius (mean of distances from center to points on the perimeter)
* texture (standard deviation of gray-scale values)
* perimeter
* area
* smoothness (local variation in radius lengths)
* compactness (perimeter^2 / area - 1.0)
* concavity (severity of concave portions of the contour)
* concave points (number of concave portions of the contour)
* symmetry
* fractal dimension (“coastline approximation” - 1)

The mean, standard error and “worst” or largest (mean of the three largest values) of these features were computed for each image, resulting in 30 features. For instance, field 3 is Mean Radius, field 13 is Radius SE, field 23 is Worst Radius."

Could be good to explain this in the presentation so that it's clear what we're analysing. Also this info is useful for deciding what visualisations to do because only the means (i.e. the first ten columns) will be interesting to look at.

To do:
* Inspect each feature to see if there are any outlying data points that need removing

## Visualisation ideas

The report in the link above has some good visualisations. We should colour the benign and malignant labelled points differently to show how their features differ.

Could include chart of which features were most important in labelling test data

## Preprocessing

1. Check for missing data
    * Doesn't seem to be any in this
2. Check for outliers
    * Probs just do this by looking at a graph
2. Encoding categorical data
    * Not needed for features, only needed for labels - 0 for B, 1 for M
3. Splitting into training and testing data
    * Decide on how much to split by
4. Feature scaling
    * Can't remember if we need to do this for all the models - ask Joel or check

Could look into more preprocessing techiniques but data seems very nice so probs not of much value.

## Presentation prep

Some notes on the main evaluation criteria:

* **Data Exploration and Processing**
   * Guess we'll just want to convey our understanding of the data, preprocessing measures that we've taken etc
* **Data Visualisation**
   * Must include at least 3, but imo the more the better
   * Some to help describe the data initially and then some to interpret the results of the analyses
* **Algorithm Implementation and Evaluation**
   * If we use a number of models, make sure they are coded and commented clearly 
   * Justify our choice of hyperparameters
   * Evaluate the models in the same ways so we can make direct comparisons, with a conclusion on which is best
* **Communication and Q&A Handling**
   * Well structured presentation (see below)
   * Make sure we split the topics between us so when a question is asked, we all know who should answer, then everyone can focus on learning their section well
* **Creativity (Some ideas for things we could do)**
   * Look into some more advanced preprocessing methods
   * Add another model to the ones we test - Neural net?
   * See if there are any more advanced or different comparison methods we could use

Presentation structure:
1. Intro:
    * Introduce ourselves
    * Explain what we will cover
2. Preprocessing:
    * Explain the structure of the data (with some visualisations)
    * Give examples of some of the steps we took to clean the data
3. The models:
    * Brief explanation of the models we tried and a bit about how they work (if there's time)
4. Model evaluation: 
    * How well the models worked, with side-by-side comparison
5. Conclusion:
    * Which model works best (for specific scenario)
    * What could be done to build on our work


Possible time-frame for project:
* Preprocess the data together
* Split the analysis between ourselves
* Spend rest of week 11 each working on our models and evaluating them
* Spend week 12 pooling our work and making the presentation and Jupyter notebook


To do:
* Decide whether to present with Jupyter or PowerPoint
* Work out who's doing what
* Work out how to present our Jupyter notebook - I reckon we want it like a scientific report

## Ask Joel

* What kind of visualisations does he find more useful in this kind of presentation
* How would their team go about this task (broadly)?
* Will we be presenting in front of other teams as well as instructors?
* Will we have to spend time explaining how the model works or will it just be quick
* Any other preprocessing methods we could try?

#Answers from Joel 
* dendragram
* feature scaling depends on model - would suggest for numerical. 


