"""Python script that generates Fig. 8 of arXiv:2509.07931v1, i.e.,
the 1-WD comparison between the 1x2-8b-1sb and 1x2-4b-2sb systems. Important
detail: here the two cluster sites have distinct Hubbard U interaction
amplitudes which leads to breaking C_2 mirror symmetry.
"""

import pyqcm
import pyqcm.cdmft
from cluster_plot import visualizer
from pyqcm.qcm_funcs import CDMFTAnalyzer, model1D

# -------------------
# Instanciating model
# -------------------


def setup_model() -> tuple[pyqcm.lattice_model, list]:
    """Creates the lattice model and sets the parameters."""
    # Instanciating model
    latt_model, varias = model1D(2, 4, [[1, 1, 1, 1], [1, 1, 1, 1]], n_bands=2)

    # Specifying parameters
    latt_model.set_target_sectors(["R0:N4:S0/R0:N6:S0/R0:N8:S0"])

    basic_params = """
    U1 = 8
    U2 = 1
    t11 = 1
    t12 = 1
    t22 = 1
    mu = 1
    """

    bath_params1 = """
    eb1-g1_1 = 1,
    eb2-g1_1 = -1,
    eb3-g1_1 = 1,
    eb4-g1_1 = -1,
    tb1-g1_1 = 1,
    tb2-g1_1 = 1,
    tb3-g1_1 = 1,
    tb4-g1_1 = 1,
    tb5-g1_1 = 1,
    tb6-g1_1 = 1,
    tb7-g1_1 = 1,
    tb8-g1_1 = 1,
    """

    bath_params2 = """
    eb1-g2_1 = 1,
    eb2-g2_1 = -1,
    eb3-g2_1 = 1,
    eb4-g2_1 = -1,
    tb1-g2_1 = 1,
    tb2-g2_1 = 1,
    tb3-g2_1 = 1,
    tb4-g2_1 = 1,
    tb5-g2_1 = 1,
    tb6-g2_1 = 1,
    tb7-g2_1 = 1,
    tb8-g2_1 = 1,
    """

    latt_model.set_parameters(basic_params + bath_params1 + bath_params2)

    return latt_model, varias


def cdmft(
    model, varias, sub_baths_weights: list, session_id: str
) -> pyqcm.model_instance:
    solution = pyqcm.cdmft.CDMFT(
        model,
        varias,
        accur_bath=1e-8,
        accur_dist=1e-12,
        method="bobyqa",
        iteration="fixed_point",
        sub_baths_weights=sub_baths_weights,
        session_id=session_id,
    )
    return solution.I


def main(
    run_cdmft: bool = False, sub_baths_weights: list = [], session_id: str = ""
) -> None:
    latt_model, varias = setup_model()
    if run_cdmft:
        updated_instance = cdmft(latt_model, varias, sub_baths_weights, session_id)
        analyzer = CDMFTAnalyzer(updated_instance)
        analyzer.compare_spectral_functions(
            w_range=(-6, 10),
            spectrum_files="./spectrum_1x2_8b_1sb_2orbs.json",
            only_independent=True,
            save="./output/1x2_8b_1sb_2orbs_vs_1x2_4b_2sb_2orbs.pdf",
            legend_options={
                "position": "upper right",
                "ncol": 1,
                "fontsize": 12,
                "frameon": True,
                "edgecolor": "black",
                "show_model_legend": True,
                "custom_labels": [
                    r"$N_{\mathrm{b}}=8$, $N_{\mathrm{sb}}=2$",
                    r"$N_{\mathrm{b}}=8$, $N_{\mathrm{sb}}=1$",
                ],
                "include_models": None,
            },
            cluster=visualizer,
            cluster_pos=(0.575, 0.015, 0.4, 0.4),
        )
    else:
        pass

    return


if __name__ == "__main__":
    main(run_cdmft=True, sub_baths_weights=[1 / 2, 1 / 2])
