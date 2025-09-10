import matplotlib.pyplot as plt
import pyxdf


# Input the full path to file here
pathToFile = '/path/to/file.xdf.gz'

# Using pyxdf to load the data
data, header = pyxdf.load_xdf(pathToFile, synchronize_clocks=True)

# Plotting the first timestamps of every stream
y_ele = 1
for stream in data:
    name = stream['info']['name'][0]
    x = stream['time_stamps']
    y = [y_ele] * len(x)
    duration = x[-1] - x[0]
    # Delete the 1 to get entire duration of stream
    plt.plot(x[:1], y[:1])
    plt.text(x[0], y[0], name, ha='left', va='top')
    print(name)
    print('Initial time:', x[0])
    print('Number of samples:', len(x))
    print('Duration:', duration)
    print('---------------------------------------------------')
    y_ele += 1
  
plt.show()
