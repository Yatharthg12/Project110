import csv
import pandas as pd 
import plotly.express as px
import plotly.figure_factory as ff 
import statistics
import plotly.graph_objects as go 
import random

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

population_mean = statistics.mean(data)
print(population_mean)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        randomindex = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean
        mean_list.append(set_of_means)
    show_fig(mean_list)

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["temp"], show_hist = False)
    fig.show()