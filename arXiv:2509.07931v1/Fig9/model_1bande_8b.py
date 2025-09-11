"""Python script that generates Fig. 9 of arXiv:2509.07931v1, i.e.,
the KS comparison between the 2x2-8b-1sb and 2x2-2b-4sb systems.
"""

import pyqcm
import pyqcm.cdmft

from pyqcm.qcm_funcs import (
    CDMFTAnalyzer
)

from clusters.cluster_1bande_8b import CM
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
    "2x2-2b-4sb",
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
model.set_target_sectors(['R0:N6:S0'])

basic_params = """
U = 8
t = 1
mu = 4
"""

bath_params1 = """
eb1-g1_1 = 1
eb2-g1_1 = -1
tb1-g1_1 = 1
tb2-g1_1 = 1
"""

bath_params2 = """
eb1-g2_1 = 1
eb2-g2_1 = -1
tb1-g2_1 = 1
tb2-g2_1 = 1
"""

bath_params3 = """
eb1-g3_1 = 1
eb2-g3_1 = -1
tb1-g3_1 = 1
tb2-g3_1 = 1
"""

bath_params4 = """
eb1-g4_1 = 1
eb2-g4_1 = -1
tb1-g4_1 = 1
tb2-g4_1 = 1
"""

model.set_parameters(basic_params + bath_params1 + bath_params2 + bath_params3 + bath_params4)

varias = [
    ['eb1-g1_1', 'eb2-g1_1', 'tb1-g1_1', 'tb2-g1_1'],
    ['eb1-g2_1', 'eb2-g2_1', 'tb1-g2_1', 'tb2-g2_1'],
    ['eb1-g3_1', 'eb2-g3_1', 'tb1-g3_1', 'tb2-g3_1'],
    ['eb1-g4_1', 'eb2-g4_1', 'tb1-g4_1', 'tb2-g4_1']
]


def cdmft(model, varias, sub_baths_weights: list, session_id: str) -> pyqcm.model_instance:
    sol = pyqcm.cdmft.CDMFT(
                            model,
                            varias,
                            accur_bath=1e-8,
                            accur_dist=1e-12,
                            iteration='fixed_point',
                            method='bobyqa',
                            sub_baths_weights=sub_baths_weights,
                            session_id=session_id
    )
    return sol.I


def main() -> None:
    updated_instance = cdmft(model, varias, [1/4 for _ in range(4)], '')
    analyzer = CDMFTAnalyzer(updated_instance)

    analyzer.compare_spectral_functions(
        spectrum_files='./spectrum_2x2-8b-1sb.json',
        only_independent=True,
        save='./output/2x2-8b-1sb_vs_2x2-2b-4sb.pdf',
        legend_options={
            'position': 'upper left',
            'ncol': 1,
            'fontsize': 12,
            'frameon': True,
            'edgecolor': 'black',
            'show_model_legend': True,
            'custom_labels': [r'$N_{\mathrm{b}}=8$, $N_{\mathrm{sb}}=4$', r'$N_{\mathrm{b}}=8$, $N_{\mathrm{sb}}=1$']
        },
        cluster=visualizer,
        cluster_pos=(0.515, 0.02, 0.45, 0.45)
    )

    return


if __name__ == "__main__":
    main()
