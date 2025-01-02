from pydantic import ValidationError
from models import PackageDimensions

# Constants for thresholds
BULKY_VOLUME_THRESHOLD = 1000000  # cm³
DIMENSION_THRESHOLD = 150  # cm
HEAVY_WEIGHT_THRESHOLD = 20  # kg

def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Determines the category for a package based on its dimensions and mass.

    Parameters:
        width: Width of the package in cm.
        height: Height of the package in cm.
        length: Length of the package in cm.
        mass: Mass of the package in kg.

    Returns:
        One of "STANDARD", "SPECIAL", or "REJECTED".
    """
    
    # Use Pydantic to validate inputs
    try:
        dims = PackageDimensions(
            width=width,
            height=height,
            length=length,
            mass=mass
        )
    except ValidationError as e:
        raise ValueError(f"Package dimension validation failed: {e}") from e

    # Calculate volume
    volume = dims.width * dims.height * dims.length

    # Determine bulky and heavy status
    bulky = volume >= BULKY_VOLUME_THRESHOLD or dims.width >= DIMENSION_THRESHOLD or dims.height >= DIMENSION_THRESHOLD or dims.length >= DIMENSION_THRESHOLD
    heavy = dims.mass >= HEAVY_WEIGHT_THRESHOLD

    # Categorize the package
    if bulky and heavy:  # Both bulky and heavy
        return "REJECTED"
    elif bulky or heavy:  # Either bulky or heavy (but not both)
        return "SPECIAL"
    else:  # Neither bulky nor heavy
        return "STANDARD"