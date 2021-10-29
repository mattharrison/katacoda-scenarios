## Load and process data

We are going to make a classifier. We want be able to predict Building Type (the *Bldg Type* column) from the other columns.

Here are the building types:

* *1Fam* - Single-family Detached	
* *2FmCon* - Two-family Conversion; originally built as one-family dwelling
* *Duplx* - Duplex
* *TwnhsE* - Townhouse End Unit
* *TwnhsI* - Townhouse Inside Unit

We will us pandas to filter out the columns. Here are the columns we will keep (I put them in a Python list for you😉):

```
    cols = ['Lot Frontage', 'Lot Area',
       'Lot Config', 'Land Slope', 'Neighborhood', 'House Style', 'Overall Qual',
       'Overall Cond', 'Year Built', 'Year Remod/Add', 'BsmtFin SF 1',
       'BsmtFin SF 2', 'Bsmt Unf SF', 'Total Bsmt SF',
       'Heating', 'Heating QC', 'Central Air', 'Electrical', '1st Flr SF',
       '2nd Flr SF', 'Bsmt Full Bath',
       'Bsmt Half Bath', 'Full Bath', 'Half Bath', 'Garage Cars', 'Mo Sold', 'Yr Sold',
       'SalePrice']
```


All of your work will be done in the `predict.py` file.

* Create a function, `get_data`, that reads the CSV file from `ames-housing-dataset.zip` and returns a pandas data frame.


* Create a function, `tweak_ames_classification`, that keeps the above columns. It should also fill in any missing values of numeric columns with 0 (we could do this will scikit-learn or pandas to do this, we will use pandas this time). Finally, it should replace missing values in the *Electrical* column with `'SBrkr'` (Standard Circuit Breakers & Romex).

## Transformer

Your next task is integrate the `tweak_ames_classification` function into a scikit-learn transformer. Create a class, `AmesClassificationTransformer` that calls `tweak_ames_classification` in the  `.transform` method.

## Pipeline

Now you need to make a pipeline for your classifier. It will have a few steps.

#. Call the ``AmesClassificationTransformer``
#. Call a `ColumnTransformer` that uses `sklearn.preprocessing.OneHotEncoder` on the categorical columns and `sklearn.preprocessing.StandardScalar` on the numeric columns.
#. Adds in a classifier on the end.

Make a function called `get_clf_pipeline` that returns the pipeline.




