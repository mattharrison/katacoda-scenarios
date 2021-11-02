## Pipeline

You are almost down! Now you need to make a pipeline for your classifier. 


Make a function called `get_clf_pipeline` that creates a pipeline. Put the following steps in your pipeline:

- The ``AmesClassificationTransformer``
- A `ColumnTransformer` that uses `sklearn.preprocessing.OneHotEncoder` on the categorical columns and `sklearn.preprocessing.StandardScalar` on the numeric columns.
- A decision tree classifier.








