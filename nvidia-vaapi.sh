# Force libva to load the nvidia backend, until libva knows which driver to
# load for the nvidia-drm driver:
export LIBVA_DRIVER_NAME=nvidia

# Disable the sandbox for the RDD process that the decoder runs in:
export MOZ_DISABLE_RDD_SANDBOX=1
