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
    match name_of_files_needed:
        case 'altum_terrain':
            return altum_terrain_rasters
        case 'm3m_terrain':
            return m3m_terrain_rasters
        case 'altum_index':
            return altum_index_rasters
        case 'm3m_index':
            return m3m_index_rasters

# Step 1: Load TIFF files
def load_tiff(file_path):
    with rasterio.open(file_path) as src:
        # Read the raster data
        raster_data = src.read()
        # Extract metadata
        metadata = src.meta
        # Extract transform function
        transform = src.transform
         # Extract transform function
        raster_sample = src.sample
    return raster_data, metadata, transform, raster_sample

def get_altum_terrain_rasters():
    altum_rasters = {
        'altum_aspect': 'SoilPredictionModel/terrain_rasters/Altum/Altum_Aspect.tif',
        'altum_convergence': 'SoilPredictionModel/terrain_rasters/Altum/Altum_Convergence.tif',
        'altum_dah': 'SoilPredictionModel/terrain_rasters/Altum/Altum_DAH.tif',
        'altum_dem': 'SoilPredictionModel/terrain_rasters/Altum/Altum_DEM.tif',
        'altum_general_curvature': 'SoilPredictionModel/terrain_rasters/Altum/Altum_General_curvature.tif',
        'altum_h_overland_dist': 'SoilPredictionModel/terrain_rasters/Altum/Altum_H_Overland_Dist.tif',
        'altum_insolation_diffuse': 'SoilPredictionModel/terrain_rasters/Altum/Altum_Insolation_Diffuse.tif',
        'altum_insolation_direct': 'SoilPredictionModel/terrain_rasters/Altum/Altum_Insolation_Direct.tif',
        'altum_mrrtf': 'SoilPredictionModel/terrain_rasters/Altum/Altum_MRRTF.tif',
        'altum_mrvbf': 'SoilPredictionModel/terrain_rasters/Altum/Altum_MRVBF.tif',
        'altum_openness_neg': 'SoilPredictionModel/terrain_rasters/Altum/Altum_Openness_Neg.tif',
        'altum_openness_pos': 'SoilPredictionModel/terrain_rasters/Altum/Altum_Openness_Pos.tif',
        'altum_overland_dist': 'SoilPredictionModel/terrain_rasters/Altum/Altum_Overland_Dist.tif',
        'altum_slope': 'SoilPredictionModel/terrain_rasters/Altum/Altum_Slope.tif',
        'altum_total_curvature': 'SoilPredictionModel/terrain_rasters/Altum/Altum_Total_curvature.tif',
        'altum_tpi': 'SoilPredictionModel/terrain_rasters/Altum/Altum_TPI.tif',
        'altum_tri': 'SoilPredictionModel/terrain_rasters/Altum/Altum_TRI.tif',
        'altum_twi': 'SoilPredictionModel/terrain_rasters/Altum/Altum_TWI.tif',
        'altum_v_dist_to_cnetwork': 'SoilPredictionModel/terrain_rasters/Altum/Altum_V_Dist_to_cnetwork.tif',
        'altum_v_overland_dist': 'SoilPredictionModel/terrain_rasters/Altum/Altum_V_Overland_Dist.tif'
    }

    altum_raster_data = {}
    for raster_name, raster_path in altum_rasters.items():
        raster_data, raster_metadata, raster_transform, raster_sample = load_tiff(raster_path)
        altum_raster_data[raster_name + '_data'] = raster_data
        altum_raster_data[raster_name + '_metadata'] = raster_metadata
        altum_raster_data[raster_name + '_transform'] = raster_transform
        altum_raster_data[raster_name + '_sample'] = raster_sample

    return altum_raster_data

