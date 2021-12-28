from pycaret.anomaly import *
from sklearn.datasets import load_breast_cancer
import time

df = load_breast_cancer(as_frame=True)['data']
df_train = df.iloc[:-10]
df_unseen = df.tail(10)

anom = setup(data = df_train, silent = True)

anom_model = create_model(model = 'iforest', fraction = 0.05)

results = assign_model(anom_model)
print(results)

plot_model(anom_model, plot = 'tsne')

plot_model(anom_model, plot = 'umap')

save_model(model = anom_model, model_name = 'iforest_model')

loaded_model = load_model('iforest_model')

loaded_model.predict(df_unseen)
loaded_model.predict_proba(df_unseen)
loaded_model.decision_function(df_unseen)