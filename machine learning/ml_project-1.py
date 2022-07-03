import pandas as pd

import numpy as np

from sklearn.preprocessing import OrdinalEncoder

from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_squared_log_error,mean_squared_error,mean_absolute_error,mean_absolute_percentage_error

import datetime

from sklearn.ensemble import RandomForestRegressor

from sklearn.linear_model import LinearRegression

from xgboost import XGBRegressor

from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt

import seaborn as sns

from keras.models import Sequential

from keras.layers import Dense

from prettytable import PrettyTable

df=pd.read_csv('../input/Participant_Data_TheMathCompany_.DSHH/train.csv')

df.head()

# Data Inspection

df.shape

df.describe().transpose()

df.info()

sns.pairplot(df, diag_kind='kde')

# Data Preprocessing

df.drop('ID',axis=1,inplace=True)

df['Levy']=df['Levy'].replace('-',np.nan)

df['Levy']=df['Levy'].astype(float)

levy_mean=0

df['Levy'].fillna(levy_mean,inplace=True)

df['Levy']=round(df['Levy'],2)

milage_formats=set()

def get_milage_format(x):

    x=x.split(' ')[1]

    milage_formats.add(x)

df['Mileage'].apply(lambda x:get_milage_format(x));

milage_formats

#since milage is in KM only we will remove 'km' from it and make it numerical

df['Mileage']=df['Mileage'].apply(lambda x:x.split(' ')[0])

df['Mileage']=df['Mileage'].astype('int')

df['Engine volume'].unique()

df['Turbo']=df['Engine volume'].apply(lambda x:1 if 'Turbo' in str(x) else 0)

df['Engine volume']=df['Engine volume'].apply(lambda x:str(x).replace('Turbo',''))

df['Engine volume']=df['Engine volume'].astype(float)

cols=['Levy','Engine volume', 'Mileage','Cylinders','Airbags']

sns.boxplot(df[cols[0]]);

cols=['Levy','Engine volume', 'Mileage','Cylinders','Airbags']

sns.boxplot(df[cols[1]]);

cols=['Levy','Engine volume', 'Mileage','Cylinders','Airbags']

sns.boxplot(df[cols[2]]);

cols=['Levy','Engine volume', 'Mileage','Cylinders','Airbags']

sns.boxplot(df[cols[3]]);

cols=['Levy','Engine volume', 'Mileage','Cylinders','Airbags']

sns.boxplot(df[cols[4]]);

def find_outliers_limit(df,col):

    print(col)

    print('-'*50)

    #removing outliers

    q25, q75 = np.percentile(df[col], 25), np.percentile(df[col], 75)

    iqr = q75 - q25

    print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))

    # calculate the outlier cutoff

    cut_off = iqr * 1.5

    lower, upper = q25 - cut_off, q75 + cut_off

    print('Lower:',lower,' Upper:',upper)

    return lower,upper

def remove_outlier(df,col,upper,lower):

    # identify outliers

    outliers = [x for x in df[col] if x (upper)]

    print('Identified outliers: %d' % len(outliers))

    # remove outliers

    outliers_removed = [x for x in df[col] if x >= lower and x <= upper]

    print('Non-outlier observations: %d' % len(outliers_removed))

    final= np.where(df[col]>upper,upper,np.where(df[col]<lower,lower,df[col]))

    return final

outlier_cols=['Levy','Engine volume','Mileage','Cylinders']

for col in outlier_cols:

    lower,upper=find_outliers_limit(df,col)

    df[col]=remove_outlier(df,col,upper,lower)

#boxplot - to see outliers

plt.figure(figsize=(20,10))

df[outlier_cols].boxplot()

df['Doors'].unique()

df['Doors']=df['Doors'].map({'04-May':'4_5','02-Mar':'2_3','>5':'5'})

df['Doors']=df['Doors'].astype(str)

#Creating Additional Features

labels=[0,1,2,3,4,5,6,7,8,9]

df['Mileage_bin']=pd.cut(df['Mileage'],len(labels),labels=labels)

df['Mileage_bin']=df['Mileage_bin'].astype(float)

labels=[0,1,2,3,4]

df['EV_bin']=pd.cut(df['Engine volume'],len(labels),labels=labels)

df['EV_bin']=df['EV_bin'].astype(float)

#Handling Categorical features

num_df=df.select_dtypes(include=np.number)

cat_df=df.select_dtypes(include=object)

encoding=OrdinalEncoder()

cat_cols=cat_df.columns.tolist()

encoding.fit(cat_df[cat_cols])

cat_oe=encoding.transform(cat_df[cat_cols])

cat_oe=pd.DataFrame(cat_oe,columns=cat_cols)

cat_df.reset_index(inplace=True,drop=True)

cat_oe.head()

num_df.reset_index(inplace=True,drop=True)

cat_oe.reset_index(inplace=True,drop=True)

final_all_df=pd.concat([num_df,cat_oe],axis=1)

