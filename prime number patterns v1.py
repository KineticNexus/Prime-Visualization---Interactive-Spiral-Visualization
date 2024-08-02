# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 00:40:23 2024

@author: halif
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, TextBox
from sympy import isprime

def generate_spiral(a, b, c, num_points):
    theta = np.linspace(0, c * np.pi, num_points)
    r = a + b * theta
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    x -= x[0]
    y -= y[0]
    return x, y

def update(val):
    a = slider_a.val
    b = slider_b.val
    c = slider_c.val
    num_points = int(slider_points.val)
    distance_between_numbers = int(slider_distance.val)
    
    x, y = generate_spiral(a, b, c, num_points)
    
    ax.clear()
    ax.plot(x, y, label='Spiral')
    
    for i in range(num_points):
        if i % distance_between_numbers == 0:
            ax.plot(x[i], y[i], 'ko', markersize=3)
            if isprime(i + 1):
                ax.plot(x[i], y[i], 'ro')
                ax.vlines(x[i], 0, y[i], colors='red', linestyles='dashed')
    
    ax.set_aspect('equal')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.legend()
    plt.draw()

def update_from_text(text, parameter):
    try:
        value = float(text)
        if parameter == 'a':
            slider_a.set_val(value)
        elif parameter == 'b':
            slider_b.set_val(value)
        elif parameter == 'c':
            slider_c.set_val(value)
        elif parameter == 'points':
            slider_points.set_val(value)
        elif parameter == 'distance':
            slider_distance.set_val(value)
    except ValueError:
        pass

initial_a, initial_b, initial_c = 0.5, 0.1, 10
initial_num_points, initial_distance_between_numbers = 1000, 10

fig, ax = plt.subplots(figsize=(10, 10))
plt.subplots_adjust(left=0.1, bottom=0.4)

x, y = generate_spiral(initial_a, initial_b, initial_c, initial_num_points)
ax.plot(x, y, label='Spiral')
ax.set_aspect('equal')
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.legend()

slider_ax = [plt.axes([0.1, 0.3 - i*0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow') for i in range(5)]
text_ax = [plt.axes([0.85, 0.3 - i*0.05, 0.1, 0.03]) for i in range(5)]

slider_a = Slider(slider_ax[0], 'a', 0.1, 20, valinit=initial_a)
slider_b = Slider(slider_ax[1], 'b', 0.001, 1, valinit=initial_b)
slider_c = Slider(slider_ax[2], 'c', 0.001, 200, valinit=initial_c)
slider_points = Slider(slider_ax[3], 'Points', 100, 5000, valinit=initial_num_points, valstep=5)
slider_distance = Slider(slider_ax[4], 'Dist. Between Numbers', 1, 100, valinit=initial_distance_between_numbers)

text_a = TextBox(text_ax[0], '')
text_b = TextBox(text_ax[1], '')
text_c = TextBox(text_ax[2], '')
text_points = TextBox(text_ax[3], '')
text_distance = TextBox(text_ax[4], '')

for slider, func in zip([slider_a, slider_b, slider_c, slider_points, slider_distance], [update]*5):
    slider.on_changed(func)

text_a.on_submit(lambda text: update_from_text(text, 'a'))
text_b.on_submit(lambda text: update_from_text(text, 'b'))
text_c.on_submit(lambda text: update_from_text(text, 'c'))
text_points.on_submit(lambda text: update_from_text(text, 'points'))
text_distance.on_submit(lambda text: update_from_text(text, 'distance'))

plt.show()