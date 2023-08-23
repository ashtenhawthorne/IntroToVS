import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,20,100)
plt.plot(x, np.sin(x))
plt.show()


#New virtual environment = terminal: python3 -m venv venvname
#Activate virtual environment = terminal: source venvfoldername/bin/activate
#Download New Library = terminal: pip install libraryname