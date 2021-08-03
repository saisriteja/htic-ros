# import pyyaml module
import yaml
from yaml.loader import SafeLoader

# Open the file and load the file
with open('tf_static.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    print(data)

from scipy.spatial.transform import Rotation as R

def making_tf_matrix(rotation,translation):
    r_w = rotation['w']
    r_x = rotation['x']
    r_y = rotation['y']
    r_z = rotation['z']
    
    t_x = translation['x']
    t_y = translation['y']
    t_z = translation['z']
    
    tf = np.identity(4)
    
    r = R.from_quat([r_x,r_y,r_z,r_w])
#     print(np.array(r.as_dcm()))
    
    tf[:3,:3] = r.as_dcm()
    tf[3:,:3] = np.array([t_x,t_y,t_z])
    
    return tf
    
    
# import pyyaml module
import yaml
from yaml.loader import SafeLoader

# Open the file and load the file
with open('tf_static.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
#     print(data)
    
    
for i in range(len(data['transforms'])):

    child_frame_id = data['transforms'][i]['child_frame_id']
    parent_frame_id = data['transforms'][i]['header']['frame_id']
    rotation_data = data['transforms'][i]['transform']['rotation']
    translation_data = data['transforms'][i]['transform']['translation']
    print 'parent is',parent_frame_id
    print 'child is', child_frame_id, '\n'
    print(making_tf_matrix(rotation_data,translation_data))
    print '\n'
    
    
