import numpy as np
import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patheffects as PathEffects
import matplotlib.colors as colors
import matplotlib.cm as cmx
import math, sys, os
from datetime import *
#from datetime import datetime
from scipy.stats import spearmanr
from sklearn.metrics import mean_absolute_error
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

#2.1. reset defaults

mpl.rcParams.update(mpl.rcParamsDefault)
var_rcparams=mpl.rcParams

#2.2. font
mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['font.sans-serif']='Times New Roman'
mpl.rcParams['font.weight']= 'normal'  # 'bold'
mpl.rcParams['font.size']=12

#2.3. figure
mpl.rcParams['figure.titlesize']=14  # for suptitle
mpl.rcParams['figure.titleweight']='normal' # for suptitle

#2.4. lines
mpl.rcParams['lines.linewidth'] = 1
mpl.rcParams['lines.linestyle'] = '-'
mpl.rcParams['lines.color'] = 'k'
mpl.rcParams['lines.marker']='None'
mpl.rcParams['lines.markerfacecolor']='gray'
mpl.rcParams['lines.markeredgecolor']='black'
mpl.rcParams['lines.markeredgewidth']=0.25
mpl.rcParams['lines.markersize']=4

#2.5. scatter
mpl.rcParams['scatter.marker']='o'
mpl.rcParams['scatter.edgecolors']='None'

#2.6. axes and grid
#2.6.1. title
mpl.rcParams['axes.titlesize']=12
mpl.rcParams['axes.titlelocation']='left'
mpl.rcParams['axes.titleweight']='bold'

#2.6.2. grid
mpl.rcParams['axes.grid']='True'
mpl.rcParams['axes.grid.which']='major'
mpl.rcParams['axes.grid.axis']='both'
mpl.rcParams['grid.color']='black'
mpl.rcParams['grid.linestyle']=':'
mpl.rcParams['grid.linewidth']=.5
mpl.rcParams['grid.alpha']=0.5

#2.6.3. labels
mpl.rcParams['axes.labelsize']=12
mpl.rcParams['axes.labelpad']=4
mpl.rcParams['axes.labelweight']='normal'
mpl.rcParams['axes.labelcolor']='black'

#2.7. ticks
mpl.rcParams['xtick.minor.visible']=True
mpl.rcParams['ytick.minor.visible']=True

#2.8. legend
mpl.rcParams['legend.fancybox']=True
mpl.rcParams['legend.edgecolor']='black'
mpl.rcParams['legend.facecolor']='white'
mpl.rcParams['legend.fontsize']=12
mpl.rcParams['legend.title_fontsize']=12
mpl.rcParams['legend.framealpha']=.5
mpl.rcParams['legend.frameon']=True
mpl.rcParams['legend.loc']='upper left'

# 2.9. diagonal (1:1)
diag_slope=1
diag_intrcpt=0

diag_x = np.linspace(0,1000)
diag_y = diag_slope*diag_x+diag_intrcpt

diag_ls="--"
diag_lw=1
diag_clr='black'

# qualitative color palette in NF alphabetical order
clrs_lst=['#e41a1c','#377eb8','#4daf4a','#984ea3','#ff7f00','#ffff33']
clr_nf1=clrs_lst[0]
clr_nf2=clrs_lst[1]
clr_nf3=clrs_lst[2]
clr_nf4=clrs_lst[3]
clr_nf5=clrs_lst[4]
clr_nf6=clrs_lst[5]

# edge color for all
clr_edg_nf='black'

# edge linewidth for all
edg_lw_nf=0.5

# marker symbols in NF alphabetical order
mkrs_list=['o','X','s','P','D','*']
mkr_nf1=mkrs_list[0]
mkr_nf2=mkrs_list[1]
mkr_nf3=mkrs_list[2]
mkr_nf4=mkrs_list[3]
mkr_nf5=mkrs_list[4]
mkr_nf6=mkrs_list[5]

# marker size for all
mkr_sze=25

# alpha for all
clr_alpha=1

#3. Page Size
full_page_width=6.69291  # 170mm
half_page_width=3.34646 # 85 mm

