class VehicleInfo(object):

    def __init__(self):
        """
        make_target: option passed to make to create binaries.  Usually sitl, and "-debug" may be appended if -D is passed to sim_vehicle.py
        default_params_filename: filename of default parameters file.  Taken to be relative to autotest dir.
        extra_mavlink_cmds: extra parameters that will be passed to mavproxy
        """
        self.options = {
    "ArduCopter": {
        "default_frame": "quad",
        "frames": {
            # COPTER
            "+": {
                "waf_target": "bin/arducopter",
                "default_params_filename": "default_params/copter.parm",
            },
	    "copter1": {
                "waf_target": "bin/arducopter",
                "default_params_filename": "default_params/copter1.parm",
            },
 	    "copter2": {
                "waf_target": "bin/arducopter",
                "default_params_filename": "default_params/copter2.parm",
            },
	    "copter3": {
                "waf_target": "bin/arducopter",
                "default_params_filename": "default_params/copter3.parm",
            },
	    "copter4": {
                "waf_target": "bin/arducopter",
                "default_params_filename": "default_params/copter4.parm",
            },
	    "copter5": {
        	"waf_target": "bin/arducopter",
        	"default_params_filename": "default_params/copter5.parm",
      	    },
    	    "copter6": {
        	"waf_target": "bin/arducopter",
        	"default_params_filename": "default_params/copter6.parm",
    	    },
    	    "copter7": {
        	"waf_target": "bin/arducopter",
        	"default_params_filename": "default_params/copter7.parm",
    	    },
            "copter8": {
        	"waf_target": "bin/arducopter",
        	"default_params_filename": "default_params/copter8.parm",
    	    },
    	    "copter9": {
        	"waf_target": "bin/arducopter",
        	"default_params_filename": "default_params/copter9.parm",
    	    },
    	    "copter10": {
        	"waf_target": "bin/arducopter",
        	"default_params_filename": "default_params/copter10.parm",
    	    },
    	    "copter11": {
        	"waf_target": "bin/arducopter",
     		"default_params_filename": "default_params/copter11.parm",
    	    },
    	    "copter12": {
        	"waf_target": "bin/arducopter",
        	"default_params_filename": "default_params/copter12.parm",
    	    },
    	    "copter13": {
        	"waf_target": "bin/arducopter",
        	"default_params_filename": "default_params/copter13.parm",
    	    },
    	    "copter14": {
        	"waf_target": "bin/arducopter",
        	"default_params_filename": "default_params/copter14.parm",
    	    },
    	    "copter15": {
        	"waf_target": "bin/arducopter",
        	"default_params_filename": "default_params/copter15.parm",
    	    },
    	    "copter16": {
        	"waf_target": "bin/arducopter",
        	"default_params_filename": "default_params/copter16.parm",
    	    },
    	    "copter17": {
        	"waf_target": "bin/arducopter",
        	"default_params_filename": "default_params/copter17.parm",
     	    },
    	    "copter18": {
       	 "waf_target": "bin/arducopter",
        	"default_params_filename": "default_params/copter18.parm",
    	    },
   	    "copter19": {
       	 "waf_target": "bin/arducopter",
        	"default_params_filename": "default_params/copter19.parm",
    	    },
    	    "copter20": {
        	"waf_target": "bin/arducopter",
        	"default_params_filename": "default_params/copter20.parm",
    	    },
    	    "copter21": {
        	"waf_target": "bin/arducopter",
        	"default_params_filename": "default_params/copter21.parm",
    	    },
    	    "copter22": {
        	"waf_target": "bin/arducopter",
        	"default_params_filename": "default_params/copter22.parm",
    	    },
    	    "copter23": {
        	"waf_target": "bin/arducopter",
        	"default_params_filename": "default_params/copter23.parm",
    	    },
   	    "copter24": {
       	 "waf_target": "bin/arducopter",
        	"default_params_filename": "default_params/copter24.parm",
     	    },
   	    "copter25": {
       	 "waf_target": "bin/arducopter",
       	"default_params_filename": "default_params/copter25.parm",
   	    },
            "quad": {
                "model": "+",
                "waf_target": "bin/arducopter",
                "default_params_filename": "default_params/copter.parm",
            },
            "X": {
                "waf_target": "bin/arducopter",
                "default_params_filename": "default_params/copter.parm",
                # this param set FRAME doesn't actually work because mavproxy
                # won't set a parameter unless it knows of it, and the
                # param fetch happens asynchronously
                "extra_mavlink_cmds": "param fetch frame; param set FRAME 1;",
            },
            "bfx": {
                "make_target": "sitl",
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/copter-bfx.parm" ],
            },
            "djix": {
                "make_target": "sitl",
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/copter-djix.parm" ],
            },
            "cwx": {
                "make_target": "sitl",
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/copter-cwx.parm" ],
            },
            "hexa": {
                "make_target": "sitl",
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/copter-hexa.parm" ],
            },
            "octa-quad": {
                "make_target": "sitl",
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/copter-octaquad.parm" ],
            },
            "octa": {
                "make_target": "sitl",
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/copter-octa.parm" ],
            },
            "tri": {
                "make_target": "sitl",
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/copter-tri.parm" ],
            },
            "y6": {
                "make_target": "sitl",
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/copter-y6.parm" ],
            },
            "dodeca-hexa": {
                "make_target": "sitl",
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/copter-dodecahexa.parm" ],
            },
            # SIM
            "IrisRos": {
                "waf_target": "bin/arducopter",
                "default_params_filename": "default_params/copter.parm",
            },

            "gazebo-iris": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-iris.parm"],
            },            
	    "gazebo-drone1": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone1.parm"],
            },
            "gazebo-drone2": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone2.parm"],
            },
            "gazebo-drone3": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone3.parm"],
            },
	    "gazebo-drone4": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone4.parm"],
            },
	    "gazebo-drone5": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone5.parm"],
            },
            "gazebo-drone6": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone6.parm"],
            },
            "gazebo-drone7": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone7.parm"],
            },
            "gazebo-drone8": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone8.parm"],
            },
	    "gazebo-drone9": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone9.parm"],
            },
	    "gazebo-drone10": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone10.parm"],
            },
	    "gazebo-drone11": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone11.parm"],
            },
	    "gazebo-drone12": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone12.parm"],
	    },
	    "gazebo-drone13": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone13.parm"],
            },
	    "gazebo-drone14": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone14.parm"],
            },
     	    "gazebo-drone15": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone15.parm"],
            },
	    "gazebo-drone16": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone16.parm"],
            },
	    "gazebo-drone17": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone17.parm"],
	    },
	    "gazebo-drone18": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone18.parm"],
	    },	
	    "gazebo-drone19": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone19.parm"],
	    },
	    "gazebo-drone20": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone20.parm"],
            },
	    "gazebo-drone21": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone21.parm"],
            },
	    "gazebo-drone22": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone22.parm"],
            },
	    "gazebo-drone23": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone23.parm"],
            },
	    "gazebo-drone24": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone24.parm"],
            },
	    "gazebo-drone25": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone25.parm"],
            },
	    "gazebo-drone26": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone26.parm"],
            },
	    "gazebo-drone27": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone27.parm"],
            },
	    "gazebo-drone28": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone28.parm"],
            },
	    "gazebo-drone29": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone29.parm"],
            },
	    "gazebo-drone30": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone30.parm"],
            },
	    "gazebo-drone31": {
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter.parm",
                                            "default_params/gazebo-drone31.parm"],
            },
            "airsim-copter": {
                "waf_target": "bin/arducopter",
                "default_params_filename": "default_params/copter.parm",
            },
            # HELICOPTER
            "heli": {
                "make_target": "sitl-heli",
                "waf_target": "bin/arducopter-heli",
                "default_params_filename": "default_params/copter-heli.parm",
            },
            "heli-dual": {
                "make_target": "sitl-heli-dual",
                "waf_target": "bin/arducopter-heli",
                "default_params_filename": ["default_params/copter-heli.parm",
                                            "default_params/copter-heli-dual.parm"],
            },
            "heli-compound": {
                "make_target": "sitl-heli-compound",
                "waf_target": "bin/arducopter-heli",
            },
            "singlecopter": {
                "make_target": "sitl",
                "waf_target": "bin/arducopter",
                "default_params_filename": "default_params/copter-single.parm",
            },
            "coaxcopter": {
                "make_target": "sitl",
                "waf_target": "bin/arducopter",
                "default_params_filename": ["default_params/copter-single.parm",
                                            "default_params/copter-coax.parm"],
            },
            "scrimmage-copter" : {
                "make_target": "sitl",
                "waf_target": "bin/arducopter",
                "default_params_filename": "default_params/copter.parm",
            },
            "calibration": {
                "extra_mavlink_cmds": "module load sitl_calibration;",
            },
        },
    },
    "ArduPlane": {
        "default_frame": "plane",
        "frames": {
            # PLANE
            "quadplane-tilttri": {
                "make_target": "sitl",
                "waf_target": "bin/arduplane",
                "default_params_filename": "default_params/quadplane-tilttri.parm",
            },
            "quadplane-tilttrivec": {
                "make_target": "sitl",
                "waf_target": "bin/arduplane",
                "default_params_filename": "default_params/quadplane-tilttrivec.parm",
            },
            "quadplane-tilthvec": {
                "make_target": "sitl",
                "waf_target": "bin/arduplane",
                "default_params_filename": ["default_params/plane.parm", "default_params/quadplane-tilthvec.parm"],
            },
            "quadplane-tri": {
                "make_target": "sitl",
                "waf_target": "bin/arduplane",
                "default_params_filename": "default_params/quadplane-tri.parm",
            },
            "quadplane-cl84" : {
                "make_target" : "sitl",
                "waf_target" : "bin/arduplane",
                "default_params_filename": "default_params/quadplane-cl84.parm",
            },
            "quadplane": {
                "waf_target": "bin/arduplane",
                "default_params_filename": "default_params/quadplane.parm",
            },
            "firefly": {
                "waf_target": "bin/arduplane",
                "default_params_filename": "default_params/firefly.parm",
            },
            "plane-elevon": {
                "waf_target": "bin/arduplane",
                "default_params_filename": ["default_params/plane.parm", "default_params/plane-elevons.parm"],
            },
            "plane-vtail": {
                "waf_target": "bin/arduplane",
                "default_params_filename": ["default_params/plane.parm", "default_params/plane-vtail.parm"],
            },
            "plane-tailsitter": {
                "waf_target": "bin/arduplane",
                "default_params_filename": "default_params/plane-tailsitter.parm",
            },
            "plane-jet": {
                "waf_target": "bin/arduplane",
                "default_params_filename": ["default_params/plane.parm", "default_params/plane-jet.parm"],
            },
            "plane": {
                "waf_target": "bin/arduplane",
                "default_params_filename": "default_params/plane.parm",
            },
            "plane-dspoilers": {
                "waf_target": "bin/arduplane",
                "default_params_filename": ["default_params/plane.parm", "default_params/plane-dspoilers.parm"]
            },
            "gazebo-zephyr": {
                "waf_target": "bin/arduplane",
                "default_params_filename": "default_params/gazebo-zephyr.parm",
            },
            "last_letter": {
                "waf_target": "bin/arduplane",
            },
            "CRRCSim": {
                "waf_target": "bin/arduplane",
            },
            "jsbsim": {
                "waf_target": "bin/arduplane",
                "default_params_filename": "default_params/plane-jsbsim.parm",
            },
            "scrimmage-plane" : {
                "make_target": "sitl",
                "waf_target": "bin/arduplane",
                "default_params_filename": "default_params/plane.parm",
            },
            "calibration": {
                "extra_mavlink_cmds": "module load sitl_calibration;",
            },
        },
    },
    "APMrover2": {
        "default_frame": "rover",
        "frames": {
            # ROVER
            "rover": {
                "waf_target": "bin/ardurover",
                "default_params_filename": "default_params/rover.parm",
            },
            "rover-skid": {
                "waf_target": "bin/ardurover",
                "default_params_filename": ["default_params/rover.parm",
                                            "default_params/rover-skid.parm"],
            },
            "balancebot": {
                "waf_target": "bin/ardurover",
                "default_params_filename": ["default_params/rover.parm",
                                            "default_params/rover-skid.parm",
                                            "default_params/balancebot.parm"],
            },
            "sailboat": {
                "waf_target": "bin/ardurover",
                "default_params_filename": ["default_params/rover.parm",
                                            "default_params/sailboat.parm"],
            },
            "sailboat-motor": {
                "waf_target": "bin/ardurover",
                "default_params_filename": ["default_params/rover.parm",
                                            "default_params/sailboat-motor.parm"],
            },
            "gazebo-rover": {
                "waf_target": "bin/ardurover",
                "default_params_filename": ["default_params/rover.parm",
                                            "default_params/rover-skid.parm"],
            },
            "calibration": {
                "extra_mavlink_cmds": "module load sitl_calibration;",
            },
        },
    },
    "ArduSub": {
        "default_frame": "vectored",
        "frames": {
            "vectored": {
                "waf_target": "bin/ardusub",
                "default_params_filename": "default_params/sub.parm",
            },
            "gazebo-bluerov2": {
                "waf_target": "bin/ardusub",
                "default_params_filename": "default_params/sub.parm",
            },
        },
    },
    "AntennaTracker": {
        "default_frame": "tracker",
        "frames": {
            "tracker": {
                "waf_target": "bin/antennatracker",
            },
        },
    },
}


    def default_frame(self, vehicle):
        return self.options[vehicle]["default_frame"]

    def default_waf_target(self, vehicle):
        """Returns a waf target based on vehicle type, which is often determined by which directory the user is in"""
        default_frame = self.default_frame(vehicle)
        return self.options[vehicle]["frames"][default_frame]["waf_target"]

    def options_for_frame(self, frame, vehicle, opts):
        """Return informatiom about how to sitl for frame e.g. build-type==sitl"""
        ret = None
        frames = self.options[vehicle]["frames"]
        if frame in frames:
            ret = self.options[vehicle]["frames"][frame]
        else:
            for p in ["octa", "tri", "y6", "firefly", "heli", "gazebo", "last_letter", "jsbsim", "quadplane", "plane-elevon", "plane-vtail", "plane", "airsim"]:
                if frame.startswith(p):
                    ret = self.options[vehicle]["frames"][p]
                    break
        if ret is None:
            if frame.endswith("-heli"):
                ret = self.options[vehicle]["frames"]["heli"]
        if ret is None:
            print("WARNING: no config for frame (%s)" % frame)
            ret = {}

        if "model" not in ret:
            ret["model"] = frame

        if "sitl-port" not in ret:
            ret["sitl-port"] = True

        if opts.model is not None:
            ret["model"] = opts.model

        if (ret["model"].find("xplane") != -1 or ret["model"].find("flightaxis") != -1):
            ret["sitl-port"] = False

        if "make_target" not in ret:
            ret["make_target"] = "sitl"

        if "waf_target" not in ret:
            ret["waf_target"] = self.default_waf_target(vehicle)

        if opts.build_target is not None:
            ret["make_target"] = opts.build_target
            ret["waf_target"] = opts.build_target

        return ret



