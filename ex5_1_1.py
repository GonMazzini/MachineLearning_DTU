# exercise 5.1.1

import numpy as np

# Names of data objects
dataobjectNames = [
    'Human',
    'Python',
    'Salmon',
    'Whale',
    'Frog',
    'Komodo dragon',
    'Bat',
    'Pigeon',
    'Cat',
    'Leopard shark',
    'Turtle',
    'Penguin',
    'Porcupine',
    'Eel',
    'Salamander',
    ]

# Attribute names
attributeNames = [
    'Body temperature',
    'Skin cover',
    'Gives birth',
    'Aquatic creature',
    'Aerial creature',
    'Has legs',
    'Hibernates'
    ]

# Attribute values
X = np.asarray(np.mat('''
    1 1 1 0 0 1 0;
    0 2 0 0 0 0 1;
    0 2 0 1 0 0 0;
    1 1 1 1 0 0 0;
    0 0 0 2 0 1 1;
    0 2 0 0 0 1 0;
    1 1 1 0 1 1 1;
    1 3 0 0 1 1 0;
    1 4 1 0 0 1 0;
    0 2 1 1 0 0 0;
    0 2 0 2 0 1 0;
    1 3 0 2 0 1 0;
    1 5 1 0 0 1 1;
    0 2 0 1 0 0 0;
    0 0 0 2 0 1 1 '''))

# Class indices
y = np.asarray(np.mat('3 4 2 3 0 4 3 1 3 2 4 1 3 2 0').T).squeeze()

# Class names
classNames = ['Amphibian', 'Bird', 'Fish', 'Mammal', 'Reptile']
    
# Number data objects, attributes, and classes
N, M = X.shape
C = len(classNames)

print('Ran Exercise 5.1.1')

# %% 
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df=pd.DataFrame(data=X, columns=attributeNames)
df['Class']=y

#sns.heatmap(df.corr(), yticklabels=False, cmap='Greens', annot=False)

# %%
def gini_impurity(classes,df,rule='None'):
    """Calculate the purity gain using Gini criterion."""

    value=[]
    for x in classes:
        value.append(sum(df['Class']==x))
    
    Ir=1-np.sum([(x/len(df))**2 for x in value])
    print(value)
    print(f'root impurity {Ir}')
    
    
    value_v1=[]
    for x in classes:
        value_v1.append(sum(df[(rule)==True]['Class']==x))
        
    Iv1=1-np.sum([(x/len(df[(rule)==True]))**2 for x in value_v1])
    print(value_v1)
    print(f'true branch impurity: {Iv1}')
    
    
    value_v2=[]
    for x in classes:
        value_v2.append(sum(df[(rule)==False]['Class']==x))
        
    Iv2=1-np.sum([(x/len(df[(rule)==False]))**2 for x in value_v2])
    print(value_v2)
    print(f'false branch impurity: {Iv2}')
    
    
    purity_gain=Ir-( len(df[(rule)==True])/len(df))*Iv1-( len(df[(rule)==False])/len(df))*Iv2
    print(f'Purity gain: {purity_gain}')
    return purity_gain



# %%
# "First split"
# gini_impurity(np.arange(0,5),df, rule=df['Body temperature']<=0.5)
# "Second level splits"
# import warnings
# warnings.filterwarnings("ignore")
# #gini_impurity(np.arange(0,5),df[split_1==True], rule=df['Skin cover']<=1.0)

# gini_impurity(np.arange(0,5),df[split_1==False], rule=df['Gives birth']<=0.5)























