import pytest
import numpy as np

import nengo
import nengo.utils.ensemble


def test_tuning_curve(Simulator):
    model = nengo.Network()
    with model:
        a = nengo.Ensemble(n_neurons=100, dimensions=1)

    sim = Simulator(model)

    pts, act = nengo.utils.ensemble.tuning_curves(a, sim)


if __name__ == "__main__":
    nengo.log(debug=True)
    pytest.main([__file__, '-v'])
