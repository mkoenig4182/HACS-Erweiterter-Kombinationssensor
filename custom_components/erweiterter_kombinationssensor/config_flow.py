import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import selector
from .const import DOMAIN

def get_data_schema(defaults=None):
    """Sicherer Aufbau des UI-Schemas mit strikter Typen-Konvertierung."""
    if defaults is None:
        defaults = {}

    # Striktes Auslesen und Absichern der Plus-Sensoren
    raw_plus = defaults.get("sensors_plus", [])
    if isinstance(raw_plus, list):
        current_plus = raw_plus
    elif isinstance(raw_plus, str):
        current_plus = [raw_plus] if raw_plus else []
    else:
        current_plus = list(raw_plus) if raw_plus else []

    # Striktes Auslesen und Absichern der Minus-Sensoren
    raw_minus = defaults.get("sensors_minus", [])
    if isinstance(raw_minus, list):
        current_minus = raw_minus
    elif isinstance(raw_minus, str):
        current_minus = [raw_minus] if raw_minus else []
    else:
        current_minus = list(raw_minus) if raw_minus else []

    # Konvertierung der Min/Max-Werte in saubere Floats
    try:
        min_val = float(defaults.get("min_value", -99999.0))
    except (ValueError, TypeError):
        min_val = -99999.0

    try:
        max_val = float(defaults.get("max_value", 99999.0))
    except (ValueError, TypeError):
        max_val = 99999.0

    return vol.Schema({
        vol.Optional("sensors_plus", default=current_plus): selector.EntitySelector(
            selector.EntitySelectorConfig(domain="sensor", multiple=True)
        ),
        vol.Optional("sensors_minus", default=current_minus): selector.EntitySelector(
            selector.EntitySelectorConfig(domain="sensor", multiple=True)
        ),
        vol.Optional("min_value", default=min_val): vol.Coerce(float),
        vol.Optional("max_value", default=max_val): vol.Coerce(float),
    })

# KORREKTUR: Der Klassenname MUSS mit dem Domänen-Namen beginnen (PascalCase)
class ErweiterterKombinationssensorFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Erstellung des Helfers beim ersten Mal."""
    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Erster Schritt bei der Neuanlage (data)."""
        if user_input is not None:
            return self.async_create_entry(title=user_input["name"], data=user_input)

        schema = vol.Schema({vol.Required("name"): str}).extend(get_data_schema().schema)
        return self.async_show_form(step_id="user", data_schema=schema)

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Schaltet das Optionen-Fenster in der UI frei."""
        return ErweiterterKombinationssensorOptionsFlowHandler(config_entry)


# KORREKTUR: Auch hier den Namen für die Optionen sauber anpassen
class ErweiterterKombinationssensorOptionsFlowHandler(config_entries.OptionsFlow):
    """Verarbeitung des Bearbeiten-Fensters über das offizielle Options-System."""

    def __init__(self, config_entry):
        """Nutzt den offiziellen Super-Init für moderne HA-Versionen (Python 3.14+)."""
        super().__init__()

    async def async_step_init(self, user_input=None):
        """Einstellungs-Formular anzeigen und im Options-Feld speichern."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        current_settings = dict(self.config_entry.options) if self.config_entry.options else dict(self.config_entry.data)

        return self.async_show_form(
            step_id="init",
            data_schema=get_data_schema(current_settings)
        )
