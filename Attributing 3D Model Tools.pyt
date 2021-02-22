'''
Attributing 3D Models with Data
This toolbox provides a collection of geoprocessing tools for attributing 3D GIS Models in ArcGISPro from Raster and Vector Data 
mark.bryant@aecom.com
'''
import sys
import os


# Tools are located in a subfolder called Scripts. Append to path
SCRIPTPATH = os.path.join(os.path.dirname(__file__), "Scripts")
sys.path.append(SCRIPTPATH)

# Do not compile .pyc files for the tool modules.
sys.dont_write_bytecode = True

# Import scripts
from add_hex_color_to_polygon import AddHexColorToPolygon
from raster_property_to_polygon import RasterPropertyToPolygon

del SCRIPTPATH


class Toolbox(object):
    """ArcGIS Python Toolbox - Attributing 3D Model Tools"""

    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = 'Attributing 3D Model Tools'
        self.alias = 'dddmodel'

        # Create sets of tools
        sa_tools = {AddHexColorToPolygon, RasterPropertyToPolygon}
        # ddd_tools{BuildingHeights from}

        # List of tool classes associated with this toolbox
        self.tools = list(sa_tools)
        # polyline_tools | polygon_tools | spider_tools)
