import numpy as np
import re
from collections import namedtuple

with open('../Inputs/15.txt') as file:
    ingr_attr_list = file.readlines()

ingr_dict = {}
for ingr_attr in ingr_attr_list:
    ingr,attr_list = ingr_attr.split(':')
    Ingr = namedtuple('Ingr',['capacity', 'durability', 'flavor' , 'texture' , 'calories' ])
    ingr_val = list(map(int,re.findall('[\-0-9]+', attr_list)))
    ingr_dict[ingr] = Ingr(*ingr_val) #unpack ingr values to insert into named tuple

attr_dict = {}
for attr in Ingr._fields:
    attr_dict[attr] = [getattr(ingr_dict[key],attr) for key in ingr_dict]

top_cookie_score = 0
for sprink in range(0,101):
    for butter in range(0, 101 - sprink):
        for choc in range(0,101 - sprink - butter):
            for candy in range(0, 101 - sprink - butter - choc):
                cookie_val = []
                for attr in attr_dict:
                    add_val = np.sum([ingr*val for ingr,val in zip([sprink,butter,choc,candy],attr_dict[attr])])

                    if add_val <= 0:
                        break #no need to continue calculation of score, it will be zero
                    else:
                        cookie_val.append(add_val)
                top_cookie_score = max(top_cookie_score,np.prod(cookie_val[0:5])) #exclude calories in prod
print(f'Part 1: {top_cookie_score}')



