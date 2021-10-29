## Pipeline

Now you need to make a pipeline for your classifier. It will have a few steps.

#. Call the ``AmesClassificationTransformer``
#. Call a `ColumnTransformer` that uses `sklearn.preprocessing.OneHotEncoder` on the categorical columns and `sklearn.preprocessing.StandardScalar` on the numeric columns.
#. Adds in a classifier on the end.

Make a function called `get_clf_pipeline` that returns the pipeline.




