# Reading_XDF_files
## CheckXDFAlignment.py
### Packages needed to run this script
1. [pyxdf](https://github.com/xdf-modules/pyxdf)
2. [matplotlib](https://matplotlib.org/stable/install/index.html)

### Running Script
Add full path to xdf file in the script
```python
pathToFile = '/path/to/file.xdf.gz'
```
Change how much of the stream is plotted. By default, only the first point is plotted.
For full stream, delete the 1.
```python
plt.plot(x[:1], y[:1])
``` 
