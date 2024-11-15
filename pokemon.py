import polars as pl
import streamlit as st

class Pokemon:
    def __init__(self, name, type1, type2):
        self.name = name
        self.type1 = type1
        self.type2 = type2

    def __str__(self):
        return f"{self.name}"



def scrape_data(df):
    '''
    inputs: data frame
    ouputs: x() y() z()
    purpose: find the x, y, z values
    '''
    x = 0
    y = 1
    z = 2
    return (x, y, z)

def find_weaknesses(team):
    '''
    inputs: team
    outputs: weaknesses
    purpose: find the weaknesses of the team
    '''
    type_to_num = {"Normal": 0, "Fire": 1, "Water": 2, "Electric": 3, "Grass": 4, "Ice": 5, "Fighting": 6, "Poison": 7, "Ground": 8, "Flying": 9, "Psychic": 10, "Bug": 11, "Rock": 12, "Ghost": 13, "Dragon": 14, "Dark": 15, "Steel": 16, "Fairy": 17}
    matrix = [[0 for i in range(18)] for j in range(18)]
    weaknesses = []
    for pokemon in team:

        weaknesses.append(pokemon)
    return weaknesses

def build_site():
    '''
    inputs: None
    outputs: None
    purpose: build the site
    '''
    st.title("Pokemon")
    st.write("This is a demo of a Pokemon site")
    #create a button to add to team
        #search by name or dex number

    #create dashboard of the team

    #create a warnings sections: type weaknesses, stat weaknesses, etc.
    return

def main():
    '''
    inputs: None
    outputs: None
    purpose: demonstrate the main logic
    '''
    df = pl.read_csv("pokemon.csv")
    x, y, z = scrape_data(df)
    build_site()

if __name__ == "__main__":
    main()