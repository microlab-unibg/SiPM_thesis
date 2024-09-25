import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as mplcm

# FONT
# font_selector = 0: Times New Roman (IEEE style)
# font_selector = 1: CMU Sans Serif (slide)
# font_selector = 2: Palatino (MDPI)
# font_selector = 3: Standard Python, no LaTex
# font_selector = 4: Plain Latex font (CMU Serif)

font_selector = 1

# TEX INTERPRETER
if font_selector == 0:
    plt.rcParams.update({"text.usetex": True, "font.family": "serif"})
    plt.rc("text.latex", preamble=r"\usepackage{siunitx}\usepackage{times}\usepackage{mathptmx}")
    font_info = "Times New Roman (IEEE style)"
    packages = ["siunitx", "times", "mathptmx"]
elif font_selector == 1:
    plt.rcParams.update({"text.usetex": True, "font.family": "sans-serif"})
    plt.rc("text.latex", preamble=r"\usepackage{siunitx}\usepackage[cm]{sfmath}\sisetup{detect-all}")
    font_info = "CMU Sans Serif (slide)"
    packages = ["siunitx", "sfmath"]
elif font_selector == 2:
    plt.rcParams.update({"text.usetex": True, "font.family": "serif"})
    plt.rc("text.latex", preamble=r"\usepackage{siunitx}\RequirePackage{mathpazo}")
    font_info = "Palatino (MDPI)"
    packages = ["siunitx", "mathpazo"]
elif font_selector == 3:
    plt.rcParams.update({"text.usetex": False})
    font_info = "Standard Python, no LaTeX"
    packages = []
elif font_selector == 4:
    plt.rcParams.update({"text.usetex": True, "font.family": "serif"})
    plt.rc("text.latex", preamble=r"\usepackage{siunitx}")
    font_info = "Plain Latex font (CMU Serif)"
    packages = ["siunitx"]

# Fontsize
fontsize = 12

# Color palette
NUM_COLORS = 6
cm = plt.get_cmap("tab10")
cNorm = colors.Normalize(vmin=0, vmax=NUM_COLORS - 1)
scalarMap = mplcm.ScalarMappable(norm=cNorm, cmap=cm)

# Markers
markers = ["o", "v", "^", ">", "<", "s", "P", "X", "D", "d", "o"]

# FIGURE
# Font size
matplotlib.rcParams["font.size"] = fontsize
# Maximum number of open figures
matplotlib.rcParams["figure.max_open_warning"] = 100
# Figure size
# Multipliers
mult_x = 1
mult_y = 1
x_dim = 6.4 * mult_x
y_dim = 4.8 * mult_y
matplotlib.rcParams["figure.figsize"] = x_dim, y_dim

# Convert figure size to mm
x_dim_mm = x_dim * 2.54 * 10  # Convert inches to mm
y_dim_mm = y_dim * 2.54 * 10  # Convert inches to mm

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
matplotlib.rcParams["ytick.right"] = True

# LEGEND
# Legend font size
matplotlib.rcParams['legend.title_fontsize'] = fontsize
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

# TITLE
# Title font size
matplotlib.rcParams["axes.titlesize"] = fontsize * 1.1

# PRINT CONFIGURATIONS
print("*** PLOT STYLESHEET SUMMARY ***")
print(f"        Font selector: {font_selector}")
print(f"           Font style: {font_info}")
print(f"          Text usetex: {plt.rcParams['text.usetex']}")
print(f"       LaTeX packages: {packages}")
print(f"          Font family: {plt.rcParams['font.family']}")
print(f"            Font size: {fontsize}")
print(f"     Number of colors: {NUM_COLORS}")
print(f"             Colormap: {cm.name}")
print(f"              Markers: {markers}")
print(f"      Figure size (X): {x_dim:.2f} inches | {x_dim_mm:.2f} mm")
print(f"      Figure size (Y): {y_dim:.2f} inches | {y_dim_mm:.2f} mm")
print(f"           Figure DPI: {matplotlib.rcParams['figure.dpi']}")
print(f"    Boxplot linewidth: {matplotlib.rcParams['axes.linewidth']}")
print(f"   X-tick major width: {matplotlib.rcParams['xtick.major.width']}")
print(f"   Y-tick major width: {matplotlib.rcParams['ytick.major.width']}")
print(f"     X-tick direction: {matplotlib.rcParams['xtick.direction']}")
print(f"     Y-tick direction: {matplotlib.rcParams['ytick.direction']}")
print(f"    X-tick label size: {matplotlib.rcParams['xtick.labelsize']}")
print(f"    Y-tick label size: {matplotlib.rcParams['ytick.labelsize']}")
print(f"    Legend title size: {matplotlib.rcParams['legend.title_fontsize']}")
print(f"     Legend font size: {matplotlib.rcParams['legend.fontsize']:.1f}")
print(f"   Legend frame alpha: {matplotlib.rcParams['legend.framealpha']:.1f}")
print(f"      Axes label size: {matplotlib.rcParams['axes.labelsize']}")
print(f"           Grid alpha: {matplotlib.rcParams['grid.alpha']}")
print(f"       Grid linewidth: {matplotlib.rcParams['grid.linewidth']}")
print(f"         Savefig bbox: {matplotlib.rcParams['savefig.bbox']}")
print(f"   Savefig pad inches: {matplotlib.rcParams['savefig.pad_inches']}")
print(f"      Axes title size: {matplotlib.rcParams['axes.titlesize']:.1f}")