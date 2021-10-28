```
# predict.py
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

def get_data():
    return pd.read_csv('ames-housing-dataset.zip')

def tweak_ames_classification(df):
    cols = ['Lot Frontage', 'Lot Area',
       'Lot Config', 'Land Slope', 'Neighborhood', 'House Style', 'Overall Qual',
       'Overall Cond', 'Year Built', 'Year Remod/Add', 'BsmtFin SF 1',
       'BsmtFin SF 2', 'Bsmt Unf SF', 'Total Bsmt SF',
       'Heating', 'Heating QC', 'Central Air', 'Electrical', '1st Flr SF',
       '2nd Flr SF', 'Bsmt Full Bath',
       'Bsmt Half Bath', 'Full Bath', 'Half Bath', 'Garage Cars', 'Mo Sold', 'Yr Sold',
       'SalePrice']
    
    return (df[cols]
 .assign(**{col:df[col].fillna(df[col].mean()) for col in df[cols].select_dtypes('number').columns},
        **{'Electrical': 'SBrkr'})
)


class AmesClassifierTransformer(BaseEstimator, TransformerMixin):
    def transform(self, X):
        # assume X is data from csv without label colum
        X = tweak_ames_classification(X)
        return X
    def fit(self, X, y):
        return self

def get_clf_pipeline(model=DecisionTreeClassifier,
                     *model_args, **model_kwargs):
    categories=['Lot Config', 'Land Slope', 'Neighborhood', 'House Style',
       'Heating', 'Heating QC', 'Central Air', 'Electrical']
    numerics = ['Lot Frontage', 'Lot Area', 'Overall Qual', 'Overall Cond',
       'Year Built', 'Year Remod/Add', 'BsmtFin SF 1', 'BsmtFin SF 2',
       'Bsmt Unf SF', 'Total Bsmt SF', '1st Flr SF', '2nd Flr SF',
       'Bsmt Full Bath', 'Bsmt Half Bath', 'Full Bath', 'Half Bath',
       'Garage Cars', 'Mo Sold', 'Yr Sold', 'SalePrice']
    preproc = ColumnTransformer(transformers=[
        ('cat', OneHotEncoder(drop='first'), categories),
        ('std', StandardScaler(), numerics )
    ])
    
    pipeline = Pipeline(
        steps=[('act', AmesClassifierTransformer()),
               ('preproc', preproc),
               ('clf', model(*model_args, **model_kwargs))
               ]
    )
    return pipeline

```
