from django.db import models
from datetime import datetime
from transductor.models import EnergyTransductor
from boogie.rest import rest_api

class Measurement(models.Model):
    """
    Abstract class responsible to create a base for measurements and optimize
    performance from queries.

    Attributes:
        collection_date (datetime): The exactly collection time.

    """
    collection_date = models.DateTimeField(default=datetime.now)

    class Meta:
        abstract = True

    def save_measurements(self, values_list):
        """
        Method responsible to save measurements based on values list received.

        Args:
            values_list (list): The list with all important
            measurements values.

        Returns:
            None
        """
        raise NotImplementedError


@rest_api()
class EnergyMeasurement(Measurement):
    """
    Class responsible to store energy measurements,
    considering a three-phase energy system.

    Attributes:
        transductor (EnergyTransductor): The transductor which conducted
        measurements.

        frequency_a (float):
        voltage_a (float): The voltage on phase A.
        voltage_b (float): The voltage on phase B.
        voltage_c (float): The voltage on phase C.
        current_a (float): The current on phase A.
        current_b (float): The current on phase B.
        current_c (float): The current on phase C.
        active_power_a (float): The active power on phase A.
        active_power_b (float): The active power on phase B.
        active_power_c (float): The active power on phase C.
        total_active_power (float): The total active power.
        reactive_power_a (float): The reactive power on phase A.
        reactive_power_b (float): The reactive power on phase B.
        reactive_power_c (float): The reactive power on phase C.
        total_reactive_power (float): The total reactive power.
        apparent_power_a (float): The apparent power on phase A.
        apparent_power_b (float): The apparent power on phase B.
        apparent_power_c (float): The apparent power on phase C.
        total_apparent_power (float): The total apparent power.
        power_factor_a (float): The power factor on phase A.
        power_factor_b (float): The power factor on phase B.
        power_factor_c (float): The power factor on phase C.
        total_power_factor (float): The total power factor.
        dht_voltage_a (float): The DHT on voltage at phase A.
        dht_voltage_b (float): The DHT on voltage at phase B.
        dht_voltage_c (float): The DHT on voltage at phase C.
        dht_current_a (float): The DHT on current at phase A.
        dht_current_b (float): The DHT on current at phase B.
        dht_current_c (float): The DHT on current at phase C.
        consumption_a (float): The total consumption on phase A. (since last reset)
        consumption_b (float): The total consumption on phase B. (since last reset)
        consumption_c (float): The total consumption on phase C. (since last reset)
        total_consumption (float): The total consumption of transductor. (since last reset)

    """
    transductor = models.ForeignKey(
        EnergyTransductor,related_name="measurements", on_delete=models.CASCADE
    )

    frequency_a = models.FloatField(default=None)
    # frequency_b = models.FloatField(default=None)
    # frequency_c = models.FloatField(default=None)
    voltage_a = models.FloatField(default=None)
    voltage_b = models.FloatField(default=None)
    voltage_c = models.FloatField(default=None)
    current_a = models.FloatField(default=None)
    current_b = models.FloatField(default=None)
    current_c = models.FloatField(default=None)
    active_power_a = models.FloatField(default=None)
    active_power_b = models.FloatField(default=None)
    active_power_c = models.FloatField(default=None)
    total_active_power = models.FloatField(default=None)
    reactive_power_a = models.FloatField(default=None)
    reactive_power_b = models.FloatField(default=None)
    reactive_power_c = models.FloatField(default=None)
    total_reactive_power = models.FloatField(default=None)
    apparent_power_a = models.FloatField(default=None)
    apparent_power_b = models.FloatField(default=None)
    apparent_power_c = models.FloatField(default=None)
    total_apparent_power = models.FloatField(default=None)
    power_factor_a = models.FloatField(default=None)
    power_factor_b = models.FloatField(default=None)
    power_factor_c = models.FloatField(default=None)
    total_power_factor = models.FloatField(default=None)
    dht_voltage_a = models.FloatField(default=None)
    dht_voltage_b = models.FloatField(default=None)
    dht_voltage_c = models.FloatField(default=None)
    dht_current_a = models.FloatField(default=None)
    dht_current_b = models.FloatField(default=None)
    dht_current_c = models.FloatField(default=None)
    consumption_a = models.FloatField(default=None)
    consumption_b = models.FloatField(default=None)
    consumption_c = models.FloatField(default=None)
    total_consumption = models.FloatField(default=None)

    def __str__(self):
        return '%s' % self.collection_date

    def save_measurements(self, values_list):
        """
        Method responsible to save measurements based on values
        list received.

        Args:
            values_list (list): The list with all important
            measurements values.

        Return:
            None
        """
        self.frequency_a = value_list[0]
        self.voltage_a = values_list[1]
        self.voltage_b = values_list[2]
        self.voltage_c = values_list[3]
        self.current_a = values_list[4]
        self.current_b = values_list[5]
        self.current_c = values_list[6]
        self.active_power_a = values_list[7]
        self.active_power_b = values_list[8]
        self.active_power_c = values_list[9]
        self.total_active_power = values_list[10]
        self.reactive_power_a = values_list[11]
        self.reactive_power_b = values_list[12]
        self.reactive_power_c = values_list[13]
        self.total_reactive_power = values_list[14]
        self.apparent_power_a = values_list[15]
        self.apparent_power_b = values_list[16]
        self.apparent_power_c = values_list[17]
        self.total_apparent_power = values_list[18]
        self.power_factor_a = values_list[19]
        self.power_factor_b = values_list[20]
        self.power_factor_c = values_list[21]
        self.total_power_factor = values_list[22]
        self.dht_voltage_a = values_list[23]
        self.dht_voltage_b = values_list[24]
        self.dht_voltage_c = values_list[25]
        self.dht_current_a = values_list[26]
        self.dht_current_b = values_list[27]
        self.dht_current_c = values_list[28]
        self.consumption_a = values_list[29]
        self.consumption_b = values_list[30]
        self.consumption_c = values_list[31]
        self.total_consumption = values_list[32]

        self.save()