def get_m3m_terrain_rasters():
    m3m_rasters = {
        'm3m_aspect': 'SoilPredictionModel/terrain_rasters/M3M/M3M_Aspect.tif',
        'm3m_convergence': 'SoilPredictionModel/terrain_rasters/M3M/M3M_Convergence.tif',
        'm3m_dah': 'SoilPredictionModel/terrain_rasters/M3M/M3M_DAH.tif',
        'm3m_dem': 'SoilPredictionModel/terrain_rasters/M3M/M3M_DEM.tif',
        'm3m_general_curvature': 'SoilPredictionModel/terrain_rasters/M3M/M3M_General_curvature.tif',
        'm3m_h_overland_dist': 'SoilPredictionModel/terrain_rasters/M3M/M3M_H_Overland_Dist.tif',
        'm3m_insolation_diffuse': 'SoilPredictionModel/terrain_rasters/M3M/M3M_Insolation_Diffuse.tif',
        'm3m_insolation_direct': 'SoilPredictionModel/terrain_rasters/M3M/M3M_Insolation_Direct.tif',
        'm3m_mrrtf': 'SoilPredictionModel/terrain_rasters/M3M/M3M_MRRTF.tif',
        'm3m_mrvbf': 'SoilPredictionModel/terrain_rasters/M3M/M3M_MRVBF.tif',
        'm3m_openness_neg': 'SoilPredictionModel/terrain_rasters/M3M/M3M_Openness_Neg.tif',
        'm3m_openness_pos': 'SoilPredictionModel/terrain_rasters/M3M/M3M_Openness_Pos.tif',
        'm3m_overland_dist': 'SoilPredictionModel/terrain_rasters/M3M/M3M_Overland_Dist.tif',
        'm3m_slope': 'SoilPredictionModel/terrain_rasters/M3M/M3M_Slope.tif',
        'm3m_total_curvature': 'SoilPredictionModel/terrain_rasters/M3M/M3M_Total_curvature.tif',
        'm3m_tpi': 'SoilPredictionModel/terrain_rasters/M3M/M3M_TPI.tif',
        'm3m_tri': 'SoilPredictionModel/terrain_rasters/M3M/M3M_TRI.tif',
        'm3m_twi': 'SoilPredictionModel/terrain_rasters/M3M/M3M_TWI.tif',
        'm3m_v_dist_to_cnetwork': 'SoilPredictionModel/terrain_rasters/M3M/M3M_V_Dist_to_cnetwork.tif',
        'm3m_v_overland_dist': 'SoilPredictionModel/terrain_rasters/M3M/M3M_V_Overland_Dist.tif'
    }

    m3m_raster_data = {}
    for raster_name, raster_path in m3m_rasters.items():
        raster_data, raster_metadata, raster_transform = load_tiff(raster_path)
        m3m_raster_data[raster_name + '_data'] = raster_data
        m3m_raster_data[raster_name + '_metadata'] = raster_metadata
        m3m_raster_data[raster_name + '_transform'] = raster_transform

    return m3m_raster_data

