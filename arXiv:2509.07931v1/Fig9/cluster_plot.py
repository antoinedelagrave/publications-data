from pyqcm.qcm_funcs import ClusterBathVisualizer

n_sites, n_baths = 4, 4

# Create a 1x4 chain with 4 bath sites, all conceptual
visualizer = ClusterBathVisualizer(
    (1, n_sites), n_baths, spacing=1, conceptual_baths=True
)

visualizer.font_size = 12
visualizer.cluster_node_size = 0.1
visualizer.conceptual_bath_size = 0.15

visualizer.set_cluster_color(0, "#6B9BD1")
visualizer.set_cluster_color(1, "#E89B8B")

# Define connections in the cluster
cluster_connections = [(i, i + 1) for i in range(n_sites)]
visualizer.set_cluster_connections(cluster_connections)

# Add links between cluster and bath sites
links = [(0, 0), (0, 1), (0, 2), (0, 3), (3, 0), (3, 1), (3, 2), (3, 3)]

visualizer.links = links

# Set the count of bath sites represented by each conceptual bath
visualizer.set_bath_count(0, 4)
visualizer.set_bath_count(1, 4)
visualizer.set_bath_count(2, 4)
visualizer.set_bath_count(3, 4)

visualizer.set_link_style(
    0, 0, color="#8BB68A", label=r"$\boldsymbol{\theta}^A$", style="dashed"
)
visualizer.set_link_style(
    0, 1, color="#B19CD9", label=r"$\boldsymbol{\tilde{\theta}}^A$", style="dashed"
)
visualizer.set_link_style(
    0, 2, color="#E6D08A", label=r"$\boldsymbol{\theta}^B$", style="dashed"
)
visualizer.set_link_style(
    0, 3, color="#D4A5A5", label=r"$\boldsymbol{\tilde{\theta}}^B$", style="dashed"
)

visualizer.set_link_style(
    3, 0, color="#8BB68A", label=r"$\boldsymbol{\theta}^A$", style="dashed"
)
visualizer.set_link_style(
    3, 1, color="#B19CD9", label=r"$\boldsymbol{\tilde{\theta}}^A$", style="dashed"
)
visualizer.set_link_style(
    3, 2, color="#E6D08A", label=r"$-\boldsymbol{\theta}^B$", style="dashed"
)
visualizer.set_link_style(
    3, 3, color="#D4A5A5", label=r"$-\boldsymbol{\tilde{\theta}}^B$", style="dashed"
)

# Set custom bath colors
visualizer.set_bath_color(0, "#8BB68A")
visualizer.set_bath_color(1, "#B19CD9")
visualizer.set_bath_color(2, "#E6D08A")
visualizer.set_bath_color(3, "#D4A5A5")
