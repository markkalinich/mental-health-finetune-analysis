"""
Model Coverage Heatmap Visualization (Figure 1)

Creates heatmaps showing model availability across fine-tuning types and model sizes.

Author: Mark Kalinich (with significant assistance from Cursor models)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path


# Configuration
CONFIG_PATH = Path(__file__).parent.parent / "config" / "models_config.csv"
OUTPUT_DIR = Path(__file__).parent.parent / "results" / "model_coverage"


# Fine-tune type mapping
FINETUNE_TYPE_MAP = {
    "PT": "Base Model",
    "IT": "Instruction-Tuned",
    "Mental Health": "Mental Health Tuned",
    "MedGemma": "Medical-Tuned",
    "Medical": "Medical-Tuned",
    "ShieldGemma": "Safety-Tuned",
    "Guard": "Safety-Tuned",
}

# Canonical order for y-axis (rows) - matches other facet plots conceptually
FINETUNE_ORDER = ["Base Model", "Instruction-Tuned", "Mental Health Tuned", "Medical-Tuned", "Safety-Tuned"]

# Colors matching the existing facet plots (gemma_version_facet_plot.py)
# Base models = cool colors (blue/green), Fine-tunes = warm colors (red/orange/purple)
FINETUNE_COLORS = {
    "Base Model": "#52B788",           # Sea Green (PT)
    "Instruction-Tuned": "#2E86AB",    # Blue (IT)
    "Mental Health Tuned": "#C73E1D",  # Red (Mental Health)
    "Medical-Tuned": "#F18F01",        # Orange (MedGemma)
    "Safety-Tuned": "#7B2D8E",         # Dark Purple (ShieldGemma)
}

# Size bucket definitions (in billions) - used for bucketed view
SIZE_BUCKETS = [
    (0, 0.5, "0-0.5B"),
    (0.5, 1, "0.5-1B"),
    (1, 2, "1-2B"),
    (2, 4, "2-4B"),
    (4, 8, "4-8B"),
    (8, 16, "8-16B"),
    (16, 32, "16-32B"),
    (32, 80, "32-80B"),
]

# Exact sizes for specific model families (for exact size view)
GEMMA3_EXACT_SIZES = ["270M", "1B", "4B", "12B", "27B"]

# Model family groupings - maps various family names to parent family and identifies version
FAMILY_GROUPINGS = {
    # Gemma family
    "gemma": ("Gemma", None),  # version from 'version' column
    "gemma1": ("Gemma", "1"),
    "gemma2": ("Gemma", "2"),
    "gemma3n": ("Gemma", "3n"),
    "medgemma": ("Gemma", None),  # use version column, treated as Medical
    "shieldgemma": ("Gemma", None),  # use version column, treated as Safety
    "mental_health": ("Gemma", None),  # Gemma-based MH models
    "gemma_therapy": ("Gemma", None),  # Gemma-based therapy models
    
    # Qwen family
    "qwen": ("Qwen", None),
    "qwen1.5": ("Qwen", "1.5"),
    "qwen2": ("Qwen", "2"),
    "qwen_medical": ("Qwen", None),
    "qwen_mental_health": ("Qwen", None),
    "qwen_guard": ("Qwen", None),
    
    # LLaMA family
    "llama1": ("LLaMA", "1"),
    "llama2": ("LLaMA", "2"),
    "llama3": ("LLaMA", "3"),
    "llama3.1": ("LLaMA", "3.1"),
    "llama3.2": ("LLaMA", "3.2"),
    "llama3.3": ("LLaMA", "3.3"),
    "llama4": ("LLaMA", "4"),
    "llama_medical": ("LLaMA", None),
    "llama_mental_health": ("LLaMA", None),
    "llama_therapy": ("LLaMA", None),
    "llama_guard": ("LLaMA", None),
}


def load_models_config(config_path: Path = CONFIG_PATH) -> pd.DataFrame:
    """Load and preprocess the models configuration."""
    df = pd.read_csv(config_path)
    
    # Map model_type to canonical fine-tune categories
    df["finetune_type"] = df["model_type"].map(FINETUNE_TYPE_MAP)
    
    # Fill any unmapped types
    df["finetune_type"] = df["finetune_type"].fillna("Other")
    
    # Parse param_billions, handling missing values
    df["param_billions"] = pd.to_numeric(df["param_billions"], errors="coerce")
    
    # Assign size buckets
    df["size_bucket"] = df["param_billions"].apply(assign_size_bucket)
    
    # Create exact size label (e.g., "270M", "1B", "27B")
    df["exact_size"] = df["param_billions"].apply(format_exact_size)
    
    # Map to parent family first (needed for version determination)
    df["parent_family"] = df["family"].apply(lambda x: FAMILY_GROUPINGS.get(x, ("Other", None))[0])
    
    # Determine display version (use family-specific version if defined, otherwise use version column)
    def get_display_version(row):
        family_info = FAMILY_GROUPINGS.get(row["family"], (None, None))
        if family_info[1] is not None:
            return family_info[1]
        return str(row["version"])
    
    df["display_version"] = df.apply(get_display_version, axis=1)
    
    # Special labeling for Gemma 3n models - use E2B/E4B notation
    # Apply to any Gemma family model with version "3n"
    def apply_gemma3n_labels(row):
        if row["parent_family"] == "Gemma" and row["display_version"] == "3n":
            if row["param_billions"] == 4.5:
                return "E2B"
            elif row["param_billions"] == 6.9:
                return "E4B"
        return row["exact_size"]
    
    df["exact_size"] = df.apply(apply_gemma3n_labels, axis=1)
    
    return df


def format_exact_size(param_billions: float) -> str:
    """Format parameter count as exact size label."""
    if pd.isna(param_billions):
        return "Unknown"
    
    if param_billions < 1:
        # Convert to millions
        return f"{int(param_billions * 1000)}M"
    else:
        # Use billions, removing trailing zeros
        if param_billions == int(param_billions):
            return f"{int(param_billions)}B"
        else:
            return f"{param_billions}B"


def assign_size_bucket(param_billions: float) -> str:
    """Assign a model to a size bucket based on parameter count."""
    if pd.isna(param_billions):
        return "Unknown"
    
    for low, high, label in SIZE_BUCKETS:
        if low <= param_billions < high:
            return label
    
    # Handle edge cases
    if param_billions >= SIZE_BUCKETS[-1][1]:
        return f"{SIZE_BUCKETS[-1][1]}B+"
    
    return "Unknown"


def filter_models_for_version(df: pd.DataFrame, parent_family: str, version: str, 
                               include_specialized: bool = True) -> pd.DataFrame:
    """
    Filter models for a specific family and version.
    
    Args:
        df: Full models dataframe
        parent_family: Parent family name (e.g., "Gemma", "Qwen", "LLaMA")
        version: Version string (e.g., "3", "3.0", "3.1", "3n", "3.1+" for combined)
        include_specialized: Whether to include specialized variants (medgemma, shieldgemma, etc.)
    """
    # Start with models from the parent family
    mask = df["parent_family"] == parent_family
    
    # Handle special "3.1+" case - combines 3.1, 3.2, 3.3, 4.0
    if version == "3.1+":
        version_mask = (
            (df["display_version"] == "3.1") |
            (df["display_version"] == "3.2") |
            (df["display_version"] == "3.3") |
            (df["display_version"] == "4") |
            (df["display_version"] == "4.0")
        )
        return df[mask & version_mask].copy()
    
    # Handle special "3n" case - ONLY match exactly "3n", not "3" or "3.0"
    if version == "3n":
        version_mask = (df["display_version"] == "3n")
        return df[mask & version_mask].copy()
    
    # Filter by version
    version_str = str(version)
    
    # For "3.0", match exactly "3.0" or "3" but not "3n" or "3.1" etc.
    if version_str == "3.0":
        version_mask = (
            (df["display_version"] == "3.0") |
            (df["display_version"] == "3")
        )
        # Explicitly exclude "3n" and other 3.x versions
        version_mask = version_mask & (df["display_version"] != "3n")
        return df[mask & version_mask].copy()
    
    # For version "3", also match "3.0" but NOT "3n"
    if version_str == "3":
        version_mask = (
            (df["display_version"] == "3") |
            (df["display_version"] == "3.0")
        )
        # Explicitly exclude "3n"
        version_mask = version_mask & (df["display_version"] != "3n")
        return df[mask & version_mask].copy()
    
    # General case
    version_mask = (
        (df["display_version"] == version_str) |
        (df["display_version"].str.startswith(version_str + ".") if "." not in version_str else False)
    )
        
    return df[mask & version_mask].copy()


def create_coverage_matrix(df: pd.DataFrame, use_exact_sizes: bool = False, 
                           exact_size_order: list = None) -> pd.DataFrame:
    """
    Create a coverage matrix showing model counts per (finetune_type, size).
    
    Rows = fine-tune types, Columns = model sizes
    
    Args:
        df: Filtered dataframe
        use_exact_sizes: If True, use exact size labels instead of buckets
        exact_size_order: List of exact sizes in desired order
    
    Returns a DataFrame with finetune types as rows and sizes as columns.
    """
    size_col = "exact_size" if use_exact_sizes else "size_bucket"
    
    # Create pivot table counting models
    matrix = pd.crosstab(df["finetune_type"], df[size_col])
    
    # Ensure all fine-tune types are present (as rows)
    for ft in FINETUNE_ORDER:
        if ft not in matrix.index:
            matrix.loc[ft] = 0
    
    # Reorder rows by fine-tune order
    matrix = matrix.reindex(FINETUNE_ORDER)
    
    # Reorder columns by size
    if use_exact_sizes and exact_size_order:
        # Use provided order, filtering to existing columns
        existing_sizes = [s for s in exact_size_order if s in matrix.columns]
        extra_sizes = [s for s in matrix.columns if s not in exact_size_order]
        ordered_cols = existing_sizes + extra_sizes
    else:
        # Use bucket order
        bucket_labels = [b[2] for b in SIZE_BUCKETS]
        existing_buckets = [b for b in bucket_labels if b in matrix.columns]
        extra_buckets = [b for b in matrix.columns if b not in bucket_labels]
        ordered_cols = existing_buckets + extra_buckets
    
    matrix = matrix[ordered_cols] if ordered_cols else matrix
    matrix = matrix.fillna(0).astype(int)
    
    return matrix


def plot_coverage_heatmap(matrix: pd.DataFrame, title: str, output_path: Path = None,
                          show_counts: bool = True, use_row_colors: bool = True):
    """
    Plot a coverage heatmap with rows = fine-tune types, columns = model sizes.
    
    Args:
        matrix: Coverage matrix from create_coverage_matrix()
        title: Plot title
        output_path: Path to save the figure (optional)
        show_counts: Whether to show count numbers in cells
        use_row_colors: If True, each row gets its own color based on fine-tune type
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    n_rows, n_cols = matrix.shape
    
    # Create the heatmap cell by cell with row-specific colors
    for i, finetune_type in enumerate(matrix.index):
        base_color = FINETUNE_COLORS.get(finetune_type, "#888888")
        
        for j, size in enumerate(matrix.columns):
            count = matrix.iloc[i, j]
            
            if count > 0:
                # Use the row's color
                facecolor = base_color
                textcolor = 'white'
            else:
                # Light gray for empty cells
                facecolor = '#f0f0f0'
                textcolor = '#888888'
            
            # Draw rectangle
            rect = plt.Rectangle((j - 0.5, i - 0.5), 1, 1, 
                                  facecolor=facecolor, edgecolor='white', linewidth=2)
            ax.add_patch(rect)
            
            # Add count text
            if show_counts and count > 0:
                ax.text(j, i, str(count), ha='center', va='center',
                       fontsize=14, fontweight='bold', color=textcolor)
    
    # Set axis limits and ticks
    ax.set_xlim(-0.5, n_cols - 0.5)
    ax.set_ylim(n_rows - 0.5, -0.5)  # Flip y-axis so first row is at top
    
    ax.set_xticks(range(n_cols))
    ax.set_xticklabels(matrix.columns, fontsize=11, fontweight='bold')
    ax.set_yticks(range(n_rows))
    ax.set_yticklabels(matrix.index, fontsize=11)
    
    # Labels and title
    ax.set_xlabel("Model Size", fontsize=13, fontweight='bold')
    ax.set_ylabel("Fine-tuning Type", fontsize=13, fontweight='bold')
    ax.set_title(title, fontsize=15, fontweight='bold', pad=15)
    
    # Remove spines
    for spine in ax.spines.values():
        spine.set_visible(False)
    
    ax.set_aspect('equal')
    plt.tight_layout()
    
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
        print(f"Saved: {output_path}")
    
    return fig, ax


