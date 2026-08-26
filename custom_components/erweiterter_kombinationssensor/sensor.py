import logging
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import STATE_UNKNOWN, STATE_UNAVAILABLE
from homeassistant.core import callback
from homeassistant.helpers.event import async_track_state_change_event

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the sensor from a config entry."""
    async_add_entities([UiMathSensor(config_entry)], True)

class UiMathSensor(SensorEntity):
    """Representation of a UI-managed Math Sensor."""

    def __init__(self, config_entry):
        self._config_entry = config_entry
        self._attr_name = config_entry.data.get("name")
        self._attr_unique_id = config_entry.entry_id

    def _get_setting(self, key, default):
        """Liest Werte aus den Optionen aus (falls bearbeitet), sonst aus den Basisdaten."""
        if self._config_entry.options and key in self._config_entry.options:
            return self._config_entry.options[key]
        return self._config_entry.data.get(key, default)

    @property
    def _s_plus(self):
        return self._get_setting("sensors_plus", [])

    @property
    def _s_minus(self):
        return self._get_setting("sensors_minus", [])

    @property
    def _min_val(self):
        return self._get_setting("min_value", -99999.0)

    @property
    def _max_val(self):
        return self._get_setting("max_value", 99999.0)

    async def async_added_to_hass(self):
        """Listen for changes on all tracked sensors."""
        @callback
        def async_listener(event):
            self.async_set_context(event.context)
            self.async_write_ha_state()

        all_entity_ids = list(set(self._s_plus + self._s_minus))
        if all_entity_ids:
            self.async_on_remove(
                **async_track_state_change_event**(self.hass, all_entity_ids, async_listener)
            )

    @property
    def native_value(self):
        """Calculate state."""
        total = 0.0
        for entity_id in self._s_plus:
            total += self._get_filtered_value(entity_id)
        for entity_id in self._s_minus:
            total -= self._get_filtered_value(entity_id)
        return round(total, 2)

    @property
    def native_unit_of_measurement(self):
        """Inherit unit of measurement from the first positive sensor."""
        if self._s_plus and len(self._s_plus) > 0:
            state_obj = self.hass.states.get(self._s_plus[0])
            if state_obj and "unit_of_measurement" in state_obj.attributes:
                return state_obj.attributes["unit_of_measurement"]
        return None

    @property
    def device_class(self):
        """Inherit device class from the first positive sensor."""
        if self._s_plus and len(self._s_plus) > 0:
            state_obj = self.hass.states.get(self._s_plus[0])
            if state_obj and "device_class" in state_obj.attributes:
                return state_obj.attributes["device_class"]
        return None

    def _get_filtered_value(self, entity_id):
        """Get state and apply exclusion."""
        state_obj = self.hass.states.get(entity_id)
        if state_obj is None or state_obj.state in (STATE_UNKNOWN, STATE_UNAVAILABLE):
            return 0.0
        try:
            val = float(state_obj.state)
            if val < self._min_val or val > self._max_val:
                _LOGGER.warning(f"Wert {val} von {entity_id} aufgrund von Grenzwerten ausgeschlossen.")
                return 0.0
            return val
        except ValueError:
            return 0.0
