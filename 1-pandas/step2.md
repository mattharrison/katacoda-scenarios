# Load and process data

In this section, you will load the data (a CSV file in `ames-housing-dataset.zip`) and prepare it for machine learning.

Open the file ``predict.py`` in the editor.

Create a function, ``get_data``, to load the data from the 
Here's a single line of runnable code:

`python3 -m pytest -k load`{{execute}}

## Clean up data

Our first goal will be to make a classifier. We want be able to predict Building Type (the *Bldg Type* column) from the other columns.

Here are the types:

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

You task is to create a function, `tweak_ames_classification`, that keeps the above columns. It should also fill in any missing values of numeric columns with 0 (we could do this will scikit-learn or pandas to do this, we will use pandas this time). Finally, it should replace missing values in the *Electrical* column with `'SBrkr'` (Standard Circuit Breakers & Romex).

Put this function in `predict.py`. Once you have finished writing the function, run this command from the terminal to test it:

`python3 -m pytest -k tweak_clf`{{execute}}

Your next task is integrate the `tweak_ames_classification` function into a scikit-learn transformer. Create a class, `AmesClassificationTransformer` that calls `tweak_ames_classification` in the  `.transform` method.

`python3 -m pytest -k clf_transformer`{{execute}}

(hint: subclass both `sklearn.base.BaseEstimator` and `sklearn.base.TransformerMixin`. Implement a `.transform` method that calls `tweak_ames_classification`. Make a `.fit` method the returns `self`.)

## Pipeline

Now you need to make a pipeline for your classifier. It will have a few steps.

#. Call the ``AmesClassificationTransformer``
#. Call a `ColumnTransformer` that uses `sklearn.preprocessing.OneHotEncoder` on the categorical columns and `sklearn.preprocessing.StandardScalar` on the numeric columns.
#. Adds in a classifier on the end.

Make a function called `get_clf_pipeline` that returns the pipeline.
