"""Python script that generates Fig. 10 of arXiv:2509.07931v1, i.e.,
the local spectral functions for the 1x4-4b-4sb system along with
the comparison between the converged hybridization functions found
in the distance function d.
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
    latt_model, varias = model1D(
        4, 4, [[1, 1, 1, 1], [-1, -1, -1, -1], [1, 1, 1, 1], [-1, -1, -1, -1]]
    )

    # Specifying parameters
    latt_model.set_target_sectors(["R0:N8:S0"])

    basic_params = """
    U = 4
    t = 1
    mu = 2
    """

    bath_params1 = """
    eb1-g1_1 = 1,
    eb2-g1_1 = -1,
    eb3-g1_1 = 1,
    eb4-g1_1 = -1,
    tb1-g1_1 = 0.5,
    tb2-g1_1 = 0.5,
    tb3-g1_1 = 0.5,
    tb4-g1_1 = 0.5,
    """

    bath_params2 = """
    eb1-g2_1 = 1,
    eb2-g2_1 = -1,
    eb3-g2_1 = 1,
    eb4-g2_1 = -1,
    tb1-g2_1 = 0.5,
    tb2-g2_1 = 0.5,
    tb3-g2_1 = 0.5,
    tb4-g2_1 = 0.5,
    """

    bath_params3 = """
    eb1-g3_1 = 1,
    eb2-g3_1 = -1,
    eb3-g3_1 = 1,
    eb4-g3_1 = -1,
    tb1-g3_1 = 0.5,
    tb2-g3_1 = 0.5,
    tb3-g3_1 = 0.5,
    tb4-g3_1 = 0.5,
    """

    bath_params4 = """
    eb1-g4_1 = 1,
    eb2-g4_1 = -1,
    eb3-g4_1 = 1,
    eb4-g4_1 = -1,
    tb1-g4_1 = 0.5,
    tb2-g4_1 = 0.5,
    tb3-g4_1 = 0.5,
    tb4-g4_1 = 0.5,
    """

    latt_model.set_parameters(
        basic_params + bath_params1 + bath_params2 + bath_params3 + bath_params4
    )

    return latt_model, varias


def cdmft(
    model, varias, sub_baths_weights: list, session_id: str
) -> pyqcm.model_instance:
    solution = pyqcm.cdmft.CDMFT(
        model,
        varias,
        iteration="fixed_point",
        accur_bath=1e-6,
        accur_dist=1e-12,
        method="bobyqa",
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

        analyzer.plot_hybridization_spectrum(
            w_c=6,
            cluster=visualizer,
            site_indices=[0, 1],
            grid_spec_params={"width_ratios": [1.25, 0.75], "wspace": 0.0},
            legend_options={"frameon": True, "framealpha": 0.75, "loc": "upper right"},
            save="./output/spectra_hybz_1x4_4b_4sb.pdf",
        )
    else:
        pass

    return


if __name__ == "__main__":
    main(run_cdmft=True, sub_baths_weights=[1 / 4, 1 / 4, 1 / 4, 1 / 4])
