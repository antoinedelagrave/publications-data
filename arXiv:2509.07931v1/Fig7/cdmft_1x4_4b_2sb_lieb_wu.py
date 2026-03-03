"""Python script that generates Fig. 7 of arXiv:2509.07931v1, i.e.,
local density curves for the 1x4-8b-1sb, 1x4-4b-2sb systems and the
exact solution from Lieb & Wu. We also compare local spectral functions
for densities framing the Mott transition.
"""

import pyqcm
import pyqcm.cdmft
from cluster_plot import visualizer
from pyqcm.qcm_funcs import CDMFTAnalyzer, model1D


def setup_model() -> tuple[pyqcm.lattice_model, list]:
    """Creates the lattice model and sets the parameters."""
    # Instanciating model
    latt_model, varias = model1D(4, 4, [[1, 1, 1, 1], [-1, -1, -1, -1]])

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
    tb1-g1_1 = 1,
    tb2-g1_1 = 1,
    tb3-g1_1 = 1,
    tb4-g1_1 = 1,
    """

    bath_params2 = """
    eb1-g2_1 = -1,
    eb2-g2_1 = 1,
    eb3-g2_1 = -1,
    eb4-g2_1 = 1,
    tb1-g2_1 = 1,
    tb2-g2_1 = 1,
    tb3-g2_1 = 1,
    tb4-g2_1 = 1,
    """

    latt_model.set_parameters(basic_params + bath_params1 + bath_params2)

    return latt_model, varias


def cdmft(
    model, varias, sub_baths_weights: list, session_id: str
) -> pyqcm.model_instance:
    solution = pyqcm.cdmft.CDMFT(
        model,
        varias,
        accur_bath=1e-6,
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
        try:
            updated_instance = cdmft(latt_model, varias, sub_baths_weights, session_id)
            analyzer = CDMFTAnalyzer(updated_instance)

            analyzer.plot_density_and_spectrum(
                mu_files=[
                    "./Densities/exact_lieb_wu.tsv",
                    "./Densities/mu_sweep_1x4_4b_2sb.tsv",
                    "./Densities/mu_sweep_1x4_8b_1sb.tsv",
                ],
                spectrum_files=[
                    # Files for sub-baths simulation (half-filled, pre-Mott, post-Mott)
                    "./Spectra/SB-CDMFT/mu=2.json",
                    "./Spectra/SB-CDMFT/mu=1.408.json",
                    "./Spectra/SB-CDMFT/mu=1.286.json",
                    # Files for benchmark simulation (half-filled, pre-Mott, post-Mott)
                    "./Spectra/CDMFT/mu=2.json",
                    "./Spectra/CDMFT/mu=1.408.json",
                    "./Spectra/CDMFT/mu=1.286.json",
                ],
                sites=[0, 1],
                cluster=visualizer,
                cluster_pos=(0.75, -0.65, 0.2, 0.7),
                marker_points=[(2, 1.0000), (1.418, 1.0000), (1.286, 0.9458)],
                labels=[
                    "Lieb-Wu",
                    r"$N_{\mathrm{b}}=8$, $N_{\mathrm{sb}}=2$",
                    r"$N_{\mathrm{b}}=8$, $N_{\mathrm{sb}}=1$",
                ],
                save="./output/lieb_wu.pdf",
            )
        except Exception as e:
            print(f"Error occurred during CDMFT simulation: {e}")
    else:
        pass

    return


if __name__ == "__main__":
    main(run_cdmft=True, sub_baths_weights=[1 / 2, 1 / 2])
