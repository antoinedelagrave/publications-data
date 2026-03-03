"""Python script that generates Fig. 6 of arXiv:2509.07931v1, i.e.,
the 1-WD comparison between the 1x4-8b-1sb and 1x4-2b-4sb systems.
"""

import pyqcm
import pyqcm.cdmft
from cluster_plot import visualizer
from pyqcm.qcm_funcs import (
    CDMFTAnalyzer,
    model1D,
)


def setup_model() -> tuple[pyqcm.lattice_model, list]:
    """Creates the lattice model and sets the parameters."""
    # Instanciating model
    latt_model, varias = model1D(4, 2, [[1, 1], [-1, -1], [1, 1], [-1, -1]])

    # Specifying parameters
    latt_model.set_target_sectors(["R0:N6:S0"])

    basic_params = """
    U = 4
    t = 1
    mu = 2
    """

    bath_params1 = """
    eb1-g1_1 = 1,
    eb2-g1_1 = -1,
    tb1-g1_1 = 1,
    tb2-g1_1 = 1,
    """

    bath_params2 = """
    eb1-g2_1 = 1,
    eb2-g2_1 = -1,
    tb1-g2_1 = 1,
    tb2-g2_1 = 1,
    """

    bath_params3 = """
    eb1-g3_1 = 1,
    eb2-g3_1 = -1,
    tb1-g3_1 = 1,
    tb2-g3_1 = 1,
    """

    bath_params4 = """
    eb1-g4_1 = 1,
    eb2-g4_1 = -1,
    tb1-g4_1 = 1,
    tb2-g4_1 = 1,
    """

    latt_model.set_parameters(
        basic_params + bath_params1 + bath_params2 + bath_params3 + bath_params4
    )

    return latt_model, varias


def cdmft(model, varias, sub_baths_weights: list) -> pyqcm.model_instance:
    solution = pyqcm.cdmft.CDMFT(
        model,
        varias,
        accur_bath=1e-6,
        accur_dist=1e-12,
        method="bobyqa",
        iteration="fixed_point",
        sub_baths_weights=sub_baths_weights,
    )
    return solution.I


def main(run_cdmft: bool = False, sub_baths_weights: list = []) -> None:
    latt_model, varias = setup_model()
    if run_cdmft:
        updated_instance = cdmft(latt_model, varias, sub_baths_weights)
        analyzer = CDMFTAnalyzer(updated_instance)

        analyzer.compare_spectral_functions(
            spectrum_files="./spectrum_1x4_8b_1sb.json",
            only_independent=True,
            save="./output/1x4_8b_1sb_vs_1x4_2b_4sb.pdf",
            legend_options={
                "position": "upper left",
                "ncol": 1,
                "fontsize": 12,
                "frameon": True,
                "edgecolor": "black",
                "show_model_legend": True,
                "custom_labels": [
                    r"$N_{\mathrm{b}}=8$, $N_{\mathrm{sb}}=4$",
                    r"$N_{\mathrm{b}}=8$, $N_{\mathrm{sb}}=1$",
                ],
            },
            cluster=visualizer,
            cluster_pos=(0.5, 0.025, 0.5, 0.5),
        )
    else:
        pass

    return


if __name__ == "__main__":
    main(run_cdmft=True, sub_baths_weights=[1 / 4 for _ in range(4)])
