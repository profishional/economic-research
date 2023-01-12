from dataclasses import dataclass, field

Percentage = float
Percentage_per_session = float

# US Dollar types
USD = float
USD_per_POKT = float
USD_per_session = float

# Simulation types
Run = int
Timestep = int

@dataclass
class ServerEnvironment:
    # Set the type (e.g. Percentage) and default value (e.g. 0.0) for each field
    type: str = ""
    hardware_costs_per_session: USD_per_session = 0.0
    cloud_costs_per_session: USD_per_session = 0.0
    third_party_costs_per_session: Percentage_per_session = 0.0 # this could be full nodes
