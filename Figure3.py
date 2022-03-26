import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)
path = "trout_data.txt"
df = pd.read_csv(path, sep='\t')

y = sns.histplot(data=df, x="alignment_scores", binwidth=3)
y.set(xlabel = "Alignment Scores (%)", ylabel="Number of Reads (in Millions)")
plt.show()
