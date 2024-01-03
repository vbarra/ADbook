#!/usr/bin/env python
# coding: utf-8

# # TP Régression linéaire

# In[1]:


try:
    import sklearn, numpy, matplotlib, ipywidgets, IPython 
except ModuleNotFoundError: 
    get_ipython().system('pip3 install --quiet sklearn numpy matplotlib ipywidgets IPython')
import sklearn, numpy, matplotlib, ipywidgets, IPython


# In[2]:


import numpy as np
import matplotlib.pyplot as plt

from ipywidgets import interact, interactive, IntSlider, Layout, interact_manual
import ipywidgets as widgets
from IPython.display import display

from sklearn.linear_model import LinearRegression,Lasso,Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


# ## Régression linéaire : premier exemple
# On s'intéresse ici à la régression d'une droite sur un nuage de points, bruité par un bruit normal $\mathcal{N}(m,\sigma^2)$, dont l'amplitude peut varier

# In[3]:


nb_points=50
# Paramètres de la "vraie droite" y=b0+b1.x
b0,b1 = 0.4,2.5

# Intervalle 
x1= np.linspace(0,10,10*nb_points)
x= np.random.choice(x1,size=nb_points)



def F(test_size,amp_bruit,var_bruit,moyenne_bruit):
    y=b0+b1*x+amp_bruit*np.random.normal(loc=moyenne_bruit,scale=var_bruit,size=nb_points)
    y_true=b0+b1*x


    X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=test_size,random_state=42)
    X_train=X_train.reshape(-1,1)
    X_test=X_test.reshape(-1,1)
    xmean = np.mean(X_train)
    ymean=np.mean(y_train)    

    
    lr = LinearRegression()
    lr.fit(X_train,y_train) 
    beta0,beta1=lr.intercept_,lr.coef_[0]

    train_pred = np.array(lr.predict(X_train))
    test_pred = np.array(lr.predict(X_test))
    train_score = lr.score(X_train,y_train)
    test_score = lr.score(X_test,y_test)
    RMSE_train=np.sqrt(np.mean(np.square(train_pred-y_train)))
    RMSE_test=np.sqrt(np.mean(np.square(test_pred-y_test)))
    
    plt.figure(figsize=(12,6))
    plt.title("Score Entrainement : {0:3.4f}, Test : {1:3.4f} --  RMSE Entrainement : {2:3.4f}, Test : {3:3.4f}".format(train_score,test_score,RMSE_train,RMSE_test),fontsize=16)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(X_train,train_pred,'r', label='Régression')
    plt.plot(x,y_true,c='black', label='Vraie droite')
    
    plt.scatter(X_train,y_train,c='b',label='Entrainement')
    plt.scatter(X_test,y_test,edgecolors='k',marker='x',c='g',s=100,label='test')
    plt.scatter(X_test,test_pred,edgecolors='k',marker='x',c='magenta',s=100,label='prédit')
    
    plt.text(6, 4, "Droite : $y = {0:3.4f}+{1:3.4f}x$".format(b0,b1),fontsize=16)
    plt.text(6, 2, "Régression : $y = {0:3.4f}+{1:3.4f}x$".format(beta0,beta1),fontsize=16)
    plt.text(6, 0, "$R={:3.4f}$".format(np.corrcoef(x,y)[0,1]),fontsize=16)

    plt.text(6, 6, "Centre de masse $X=({0:3.3f},{0:3.3f})^T$".format(xmean,ymean),fontsize=16)

    plt.text(xmean,ymean,"X",fontsize=20,label='Centre de masse')    


    plt.grid(True)
    plt.legend(loc='best')
    
    plt.tight_layout()
    plt.savefig('regression.png',dpi=100)


# In[4]:


m = interactive(F,amp_bruit=(0,5,1),var_bruit=(0,2,0.1),moyenne_bruit=(-3,3,0.5),
               test_size=widgets.RadioButtons(options={"10%":0.1,"30%":0.3,"50%":0.5},description="Test"),disabled=False,continuous_update=False)
display(m)


# ## Linéaire ne veut pas dire droite...

# In[5]:


nb_points=50
x1= np.linspace(-5,5,10*nb_points)
x= np.random.choice(x1,size=nb_points)


# In[6]:


def func_fit(model_type,test_size,degree,amp_bruit,var_bruit,moyenne_bruit):
    y=2*x-0.6*x**2+0.2*x**3+18*np.sin(x)
    y1=2*x1-0.6*x1**2+0.2*x1**3+18*np.sin(x1)
    y= y+amp_bruit*np.random.normal(loc=moyenne_bruit,scale=var_bruit,size=nb_points)
    
    X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=test_size,random_state=55)
    
    if (model_type=='Linéaire'):
        model = make_pipeline(StandardScaler(),PolynomialFeatures(degree,interaction_only=False),LinearRegression())
    if (model_type=='LASSO'):    
        model = make_pipeline(StandardScaler(),PolynomialFeatures(degree,interaction_only=False),Lasso())
        
    if (model_type=='Ridge'):    
        model = make_pipeline(StandardScaler(),PolynomialFeatures(degree,interaction_only=False),Ridge())
    
    X_train=X_train.reshape(-1,1)
    X_test=X_test.reshape(-1,1)
    
    model.fit(X_train,y_train)
    
    train_pred = np.array(model.predict(X_train))
    train_score = model.score(X_train,y_train)

    test_pred = np.array(model.predict(X_test))
    test_score = model.score(X_test,y_test)
    
    RMSE_train=np.sqrt(np.mean(np.square(train_pred-y_train)))
    RMSE_test=np.sqrt(np.mean(np.square(test_pred-y_test)))
       
    plt.figure(figsize=(14,6))
    plt.title("Score Entrainement : {0:3.4f}, Test : {1:3.4f} --  RMSE Entrainement : {2:3.4f}, Test : {3:3.4f}".format(train_score,test_score,RMSE_train,RMSE_test),fontsize=16)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.scatter(X_train,y_train,c='blue',label='Entraînement')
    plt.scatter(X_test,y_test,marker='x',c='g',s=100,label='test')
    plt.scatter(X_test,test_pred,marker='x',c='magenta',s=100,label='predit')
    plt.plot(x1,y1,c='k',lw=2,label='Vraie courbe')
    y2 = model.predict(x1.reshape(-1,1))
    plt.plot(x1,y2,c='r',lw=2,label='Courbe prédite')

    plt.grid(True)
    plt.legend(loc='best')
    
    plt.tight_layout()
       
    return (train_score,test_score)    


# In[7]:


m = interactive(func_fit,model_type=widgets.RadioButtons(options=['Linéaire','LASSO', 'Ridge'],description = "Choose Model",layout=Layout(width='250px')),
                test_size=widgets.RadioButtons(options={"10%":0.1,"30% ":0.3,"50%":0.5},description="Test"),
               degree=widgets.IntSlider(min=1,max=30,step=1,description= 'Degré',continuous_update=False),amp_bruit=(0,5,1),var_bruit=(0,2,0.1),moyenne_bruit=(-3,3,0.5))
display(m)


# In[ ]:




