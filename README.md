Code for running the Weather Research & Forecasting Model (WRF) model.

wrf_settings.py contains code to specify WRF model settings and data locations for specific test cases.
make_namelist.py contains code to generate the namelist for the specfic model run.
run_fwd_.ipynb is driver code used to do a forward WRF run of the specified experiment.
run_trj_adj_merge_tlm.ipynb is driver code used to do a trajectory, adjoint, and tanglent linear model run of the specified experiment.
run_fwdopt.ipynb is driver code to do a foreward WRF run with opitmal pertubations of the specified experiment.
