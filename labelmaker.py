#LCST Plotter
#Author: ESTC

import numpy
import streamlit
import matplotlib.pyplot as plt
import pandas

def launch_app():
    streamlit.title("Phase Diagram Plotter")
    global cation, anion, mw_cat, mw_an, datafile 
    cation = streamlit.text_input("Enter the abbreviation of the cation:")
    # mw_cat = streamlit.text_input("Enter the molecular weight of the cation:")
    anion = streamlit.text_input("Enter the abbreviationo of the anion:")
    # mw_an = streamlit.text_input("Enter the molecular weight of the anion:")
    T_start = streamlit.text_input("Enter start temperature in °C")
    streamlit.text_input("Enter your initials:")
    datafile = streamlit.file_uploader("Upload the LCST file:",type="xlsx")


def load_data(datafile):
    global T,x1a,x1b,x1
    data = pandas.read_excel(datafile)
    T = data['T']-273.15
    x1a = data["x'1"]
    x1b = data['x"1']
    # x1 = 
    streamlit.dataframe(data)

def make_plot(x1a,x1b,T,cation,anion):
    fig,ax = plt.subplots()
    ax.set_title("Predicted Phase Diagram of Aqueous ["+cation+"]["+anion+"]")
    ax.scatter(x1a,T,marker=".",c="blue")
    ax.scatter(x1b,T,marker=".",c="blue")
    ax.set_xlabel("Water Mole Fraction")
    ax.set_xlim([0,1.05])
    ax.set_ylabel("Temperature (°C)")
    ax.set_ylim([50,250])
    plt.savefig(cation+"_"+anion+".png")
    streamlit.pyplot(fig)

launch_app()
if datafile is not None:
    load_data(datafile)
    make_plot(x1a,x1b,T,cation,anion)
    
