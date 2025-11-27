# Import AI Earth SDK and authenticate
import aie
aie.authenticate()  # Authenticate with AI Earth platform
aie.initialize()    # Initialize the AI Earth environment

# Define study area using vector boundary
region = aie.featurecollection('user/your_vector_file_id')  # Replace with actual vector file ID
geometry = region.geometry()  # Extract geometry from the feature collection

# Select dataset and process imagery
dataset = aie.imagecollection('sentinel_msil2a') \
    .filterbounds(geometry) \  # Filter by geographic boundary
    .filterdate('start_date', 'end_date')  # Replace with specific date range
image = dataset.mosaic().clip(geometry)  # Create mosaic and clip to study area

# Initialize building extraction task
task = aie.tasks.building_extraction(image, 'output_asset_name', scale=10)  # scale defines output resolution in meters
task.start()  # Execute the building extraction task