#Checking correlation

final_all_df['price_log']=np.log(final_all_df['Price'])

plt.figure(figsize=(20,10))

sns.heatmap(round(final_all_df.corr(),2),annot=True);

cols_drop=['Price','price_log','Cylinders']

final_all_df.columns

X=final_all_df.drop(cols_drop,axis=1)

y=final_all_df['Price']

# Data Splitting and Scaling

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=25)

scaler=StandardScaler()

X_train_scaled=scaler.fit_transform(X_train)

X_test_scaled=scaler.transform(X_test)

# Model Building

def train_ml_model(x,y,model_type):

    if model_type=='lr':

        model=LinearRegression()

    elif model_type=='xgb':

        model=XGBRegressor()

    elif model_type=='rf':

        model=RandomForestRegressor()

    model.fit(X_train_scaled,np.log(y))

    return model

def model_evaluate(model,x,y):

    predictions=model.predict(x)

    predictions=np.exp(predictions)

    mse=mean_squared_error(y,predictions)

    mae=mean_absolute_error(y,predictions)

    mape=mean_absolute_percentage_error(y,predictions)

    msle=mean_squared_log_error(y,predictions)

    mse=round(mse,2)

    mae=round(mae,2)

    mape=round(mape,2)

    msle=round(msle,2)

    return [mse,mae,mape,msle]

model_lr=train_ml_model(X_train_scaled,y_train,'lr')

model_xgb=train_ml_model(X_train_scaled,y_train,'xgb')

model_rf=train_ml_model(X_train_scaled,y_train,'rf')

## Deep Learning

### Small Network

model_dl_small=Sequential()

model_dl_small.add(Dense(16,input_dim=X_train_scaled.shape[1],activation='relu'))

model_dl_small.add(Dense(8,activation='relu'))

model_dl_small.add(Dense(4,activation='relu'))

model_dl_small.add(Dense(1,activation='linear'))

model_dl_small.compile(loss='mean_squared_error',optimizer='adam')

model_dl_small.summary()

epochs=20

batch_size=10

model_dl_small.fit(X_train_scaled,np.log(y_train),verbose=0,validation_data=(X_test_scaled,np.log(y_test)),epochs=epochs,batch_size=batch_size)

#plot the loss and validation loss of the dataset

history_df = pd.DataFrame(model_dl_small.history.history)

plt.figure(figsize=(20,10))

plt.plot(history_df['loss'], label='loss')

plt.plot(history_df['val_loss'], label='val_loss')

plt.xticks(np.arange(1,epochs+1,2))

plt.yticks(np.arange(1,max(history_df['loss']),0.5))

plt.legend()

plt.grid()

### Large Network

model_dl_large=Sequential()

model_dl_large.add(Dense(64,input_dim=X_train_scaled.shape[1],activation='relu'))

model_dl_large.add(Dense(32,activation='relu'))

model_dl_large.add(Dense(16,activation='relu'))

model_dl_large.add(Dense(1,activation='linear'))

model_dl_large.compile(loss='mean_squared_error',optimizer='adam')

model_dl_large.summary()

epochs=20

batch_size=10

model_dl_large.fit(X_train_scaled,np.log(y_train),verbose=0,validation_data=(X_test_scaled,np.log(y_test)),epochs=epochs,batch_size=batch_size)

#plot the loss and validation loss of the dataset

history_df = pd.DataFrame(model_dl_large.history.history)

plt.figure(figsize=(20,10))

plt.plot(history_df['loss'], label='loss')

plt.plot(history_df['val_loss'], label='val_loss')

plt.xticks(np.arange(1,epochs+1,2))

plt.yticks(np.arange(1,max(history_df['loss']),0.5))

plt.legend()

plt.grid()

summary=PrettyTable(['Model','MSE','MAE','MAPE','MSLE'])

summary.add_row(['LR']+model_evaluate(model_lr,X_test_scaled,y_test))

summary.add_row(['XGB']+model_evaluate(model_xgb,X_test_scaled,y_test))

summary.add_row(['RF']+model_evaluate(model_rf,X_test_scaled,y_test))

summary.add_row(['DL_SMALL']+model_evaluate(model_dl_small,X_test_scaled,y_test))

summary.add_row(['DL_LARGE']+model_evaluate(model_dl_large,X_test_scaled,y_test))

print(summary)

y_pred=np.exp(model_rf.predict(X_test_scaled))

number_of_observations=20

x_ax = range(len(y_test[:number_of_observations]))

plt.figure(figsize=(20,10))

plt.plot(x_ax, y_test[:number_of_observations], label="True")

plt.plot(x_ax, y_pred[:number_of_observations], label="Predicted")

plt.title("Car Price - True vs Predicted data")

plt.xlabel('Observation Number')

plt.ylabel('Price')

plt.xticks(np.arange(number_of_observations))

plt.legend()

plt.grid()

plt.show()