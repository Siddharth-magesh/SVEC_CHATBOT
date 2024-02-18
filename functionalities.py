# functions.py
from random import randint
import json
import requests
import pickle
from production_learning_model import *
           
def temperature_prediction(loc):
    with open('location.json', 'r') as file:
        data = json.load(file)
        for item in data:
            if item['location'].lower() == loc.lower():
                lati = item['latnlon']['lat']
                long = item['latnlon']['lon']
                response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lati}&lon={long}&appid=3a828979b8653572ed653e4535eb8747")
                x = response.json()
                temp = x['main']['temp']
                humidity = x['main']['humidity']
                return (str(temp-273))

    
def budget_prediction(cost_cap,coefficients):
    def finding_min_cost_list(solved):
        every_price_list = [item[1] for item in solved]
        min_cost = min(every_price_list)
        for item in solved:
            if item[1] == min_cost:
                return item
    
    
    def f_x(coefficients, x_values):
        return sum(coeff * x for coeff, x in zip(coefficients, x_values))
    
    
    def getting_values(cost_cap, coefficients):
        matrix_prices = [[randint(1, 100) for _ in range(30)] for _ in range(5)]
        solved = []
        for i in range(len(matrix_prices[0])):
            x_values = [matrix_prices[j][i] for j in range(len(matrix_prices))]
            price = f_x(coefficients, x_values)
            if price <= cost_cap:
                solved.append([x_values, price])
        if not solved:
            return -1
        else:
            result = finding_min_cost_list(solved)
            selected_x_values = result[0]
            #return(selected_x_values,result[1]) check this again
            return(result[1])
        
    final_result=getting_values(cost_cap,coefficients)
    return final_result
