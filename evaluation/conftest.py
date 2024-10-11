import os
from hypothesis import settings, Verbosity

settings.register_profile("sound_valid", max_examples=1000)
settings.register_profile("property_coverage", max_examples=100)
settings.register_profile("debug", 
                          max_examples=10,
                          )
settings.load_profile(os.getenv("HYPOTHESIS_PROFILE", "debug"))