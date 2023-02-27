#!/usr/bin/env python
# coding: utf-8

# #### import package

# In[54]:


# Import standard packages
get_ipython().run_line_magic('matplotlib', 'notebook')
import matplotlib.pyplot as plt
plt.ioff() # turn off interactive plotting mode
import numpy as np
import pandas as pd
# Xarray is conventionally imported as 'xr'
import xarray as xr


# #### open dataset

# In[66]:


#open dataset
ds_var_bottom=xr.open_dataset('~/case1/swm.cdf')
ds_flat_bottom=xr.open_dataset('~/case2/swm.cdf')


# ### animation part

# In[67]:


#animation part
from matplotlib import animation
fig, ax = plt.subplots()
#ax.contourf(lon,lat,air[0,:,:])
def animate(i): # i represents one frame in the animation
    data = ds_flat_bottom.h[i,:,:] # slice data advancing one timestep
    ax.cla()
    data.plot(ax=ax, cmap="RdYlBu_r", add_colorbar=False, vmin=-2, vmax=2)


# In[68]:


# Instantiate the animator.
anim = animation.FuncAnimation(fig,
                               animate,
                               frames=120, # 12 frames = 12 months
                               interval=200, # 200 milliseconds interval between each frame
                               blit=False, repeat=False) # for blit=True, only the changes are plotted
plt.show()


# ### Wave propagation part

# In[72]:


plt.subplot(2,2,1)
ds_var_bottom.h[0,:,:].plot(cmap="RdYlBu_r", vmin=-2, vmax=2)
plt.xlabel('x')
plt.ylabel('y')
plt.plot([500,0],[0,500],'k-')

plt.subplot(2,2,2)
ds_var_bottom.h[20,:,:].plot(cmap="RdYlBu_r", vmin=-2, vmax=2)
plt.xlabel('x')
plt.ylabel('y')
plt.plot([500,0],[0,500],'k-')

plt.subplot(2,2,3)
ds_var_bottom.h[40,:,:].plot(cmap="RdYlBu_r", vmin=-2, vmax=2)
plt.xlabel('x')
plt.ylabel('y')
plt.plot([500,0],[0,500],'k-')

plt.subplot(2,2,4)
ds_var_bottom.h[59,:,:].plot(cmap="RdYlBu_r", vmin=-2, vmax=2)
plt.xlabel('x')
plt.ylabel('y')
plt.plot([500,0],[0,500],'k-')
plt.show()
plt.savefig('swm_bar_bottom'+'png')


# ####Produce Hovmoeller diagrams for each experiment 

# In[74]:


h_flat_diag=np.zeros((60,500))
h_var_diag=np.zeros((60,500))
for i in range(500):
    h_flat_diag[:,i]=(ds_flat_bottom.h[:,i,i]);
    h_var_diag[:,i]=(ds_var_bottom.h[:,i,i])
    


# In[78]:


ds_flat_diag=xr.Dataset(data_vars={'h':(['time','xpos'],h_flat_diag)})
ds_flat_diag.h.plot()
plt.title('Hovmoeller diagram flat')
plt.xlabel('x')
plt.ylabel('time')
plt.grid()
plt.show()


# In[77]:


ds_var_diag=xr.Dataset(data_vars={'h':(['time','xpos'],h_var_diag)})
ds_var_diag.h.plot()
plt.title('Hovmoeller diagram flat')
plt.xlabel('x')
plt.ylabel('time')
plt.grid()
plt.show()


# In[ ]:




