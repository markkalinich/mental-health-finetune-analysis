#!/bin/bash
# Model Registry for Linux Box
# 
# NOTE: This file is now DEPRECATED. Model configuration is loaded from:
#   config/models_config.csv (single source of truth)
#
# This file is kept for backward compatibility but all model definitions
# should be added to the CSV file instead.
#
# To add a new model, add a row to config/models_config.csv with:
#   family,size,version,lm_studio_id,gemma_generation,model_type,enabled
#
# Last updated: Dec 5, 2025

# Legacy arrays (kept for backward compatibility, not used)
FAMILIES=()  # Now loaded from CSV via get_all_families()

echo "ℹ️  Note: Model definitions now loaded from config/models_config.csv"
