from .base.component import Component
from .base.enums import DataTypes,RegisterTypes
from .base.data_value import DataValue

class Boiler(Component):
    def __init__(self) -> None:
        super().__init__(input_address=500, holding_address=32000)
        self.temperature = DataValue(address=0,multiplier=0.1)
        self.state = DataValue(address=1,type=DataTypes.UINT)
        self.mode = DataValue(address=2,type=DataTypes.UINT)
        
        self.target_temperature = DataValue(address=0,multiplier=10,register_type=RegisterTypes.Holding)
        self.single_charge = DataValue(address=1,register_type=RegisterTypes.Holding)
        self.holding_mode= DataValue(address=2,register_type=RegisterTypes.Holding)
        self.circulation = DataValue(address=3,register_type=RegisterTypes.Holding)