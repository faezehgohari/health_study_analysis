import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

def hist_distribution_systolic_blood_pressure(df):
    '''
    Distribution of systolic blood pressure graph
    '''
    fig, ax = plt.subplots(figsize=(8,5))
    ax.hist(df["systolic_bp"], bins=20, edgecolor='black')
    ax.set_title("Fördelning av systoliskt blodtryck")
    ax.set_xlabel("Systoliskt blodtryck (mmHg)")
    ax.set_ylabel("Antal personer")
    return ax

def boxplot_distribution_weight_by_gender(df):
    '''
    Distribution of weight by gender graph
    '''
    fig, ax = plt.subplots(figsize=(8,5))
    ax.boxplot([df[df['sex']=='M']['weight'],
             df[df['sex']=='F']['weight']],
            tick_labels=['Män', 'Kvinnor'])
    ax.set_title("Viktfördelning per kön")
    ax.set_xlabel("Kön")
    ax.set_ylabel("Vikt (kg)")
    ax.grid(axis='y', linestyle='--' , alpha=0.4)
    return ax

def bar_percentage_smokers(df):
    '''
    Percentage of smokers graph
    '''
    fig, ax = plt.subplots(figsize=(8,5))
    smoker_counts = df['smoker'].value_counts(normalize=True) * 100
    ax.bar(smoker_counts.index, smoker_counts.values, edgecolor='black')
    ax.set_title("Andel rökare (%)")
    ax.set_xlabel("Procent (%)")
    ax.set_ylabel("Rökstatus")
    ax.grid(axis='y', linestyle='--' , alpha=0.4)
    return ax