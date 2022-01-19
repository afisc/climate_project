
# To run this script successfully you will need to have registed at
# the Copernicus Climate Data Store and have to have configured
# a local API Config with your API key

import cdsapi
# Creating Client object to work with the CDS-API
c = cdsapi.Client()

# Defining data formats
grid = [0.25, 0.25]
area = [90, -180 + 0.75 / 2, -90, 180]
year = ['{}'.format(y) for y in range(1979, 2019)]
month = ['{:02d}'.format(m) for m in range(1, 13)]

# download directory
dl_dir = 'data/'

# Code generated on the copernicus.eu homepage and modified
c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'format': 'netcdf',
        'product_type': 'monthly_averaged_reanalysis',
        'variable': [
            '2m_temperature', 'high_cloud_cover', 'low_cloud_cover',
            'medium_cloud_cover', 'total_cloud_cover', 'total_precipitation',
            'low_vegetation_cover', 'high_vegetation_cover', 'evaporation'
        ],
        'year': year,
        'month': month,
        'time': '00:00',
        'area': [
            15, -83, -25,
            -32
        ],
    },
    dl_dir + 'ERA5_HighRes_amazon_region_data.nc')
