## TFApy - Time Frequency Analysis UI - early Beta :rocket: ##

Tools for time-frequency analysis with Morlet Wavelets
Inspired by 'A Practical Guide to Wavelet Analysis' from Torrence
and Compo 1998
and 'Identification of Chirps with Continuous Wavelet Transform'
from Carmona,Hwang and Torresani 1995.

Version 0.4 June 2018, Gregor Mönke (gregor.moenke@embl.de) and Frieda Sorgenfrei 

### Features ###

* Optimal sinc filter
* Fourier analysis
* Wavelet analysis 
* Ridge detection
* Phase extraction 

### Things not ready yet ###

* Dedicated results window after ridge detection 
* Results export (you can save the Wavelet Spectrum)
* Synthetic signal generator

### Installation and Requirements ###

The program needs some scientific python libraries (detailed list will come), it's most
convenient to install [Anaconda 3] (https://conda.io/docs/user-guide/install/download.html) to
get all required Python libraries.

No real 'installation' yet, just download (or clone) the
repository and run ``` TFApy.py ``` on the terminal 
from the ``` /src ``` directory.

##### Mac OS #####

After downloading the repository, double click the 
``` TFApy_MacOS ``` command file. It will open a 
terminal in the background and runs the TFApy program.

### Usage ###

##### Data import #####

Just open your saved time-series data by using ``` Open ``` 
from the (small) main window. Supported input formats are:
``` .xls, .xlsx, .csv, .tsv and .txt ```. For other file
extensions, white space separation of the data is assumed.
Please see examples of the supported formats in the 
``` data_examples ``` directory.

##### Inspection/Detrending #####

After successful import, you can simply click on the table representing
your data to select a specific time-series in the ``` DataViewer ```. 
Alternatively, select a specific time-series from the drop-down menu in the upper left.
To get the correct numbers/units you can change the sampling interval 
and unit name in the top line of the ``` DataViewer ```.
To apply the sinc-filter detrending, enter a (positive) Number for the ``` cut-off-period ```. 
All periods bigger than the one entered will be removed from the data. Click ``` Refresh Plot ```
and check the ``` Trend ``` and/or ``` Detrended Signal ``` checkbox(es) to see the effect of the filter.