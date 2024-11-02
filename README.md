**Sandbar Detector Plugin for QGIS**

Overview:

The Sandbar Detector plugin is a tool for automating the detection of riverbed forms within the Quantum Geographic Information System (QGIS). Developed in Python, this plugin leverages the Sentinel Water Mask (SWM) and high-resolution Sentinel-2 satellite data to efficiently differentiate between land and water, providing consistent and accurate results essential for hydrological studies and environmental monitoring.

**Key Features**

Automated Riverbed Detection: Streamlines the process of identifying riverbed forms, saving time and reducing the potential for human error.

High Precision: Utilizes the SWM index with high-resolution Sentinel-2 data to provide precise differentiation between water and land.

User-Friendly Interface: Simple and intuitive interface, making it accessible to users without extensive experience in remote sensing or GIS.

Open Source: Fully open-source, allowing for modifications and enhancements by the community.


**Installation**
Copy the plugin folder to your QGIS plugins directory:

On Windows: C:\Users\[YourUsername]\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins

On macOS and Linux: ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins

Restart QGIS and enable the Sandbar Detector plugin from the Plugin Manager.

**Usage**
Open QGIS and load Sentinel-2 Level 1C images, including Bands 2, 3, 8, and 11.
Launch the Sandbar Detector plugin from the Plugins menu.
Select the required bands in the dialog window.
Run the analysis, which will process the data, apply the SWM index, and generate a binary water mask image.
The plugin outputs a vector layer that clearly differentiates between land and water areas, ready for further analysis.

Requirements:
QGIS: Version 3.x or higher
Python: Version 3.9
Dependencies: PyQt5, Pandas, NumPy, GDAL
Contributions
We welcome contributions from the community to enhance the plugin's functionality. Feel free to open issues, submit pull requests, or suggest improvements.

License:
This project is licensed under the GNU General Public License (GPL). You are free to use, modify, and distribute this software under the terms of the GPL, which ensures that any derivative work must also be open and free.

Acknowledgements:
This plugin was developed as part of hydrological research supported by the Environmental Engineering, Mining, and Energy scientific discipline.

Contact:
For questions or support, contact the author:

Author: Klaudia Kryniecka
Email: klaudia.kryniecka@pw.edu.pl
