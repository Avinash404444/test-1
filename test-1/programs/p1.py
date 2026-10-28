import seaborn as sns
import matplotlib.pyplot as plt
print("Seaborn version:", sns.__version__)
print("Libraries imported successfully!")
palettes = ["deep", "muted", "pastel",
"bright", "dark", "colorblind"]
for palette in palettes:
sns.palplot(sns.color_palette(palette))
plt.title(f"{palette.capitalize()} Palette")
plt.show()
