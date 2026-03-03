import pyqcm

ns, nb = 4, 2
no = ns + nb
CM = pyqcm.cluster_model(ns, nb)


# Creating bath energies
def new_eb(x, sb_name) -> None:
    for i in range(1, nb + 1):
        lab = i + ns
        CM.new_operator(
            f"eb{i}-{sb_name}", "one-body", [(lab, lab, 1.0), (lab + no, lab + no, 1.0)]
        )
    return


new_eb(1, "g1")
new_eb(2, "g1")

new_eb(1, "g2")
new_eb(2, "g2")

new_eb(1, "g3")
new_eb(2, "g3")

new_eb(1, "g4")
new_eb(2, "g4")


def new_tb(x, seq, sb_name) -> None:
    elem = []
    for i in range(ns):
        elem.append((i + 1, x + ns, seq[i]))
    for i in range(ns):
        elem.append((i + no + 1, x + no + ns, seq[i]))
    CM.new_operator(f"tb{x}-{sb_name}", "one-body", elem)
    return


new_tb(1, [1, 1, 1, 1], "g1")
new_tb(2, [1, 1, 1, 1], "g1")

new_tb(1, [1, 1, -1, -1], "g2")
new_tb(2, [1, 1, -1, -1], "g2")

new_tb(1, [1, -1, 1, -1], "g3")
new_tb(2, [1, -1, 1, -1], "g3")

new_tb(1, [1, -1, -1, 1], "g4")
new_tb(2, [1, -1, -1, 1], "g4")
