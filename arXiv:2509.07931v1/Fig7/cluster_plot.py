from pyqcm.qcm_funcs import (
        ClusterBathVisualizer
)

# Create a 1x4 chain with 2 bath sites, all conceptual
visualizer = ClusterBathVisualizer((1, 4), 2, spacing=1, conceptual_baths=True)

visualizer.font_size = 12
visualizer.cluster_node_size = 0.1
visualizer.conceptual_bath_size = 0.1

visualizer.set_cluster_color(0, '#6B9BD1')
visualizer.set_cluster_color(1, '#E89B8B')

# Define connections in the cluster
cluster_connections = [(i, i + 1) for i in range(3)]
visualizer.set_cluster_connections(cluster_connections)

# Add links between cluster and bath sites
links = [(0, 0), (0, 1), (3, 0), (3, 1)]
visualizer.links = links

# Set the count of bath sites represented by each conceptual bath
visualizer.set_bath_count(0, 4)
visualizer.set_bath_count(1, 4)

visualizer.set_link_style(0, 0, color="#8BB68A", label=r"$\boldsymbol{\theta}^A$", style='dashed')
visualizer.set_link_style(0, 1, color="#B19CD9", label=r"$\boldsymbol{\theta}^{B}$", style='dashed')
visualizer.set_link_style(3, 0, color="#8BB68A", label=r"$\boldsymbol{\theta}^A$", style='dashed')
visualizer.set_link_style(3, 1, color="#B19CD9", label=r"$-\boldsymbol{\theta}^{B}$", style='dashed')

# Set custom bath colors
visualizer.set_bath_color(0, "#8BB68A")
visualizer.set_bath_color(1, "#B19CD9")
