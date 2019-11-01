# Ahna Knudsen
# Lab 3 
# 11/1/19
# Description:

>>> from arcpy import env
>>> env.workspace = "Y:\Personal\aknudsen\Lab_3_Geoprocessing_Python"
# clip analysis. input: parks clip feature: zip output: parks_Clip 
>>> arcpy.Clip_analysis("parks", "zip", "Results/parks_Clip.shp")
<Result 'Y:\\Personal\\aknudsen\\Lab_3_Geoprocessing_Python\\Results\\parks_Clip.shp'>
# buffer analysis. input:facilites output: facilites_buffer buffer distance: 500 meters 
>>> arcpy.Buffer_analysis("facilities.shp", "Results/facilities_buffer.shp", "500 METERS")
<Result 'Y:\\Personal\\aknudsen\\Lab_3_Geoprocessing_Python\\Results\\facilities_buffer.shp'>
# buffer analysis with dissolving. input:facilites output: facilites_buffer buffer distance: 500 meters dissolve parameters: ALL 
>>> arcpy.Buffer_analysis("facilities.shp", "Results/facilities_buffer.shp", "500 METERS", "", "", "ALL")
<Result 'Y:\\Personal\\aknudsen\\Lab_3_Geoprocessing_Python\\Results\\facilities_buffer.shp'>
# you can first assign the value of a parameter to a variable, and then use the variables in the code that calls the tool.
>>> in_features = "bike_routes.shp"
>>> clip_features = "zip.shp"
>>> out_features = "bike_Clip.shp"
>>> xy_tolerance = ""
# run clip tool with defined variables
arcpy.Clip_analysis(in_features, clip_features, out_features, xy_tolerance)
<Result 'Y:\\Personal\\aknudsen\\Lab_3_Geoprocessing_Python\\bike_Clip.shp'>
