"""Python script that generates Fig. 11c of arXiv:2509.07931v1, i.e.,
the local spectral function and the converged hybridization functions
are compared with CT-HYB solution for the 2x2-8b-4sb system away from
half-filling.
"""

import pyqcm
import pyqcm.cdmft
from cluster_plot import visualizer
from clusters.cluster_1bande_8b import CM
from pyqcm.qcm_funcs import CDMFTAnalyzer

# Construction of the lattice model
clus = pyqcm.cluster(CM, [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0]])
model = pyqcm.lattice_model("2D-4s-8b-4sb", [clus], [[2, 0, 0], [0, 2, 0]])

# Defining Operators (interaction: U, hoppings: t)
model.interaction_operator("U")

model.hopping_operator("t", [1, 0, 0], -1)
model.hopping_operator("t", [0, 1, 0], -1)

# Setting parameters
model.set_target_sectors(["R0:N10:S0/R0:N11:S-1/R0:N11:S1/R0:N12:S0"])

basic_params = """
U = 8
t = 1
mu = 2
"""

bath_params1 = """
eb1-g1_1 = 1
eb2-g1_1 = -1
eb3-g1_1 = 1
eb4-g1_1 = -1
eb5-g1_1 = 1
eb6-g1_1 = -1
eb7-g1_1 = 1
eb8-g1_1 = -1
tb1-g1_1 = 0.5
tb2-g1_1 = 0.5
tb3-g1_1 = 0.5
tb4-g1_1 = 0.5
tb5-g1_1 = 0.5
tb6-g1_1 = 0.5
tb7-g1_1 = 0.5
tb8-g1_1 = 0.5
"""

bath_params2 = """
eb1-g2_1 = 1
eb2-g2_1 = -1
eb3-g2_1 = 1
eb4-g2_1 = -1
eb5-g2_1 = 1
eb6-g2_1 = -1
eb7-g2_1 = 1
eb8-g2_1 = -1
tb1-g2_1 = 0.5
tb2-g2_1 = 0.5
tb3-g2_1 = 0.5
tb4-g2_1 = 0.5
tb5-g2_1 = 0.5
tb6-g2_1 = 0.5
tb7-g2_1 = 0.5
tb8-g2_1 = 0.5
"""

bath_params3 = """
eb1-g3_1 = 1
eb2-g3_1 = -1
eb3-g3_1 = 1
eb4-g3_1 = -1
eb5-g3_1 = 1
eb6-g3_1 = -1
eb7-g3_1 = 1
eb8-g3_1 = -1
tb1-g3_1 = 0.5
tb2-g3_1 = 0.5
tb3-g3_1 = 0.5
tb4-g3_1 = 0.5
tb5-g3_1 = 0.5
tb6-g3_1 = 0.5
tb7-g3_1 = 0.5
tb8-g3_1 = 0.5
"""

bath_params4 = """
eb1-g4_1 = 1
eb2-g4_1 = -1
eb3-g4_1 = 1
eb4-g4_1 = -1
eb5-g4_1 = 1
eb6-g4_1 = -1
eb7-g4_1 = 1
eb8-g4_1 = -1
tb1-g4_1 = 0.5
tb2-g4_1 = 0.5
tb3-g4_1 = 0.5
tb4-g4_1 = 0.5
tb5-g4_1 = 0.5
tb6-g4_1 = 0.5
tb7-g4_1 = 0.5
tb8-g4_1 = 0.5
"""

model.set_parameters(
    basic_params + bath_params1 + bath_params2 + bath_params3 + bath_params4
)

varias = [
    [
        "eb1-g1_1",
        "eb2-g1_1",
        "eb3-g1_1",
        "eb4-g1_1",
        "eb5-g1_1",
        "eb6-g1_1",
        "eb7-g1_1",
        "eb8-g1_1",
        "tb1-g1_1",
        "tb2-g1_1",
        "tb3-g1_1",
        "tb4-g1_1",
        "tb5-g1_1",
        "tb6-g1_1",
        "tb7-g1_1",
        "tb8-g1_1",
    ],
    [
        "eb1-g2_1",
        "eb2-g2_1",
        "eb3-g2_1",
        "eb4-g2_1",
        "eb5-g2_1",
        "eb6-g2_1",
        "eb7-g2_1",
        "eb8-g2_1",
        "tb1-g2_1",
        "tb2-g2_1",
        "tb3-g2_1",
        "tb4-g2_1",
        "tb5-g2_1",
        "tb6-g2_1",
        "tb7-g2_1",
        "tb8-g2_1",
    ],
    [
        "eb1-g3_1",
        "eb2-g3_1",
        "eb3-g3_1",
        "eb4-g3_1",
        "eb5-g3_1",
        "eb6-g3_1",
        "eb7-g3_1",
        "eb8-g3_1",
        "tb1-g3_1",
        "tb2-g3_1",
        "tb3-g3_1",
        "tb4-g3_1",
        "tb5-g3_1",
        "tb6-g3_1",
        "tb7-g3_1",
        "tb8-g3_1",
    ],
    [
        "eb1-g4_1",
        "eb2-g4_1",
        "eb3-g4_1",
        "eb4-g4_1",
        "eb5-g4_1",
        "eb6-g4_1",
        "eb7-g4_1",
        "eb8-g4_1",
        "tb1-g4_1",
        "tb2-g4_1",
        "tb3-g4_1",
        "tb4-g4_1",
        "tb5-g4_1",
        "tb6-g4_1",
        "tb7-g4_1",
        "tb8-g4_1",
    ],
]


def perform_cdmft(
    model, varias, sub_baths_weights: list, session_id: str
) -> pyqcm.model_instance:
    sol = pyqcm.cdmft.CDMFT(
        model,
        varias,
        sub_baths_weights=sub_baths_weights,
        method="bobyqa",
        accur_bath=1e-6,
        accur_dist=1e-12,
        iteration="fixed_point",
        session_id=session_id,
    )
    return sol.I


def main() -> None:
    updated_instance = perform_cdmft(model, varias, [1 / 4 for _ in range(4)], None)
    analyzer = CDMFTAnalyzer(updated_instance)
    analyzer.plot_hybridization_spectrum(
        w_c=2,
        cluster=visualizer,
        site_indices=[0],
        grid_spec_params={
            "width_ratios": [1.2, 0.8],  # Make cluster subplot relatively larger
            "wspace": 0.05,  # Add more space between plots
        },
        legend_options={"frameon": True, "framealpha": 0.75, "loc": "center right"},
        cthyb_file="./CT_HYB.dat",
        save="./output/spectra_hybz_2x2_8b_4sb_doped.pdf",
    )
    return


if __name__ == "__main__":
    main()