def create_single_version_heatmap(parent_family: str = "Gemma", version: str = "3.0",
                                   show_counts: bool = True, use_exact_sizes: bool = True,
                                   enabled_only: bool = True):
    """
    Create a heatmap for a single model family version.
    
    Args:
        parent_family: Parent family name (e.g., "Gemma")
        version: Version string (e.g., "3.0")
        show_counts: Whether to show count numbers
        use_exact_sizes: Whether to use exact sizes instead of buckets
        enabled_only: Whether to filter to enabled models only
    """
    # Load data
    df = load_models_config()
    
    # Filter to enabled models if requested
    if enabled_only:
        df = df[df["enabled"] == True]
    
    # Filter to specific family and version
    df_filtered = filter_models_for_version(df, parent_family, version)
    
    if len(df_filtered) == 0:
        print(f"No models found for {parent_family} {version}")
        return None
    
    print(f"\nModels for {parent_family} {version}:")
    print(df_filtered[["family", "size", "version", "model_type", "finetune_type", 
                       "param_billions", "exact_size"]].to_string())
    
    # Determine exact size order for this family/version
    if use_exact_sizes:
        # Get unique sizes and sort by param_billions
        size_order_df = df_filtered[["exact_size", "param_billions"]].drop_duplicates()
        size_order_df = size_order_df.sort_values("param_billions")
        exact_size_order = size_order_df["exact_size"].tolist()
    else:
        exact_size_order = None
    
    # Create coverage matrix
    matrix = create_coverage_matrix(df_filtered, use_exact_sizes=use_exact_sizes, 
                                    exact_size_order=exact_size_order)
    
    print(f"\nCoverage Matrix:")
    print(matrix)
    
    # Create output path
    size_type = "exact" if use_exact_sizes else "bucketed"
    output_path = OUTPUT_DIR / f"{parent_family.lower()}_{version.replace('.', '_')}_coverage_{size_type}.png"
    
    # Plot
    title = f"{parent_family} {version} - Model Coverage"
    fig, ax = plot_coverage_heatmap(matrix, title, output_path, show_counts=show_counts)
    
    plt.show()
    
    return matrix


