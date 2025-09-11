from pyqcm.qcm_funcs import (
        ClusterBathVisualizer
)

n_sites, n_baths = 2, 2

# Create a 1x4 chain with 2 bath sites, all conceptual
visualizer = ClusterBathVisualizer((1, n_sites), n_baths, spacing=1, conceptual_baths=True)

# Modify sizes directly
visualizer.conceptual_bath_size = 0.1
visualizer.font_size = 12

visualizer.set_cluster_color(0, '#6B9BD1')
visualizer.set_cluster_color(1, '#E89B8B')

# Define connections in the cluster
cluster_connections = [(i, i + 1) for i in range(n_sites)]
visualizer.set_cluster_connections(cluster_connections)

# Add links between cluster and bath sites
links = [(0, 0), (0, 1), (1, 0), (1, 1)]
visualizer.links = links

# Set the count of bath sites represented by each conceptual bath
visualizer.set_bath_count(0, 4)
visualizer.set_bath_count(1, 4)

visualizer.set_link_style(0, 0, color="#8BB68A", label=r"$\boldsymbol{\theta}^{1}$", style='dashed')
visualizer.set_link_style(0, 1, color="#B19CD9", label=r"$\boldsymbol{\theta}^{2}$", style='dashed')
visualizer.set_link_style(1, 0, color="#8BB68A", label=r"$\boldsymbol{\tilde{\theta}}^{1}$", style='dashed')
visualizer.set_link_style(1, 1, color="#B19CD9", label=r"$\boldsymbol{\tilde{\theta}}^{2}$", style='dashed')

# Set custom bath colors
visualizer.set_bath_color(0, "#8BB68A")
visualizer.set_bath_color(1, "#B19CD9")
