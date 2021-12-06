import pandas as pd
import matplotlib.pyplot as plt
import statistics
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


class Final():
    
    def __init__(self):
    
        data = pd.read_csv("whr happiness.csv")
        self.df = pd.DataFrame(data)
    
    #Lance
    def graphical_sum(self):
        #print(self.df)
        plt.scatter(self.df["Rank by 2020 score"], self.df["Rank by 2017-19 score"])
        plt.xlabel("Rank by 2020 Score")
        plt.ylabel("Rank by 2017-19 Score")
        plt.show()
        plt.close()
        #Scatter plot showing how the happiest countries have imporved or gotten less happy.
        
    #Ethan
    def numerical_sum(self):
        print("Mean: " , self.df['Score_2017-19'].mean())
        print("\nMedian : " , self.df['Score_2017-19'].median())
        print("\nSTD: " , self.df['Score_2017-19'].std())
        print("\nQuartiles: \n" , self.df['Score_2017-19'].quantile([0.25, 0.75], interpolation='nearest') , "\n")
        
    #Lance
    def numstdev(self,data,number):
        set_size = len(data)
        mean  = statistics.mean(data)
        stdev = statistics.stdev(data)
        stdevbelow = mean - stdev*(number)
        stdevabove = mean + stdev*(number)
        new_set = []
        #print(set_size)
        #print(stdev)
        for num in data:
            #print(num)
            if stdevbelow <= num and stdevabove >= num:
                new_set.append(num)
        return len(new_set)/set_size
    
    def normal_dis(self):
        print("="*20)
        print("Normal Distrobution")
        print("Scores 2020")
        print("Percent within one standard deviation of mean :: ", self.numstdev(self.df["Score, 2020"],1))
        print("Percent within two standard deviation of mean :: ", self.numstdev(self.df["Score, 2020"],2))
        print("Percent within three standard deviation of mean :: ", self.numstdev(self.df["Score, 2020"],3))
        print("Scores 2017-2019")
        print("Percent within one standard deviation of mean :: ", self.numstdev(self.df["Score_2017-19"],1))
        print("Percent within two standard deviation of mean :: ", self.numstdev(self.df["Score_2017-19"],2))
        print("Percent within three standard deviation of mean :: ", self.numstdev(self.df["Score_2017-19"],3))
    #Ethan
    def hypothesis_tests(self):
        print(sc.ttest_1samp(self.df['Score_2017-19'], 5, alternative="greater"))
        
    #Lance
    def linear_regression(self):
        print("="*20)
        print("Linear Regression")
        x = self.df[["Score, 2020","Rank by 2017-19 score"]]
        #z = self.df["Rank by 2017-19 score"]
        #print(x,z)

    
        y = self.df["Score_2017-19"]
        x_train,x_test,y_train,y_test = train_test_split(x,y,train_size = 0.3,random_state=100)
        
        mlr = LinearRegression()
        mlr.fit(x_train,y_train)
        
        y_pred_mlr = mlr.predict(x_test)
        mlr_dif = pd.DataFrame({"2017-19 scores":y_test,"2020 scores":y_pred_mlr})
        print(mlr_dif)
        meanAbsError = metrics.mean_absolute_error(y_test,y_pred_mlr)
        meanSqError = metrics.mean_squared_error(y_test,y_pred_mlr)
        rootMeanSqError = np.sqrt(metrics.mean_squared_error(y_test, y_pred_mlr))
        
        print("R Squared {:.2f}".format(mlr.score(x,y)*100))
        print("Mean Absolute Error:: ",meanAbsError)
        print("Mean Square Error:: ",meanSqError)
        print("Root Mean Square error::",rootMeanSqError)
        
    def main(self):
        self.numerical_sum()
        self.hypothesis_tests()
   
if __name__ == '__main__':
    final = Final()
    final.main()
   
    