def consolidate_similar_sizes(sizes_with_values: list) -> dict:
    """
    Consolidate model sizes using custom rules based on marketing conventions.
    
    Rules:
    - E2B, E4B (Gemma 3n) → keep as-is (special notation)
    - All <1B models → "<1B"
    - 1.2B → 1B (LLaMA 3.2 advertised as 1B)
    - 1.8B → 2B (Qwen 1.8B grouped with 2B)
    - 2.6B → 2B (ShieldGemma/Gemma 2 advertised as 2B)
    - 3.2B → 3B (LLaMA 3.2 models advertised as 3B)
    - 7.6B → 7B (Qwen UMLS is a 7B model)
    - 8.2B → 8B (Qwen Guard advertised as 8B)
    - 9.2B → 9B (ShieldGemma advertised as 9B)
    - Other sizes within 5% → consolidated
    
    Args:
        sizes_with_values: List of (size_label, param_billions) tuples
    
    Returns:
        dict mapping original size labels to consolidated size labels
    """
    if not sizes_with_values:
        return {}
    
    mapping = {}
    
    for label, value in sizes_with_values:
        # Special case: Gemma 3n E2B/E4B labels - keep as-is
        if label in ["E2B", "E4B"]:
            mapping[label] = label
            continue
            
        if pd.isna(value) or value == 0:
            mapping[label] = label
            continue
        
        # Rule 1: All <1B models → "<1B"
        if value < 1.0:
            mapping[label] = "<1B"
        # Rule 2: 1.2B → 1B
        elif 1.15 <= value <= 1.25:
            mapping[label] = "1B"
        # Rule 3: 1.8B → 2B
        elif 1.7 <= value <= 1.9:
            mapping[label] = "2B"
        # Rule 4: 2.6B → 2B (ShieldGemma/Gemma 2)
        elif 2.5 <= value <= 2.7:
            mapping[label] = "2B"
        # Rule 5: 3.2B → 3B (LLaMA 3.2)
        elif 3.1 <= value <= 3.3:
            mapping[label] = "3B"
        # Rule 6: 7.6B → 7B (Qwen UMLS)
        elif 7.5 <= value <= 7.7:
            mapping[label] = "7B"
        # Rule 7: 8.2B → 8B
        elif 8.1 <= value <= 8.3:
            mapping[label] = "8B"
        # Rule 8: 9.2B → 9B
        elif 9.1 <= value <= 9.3:
            mapping[label] = "9B"
        # Rule 9: Round to nearest standard size if within 5%
        else:
            # Standard sizes: 1, 2, 3, 4, 7, 8, 9, 12, 13, 14, 17, 27, 32, 33, 70
            standard_sizes = [1, 2, 3, 4, 7, 8, 9, 12, 13, 14, 17, 20, 27, 32, 33, 70, 120]
            
            # Check if close to a standard size (within 5%)
            matched = False
            for std_size in standard_sizes:
                if abs(value - std_size) / std_size <= 0.05:
                    mapping[label] = f"{std_size}B"
                    matched = True
                    break
            
            if not matched:
                # Keep original label
                mapping[label] = label
    
    return mapping


