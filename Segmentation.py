import pyclesperanto_prototype as cle

def segmentation(image):
    
    #Noise removal
    g_blur = cle.gaussian_blur(image, sigma_x=1.0, sigma_y=1.0, sigma_z=1.0)
    
    #Background subtracton
    background_subtracted = cle.top_hat_box(g_blur, radius_x=10.0, radius_y=10.0, radius_z=10.0)
        
    #Segmentation
    output_labels = cle.voronoi_otsu_labeling(background_subtracted, spot_sigma=2.0, outline_sigma=0.0)
    
    return output_labels
