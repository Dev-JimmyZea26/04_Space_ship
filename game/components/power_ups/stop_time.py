from game.components.power_ups.power_up import PowerUp
from game.utils.constants import STOP_TIME, STOP_TIME_TYPE

class StopTime(PowerUp):
    
    def __init__(self):
        super().__init__(STOP_TIME, STOP_TIME_TYPE)