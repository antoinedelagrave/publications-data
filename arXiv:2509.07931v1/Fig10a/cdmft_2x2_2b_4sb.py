"""Python script that generates Fig. 10a of arXiv:2509.07931v1, i.e.,
the 1-WD comparison between the 2x2-8b-1sb and 2x2-2b-4sb systems along
with the converged hybridization functions compared with CT-HYB solution,
all at half-filling.
"""

import pyqcm
import pyqcm.cdmft
from cluster_plot import visualizer
from clusters.cluster_1bande_8b import CM
from pyqcm.qcm_funcs import CDMFTAnalyzer

# Construction of the lattice model
clus = pyqcm.cluster(CM, [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0]])
model = pyqcm.lattice_model("2x2-2b-4sb", [clus], [[2, 0, 0], [0, 2, 0]])

# Defining Operators (interaction: U, hoppings: t)
model.interaction_operator("U")

model.hopping_operator("t", [1, 0, 0], -1)
model.hopping_operator("t", [0, 1, 0], -1)

# Setting parameters
model.set_target_sectors(["R0:N6:S0"])

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

model.set_parameters(
    basic_params + bath_params1 + bath_params2 + bath_params3 + bath_params4
)

varias = [
    ["eb1-g1_1", "eb2-g1_1", "tb1-g1_1", "tb2-g1_1"],
    ["eb1-g2_1", "eb2-g2_1", "tb1-g2_1", "tb2-g2_1"],
    ["eb1-g3_1", "eb2-g3_1", "tb1-g3_1", "tb2-g3_1"],
    ["eb1-g4_1", "eb2-g4_1", "tb1-g4_1", "tb2-g4_1"],
]


def cdmft(
    model, varias, sub_baths_weights: list, session_id: str
) -> pyqcm.model_instance:
    sol = pyqcm.cdmft.CDMFT(
        model,
        varias,
        accur_bath=1e-6,
        accur_dist=1e-12,
        iteration="fixed_point",
        method="bobyqa",
        sub_baths_weights=sub_baths_weights,
        session_id=session_id,
    )
    return sol.I


def main() -> None:
    updated_instance = cdmft(model, varias, [1 / 4 for _ in range(4)], "")
    analyzer = CDMFTAnalyzer(updated_instance)

    analyzer.plot_hybridization_spectrum(
        w_c=2,
        cluster=visualizer,
        site_indices=[0],
        grid_spec_params={
            "width_ratios": [1.2, 0.8],  # Make cluster subplot relatively larger
            "wspace": 0.0,  # Add more space between plots
        },
        legend_options={"frameon": True, "framealpha": 0.75, "loc": "lower right"},
        cthyb_file="./CT_HYB.dat",
        spectrum_file="./half_filled_spectrum.json",
        save="./output/spectra_hybz_2x2_2b_4sb_half_filling.pdf",
    )

    return


if __name__ == "__main__":
    main()
