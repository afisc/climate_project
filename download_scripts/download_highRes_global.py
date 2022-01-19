# Code taken and adapted from Fabien Maussions Lecture Content
# https://gist.github.com/fmaussion/16c1119d8658cf4af9d3218dd5b1adf4

# To run this script successfully you will need to have registed at
# the Copernicus Climate Data Store and have to have configured
# a local API Config with your API key

import cdsapi
# Creating Client object to work with the CDS-API
c = cdsapi.Client()

# Defining data formats
grid = [0.25, 0.25]
area = [90, -180 + 0.75 / 2, -90, 180]
year = ['{}'.format(y) for y in range(1979, 2022)]
month = ['{:02d}'.format(m) for m in range(1, 13)]

# download directory
dl_dir = 'data/'

# retrieving high-resolution(0.25°) Invariant data
c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': [
            'land_sea_mask', 'model_bathymetry', 'orography'
        ],
        'grid': grid,
        'area': area,
        'year': '1979',
        'month': '01',
        'day': '01',
        'time': '00:00'
    },
    dl_dir + 'ERA5_HighRes_Invariant.nc')

# retrieving high-resolution(0.25°) PRCP data
c.retrieve(
    'reanalysis-era5-single-levels-monthly-means',
    {
        'format': 'netcdf',
        'product_type': 'monthly_averaged_reanalysis',
        'variable': [
            'total_precipitation'
        ],
        'grid': grid,
        'area': area,
        'year': year,
        'month': month,
        'time': '00:00'
    },
    dl_dir + 'ERA5_HighRes_Monthly_tp.nc')


# retrieving high-resolution(0.25°) Temp. data
c.retrieve(
    'reanalysis-era5-single-levels-monthly-means',
    {
        'format': 'netcdf',
        'product_type': 'monthly_averaged_reanalysis',
        'variable': [
            '2m_temperature'
        ],
        'grid': grid,
        'area': area,
        'year': year,
        'month': month,
        'time': '00:00'
    },
    dl_dir + 'ERA5_HighRes_Monthly_t2m.nc')


c.retrieve(
    'reanalysis-era5-single-levels-monthly-means',
    {
        'format': 'netcdf',
        'product_type': 'monthly_averaged_reanalysis',
        'variable': [
            'high_cloud_cover', 'low_cloud_cover', 'medium_cloud_cover',
            'total_cloud_cover', 'total_column_cloud_ice_water',
            'total_column_cloud_liquid_water',
        ],
        'grid': grid,
        'area': area,
        'year': year,
        'month': month,
        'time': '00:00'
    },
    dl_dir + 'ERA5_HighRes_Monthly_clouds.nc')
