# ============================================================================
# Program:    create_cartesian.py (Google Colab)
# Purpose:    Create all combinations of determination level values
#             from one year to the next year using a Cartesian product.
# ============================================================================

import pandas as pd
from datetime import datetime
from google.colab import files

# ----------------------------------------------------------------------------
# SECTION 1: Define Input DataFrames for DL2019 and DL2020
# ----------------------------------------------------------------------------

# Dataset #1 – Determination Levels for 2019
dl_2019 = {
    'DL': ['DL0', 'DL1', 'DL2', 'DL3', 'DL4'],
    'DL2019': [0, 1, 2, 3, 4]
}
df_2019 = pd.DataFrame(dl_2019)

# Dataset #2 – Determination Levels for 2020
dl_2020 = {
    'DL': ['DL1', 'DL2', 'DL3', 'DL4'],
    'DL2020': [1, 2, 3, 4]
}
df_2020 = pd.DataFrame(dl_2020)

# ----------------------------------------------------------------------------
# SECTION 2: Generate Cartesian Product of DL2019 × DL2020
# ----------------------------------------------------------------------------

# Add temporary key to simulate full join
df_2019['_key'] = 1
df_2020['_key'] = 1

# Merge on the dummy key to generate all combinations
cartesian_df = pd.merge(df_2019, df_2020, on='_key')

# Drop helper columns and redundant DL labels
cartesian_df = cartesian_df.drop(columns=['_key', 'DL_x', 'DL_y'])

# ----------------------------------------------------------------------------
# SECTION 3: Display and Export Output
# ----------------------------------------------------------------------------

# Display result in Colab
print("▶ Cartesian Product of 2019 and 2020 Determination Levels:")
display(cartesian_df)

# Generate filename and export to Excel
today_str = datetime.today().strftime("%Y%m%d")
output_filename = f"{today_str}_Cartesian_DL_Combos.xlsx"
cartesian_df.to_excel(output_filename, index=False)

# Trigger file download in Google Colab
files.download(output_filename)

# ============================================================================
# Python Program End
# ============================================================================
