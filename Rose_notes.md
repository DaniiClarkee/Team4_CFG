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

## Ask Joel

* What kind of visualisations does he find more useful in this kind of presentation
* How would their team go about this task (broadly)?
* Will we be presenting in front of other teams as well as instructors?

