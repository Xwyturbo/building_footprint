import arcpy
arcpy.env.workspace = "example_shpfile/example"
fcs = arcpy.ListFeatureClasses()
lspt = []
for fc in fcs:
    lspt.append(fc)
arcpy.Merge_management(lspt,"building_footprint_example.shp")
