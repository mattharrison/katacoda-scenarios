## Pipeline

Now you need to make a pipeline for your classifier. Put the following steps in your pipeline:

- The ``AmesClassificationTransformer``
- A `ColumnTransformer` that uses `sklearn.preprocessing.OneHotEncoder` on the categorical columns and `sklearn.preprocessing.StandardScalar` on the numeric columns.
- A decision tree classifier.

Make a function called `get_clf_pipeline` that returns the pipeline.




