from pydantic import BaseModel, PositiveFloat

class PackageDimensions(BaseModel):
    # PositiveFloat ensures the value is strictly > 0
    width: PositiveFloat
    height: PositiveFloat
    length: PositiveFloat
    mass: PositiveFloat
