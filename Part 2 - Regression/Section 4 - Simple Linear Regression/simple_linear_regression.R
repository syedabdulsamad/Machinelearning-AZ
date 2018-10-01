# Data processing
dataset = read.csv('Salary_Data.csv')

# dataset = dataset[, 2:3]

#install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# feature scaling
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])


# Simple linear regression
regressor = lm(formula = Salary ~ YearsExperience, data = training_set)
y_pred = predict(regressor, newdata = test_set)
#install.packages('ggplot2')
library(ggplot2)
ggplot() + geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary), 
                      colour = 'red') + 
  geom_point(aes(x = test_set$YearsExperience, y = training_set$Salary), 
             colour = 'green') + 
  geom_point(aes(x = test_set$YearsExperience, y = y_pred), 
             colour = 'yellow') + 
  
  
  
  geom_line(aes(x = training_set$YearsExperience, y =  predict(regressor, newdata = training_set)), 
            colour = 'blue') + 
  ggtitle('Salary vs Experience in years') + 
  xlab('Expenience') + 
  ylab('Salary')