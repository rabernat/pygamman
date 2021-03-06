# This is a wrapper function for gamma_n and neutral density
# This shows how the fortran wrappers are called

import numpy as np
# load fortran library
from pygamman import gamman as gn

def gamma_n(salt,temp,pres,n,lon,lat):
	gamma_arr,dgl,dgh = gn.gamma_n(salt,temp,pres,n,lon,lat)
	return gamma_arr,dgl,dgh

def neutral_surfaces(salt,temp,pres,gamma_n,n,glevels,nlevels):
	sns,tns,pns,dsns,dtns,dpns = gn.neutral_surfaces(salt,temp,pres,gamma_n,n,glevels,nlevels)
	return sns,tns,pns,dsns,dtns,dpns



