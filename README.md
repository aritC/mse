# MSE (Mean Squared Error)

MSE measures the average amount that the model's prediction varies from the correct value. It is a measure of model's performance over a training set.
The cost in Higher when the model is performing poorly on the training set.

## How to run

Reads CSV file named : trainingset containing
x's : input features for the model
y_true : the actual value
y_pred : the model's prediction
and will then calculate the MSE

```
python ./mse/py
```

## Explanation

For Each Training Example:
We calculate the square of the difference between
the predicted value and the actual value
and sum them to the sum of Squared Errors and
Then ultimately divde the same with ( 2 \* m )
where m : No. of training Examples


We divide by m to get the average and by 2 to simply
calculations going forward when we have to find the
derivative of the same to minimize the cost
