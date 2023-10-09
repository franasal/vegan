
import streamlit as st
import json
from io import StringIO
from contextlib import contextmanager, redirect_stdout
from playsound import playsound
import sys
import time


@contextmanager
def st_capture(output_func):
    with StringIO() as stdout, redirect_stdout(stdout):
        old_write = stdout.write

        def new_write(string):
            ret = old_write(string)
            output_func(stdout.getvalue())
            return ret

        stdout.write = new_write
        yield

def progressbar_alarm(it, alarm1, alarm2 , prefix="", size=60, out=sys.stdout): # Python3.6+
    count = len(it)
    start = time.time()
    def show(j):
        x = int(size*j/count)
        remaining = ((time.time() - start) / j) * (count - j)

        mins, sec = divmod(remaining, 60)
        time_str = f"{int(mins):02}:{sec:05.2f}"

        print(f"{prefix}[{u'█'*x}{('.'*(size-x))}] {j}/{count} Est wait {time_str}", end='\r', file=out, flush=True)

    for i, item in enumerate(it):
        yield item
        show(i+1)
        if i ==alarm1:
            playsound('shovel-gong.mp3')
        elif i ==alarm2-1:
            playsound('gong1-94016.mp3')
    print("\n", flush=True, file=out)

def printProgressBar(value,label):
    n_bar = 40 #size of progress bar
    max = 100
    j= value/max
    st.write('\r')
    bar = '█' * int(n_bar * j)
    bar = bar + '-' * int(n_bar * (1-j))

    st.write(f"{label.ljust(10)} | [{bar:{n_bar}s}] {int(100 * j)}% ")


def calculate_cost_per_animals_in_sanctuary(sanctuary_name, data):
    # Find the sanctuary in the data
    sanctuary = None
    for s in data['sanctuaries']:
        if s['name'] == sanctuary_name:
            sanctuary = s
            break

    if sanctuary is None:
        return "Sanctuary not found."

    # Initialize a dictionary to store information for all animals
    all_animals_info = {}

    # Iterate through all animals in the sanctuary
    for animal in sanctuary['animals']:
        # Find the cost information for the animal's species
        animal_species = animal['species'].lower()
        animal_cost = None
        for cost_info in data['animal_cost']:
            if cost_info['species'] == animal_species:
                animal_cost = cost_info
                break

        if animal_cost is None:
            return "Animal species cost information not found."

        # Calculate total cost based on life expectancy
        life_expectancy = animal_cost['life_expectancy_months']
        monthly_cost = animal_cost['monthly_cost']
        total_cost = monthly_cost * (life_expectancy / 12)

        # Calculate current budget as a percentage of the total cost
        current_budget = animal['current_budget']
        budget_percentage = (current_budget / total_cost) * 100

        # Store information for this animal in the dictionary
        animal_info = {
            "Animal Name": animal['name'],
            "Animal Age": animal['age'],
            "Species": animal['species'],
            "Total Cost to Maintain": total_cost,
            "Current Budget": current_budget,
            "Current Budget Percentage": budget_percentage
        }

        # Add the animal's information to the dictionary
        all_animals_info[animal['name']] = animal_info

    return all_animals_info
