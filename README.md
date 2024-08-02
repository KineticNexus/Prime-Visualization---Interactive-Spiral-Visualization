# Interactive Spiral Visualization

This Python script creates an interactive visualization of a spiral with prime number highlighting. It uses matplotlib to generate the spiral and provide an interactive interface for adjusting various parameters of the spiral in real-time.

## Features

- Generates a spiral based on the equation r = a + b * θ
- Highlights prime numbers on the spiral
- Interactive sliders to adjust spiral parameters:
  - a: Starting radius
  - b: Growth rate
  - c: Number of turns
  - Number of points
  - Distance between highlighted numbers
- Text input boxes for precise parameter adjustment

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- SymPy

## Usage

1. Run the script:
   ```
   python spiral_visualization.py
   ```
2. Use the sliders to adjust the spiral parameters:
   - Move the sliders left or right to change values
   - Enter specific values in the text boxes next to each slider
3. Observe how the changes affect the spiral shape and prime number distribution

## How it works

1. The spiral is generated using polar coordinates (r, θ) converted to Cartesian coordinates (x, y).
2. Points on the spiral are plotted at regular intervals.
3. Prime numbers are highlighted in red.
4. The matplotlib animation features allow for real-time updates as parameters are changed.

## Customization

You can modify the range of the sliders or add new parameters by adjusting the slider and text box definitions in the code.

## Contributing

Feel free to fork this project, submit issues, or send pull requests to improve the visualization or add new features.

## License

[MIT License](https://opensource.org/licenses/MIT)
