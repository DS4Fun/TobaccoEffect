import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from yellowbrick.regressor import ResidualsPlot

import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std

def plot_residuals(x, y, title, standard=True):
    scaler = StandardScaler()
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, random_state=1)

    if standard:
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.fit_transform(X_test)

    # fit the transformed features to Linear Regression
    poly_model = LinearRegression()
    # poly_model.fit(X_train_poly, Y_train)
    ax = plt.axes()
    ax.set_title(title)
    visualizer = ResidualsPlot(poly_model, ax=ax)
    visualizer.fit(X_train, Y_train)  # Fit the training data to the visualizer
    visualizer.score(X_test, Y_test)  # Evaluate the model on the test data
    visualizer.show()  # Finalize and render the figure


def compute_ols(x, y):
    x = sm.add_constant(x)
    model = sm.OLS(y, x)
    res = model.fit()
    return res


df = pd.read_csv('data/tobacco_data.csv')

df.drop(['Country', 'Year' ] , axis=1, inplace=True)
y_f = np.array(df['Tobac_Use_F'])
y_m = np.array(df['Tobac_Use_M'])

lr_df = df.drop(['Tobac_Use_M', 'Tobac_Use_F'] , axis=1)
# x = lr_df.to_numpy()
cols = ['Tax_2015',
       'Happiness_Score', 'Afford_2015', 'Ban_Score_Dir_Ads',
       'Ban_Score_Indr_Ads', 'Ban_Score_add_indir_ads', 'Warn_Score',
       'Ban_Score_places']


x = lr_df
res_f = compute_ols(x, y_f)
res_m = compute_ols(x, y_m)

print("Female results:")
print(res_f.summary())

print("Male results:")
print(res_m.summary())
