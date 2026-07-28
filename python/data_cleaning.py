"""
Automotive Powertrain Reliability Analysis

Data Cleaning Script

Author: Rohith T
"""

import pandas as pd

# Load datasets
vehicle_master = pd.read_csv("vehicle_master.csv")
failure_profile = pd.read_csv("powertrain_failure_profile.csv")

print(vehicle_master.head())
print(failure_profile.head())

df["Component"].unique()

<StringArray>
[                                          'Battery',
                                          'Injector',
                                         'Fuel Pump',
                                            'Clutch',
                                     'AC Compressor',
                                        'Suspension',
                                               'ECU',
                                      'Turbocharger',
                                           'Sensors',
                                   'Steering System',
 ...
 '4-Speed Automatic Transmission (Torque Converter)',
                                    'Fuel Injectors',
                       'Engine ECU / ISG Controller',
                            'Electric AC Compressor',
                           'Hybrid ECU / Engine ECU',
                 'Hybrid ECU / Power Management ECU',
                      'Fuel Injectors (D-4S System)',
                       'High/Low Pressure Fuel Pump',
              'Fuel Injectors (D-4S Dual Injection)',
                   'Fuel Pump (Low & High Pressure)']
Length: 116, dtype: str

df["Component"] = df["Component"].replace({
    # Injectors
    "Fuel Injector": "Injector",
    "Petrol Injector": "Injector",
    "MPFI Injector": "Injector",
    "GDI Injector": "Injector",
    "Common Rail Injector": "Injector",
    "Common-Rail Injector": "Injector",
    "Direct Fuel Injector": "Injector",
    "Fuel Injectors": "Injector",
    "Fuel Injectors (D-4S System)": "Injector",
    "Fuel Injectors (D-4S Dual Injection)": "Injector",
    "Petrol Injectors": "Injector",
    "Petrol/CNG Injectors": "Injector",
    "Petrol & CNG Injectors": "Injector",

    # Fuel Pumps
    "Petrol Fuel Pump": "Fuel Pump",
    "Electric Fuel Pump": "Fuel Pump",
    "High Pressure Fuel Pump": "Fuel Pump",
    "High-Pressure Fuel Pump": "Fuel Pump",
    "High-Pressure Fuel Pump (Denso)": "Fuel Pump",
    "High/Low Pressure Fuel Pump": "Fuel Pump",
    "Fuel Pump (Low & High Pressure)": "Fuel Pump",

    # Clutch
    "Conventional Clutch": "Clutch",
    "Clutch Assembly": "Clutch",
    "Clutch Assembly (AMT)": "Clutch",
    "AMT Clutch Assembly": "Clutch",
    "iMT Clutch Actuator": "Clutch",
    "AMT Clutch Actuator": "Clutch"
})

df["Component"] = df["Component"].replace({
    # Injectors
    "Fuel Injector": "Injector",
    "Petrol Injector": "Injector",
    "MPFI Injector": "Injector",
    "GDI Injector": "Injector",
    "Common Rail Injector": "Injector",
    "Common-Rail Injector": "Injector",
    "Direct Fuel Injector": "Injector",
    "Fuel Injectors": "Injector",
    "Fuel Injectors (D-4S System)": "Injector",
    "Fuel Injectors (D-4S Dual Injection)": "Injector",
    "Petrol Injectors": "Injector",
    "Petrol/CNG Injectors": "Injector",
    "Petrol & CNG Injectors": "Injector",

    # Fuel Pumps
    "Petrol Fuel Pump": "Fuel Pump",
    "Electric Fuel Pump": "Fuel Pump",
    "High Pressure Fuel Pump": "Fuel Pump",
    "High-Pressure Fuel Pump": "Fuel Pump",
    "High-Pressure Fuel Pump (Denso)": "Fuel Pump",
    "High/Low Pressure Fuel Pump": "Fuel Pump",
    "Fuel Pump (Low & High Pressure)": "Fuel Pump",

    # Clutch
    "Conventional Clutch": "Clutch",
    "Clutch Assembly": "Clutch",
    "Clutch Assembly (AMT)": "Clutch",
    "AMT Clutch Assembly": "Clutch",
    "iMT Clutch Actuator": "Clutch",
    "AMT Clutch Actuator": "Clutch"
})

df["Component"] = df["Component"].replace({
    "12V Battery": "Battery",
    "12V Auxiliary Battery": "Battery",
    "Battery (12V Auxiliary)": "Battery",
    "Battery Management Sensor": "Battery",
    "Battery Thermal Management": "Battery",
    "Battery Management System (BMS)": "Battery"
})
df["Component"] = df["Component"].replace({
    "Engine ECU": "ECU",
    "Engine ECU / CNG ECU": "ECU",
    "Engine ECU / Smart Hybrid Controller": "ECU",
    "Engine ECU / Smart Hybrid Controller / AMT Control Module": "ECU",
    "Engine ECU / Hybrid Control Module": "ECU",
    "Engine ECU / CNG Control System": "ECU",
    "Engine ECU / Smart Hybrid & CNG Control Logic": "ECU",
    "Engine ECU / Smart Hybrid & CNG Control Module": "ECU",
    "Engine ECU / AMT Control Module": "ECU",
    "Engine ECU / SHVS AMT Control Module": "ECU",
    "Engine ECU / SHVS Controller": "ECU",
    "Engine ECU / Transmission Control Module": "ECU",
    "Engine ECU / Hybrid Control ECU": "ECU",
    "Engine ECU / Hybrid Controller": "ECU",
    "Engine ECU / ISG Controller": "ECU",
    "Hybrid ECU / Engine ECU": "ECU",
    "Hybrid ECU / Power Management ECU": "ECU"
})

df.to_csv(
    "powertrain_failure_profile_postgres.csv",
    index=False,
    encoding="utf-8",
    quoting=csv.QUOTE_ALL
)

print("✅ CSV created successfully.")
