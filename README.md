# CBR-P200-PI
A nomograph code to calculate the CBR of a soil knowing the percent fines and plasticity index, or any two of the three parameters. This code can easily be modified to show different scales and plot different isopleths.

To change the scales, change the "u_min" and "u_max" values of each parameter to suit your needs.

The isopleth can be elimated entirely by deleting "isopleth_values" or can be changed to any valid set of values. The order of the isopleth example array is the order of the functions indicated just above that portion of the code.

The order of the three lines can also be changed by changing "f1_params", "f2_params", and "f3_params" to the order you want, left to right.

# Requirements

In addition to Python, this requires the [PyNomo library](https://github.com/lefakkomies/pynomo).
