import matplotlib.pyplot as plt
import yt

# Load the dataset.
ds = yt.load("IsolatedGalaxy/galaxy0030/galaxy0030")

# Create a sphere of radius 1 Mpc centered on the max density location.
sp = ds.sphere("max", (1, "Mpc"))

# Calculate and store the bulk velocity for the sphere.
bulk_velocity = sp.quantities['BulkVelocity']()
sp.set_field_parameter('bulk_velocity', bulk_velocity)

# Create a 1D profile object for profiles over radius
# and add a velocity profile.
prof = yt.create_profile(sp, 'radius', ('gas', 'velocity_magnitude'),
                         units = {'radius': 'kpc'},
                         extrema = {'radius': ((0.1, 'kpc'), (1000.0, 'kpc'))},
                         weight_field='cell_mass')

# Plot the average velocity magnitude.
plt.loglog(prof.x, prof['gas', 'velocity_magnitude'], label='Mean')
# Plot the variance of the velocity madnitude.
plt.loglog(prof.x, prof.variance['gas', 'velocity_magnitude'],
           label='Standard Deviation')
plt.xlabel('r [kpc]')
plt.ylabel('v [cm/s]')
plt.legend()

plt.savefig('velocity_profiles.png')
