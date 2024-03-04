import rasterio
from rasterio.plot import show
from rasterio.transform import rowcol

def get_paths_to_files(name_of_files_needed):
    altum_terrain_rasters = [
        'SoilPredictionModel/terrain_rasters/Altum/Altum_Aspect.tif',
        'SoilPredictionModel/terrain_rasters/Altum/Altum_Convergence.tif',
        'SoilPredictionModel/terrain_rasters/Altum/Altum_DAH.tif',
        'SoilPredictionModel/terrain_rasters/Altum/Altum_DEM.tif',
        'SoilPredictionModel/terrain_rasters/Altum/Altum_General_curvature.tif',
        'SoilPredictionModel/terrain_rasters/Altum/Altum_H_Overland_Dist.tif',
        'SoilPredictionModel/terrain_rasters/Altum/Altum_Insolation_Diffuse.tif',
        'SoilPredictionModel/terrain_rasters/Altum/Altum_Insolation_Direct.tif',
        'SoilPredictionModel/terrain_rasters/Altum/Altum_MRRTF.tif',
        'SoilPredictionModel/terrain_rasters/Altum/Altum_MRVBF.tif',
        'SoilPredictionModel/terrain_rasters/Altum/Altum_Openness_Neg.tif',
        'SoilPredictionModel/terrain_rasters/Altum/Altum_Openness_Pos.tif',
        'SoilPredictionModel/terrain_rasters/Altum/Altum_Overland_Dist.tif',
        'SoilPredictionModel/terrain_rasters/Altum/Altum_Slope.tif',
        'SoilPredictionModel/terrain_rasters/Altum/Altum_Total_curvature.tif',
        'SoilPredictionModel/terrain_rasters/Altum/Altum_TPI.tif',
        'SoilPredictionModel/terrain_rasters/Altum/Altum_TRI.tif',
        'SoilPredictionModel/terrain_rasters/Altum/Altum_TWI.tif',
        'SoilPredictionModel/terrain_rasters/Altum/Altum_V_Dist_to_cnetwork.tif',
        'SoilPredictionModel/terrain_rasters/Altum/Altum_V_Overland_Dist.tif'
    ]

    m3m_terrain_rasters = [
        'SoilPredictionModel/terrain_rasters/M3M/M3M_Aspect.tif',
        'SoilPredictionModel/terrain_rasters/M3M/M3M_Convergence.tif',
        'SoilPredictionModel/terrain_rasters/M3M/M3M_DAH.tif',
        'SoilPredictionModel/terrain_rasters/M3M/M3M_DEM.tif',
        'SoilPredictionModel/terrain_rasters/M3M/M3M_General_curvature.tif',
        'SoilPredictionModel/terrain_rasters/M3M/M3M_H_Overland_Dist.tif',
        'SoilPredictionModel/terrain_rasters/M3M/M3M_Insolation_Diffuse.tif',
        'SoilPredictionModel/terrain_rasters/M3M/M3M_Insolation_Direct.tif',
        'SoilPredictionModel/terrain_rasters/M3M/M3M_MRRTF.tif',
        'SoilPredictionModel/terrain_rasters/M3M/M3M_MRVBF.tif',
        'SoilPredictionModel/terrain_rasters/M3M/M3M_Openness_Neg.tif',
        'SoilPredictionModel/terrain_rasters/M3M/M3M_Openness_Pos.tif',
        'SoilPredictionModel/terrain_rasters/M3M/M3M_Overland_Dist.tif',
        'SoilPredictionModel/terrain_rasters/M3M/M3M_Slope.tif',
        'SoilPredictionModel/terrain_rasters/M3M/M3M_Total_curvature.tif',
        'SoilPredictionModel/terrain_rasters/M3M/M3M_TPI.tif',
        'SoilPredictionModel/terrain_rasters/M3M/M3M_TRI.tif',
        'SoilPredictionModel/terrain_rasters/M3M/M3M_TWI.tif',
        'SoilPredictionModel/terrain_rasters/M3M/M3M_V_Dist_to_cnetwork.tif',
        'SoilPredictionModel/terrain_rasters/M3M/M3M_V_Overland_Dist.tif'
    ]

    altum_ndvi_savi = [
        'SoilPredictionModel/index_rasters/Altum/Altum_NDVI.tif',
        'SoilPredictionModel/index_rasters/Altum/Altum_SAVI.tif',
    ]
    
    altum_index_rasters = [
        'SoilPredictionModel/index_rasters/Altum/Altum_CLG.tif',
        'SoilPredictionModel/index_rasters/Altum/Altum_CTVI.tif',
        'SoilPredictionModel/index_rasters/Altum/Altum_DVI.tif',
        'SoilPredictionModel/index_rasters/Altum/Altum_EVI2.tif',
        'SoilPredictionModel/index_rasters/Altum/Altum_GEMI.tif',
        'SoilPredictionModel/index_rasters/Altum/Altum_GNDVI.tif',
        'SoilPredictionModel/index_rasters/Altum/Altum_KNDVI.tif',
        'SoilPredictionModel/index_rasters/Altum/Altum_MCARI.tif',
        'SoilPredictionModel/index_rasters/Altum/Altum_MSAVI.tif',
        'SoilPredictionModel/index_rasters/Altum/Altum_MSAVI2.tif',
        'SoilPredictionModel/index_rasters/Altum/Altum_NDVI.tif',
        'SoilPredictionModel/index_rasters/Altum/Altum_NDWI.tif',
        'SoilPredictionModel/index_rasters/Altum/Altum_NRVI.tif',
        'SoilPredictionModel/index_rasters/Altum/Altum_RVI.tif',
        'SoilPredictionModel/index_rasters/Altum/Altum_SAVI.tif',
        'SoilPredictionModel/index_rasters/Altum/Altum_SR.tif',
        'SoilPredictionModel/index_rasters/Altum/Altum_TTVI.tif',
        'SoilPredictionModel/index_rasters/Altum/Altum_TVI.tif',
        'SoilPredictionModel/index_rasters/Altum/Altum_WDVI.tif'
    ]

    m3m_index_rasters = [
        'SoilPredictionModel/index_rasters/M3M/M3M_CLG.tif',
        'SoilPredictionModel/index_rasters/M3M/M3M_CTVI.tif',
        'SoilPredictionModel/index_rasters/M3M/M3M_DVI.tif',
        'SoilPredictionModel/index_rasters/M3M/M3M_EVI2.tif',
        'SoilPredictionModel/index_rasters/M3M/M3M_GEMI.tif',
        'SoilPredictionModel/index_rasters/M3M/M3M_GNDVI.tif',
        'SoilPredictionModel/index_rasters/M3M/M3M_KNDVI.tif',
        'SoilPredictionModel/index_rasters/M3M/M3M_MCARI.tif',
        'SoilPredictionModel/index_rasters/M3M/M3M_MSAVI.tif',
        'SoilPredictionModel/index_rasters/M3M/M3M_MSAVI2.tif',
        'SoilPredictionModel/index_rasters/M3M/M3M_NDVI.tif',
        'SoilPredictionModel/index_rasters/M3M/M3M_NDWI.tif',
        'SoilPredictionModel/index_rasters/M3M/M3M_NRVI.tif',
        'SoilPredictionModel/index_rasters/M3M/M3M_RVI.tif',
        'SoilPredictionModel/index_rasters/M3M/M3M_SAVI.tif',
        'SoilPredictionModel/index_rasters/M3M/M3M_SR.tif',
        'SoilPredictionModel/index_rasters/M3M/M3M_TTVI.tif',
        'SoilPredictionModel/index_rasters/M3M/M3M_TVI.tif',
        'SoilPredictionModel/index_rasters/M3M/M3M_WDVI.tif'
    ]

    climate_altum = [
        'SoilPredictionModel/climate_rasters/Altum/Altum_Year_2022Y_EMT.tif'
    ]
    
    match name_of_files_needed:
        case 'altum_terrain':
            return altum_terrain_rasters
        case 'm3m_terrain':
            return m3m_terrain_rasters
        case 'altum_index':
            return altum_index_rasters
        case 'm3m_index':
            return m3m_index_rasters
        case 'climate_altum':
            return climate_altum
        case 'altum_ndvi_savi':
            return altum_ndvi_savi

def load_tiff(file_path):
    with rasterio.open(file_path) as src:
        raster_data = src.read()
        metadata = src.meta
        transform = src.transform
        raster_sample = src.sample
    return raster_data, metadata, transform, raster_sample
