import pandas as pd
import numpy as np

'''
    Reads CSV file named : trainingset containing
        x's : input features for the model
        y_true : the actual value
        y_pred : the model's prediction

    and will then calculate the MSE
    
'''
df = pd.read_csv('./trainingset.csv')

print("Training Set : \n", df)

sum = 0
'''
    For Each Training Example:
        We calculate the square of the difference between 
            the predicted value and the actual value
    and sum them to the sum of Squared Errors and 
    Then ultimately divde the same with ( 2 * m )
    where m : No. of training Examples

    We divide by m to get the average and by 2 to simply 
    calculations going forward when we have to find the 
    derivative of the same to minimize the cost
    
'''
for index, row in df.iterrows():
    sum += np.square(row['y_pred'] - row['y_true'])

print("MSE : ", sum / (2 * df.shape[0]))
