"""ALS model. 2025-06-12"""
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score

def train(X,y):
    m=GradientBoostingClassifier(n_estimators=200,learning_rate=0.05,max_depth=4,random_state=42)
    m.fit(X,y); return m

def cv_score(m,X,y,cv=5):
    s=cross_val_score(m,X,y,cv=StratifiedKFold(cv,shuffle=True,random_state=42),scoring="f1_weighted")
    return {"mean_f1":s.mean(),"std":s.std()}