def create_facet_plot(families: list = None, enabled_only: bool = True, 
                      show_counts: bool = True):
    """
    Create a facet plot showing coverage for multiple model families and versions.
    All heatmap cells have the same size across all panels.
    Uses exact model sizes, consolidating sizes within 25% of each other.
    
    Args:
        families: List of (parent_family, versions) tuples. If None, auto-detect.
        enabled_only: Whether to filter to enabled models only
        show_counts: Whether to show count numbers
    """
    # Load data
    df = load_models_config()
    
    if enabled_only:
        df = df[df["enabled"] == True]
    
    # Auto-detect families and versions if not provided
    if families is None:
        # Define specific versions to show for each family
        families = [
            ("Gemma", ["1", "1.0", "2", "2.0", "3", "3.0", "3n"]),
            ("LLaMA", ["1", "1.0", "2", "2.0", "3.0", "3.1+"]),  # 3.1+ combines 3.1, 3.2, 3.3
            ("Qwen", ["1.5", "2", "2.0", "3", "3.0"]),
        ]
        
        # Filter to versions that actually have models
        filtered_families = []
        for parent, versions in families:
            existing_versions = []
            for v in versions:
                # Handle special "3.1+" case for LLaMA
                if v == "3.1+" and parent == "LLaMA":
                    # Check if any of 3.1, 3.2, 3.3, 4 have models
                    has_models = False
                    for sub_v in ["3.1", "3.2", "3.3", "4", "4.0"]:
                        df_v = filter_models_for_version(df, parent, sub_v)
                        if len(df_v) > 0:
                            has_models = True
                            break
                    if has_models and "3.1+" not in existing_versions:
                        existing_versions.append("3.1+")
                else:
                    df_v = filter_models_for_version(df, parent, v)
                    if len(df_v) > 0 and v not in existing_versions:
                        # Normalize version display (prefer "1" over "1.0" if both exist)
                        normalized = v.rstrip(".0") if v.endswith(".0") else v
                        if normalized not in existing_versions:
                            existing_versions.append(normalized)
            if existing_versions:
                filtered_families.append((parent, existing_versions))
        families = filtered_families
    
    # Collect all exact sizes across all panels with their param_billions values
    all_sizes_with_values = []
    for parent_family, versions in families:
        for version in versions:
            df_v = filter_models_for_version(df, parent_family, version)
            for _, row in df_v.iterrows():
                if pd.notna(row["param_billions"]) and row["exact_size"] != "Unknown":
                    all_sizes_with_values.append((row["exact_size"], row["param_billions"]))
    
    # Remove duplicates (keep unique size labels with their values)
    unique_sizes = {}
    for label, value in all_sizes_with_values:
        if label not in unique_sizes:
            unique_sizes[label] = value
    
    sizes_list = [(label, value) for label, value in unique_sizes.items()]
    
    # Consolidate similar sizes using custom rules
    size_mapping = consolidate_similar_sizes(sizes_list)
    
    # Apply mapping to dataframe
    df["consolidated_size"] = df["exact_size"].map(lambda x: size_mapping.get(x, x))
    
    # Get unique consolidated sizes and sort by value
    consolidated_sizes = set(size_mapping.values())
    
    def size_sort_key(s):
        if s == "Unknown":
            return 999
        if s == "<1B":
            return 0.5  # Place <1B at the beginning
        if s == "E2B":
            return 4.5  # Gemma 3n E2B (4.5B parameters)
        if s == "E4B":
            return 6.9  # Gemma 3n E4B (6.9B parameters)
        if s.endswith("M"):
            return float(s[:-1]) / 1000
        elif s.endswith("B"):
            return float(s[:-1])
        return 0
    
    all_sizes_ordered = sorted(consolidated_sizes, key=size_sort_key)
    
    # Determine grid size
    n_rows = len(families)
    n_cols = max(len(versions) for _, versions in families)
    n_finetune_rows = len(FINETUNE_ORDER)
    
    # Pre-calculate the number of size columns for each panel
    # This is needed to set proper width ratios for GridSpec
    panel_col_counts = []
    for parent_family, versions in families:
        row_counts = []
        for version in versions:
            df_v = filter_models_for_version(df, parent_family, version).copy()
            if len(df_v) > 0:
                df_v["consolidated_size"] = df_v["exact_size"].map(lambda x: size_mapping.get(x, x))
                # Count non-empty sizes
                size_counts = df_v.groupby("consolidated_size").size()
                unique_sizes = len(size_counts)
                row_counts.append(max(unique_sizes, 1))
            else:
                row_counts.append(1)
        # Pad with 1s if this family has fewer versions
        while len(row_counts) < n_cols:
            row_counts.append(1)
        panel_col_counts.append(row_counts)
    
    # Calculate width ratios - use max columns per version column across all families
    width_ratios = []
    for col_idx in range(n_cols):
        max_cols_for_version = max(panel_col_counts[row_idx][col_idx] for row_idx in range(n_rows))
        width_ratios.append(max_cols_for_version)
    
    # Fixed cell size for consistent appearance
    cell_size = 0.5  # inches per cell
    panel_height = n_finetune_rows * cell_size + 0.8  # Add padding for title
    
    # Calculate figure width based on actual width ratios
    total_width_units = sum(width_ratios)
    fig_width = total_width_units * cell_size + 3.0  # Add space for labels and legend
    fig_height = panel_height * n_rows + 1.0  # Add space for title
    
    # Use GridSpec for variable width columns
    from matplotlib.gridspec import GridSpec
    fig = plt.figure(figsize=(fig_width, fig_height))
    gs = GridSpec(n_rows, n_cols, figure=fig, width_ratios=width_ratios, wspace=0.15, hspace=0.4)
    
    # Create axes array
    axes = [[fig.add_subplot(gs[row, col]) for col in range(n_cols)] for row in range(n_rows)]
    axes = np.array(axes)
    
    # Store max sizes per column for consistent xlim across all panels in same column
    max_sizes_per_col = width_ratios  # This is already the max column count per version column

    for row_idx, (parent_family, versions) in enumerate(families):
        for col_idx in range(n_cols):
            ax = axes[row_idx, col_idx]
            
            if col_idx < len(versions):
                version = versions[col_idx]
                df_filtered = filter_models_for_version(df, parent_family, version).copy()
                
                if len(df_filtered) > 0:
                    # Apply consolidated size mapping
                    df_filtered["consolidated_size"] = df_filtered["exact_size"].map(
                        lambda x: size_mapping.get(x, x))
                    
                    # Create matrix with consolidated sizes
                    matrix = pd.crosstab(df_filtered["finetune_type"], df_filtered["consolidated_size"])
                    
                    # Ensure all fine-tune types are present (as rows)
                    for ft in FINETUNE_ORDER:
                        if ft not in matrix.index:
                            matrix.loc[ft] = 0
                    matrix = matrix.reindex(FINETUNE_ORDER)
                    
                    # REMOVE EMPTY COLUMNS: Only keep sizes that have at least one model
                    non_empty_cols = [col for col in matrix.columns if matrix[col].sum() > 0]
                    
                    # Sort the non-empty columns by size
                    def size_sort_key_local(s):
                        if s == "Unknown":
                            return 999
                        if s == "<1B":
                            return 0.5
                        if s == "E2B":
                            return 4.5
                        if s == "E4B":
                            return 6.9
                        if s.endswith("M"):
                            return float(s[:-1]) / 1000
                        elif s.endswith("B"):
                            return float(s[:-1])
                        return 0
                    
                    non_empty_cols_sorted = sorted(non_empty_cols, key=size_sort_key_local)
                    matrix = matrix[non_empty_cols_sorted]
                    matrix = matrix.fillna(0).astype(int)
                    
                    # Update panel_sizes for this specific panel
                    panel_sizes = non_empty_cols_sorted
                    
                    # Plot this panel using panel-specific sizes (left-aligned)
                    for i, finetune_type in enumerate(FINETUNE_ORDER):
                        base_color = FINETUNE_COLORS.get(finetune_type, "#888888")
                        
                        for j, size in enumerate(panel_sizes):
                            count = matrix.loc[finetune_type, size] if finetune_type in matrix.index else 0
                            
                            if count > 0:
                                facecolor = base_color
                                textcolor = 'white'
                            else:
                                facecolor = '#f0f0f0'
                                textcolor = '#888888'
                            
                            rect = plt.Rectangle((j - 0.5, i - 0.5), 1, 1,
                                                  facecolor=facecolor, edgecolor='white', linewidth=1.5)
                            ax.add_patch(rect)
                            
                            if show_counts and count > 0:
                                ax.text(j, i, str(count), ha='center', va='center',
                                       fontsize=10, fontweight='bold', color=textcolor)
                    
                    # Axis setup - use max sizes for this column for consistent box sizes
                    max_cols_this_version = max_sizes_per_col[col_idx]
                    ax.set_xlim(-0.5, max_cols_this_version - 0.5)
                    ax.set_ylim(len(FINETUNE_ORDER) - 0.5, -0.5)
                    
                    ax.set_xticks(range(len(panel_sizes)))
                    ax.set_xticklabels(panel_sizes, rotation=45, ha='right', fontsize=8)
                    ax.set_yticks(range(len(FINETUNE_ORDER)))
                    
                    # Only show y-tick labels on first column
                    if col_idx == 0:
                        ax.set_yticklabels(FINETUNE_ORDER, fontsize=9)
                    else:
                        ax.set_yticklabels([])
                    
                    ax.set_title(f"{parent_family} {version}", fontsize=11, fontweight='bold', pad=8)
                    
                    for spine in ax.spines.values():
                        spine.set_visible(False)
                    
                    ax.set_aspect('equal')
                else:
                    ax.text(0.5, 0.5, "No models", ha='center', va='center', 
                           transform=ax.transAxes, fontsize=10, color='gray')
                    ax.set_title(f"{parent_family} {version}", fontsize=11)
                    ax.axis('off')
            else:
                ax.axis('off')
    
    # Create legend
    legend_elements = [
        mpatches.Patch(facecolor=FINETUNE_COLORS[ft], edgecolor='white', label=ft)
        for ft in FINETUNE_ORDER
    ]
    legend_elements.append(mpatches.Patch(facecolor='#f0f0f0', edgecolor='gray', label='Not Available'))
    
    # Position legend at bottom right of the page
    fig.legend(handles=legend_elements, loc='lower right', bbox_to_anchor=(0.89, 0.10),
               fontsize=12, framealpha=0.9, title='Fine-tuning Type', title_fontsize=13.5)
    
    plt.suptitle("Model Coverage by Fine-tuning Type and Size", fontsize=14, fontweight='bold', y=0.99)
    plt.subplots_adjust(left=0.08, right=0.88, top=0.94, bottom=0.08)
    
    # Save
    output_path = OUTPUT_DIR / "model_coverage_facet.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
    print(f"Saved: {output_path}")
    
    plt.show()
    
    return fig