def get_altum_index_rasters(index_name):
    altum_index_rasters = {
        'altum_clg': 'SoilPredictionModel/index_rasters/Altum/Altum_CLG.tif',
        'altum_ctvi': 'SoilPredictionModel/index_rasters/Altum/Altum_CTVI.tif',
        'altum_dvi': 'SoilPredictionModel/index_rasters/Altum/Altum_DVI.tif',
        'altum_evi2': 'SoilPredictionModel/index_rasters/Altum/Altum_EVI2.tif',
        'altum_gemi': 'SoilPredictionModel/index_rasters/Altum/Altum_GEMI.tif',
        'altum_gndvi': 'SoilPredictionModel/index_rasters/Altum/Altum_GNDVI.tif',
        'altum_kndvi': 'SoilPredictionModel/index_rasters/Altum/Altum_KNDVI.tif',
        'altum_mcari': 'SoilPredictionModel/index_rasters/Altum/Altum_MCARI.tif',
        'altum_msavi': 'SoilPredictionModel/index_rasters/Altum/Altum_MSAVI.tif',
        'altum_msavi2': 'SoilPredictionModel/index_rasters/Altum/Altum_MSAVI2.tif',
        'altum_ndvi': 'SoilPredictionModel/index_rasters/Altum/Altum_NDVI.tif',
        'altum_ndwi': 'SoilPredictionModel/index_rasters/Altum/Altum_NDWI.tif',
        'altum_nrvi': 'SoilPredictionModel/index_rasters/Altum/Altum_NRVI.tif',
        'altum_rvi': 'SoilPredictionModel/index_rasters/Altum/Altum_RVI.tif',
        'altum_savi': 'SoilPredictionModel/index_rasters/Altum/Altum_SAVI.tif',
        'altum_sr': 'SoilPredictionModel/index_rasters/Altum/Altum_SR.tif',
        'altum_ttv': 'SoilPredictionModel/index_rasters/Altum/Altum_TTVI.tif',
        'altum_tvi': 'SoilPredictionModel/index_rasters/Altum/Altum_TVI.tif',
        'altum_wdvi': 'SoilPredictionModel/index_rasters/Altum/Altum_WDVI.tif'
    }

    raster_path = altum_index_rasters.get(index_name.lower())
    if raster_path:
        raster_data, raster_metadata, raster_transform = load_tiff(raster_path)
        return raster_data, raster_metadata, raster_transform
    else:
        print("Raster not found.")
        return None, None, None


def get_m3m_index_rasters(index_name):
    m3m_index_rasters = {
        'm3m_clg': 'SoilPredictionModel/index_rasters/M3M/M3M_CLG.tif',
        'm3m_ctvi': 'SoilPredictionModel/index_rasters/M3M/M3M_CTVI.tif',
        'm3m_dvi': 'SoilPredictionModel/index_rasters/M3M/M3M_DVI.tif',
        'm3m_evi2': 'SoilPredictionModel/index_rasters/M3M/M3M_EVI2.tif',
        'm3m_gemi': 'SoilPredictionModel/index_rasters/M3M/M3M_GEMI.tif',
        'm3m_gndvi': 'SoilPredictionModel/index_rasters/M3M/M3M_GNDVI.tif',
        'm3m_kndvi': 'SoilPredictionModel/index_rasters/M3M/M3M_KNDVI.tif',
        'm3m_mcari': 'SoilPredictionModel/index_rasters/M3M/M3M_MCARI.tif',
        'm3m_msavi': 'SoilPredictionModel/index_rasters/M3M/M3M_MSAVI.tif',
        'm3m_msavi2': 'SoilPredictionModel/index_rasters/M3M/M3M_MSAVI2.tif',
        'm3m_ndvi': 'SoilPredictionModel/index_rasters/M3M/M3M_NDVI.tif',
        'm3m_ndwi': 'SoilPredictionModel/index_rasters/M3M/M3M_NDWI.tif',
        'm3m_nrvi': 'SoilPredictionModel/index_rasters/M3M/M3M_NRVI.tif',
        'm3m_rvi': 'SoilPredictionModel/index_rasters/M3M/M3M_RVI.tif',
        'm3m_savi': 'SoilPredictionModel/index_rasters/M3M/M3M_SAVI.tif',
        'm3m_sr': 'SoilPredictionModel/index_rasters/M3M/M3M_SR.tif',
        'm3m_ttv': 'SoilPredictionModel/index_rasters/M3M/M3M_TTVI.tif',
        'm3m_tvi': 'SoilPredictionModel/index_rasters/M3M/M3M_TVI.tif',
        'm3m_wdvi': 'SoilPredictionModel/index_rasters/M3M/M3M_WDVI.tif'
    }

    raster_path = m3m_index_rasters.get(index_name.lower())
    if raster_path:
        raster_data, raster_metadata, raster_transform = load_tiff(raster_path)
        return raster_data, raster_metadata, raster_transform
    else:
        print("Raster not found.")
        return None, None, None
