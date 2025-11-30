import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import seaborn as sns

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

def bar_real_vs_simulated(df , values):
    '''
    Comparison between real and simulated disease proportions graph
    '''
    labels = ['Verklig', 'Simulerad']
    fig, ax = plt.subplots(figsize=(8,5))
    ax.bar(labels, values, color=['#4C72B0', '#76B7B2'], edgecolor='black', linewidth=1)
    ax.set_title("Jämförelse mellan verklig och simulerad sjukdomsandel")
    #ax.set_xlabel("Procent (%)")
    ax.set_ylabel("Andel personer med sjukdom (%)")
    ax.set_ylim(0, max(values) + 1)
    ax.grid(axis='y', linestyle='--', alpha=0.4)
    for i, v in enumerate(values):
        ax.text(i, v+0.3, f"{v:.2f}%", ha='center', fontsize=11)
    return ax

def extended_visualization(df):
    fig, axs = plt.subplots(1, 2, figsize=(14,5))

    # Scatter plot: blodtryck vs ålder
    sns.scatterplot(x='age', y='systolic_bp', hue='disease', data=df, 
                    palette='Set1', alpha=0.7, ax=axs[0])
    sns.regplot(x='age', y='systolic_bp', data=df, scatter=False, color='black', ax=axs[0])
    axs[0].set_xlabel("Ålder")
    axs[0].set_ylabel("Systoliskt blodtryck")
    axs[0].set_title("Relation mellan ålder och systoliskt blodtryck")

    # Bar plot: sjukdomsförekomst per kön
    disease_by_sex = df.groupby('sex', observed=False)['disease'].apply(lambda x: x.astype(int).mean() * 100)

    axs[1].bar(disease_by_sex.index, disease_by_sex.values, color=['#4C72B0','#76B7B2'], edgecolor='black')
    axs[1].set_ylabel("Andel med sjukdom (%)")
    axs[1].set_ylim(0, 100)
    axs[1].set_title("Sjukdomsförekomst per kön")
    for i, v in enumerate(disease_by_sex.values):
        axs[1].text(i, v + 1, f"{v:.1f}%", ha='center')

    plt.tight_layout()
    return fig, axs
