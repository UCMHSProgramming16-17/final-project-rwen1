# This program's purpose is to plot a visual representation of the Pokedex
import pandas as pd
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool
import math
import random

# Read the CSV files containing necessary data
stats = pd.read_csv("Pokemon.csv")
imgs = pd.read_csv("pokeSprites.csv")

# Plot output location
output_file("pokedex.html")

# Create custom lists for data to be displayed
sprite = []
for x in range(len(stats['#'])):
    sprite.append(imgs['URL'][stats['#'][x] - 1])
legendary = []
for x in stats['Legendary']:
    if x:
        legendary.append("Legendary")
    else:
        legendary.append(" ")

# Create a list for each color to be used in the plot
colorMap = {'Normal': '#ba9c66', 'Fire': '#ff9854', 'Water': '#63beff', 'Electric': '#ffef63', 'Grass': '#5cd66a', 'Ice': '#82e5de', 'Fighting': '#7c281f', 'Poison': '#511568', 'Ground': '#bc9a2b', 'Flying': '#c089c1', 'Psychic': '#ff0094', 'Bug': '#8bcc22', 'Rock': '#77471a', 'Ghost': '#3a2542', 'Dragon': '#2a4df6', 'Dark': '#211712', 'Steel': '#aeb8bf', 'Fairy': '#e55ee0'}
colors = [colorMap[x] for x in stats['Type 1']]

# Define the data to be used in the plot
source = ColumnDataSource(
        data=dict(
            num = stats['#'],
            total = stats['Total'],
            desc = stats['Name'],
            image = sprite,
            type1 = stats['Type 1'],
            type2 = stats['Type 2'],
            gen = stats['Generation'],
            legend = legendary,
        )
    )

# Define the data to be shown when hovering the cursor
hover = HoverTool(
        tooltips="""
        <div>
            <div>
                <img
                    src="@image" height="42" alt="@image" width="42"
                    style="float: left; margin: 0px 5px 5px 0px;"
                    border="0"
                ></img>
            </div>
            <div>
                <span style="font-size: 17px; font-weight: bold;">@desc</span>
                <span style="font-size: 15px; color: #996666;">[@num]</span>
            </div>
            <div>
                <span style="font-size: 14px;">@type1 @type2</span>
            </div>
            <div>
                <span style="font-size: 12px; color: #446644;">Gen</span>
                <span style="font-size: 12px; color: #446644;">@gen</span>
            </div>
            <div>
                <span style="font-size: 14px; color: #a89430;">@legend</span>
            </div>
        </div>
        """
    )

# Create a graph to plot on
pokePlot = figure(plot_width = 800, plot_height = 800, tools = [hover], title = "Pokédex")
pokePlot.xaxis.axis_label = "Pokédex Number"
pokePlot.yaxis.axis_label = "Power"

# Plot circles according to the Pokedex number and total stat value of each Pokemon
pokePlot.circle('num', 'total', size = 8, source = source, color = colors)

# Complete the plot
show(pokePlot)
