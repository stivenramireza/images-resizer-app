def get_image_id(path):
    return path.split('/')[-2]

def get_filename(path):
    return path.split('/')[-1][3:]