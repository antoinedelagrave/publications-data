"""Python script that generates Fig. 11 of arXiv:2509.07931v1, i.e.,
the local spectral functions for the 2x2-4b-4sb system along with
the comparison between the converged hybridization functions found
in the distance function d.
"""

import pyqcm
import pyqcm.cdmft

from clusters.cluster_1bande_8b import CM
from pyqcm.qcm_funcs import (
    CDMFTAnalyzer
)

from cluster_plot import visualizer


# Construction of the lattice model
clus = pyqcm.cluster(
    CM,
    [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [1, 1, 0]
    ])
model = pyqcm.lattice_model(
    "2D-4s-4b-4sb",
    [clus],
    [
        [2, 0, 0],
        [0, 2, 0]
    ])

# Defining Operators (interaction: U, hoppings: t)
model.interaction_operator("U")

model.hopping_operator("t",[1, 0, 0], -1)
model.hopping_operator("t",[0, 1, 0], -1)

# Setting parameters
model.set_target_sectors(['R0:N8:S0'])

basic_params = """
U = 8
t = 1
mu = 4
"""

bath_params1 = """
eb1-g1_1 = 1
eb2-g1_1 = -1
eb3-g1_1 = 1
eb4-g1_1 = -1
tb1-g1_1 = 1
tb2-g1_1 = 1
tb3-g1_1 = 1
tb4-g1_1 = 1
"""

bath_params2 = """
eb1-g2_1 = 1
eb2-g2_1 = -1
eb3-g2_1 = 1
eb4-g2_1 = -1
tb1-g2_1 = 1
tb2-g2_1 = 1
tb3-g2_1 = 1
tb4-g2_1 = 1
"""

bath_params3 = """
eb1-g3_1 = 1
eb2-g3_1 = -1
eb3-g3_1 = 1
eb4-g3_1 = -1
tb1-g3_1 = 1
tb2-g3_1 = 1
tb3-g3_1 = 1
tb4-g3_1 = 1
"""

bath_params4 = """
eb1-g4_1 = 1
eb2-g4_1 = -1
eb3-g4_1 = 1
eb4-g4_1 = -1
tb1-g4_1 = 1
tb2-g4_1 = 1
tb3-g4_1 = 1
tb4-g4_1 = 1
"""

model.set_parameters(basic_params + bath_params1 + bath_params2 + bath_params3 + bath_params4)

varias = [
    ['eb1-g1_1', 'eb2-g1_1', 'eb3-g1_1', 'eb4-g1_1',
    'tb1-g1_1', 'tb2-g1_1', 'tb3-g1_1', 'tb4-g1_1'],
    ['eb1-g2_1', 'eb2-g2_1', 'eb3-g2_1', 'eb4-g2_1',
    'tb1-g2_1', 'tb2-g2_1', 'tb3-g2_1', 'tb4-g2_1'],
    ['eb1-g3_1', 'eb2-g3_1', 'eb3-g3_1', 'eb4-g3_1',
    'tb1-g3_1', 'tb2-g3_1', 'tb3-g3_1', 'tb4-g3_1'],
    ['eb1-g4_1', 'eb2-g4_1', 'eb3-g4_1', 'eb4-g4_1',
    'tb1-g4_1', 'tb2-g4_1', 'tb3-g4_1', 'tb4-g4_1']
]


def cdmft(model, varias, sub_baths_weights: list, session_id: str) -> pyqcm.model_instance:
    sol = pyqcm.cdmft.CDMFT(
                            model,
                            varias,
                            sub_baths_weights=sub_baths_weights,
                            method='bobyqa',
                            accur_bath=1e-8,
                            accur_dist=1e-10,
                            wc=4,
                            iteration='fixed_point',
                            session_id=session_id
    )
    return sol.I


def main() -> None:
    updated_instance = cdmft(model, varias, [1/4 for _ in range(4)], '')
    analyzer = CDMFTAnalyzer(updated_instance)

    analyzer.plot_hybridization_spectrum(w_c=6,
        cluster=visualizer,
        site_indices=[0],
        grid_spec_params={
            'width_ratios': [1.2, 0.8],
            'wspace': 0.0
        },
        legend_options = {
            'frameon': True,
            'framealpha': 0.75,
            'loc': 'center right'
        },
        save='./output/spectra_hybz_2x2-4b-4sb.pdf')
    return


if __name__ == "__main__":
    main()
