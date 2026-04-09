import datetime

def generate_namelist(run_hours = 0, start_year=None, start_month=None, start_day=None, start_hour=None, end_year=None, end_month=None, end_day=None, end_hour=None, interval_seconds=None, time_step=None, e_we = None, e_sn = None, dx = None, dy = None, wrf_dir=None, exp_name=None, run_type=None):
    # print("--- Namelist Generator ---")
    # Get user input

    if run_type == "trj":
        # Note: auxhist6_end_h is also set to run_hours to match the original file's logic.
        namelist_content = """&time_control
        run_hours=""" + str(run_hours) + """,
        start_year=""" + str(start_year) + """,
        start_month=""" + str(start_month) + """,
        start_day=""" + str(start_day) + """,
        start_hour=""" + str(start_hour) + """,
        end_year=""" + str(end_year) + """,
        end_month=""" + str(end_month) + """,
        end_day=""" + str(end_day) + """,
        end_hour=""" + str(end_hour) + """,
        interval_seconds=""" + str(interval_seconds) + """,
        input_from_file=true,
        debug_level=0,
        frames_per_auxhist2=1,
        io_form_auxhist6=2,
        auxhist6_interval_s=60,
        auxhist6_begin_h=0,
        auxhist6_end_h=""" + str(run_hours) + """,
        auxhist6_outname="./auxhist6_d<domain>_<date>",
        frames_per_auxhist6=1,  
        history_interval=60,
        frames_per_outfile=1,
        inputout_interval=60,
        inputout_begin_h=0,
        inputout_end_h=36,
        iofields_filename="./plus.io_config"
        ignore_iofields_warning=true,
        write_input=false,
        /
        &fdda
        /
        &domains
        time_step=""" + str(time_step) + """,
        e_we=""" + str(e_we) + """,
        e_sn=""" + str(e_sn) + """,
        e_vert=41,
        num_metgrid_levels=27,
        num_metgrid_soil_levels=4,
        dx=""" + str(dx) + """,
        dy=""" + str(dy) + """,
        i_parent_start=0,
        j_parent_start=0,
        smooth_option=0,
        grid_id=1,
        parent_id=0,
        parent_grid_ratio=1,
        parent_time_step_ratio=1,
        feedback=0,	
        force_sfc_in_vinterp=1,
        p_top_requested=5000,
        interp_type=2,
        hypsometric_opt                     = 2,
        /
        &dfi_control
        /
        &physics
        mp_physics=    7,
        ra_lw_physics= 1,
        ra_sw_physics= 2,
        radt=         15,
        sf_sfclay_physics=1,
        sf_surface_physics=2,
        bl_pbl_physics=1,
        cu_physics=    1,
        cudt=          0,
        isfflx=1,
        ifsnow=1,
        icloud=1,
        surface_input_source=3,
        num_soil_layers=4,
        num_land_cat=21
        mp_zero_out=0,
        mp_zero_out_thresh=1.e-8,
        /
        &dynamics
        dyn_opt = 2,
        w_damping=1,
        diff_opt=1,
        km_opt=4,
        damp_opt=3
        dampcoef=0.2,
        base_temp=290.0,
        gwd_opt=1,
        iso_temp=200.,
        use_theta_m=0,
        /
        &bdy_control
        spec_bdy_width=5,
        spec_zone=1,
        relax_zone=4,
        specified=true,
        nested=.false.,
        /
        &grib2
        /
        &namelist_quilt
        /
        &perturbation
        trajectory_io=.false.,
        /"""

        # Write out to the file
        with open(wrf_dir + "exp_files/" + exp_name + "/namelists/namelist.input.trj." + exp_name, "w") as f:
            f.write(namelist_content)
        
        print(f"\nSuccess! 'namelist.input.trj.{exp_name}' has been generated.")
    elif run_type == "adj":
        namelist_content = """&time_control
        run_hours=""" + str(run_hours) + """,
        start_year=""" + str(start_year) + """,
        start_month=""" + str(start_month) + """,
        start_day=""" + str(start_day) + """,
        start_hour=""" + str(start_hour) + """,
        end_year=""" + str(end_year) + """,
        end_month=""" + str(end_month) + """,
        end_day=""" + str(end_day) + """,
        end_hour=""" + str(end_hour) + """,
        interval_seconds=""" + str(interval_seconds) + """,
        input_from_file=true,
        debug_level=0,
        auxhist7_outname="./adjout_d<domain>_<date>",
        auxhist7_interval_h=1,
        io_form_auxhist7=2,

        frames_per_auxhist7=1,
        auxinput6_inname="./auxhist6_d<domain>_<date>",
        auxinput6_interval_s=60,
        io_form_auxinput6=2,
        frames_per_auxinput6=1,
        auxinput7_inname="./wrfout_d<domain>_<date>",
        auxinput7_interval_s=3600,
        io_form_auxinput7=2,
        frames_per_auxinput7=1,
        iofields_filename="./plus.io_config",
        ignore_iofields_warning=true,
        write_input=true,

        /
        &fdda
        /
        &domains
        time_step=""" + str(time_step) + """,
        e_we=""" + str(e_we) + """,
        e_sn=""" + str(e_sn) + """,
        e_vert=41,
        num_metgrid_levels=34,
        num_metgrid_soil_levels=4,
        dx=""" + str(dx) + """,
        dy=""" + str(dy) + """,
        i_parent_start=0,
        j_parent_start=0,
        smooth_option=0,
        grid_id=1,
        parent_id=0,
        parent_grid_ratio=1,
        parent_time_step_ratio=1,
        feedback=0,	
        force_sfc_in_vinterp=1,
        p_top_requested=5000,
        hypsometric_opt                     = 2,
        /
        &dfi_control
        /
        &physics
        mp_physics_ad=    98,
        ra_lw_physics= 0,
        ra_sw_physics= 0,
        radt=          15,
        sf_sfclay_physics=0,
        sf_surface_physics=2,
        bl_pbl_physics=98,
        cu_physics=0,
        cudt=0,
        num_soil_layers=4,
        num_land_cat=21,
        mp_zero_out=0,
        mp_zero_out_thresh=1.e-8,
        traj_opt=0,
        /
        &dynamics
        dyn_opt                             = 302,
        w_damping=0,
        diff_opt=0,
        km_opt=1,
        dampcoef=0.2,
        base_temp=290.0,
        use_theta_m=0,
        /
        &bdy_control
        specified=true,
        /
        &grib2
        /
        &namelist_quilt
        /
        &perturbation
        trajectory_io=.false.,
        /"""


        # Write out to the file
        with open(wrf_dir + "exp_files/" + exp_name + "/namelists/namelist.input.adj." + exp_name, "w") as f:
            f.write(namelist_content)

        print(f"\nSuccess! 'namelist.input.adj.{exp_name}' has been generated.")

    elif run_type == "tlm":
        namelist_content = """&time_control
        run_hours=""" + str(run_hours) + """,
        start_year=""" + str(start_year) + """,
        start_month=""" + str(start_month) + """,
        start_day=""" + str(start_day) + """,
        start_hour=""" + str(start_hour) + """,
        end_year=""" + str(end_year) + """,
        end_month=""" + str(end_month) + """,
        end_day=""" + str(end_day) + """,
        end_hour=""" + str(end_hour) + """,
        interval_seconds=""" + str(interval_seconds) + """,
        input_from_file=true,
        debug_level=0,
        auxhist8_outname="./tlmout_d<domain>_<date>",
        auxhist8_interval_h=1,
        io_form_auxhist8=2,

        frames_per_auxhist8=1,
        auxinput6_inname="./auxhist6_d<domain>_<date>",
        auxinput6_interval_s=60,
        io_form_auxinput6=2,
        frames_per_auxinput6=1,
        auxinput9_inname="./wrfout_d<domain>_<date>",
        auxinput9_interval_s=3600,
        io_form_auxinput9=2,
        frames_per_auxinput9=1,
        iofields_filename="./plus.io_config",
        ignore_iofields_warning=true,
        write_input=true,

        /
        &fdda
        /
        &domains
        time_step=""" + str(time_step) + """,
        e_we=""" + str(e_we) + """,
        e_sn=""" + str(e_sn) + """,
        e_vert=41,
        num_metgrid_levels=34,
        num_metgrid_soil_levels=4,
        dx=""" + str(dx) + """,
        dy=""" + str(dy) + """,
        i_parent_start=0,
        j_parent_start=0,
        smooth_option=0,
        grid_id=1,
        parent_id=0,
        parent_grid_ratio=1,
        parent_time_step_ratio=1,
        feedback=0,	
        force_sfc_in_vinterp=1,
        p_top_requested=5000,
        hypsometric_opt                     = 2,
        /
        &dfi_control
        /
        &physics
        mp_physics_ad=    98,
        ra_lw_physics= 0,
        ra_sw_physics= 0,
        radt=          15,
        sf_sfclay_physics=0,
        sf_surface_physics=2,
        bl_pbl_physics=98,
        cu_physics=0,
        cudt=0,
        num_soil_layers=4,
        num_land_cat=21,
        mp_zero_out=0,
        mp_zero_out_thresh=1.e-8,
        traj_opt=0,
        /
        &dynamics
        dyn_opt                             = 202,
        w_damping=0,
        diff_opt=0,
        km_opt=1,
        dampcoef=0.2,
        base_temp=290.0,
        use_theta_m=0,
        /
        &bdy_control
        specified=true,
        /
        &grib2
        /
        &namelist_quilt
        /
        &perturbation
        trajectory_io=.false.,
        check_TL = .true.,
        tl_standalone = .true.
        /"""


        # Write out to the file
        with open(wrf_dir + "exp_files/" + exp_name + "/namelists/namelist.input.tlm." + exp_name, "w") as f:
            f.write(namelist_content)

        print(f"\nSuccess! 'namelist.input.tlm.{exp_name}' has been generated.")

    elif run_type == "fwd":
        namelist_content = """&time_control
        run_hours=""" + str(run_hours) + """,
        start_year=""" + str(start_year) + """,
        start_month=""" + str(start_month) + """,
        start_day=""" + str(start_day) + """,
        start_hour=""" + str(start_hour) + """,
        end_year=""" + str(end_year) + """,
        end_month=""" + str(end_month) + """,
        end_day=""" + str(end_day) + """,
        end_hour=""" + str(end_hour) + """,
        interval_seconds=""" + str(interval_seconds) + """,
        input_from_file=true,
        debug_level=0,
        frames_per_auxhist2=1,
        io_form_auxhist6=2,
        history_interval=60,
        frames_per_outfile=99,
        inputout_interval=60,
        inputout_begin_h=0,
        inputout_end_h=36,
        iofields_filename="./plus.io_config"
        ignore_iofields_warning=true,
        write_input=false,
        /
        &fdda
        /
        &domains
        time_step=""" + str(time_step) + """,
        e_we=""" + str(e_we) + """,
        e_sn=""" + str(e_sn) + """,
        e_vert=41,
        num_metgrid_levels=34,
        num_metgrid_soil_levels=4,
        dx=""" + str(dx) + """,
        dy=""" + str(dy) + """,
        i_parent_start=0,
        j_parent_start=0,
        smooth_option=0,
        grid_id=1,
        parent_id=0,
        parent_grid_ratio=1,
        parent_time_step_ratio=1,
        feedback=0,	
        force_sfc_in_vinterp=1,
        p_top_requested=5000,
        interp_type=2,
        hypsometric_opt                     = 2,
        /
        &dfi_control
        /
        &physics
        mp_physics=    7,
        ra_lw_physics= 1,
        ra_sw_physics= 2,
        radt=         15,
        sf_sfclay_physics=1,
        sf_surface_physics=2,
        bl_pbl_physics=1,
        cu_physics=    1,
        cudt=          0,
        isfflx=1,
        ifsnow=1,
        icloud=1,
        surface_input_source=3,
        num_soil_layers=4,
        num_land_cat=21
        mp_zero_out=0,
        mp_zero_out_thresh=1.e-8,
        /
        &dynamics
        dyn_opt = 2,
        w_damping=1,
        diff_opt=1,
        km_opt=4,
        damp_opt=3
        dampcoef=0.2,
        base_temp=290.0,
        gwd_opt=1,
        iso_temp=200.,
        use_theta_m=0,
        /
        &bdy_control
        spec_bdy_width=5,
        spec_zone=1,
        relax_zone=4,
        specified=true,
        nested=.false.,
        /
        &grib2
        /
        &namelist_quilt
        /
        &perturbation
        trajectory_io=.false.,
        / """


        # Write out to the file
        with open(wrf_dir + "exp_files/" + exp_name + "/namelists/namelist.input.fwd." + exp_name, "w") as f:
            f.write(namelist_content)

        print(f"\nSuccess! 'namelist.input.fwd.{exp_name}' has been generated.")

if __name__ == "__main__":
    generate_namelist()