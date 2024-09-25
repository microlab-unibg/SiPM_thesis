import matplotlib
import matplotlib.pyplot as plt

# FONT
# font_selector = 0: CMU Serif (Times New Roman, IEEE)
# font_selector = 1: CMU Sans Serif (slide)
# font_selector = 2: Palatino (MDPI)
font_selector = 0

# TEX INTERPRETER
# Interpreter set to LaTex
if font_selector == 1:
    plt.rcParams.update({"text.usetex": True, "font.family": "sans-serif"})
    plt.rc("text.latex", preamble=r"\usepackage{siunitx}\usepackage[cm]{sfmath}\sisetup{detect-all}")
elif font_selector == 0:
    plt.rcParams.update({"text.usetex": True, "font.family": "serif"})
    plt.rc("text.latex", preamble=r"\usepackage{siunitx}\usepackage{times}\usepackage{mathptmx}")
else:
    plt.rcParams.update({"text.usetex": True, "font.family": "serif"})
    plt.rc("text.latex", preamble=r"\usepackage{siunitx}\RequirePackage{mathpazo}")
    
fontsize = 12

# FIGURE
# Font size
matplotlib.rcParams["font.size"] = fontsize
# Maximum number of open figures
matplotlib.rcParams["figure.max_open_warning"] = 100
# Figure size
# Multipliers
mult_x = 0.8
mult_y = 0.8
cm = 1/2.54  # centimeters in inches
matplotlib.rcParams["figure.figsize"] = 6.4 * mult_x, 4.8 * mult_y
print(6.4 * mult_x / cm)
print(4.8 * mult_y / cm)
# Figure resolution
matplotlib.rcParams["figure.dpi"] = 100


# BOXPLOT
# Boxplot line width
matplotlib.rcParams["axes.linewidth"] = 0.7

# TICKS
# Tick width
matplotlib.rcParams["xtick.major.width"] = 0.7
matplotlib.rcParams["ytick.major.width"] = 0.7
# Tick direction
matplotlib.rcParams["xtick.direction"] = "in"
matplotlib.rcParams["ytick.direction"] = "in"
# Tick label size
matplotlib.rcParams["xtick.labelsize"] = fontsize
matplotlib.rcParams["ytick.labelsize"] = fontsize
# Minor ticks
matplotlib.rcParams["xtick.minor.visible"] = True
matplotlib.rcParams["ytick.minor.visible"] = True
matplotlib.rcParams["xtick.top"] = True
matplotlib.rcParams["xtick.minor.top"] = True
matplotlib.rcParams["ytick.right"] = True
matplotlib.rcParams["ytick.minor.right"] = True

# LEGEND
# Legend font size
matplotlib.rcParams["legend.fontsize"] = fontsize
matplotlib.rcParams["legend.framealpha"] = 0

# AXIS
# Label size
matplotlib.rcParams["axes.labelsize"] = fontsize

# GRID
# Grid transparency
matplotlib.rcParams["grid.alpha"] = 0.3
# Grid linewidth
matplotlib.rcParams["grid.linewidth"] = 0.7

# SAVEFIG
# White margins
matplotlib.rcParams["savefig.bbox"] = "tight"
matplotlib.rcParams["savefig.pad_inches"] = 0.01

