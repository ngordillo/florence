This repository contains scripts to run the Weather Research & Forecasting Model (WRF) model in order to do optimal perturbation analysis for a specified test case. These scripts provide a workflow for a forward, adjoint, and tangent linear run through the WRF model using the user-defined parameters set in wrf_settings and make_namelist.py. This workflow can repeated by running the forward model using the found optimal perturbations. 

Description of scripts: 
* wrf_settings.py contains code to specify WRF model settings and data locations for specific test cases.
* make_namelist.py contains code to generate the namelist for the specific model run.
* run_fwd_.ipynb is driver code used to do a forward WRF run of the specified experiment.
* run_trj_adj_merge_tlm.ipynb is driver code used to do a trajectory, adjoint, and tangent linear model run of the specified experiment.
* run_fwdopt.ipynb is driver code to do a forward WRF run with optimal perturbations of the specified experiment.