def summarize_coverage(enabled_only: bool = True):
    """Print a summary of model coverage across all families."""
    df = load_models_config()
    
    if enabled_only:
        df = df[df["enabled"] == True]
    
    print("=" * 80)
    print("MODEL COVERAGE SUMMARY")
    print("=" * 80)
    
    for parent_family in ["Gemma", "Qwen", "LLaMA"]:
        family_df = df[df["parent_family"] == parent_family]
        if len(family_df) == 0:
            continue
            
        print(f"\n{parent_family}")
        print("-" * 40)
        
        versions = sorted(family_df["display_version"].unique())
        for version in versions:
            version_df = filter_models_for_version(df, parent_family, version)
            if len(version_df) == 0:
                continue
                
            finetune_counts = version_df["finetune_type"].value_counts()
            print(f"  {version}: {len(version_df)} models")
            for ft in FINETUNE_ORDER:
                count = finetune_counts.get(ft, 0)
                if count > 0:
                    print(f"    - {ft}: {count}")


if __name__ == "__main__":
    # Summary
    summarize_coverage(enabled_only=True)
    
    # Single version heatmap (Gemma 3) with EXACT sizes
    print("\n" + "=" * 80)
    print("Creating Gemma 3.0 heatmap with exact sizes...")
    print("=" * 80)
    create_single_version_heatmap("Gemma", "3.0", show_counts=True, use_exact_sizes=True)
    
    # Facet plot for all families (using consolidated exact sizes)
    print("\n" + "=" * 80)
    print("Creating facet plot...")
    print("=" * 80)
    create_facet_plot(enabled_only=True, show_counts=True)
