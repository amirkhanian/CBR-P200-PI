"""
    TYPE_1__CBR_PI_P200.py

    A Type 1 nomograph of the relationship between CBR, fines percentage,
    and plasticity index. The equation is from:
        
       Geotechnical Aspects of Pavements
       FHWA NHI-05-037
       May 2006
       
    The mathematical work to generate the nomograph was performed by
    
    Armen Amirkhanian
    
    and is representing the function found on Page 5-53 of the reference:
    
                     75
    CBR = --------------------------
           1 + 0.00728 * P200 * PI
    
    The resulting code/software is a modification of an example file
    in the pynomo package. This modified code is released under the terms
    of the GNU General Public License, either version 3 or a later version
    at the user's discretion. The original copyright and license notice for
    the example file is below.

    Copyright (C) 2007-2009  Leif Roschier

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    This process would have been impossible without the incredible pynomo
    package from Leif Roschier!
"""
import sys
import numpy as np

sys.path.insert(0, "..")
# sys.path[:0] = [".."]
from pynomo.nomographer import Nomographer

CBR = {
    'u_min': 1.0,
    'u_max': 74.0,
    'function': lambda u: -np.log10((75/u)-1),
    'title': r'CBR',
    'tick_levels': 3,
    'tick_text_levels': 1,
}

PI = {
    'u_min': 1.0,
    'u_max': 50.0,
    'function': lambda u: np.log10(u),
    'title': r'Plasticity Index (PI)',
    'tick_levels': 3,
    'tick_text_levels': 1,
}

P200 = {
    'u_min': 1.0,
    'u_max': 100.0,
    'function': lambda u: np.log10(0.00728*u),
    'title': r'Passing \#200',
    'tick_levels': 3,
    'tick_text_levels': 1,
}

block_1_params = {
    'block_type': 'type_1',
    'width': 10.0,
    'height': 10.0,
    'f1_params': P200,
    'f2_params': CBR,
    'f3_params': PI,
    'isopleth_values': [[40, 'x', 20]],
}

main_params = {
    'filename': 'CBR_PI_P200.pdf',
    'paper_height': 10.0,
    'paper_width': 10.0,
    'block_params': [block_1_params],
    'transformations': [('rotate', 0.01), ('scale paper',)],
    'title_x': 5.0,
    'title_y': 0.25,
    'title_str': r'$CBR={75 \over 1+0.00728P_{200}PI}$',
    'debug': False,
}
Nomographer(main_params)
