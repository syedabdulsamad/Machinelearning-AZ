# Data processing
dataset = read.csv('Data.csv')
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary)

# Labeling data

dataset$Country = factor(dataset$Country, 
                         c('France', 'Spain', 'Germany'),
                         c(1,2,3))
dataset$Purchased = factor(dataset$Purchased, 
                           c('No', 'Yes'),
                           c(0,1))
