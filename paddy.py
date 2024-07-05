import random
import time

class SmartAgricultureSystem:
    def __init__(self):
        self.temperature_sensor = TemperatureSensor()
        self.humidity_sensor = HumiditySensor()
        self.soil_moisture_sensor = SoilMoistureSensor()
        self.water_pump = WaterPump()
        self.fertilizer_dispenser = FertilizerDispenser()

    def monitor_environment(self):
        temperature = self.temperature_sensor.get_reading()
        humidity = self.humidity_sensor.get_reading()
        soil_moisture = self.soil_moisture_sensor.get_reading()

        print(f"Temperature: {temperature}°C, Humidity: {humidity}%, Soil Moisture: {soil_moisture}%")

        if soil_moisture < 30:
            print("Soil moisture is low. Initiating watering.")
            self.water_pump.turn_on()
            time.sleep(5)  # Simulating watering for 5 seconds
            self.water_pump.turn_off()

        if temperature > 30:
            print("High temperature detected. Dispensing fertilizer.")
            self.fertilizer_dispenser.dispense()

class TemperatureSensor:
    def get_reading(self):
        # Simulating temperature readings between 20 and 40 degrees Celsius
        return round(random.uniform(20, 40), 2)

class HumiditySensor:
    def get_reading(self):
        # Simulating humidity readings between 40% and 80%
        return round(random.uniform(40, 80), 2)

class SoilMoistureSensor:
    def get_reading(self):
        # Simulating soil moisture readings between 10% and 80%
        return round(random.uniform(10, 80), 2)

class WaterPump:
    def turn_on(self):
        print("Water pump turned on.")

    def turn_off(self):
        print("Water pump turned off.")

class FertilizerDispenser:
    def dispense(self):
        print("Fertilizer dispenser activated. Dispensing fertilizer.")

if __name__ == "__main__":
    agriculture_system = SmartAgricultureSystem()

    try:
        while True:
            agriculture_system.monitor_environment()
            time.sleep(10)  # Simulating monitoring every 10 seconds
    except KeyboardInterrupt:
        print("Monitoring stopped.")
