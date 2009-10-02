import numpy as np
import pylab as P
from enthought.mayavi import mlab
from scipy.integrate import odeint


######################################################################
def lorenz(x, y, z, s=10.,r=28., b=8./3.):
    """The Lorenz system."""
    u = s*(y-x)
    v = r*x -y - x*z
    w = x*y - b*z
    return u, v, w

def lorenz_ode(r, t):
    x, y, z = r
    u, v, w = lorenz(x, y, z)
    return np.array([u, v, w])

def show_lorenz(new_fig=True):
    x, y, z = np.mgrid[-50:50:100j,-50:50:100j,-10:60:70j]
    u, v, w = lorenz(x, y, z)

    if new_fig:
        fig = mlab.figure(size=(600,600), bgcolor=(0, 0, 0))

    # Plot the flow of trajectories with suitable parameters.
    f = mlab.flow(x, y, z, u, v, w, line_width=3, colormap='Paired')
    f.module_manager.scalar_lut_manager.reverse_lut = True
    f.stream_tracer.integration_direction = 'both'
    f.stream_tracer.maximum_propagation = 200

def show_lorenz_traj(start=(0.,0.,0.)):
    t = np.linspace(0., 50., 2000)
    ret = lorenz_traj(t, np.asarray(start))
    x, y, z = ret[:,0], ret[:,1], ret[:,2]
    mlab.plot3d(x, y, z, t, tube_radius=None)


def lorenz_traj(t, start=(0.,0.,0.)):
    return odeint(lorenz_ode, start, t)
    

######################################################################

def convection_cell(x, y, z):
    """velocity field of a multi-axis convection cell [1], in
    hydrodynamics, as defined by its components sampled on a grid. 
    """
    u =  np.sin(np.pi*x) * np.cos(np.pi*z)
    v = -2*np.sin(np.pi*y) * np.cos(2*np.pi*z)
    w = np.cos(np.pi*x)*np.sin(np.pi*z) + np.cos(np.pi*y)*np.sin(2*np.pi*z)
    return u, v, w

def show_convection1(new_fig=True):
    x, y, z = np.mgrid[0:1:20j, 0:1:20j, 0:1:20j]
    u, v, w = convection_cell(x, y, z)
    if new_fig:
        mlab.figure(size=(600,600))

    mlab.quiver3d(u, v, w)
    mlab.outline()

def show_convection2(new_fig=True):
    x, y, z = np.mgrid[0:1:20j, 0:1:20j, 0:1:20j]
    u, v, w = convection_cell(x, y, z)
    if new_fig:
        mlab.figure(size=(600,600))

    src = mlab.pipeline.vector_field(u, v, w)
    mlab.pipeline.vectors(src, mask_points=20, scale_factor=3.)
    mlab.outline()

def show_convection3(new_fig=True):
    x, y, z = np.mgrid[0:1:20j, 0:1:20j, 0:1:20j]
    u, v, w = convection_cell(x, y, z)

    if new_fig:
        mlab.figure(fgcolor=(0., 0., 0.), bgcolor=(0.5, 0.5, 0.5),
                    size=(600,600))
    src = mlab.pipeline.vector_field(u, v, w)
    magnitude = mlab.pipeline.extract_vector_norm(src)
    mlab.outline()

    # We apply the following modules on the magnitude object, in order to
    # be able to display the norm of the vectors, eg as the color.
    iso = mlab.pipeline.iso_surface(magnitude, contours=[1.9, ], 
                                    opacity=0.3)

    vec = mlab.pipeline.vectors(magnitude, 
                                mask_points=40,
                                line_width=1,
                                color=(1, 1, 1),
                                scale_factor=4.)

    flow = mlab.pipeline.streamline(magnitude, 
                                    seedtype='plane',
                                    seed_visible=True,
                                    seed_scale=0.5,
                                    seed_resolution=1,
                                    linetype='ribbon',)

    vcp = mlab.pipeline.vector_cut_plane(magnitude, mask_points=2,
                                         scale_factor=4,
                                         colormap='jet',
                                         plane_orientation='x_axes')


def test():
    show_lorenz()
    show_lorenz_traj((10, 50, 50))
    show_convection1()
    show_convection2()
    show_convection3()

if __name__ == '__main__':
    test()

