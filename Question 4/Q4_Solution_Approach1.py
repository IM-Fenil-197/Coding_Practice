import pandas as pd

# Function to categorize descriptions based on keywords
def categorize_description(description):
    description_lower = description.lower().replace('-', ' ').replace('_', ' ')
    
    if 'motor' in description_lower:
        return 'motor'
    elif 'gb' in description_lower or 'gearbox' in description_lower:
        return 'gearbox'
    elif 'fan' in description_lower or 'blower' in description_lower:
        return 'blower'
    elif 'pulley' in description_lower or 'de' in description_lower or 'nde' in description_lower:
        return 'bearing'
    elif 'compressor' in description_lower:
        return 'compressor'
    else:
        return 'unknown'

# Sample dataset
data = {
    'Description': [
        'MOTOR - DE',
        'GB I/P - NDE',
        'EXPELLER - DE',
        'EXPELLER - NDE',
        'MOTOR - DE',
        'GB I/P - NDE',
        'EXPELLER - DE',
        'EXPELLER - NDE',
        'MODLER_GRINDING_WHEEL - Motor DE',
        'MODLER_REGULATING-WHEEL - Motor DE',
        'SAFED_MACHINE_2_T2 _Motor DE',
        'SAFED_MACHINE_2_T4 - Motor DE',
        'BLOWER_1 - Motor DE',
        'DOWEL_RH_OP30_202091700',
        'MILLING_LH_OP10_202091300',
        'MILLING_LH_OP20_202091500',
        'MILLING_RH_OP10_202091400',
        'MILLING_RH_OP20_202091600',
        '_ML_G11_MOTOR_DE',
        'Base_Coat_Exhst_Shaft_Fan',
        'Base_Coat_Exhst_Shaft_Pulley',
        'Heating_Zone_Motor_DE',
        'Compressor',
        'GearBox I/p',
        'PCR_TRIPLEX_EXTRUDER_150_MM_GB_INT_DE'
    ]
}


# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Apply the categorize_description function to the 'Description' column
df['Category'] = df['Description'].apply(categorize_description)

# Display the resulting DataFrame
print(df)