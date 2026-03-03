from pyqcm.qcm_funcs import ClusterBathVisualizer

# Test 3: All conceptual baths with more bath sites
visualizer = ClusterBathVisualizer((2, 2), 4, spacing=1, conceptual_baths=True)
visualizer.set_cluster_connections([(0, 1), (1, 3), (3, 2), (2, 0)])

visualizer.link_width = 1
visualizer.font_size = 10
visualizer.cluster_node_size = 0.1
visualizer.conceptual_bath_size = 0.1
visualizer.set_cluster_color(2, "#6B9BD1")

# Connect each cluster site to 8 bath sites
links = [
    (0, 0),
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 0),
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 0),
    (2, 1),
    (2, 2),
    (2, 3),
    (3, 0),
    (3, 1),
    (3, 2),
    (3, 3),
]
visualizer.links = links

# Links style
visualizer.set_link_style(
    0,
    0,
    curve_amount=-0.1,
    color="#8BB68A",
    label=r"$\boldsymbol{\theta}^{A_1}$",
    style="dashed",
    label_position=0.35,
)
visualizer.set_link_style(
    1,
    0,
    curve_amount=-0.75,
    color="#8BB68A",
    label=r"$\boldsymbol{\theta}^{A_1}$",
    style="dashed",
)
visualizer.set_link_style(
    2,
    0,
    curve_amount=0.75,
    color="#8BB68A",
    label=r"$\boldsymbol{\theta}^{A_1}$",
    style="dashed",
)
visualizer.set_link_style(
    3,
    0,
    curve_amount=0.75,
    color="#8BB68A",
    label=r"$\boldsymbol{\theta}^{A_1}$",
    style="dashed",
    label_position=0.66,
)

visualizer.set_link_style(
    0,
    1,
    curve_amount=0.9,
    color="#B19CD9",
    label=r"$-\boldsymbol{\theta}^{B_1}$",
    style="dashed",
)
visualizer.set_link_style(
    1,
    1,
    curve_amount=-0.1,
    color="#B19CD9",
    label=r"$\boldsymbol{\theta}^{B_1}$",
    style="dashed",
    label_position=0.35,
)
visualizer.set_link_style(
    2,
    1,
    curve_amount=0.75,
    color="#B19CD9",
    label=r"$\boldsymbol{\theta}^{B_1}$",
    style="dashed",
    label_position=0.66,
)
visualizer.set_link_style(
    3,
    1,
    curve_amount=-0.75,
    color="#B19CD9",
    label=r"$-\boldsymbol{\theta}^{B_1}$",
    style="dashed",
)

visualizer.set_link_style(
    0,
    2,
    curve_amount=0.75,
    color="#E6D08A",
    label=r"$\boldsymbol{\theta}^{B_2}$",
    style="dashed",
    label_position=0.66,
)
visualizer.set_link_style(
    1,
    2,
    curve_amount=0.9,
    color="#E6D08A",
    label=r"$-\boldsymbol{\theta}^{B_2}$",
    style="dashed",
    label_position=0.45,
)
visualizer.set_link_style(
    2,
    2,
    curve_amount=-0.75,
    color="#E6D08A",
    label=r"$\boldsymbol{\theta}^{B_2}$",
    style="dashed",
    label_position=0.6,
)
visualizer.set_link_style(
    3,
    2,
    curve_amount=-0.1,
    color="#E6D08A",
    label=r"$-\boldsymbol{\theta}^{B_2}$",
    style="dashed",
)

visualizer.set_link_style(
    0,
    3,
    curve_amount=-0.75,
    color="#D4A5A5",
    label=r"$-\boldsymbol{\theta}^{A_2}$",
    style="dashed",
)
visualizer.set_link_style(
    1,
    3,
    curve_amount=0.75,
    color="#D4A5A5",
    label=r"$\boldsymbol{\theta}^{A_2}$",
    style="dashed",
    label_position=0.66,
)
visualizer.set_link_style(
    2,
    3,
    curve_amount=-0.1,
    color="#D4A5A5",
    label=r"$\boldsymbol{\theta}^{A_2}$",
    style="dashed",
    label_position=0.35,
)
visualizer.set_link_style(
    3,
    3,
    curve_amount=0.9,
    color="#D4A5A5",
    label=r"$-\boldsymbol{\theta}^{A_2}$",
    style="dashed",
)

visualizer.set_bath_color(0, "#8BB68A")
visualizer.set_bath_color(1, "#B19CD9")
visualizer.set_bath_color(2, "#E6D08A")
visualizer.set_bath_color(3, "#D4A5A5")


for i in range(4):
    visualizer.set_bath_count(i, 8)
