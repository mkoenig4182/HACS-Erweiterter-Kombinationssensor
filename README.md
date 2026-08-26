# Erweiterter Kombinationssensor (+-) for Home Assistant

[![hacs_badge](https://shields.io)](https://hacs.xyz)
![Version](https://shields.io)

Ein mächtiger, über die Benutzeroberfläche (UI) gesteuerter Helfer für Home Assistant. Er erlaubt es, beliebig viele Sensoren zu addieren, zu subtrahieren und gleichzeitig fehlerhafte Werte (Ausreißer) automatisch auszuschließen.

*A powerful UI-managed helper for Home Assistant that allows you to sum, subtract, and automatically filter out outlier values across multiple sensors.*

---

## 🇩🇪 Funktionen (Deutsch)

Der standardmäßige Kombinations-Helfer von Home Assistant erlaubt leider nur das Addieren von Werten. Diese Erweiterung schließt diese Lücke vollständig und fügt erweiterte Filter hinzu:

* **Dynamische Plus/Minus-Listen:** Fügen Sie beliebig viele Sensoren hinzu, die addiert werden sollen, und beliebig viele, die abgezogen werden.
* **Wert-Ausschluss (Filter):** Definieren Sie globale Mindest- und Höchstgrenzen. Werte außerhalb dieses Bereichs (z. B. unplausible Peak-Fehlmessungen wie `99999` oder negative Werte) werden automatisch ignoriert.
* **Automatische Einheitenübernahme:** Maßeinheit (`W`, `kWh`, `°C` etc.) und Geräteklasse (z. B. Energie/Leistung) werden vollautomatisch vom ersten ausgewählten Sensor geerbt.
* **100% UI-Gesteuert:** Keine Konfiguration in der `configuration.yaml` nötig. Erstellen, Bearbeiten und Löschen funktionieren direkt über das Home Assistant Helfer-Menü.
* **Zukunftssicher:** Vollständig kompatibel mit modernen Home Assistant Versionen (inkl. Python 3.14+).

### Installation via HACS

1. Öffnen Sie **HACS** in Ihrem Home Assistant.
2. Klicken Sie oben rechts auf die drei Punkte und wählen Sie **Benutzerdefinierte Repositories**.
3. Fügen Sie die URL dieses GitHub-Repositorys hinzu und wählen Sie als Kategorie **Integration**.
4. Klicken Sie auf **Hinzufügen** und installieren Sie die Erweiterung.
5. Starten Sie Home Assistant neu.

### Einrichtung in Home Assistant

1. Gehen Sie auf **Einstellungen** ➔ **Geräte & Dienste** ➔ **Helfer**.
2. Klicken Sie unten rechts auf **Helfer erstellen**.
3. Scrollen Sie ganz nach unten und wählen Sie **Über eine Integration erstellen**.
4. Suchen Sie nach **Erweiterter Kombinationssensor (+-)**.

---

## 🇬🇧 Features (English)

The native Home Assistant combination helper only supports summing up values. This custom component closes that gap and adds advanced validation:

* **Dynamic Plus/Minus Lists:** Add as many sensors as you want for addition, and as many as you need for subtraction.
* **Value Exclusion (Outlier Filter):** Set global minimum and maximum thresholds. Any value outside this range (e.g., faulty peaks like `99999` or sudden negative drops) will be automatically ignored.
* **Automatic Unit Inheritance:** The unit of measurement (`W`, `kWh`, `°C`, etc.) and device class are automatically inherited from the first positive sensor.
* **100% UI-Managed:** No `configuration.yaml` required. Creating, updating, and deleting can be done entirely through the Home Assistant Helpers menu.
* **Future-Proof:** Fully compatible with modern Home Assistant versions (including Python 3.14+).

### Installation via HACS

1. Open **HACS** in your Home Assistant dashboard.
2. Click the three dots in the top right corner and select **Custom repositories**.
3. Paste the URL of this GitHub repository and select **Integration** as the category.
4. Click **Add** and install the integration.
5. Restart Home Assistant.

### Configuration

1. Navigate to **Settings** ➔ **Devices & Services** ➔ **Helpers**.
2. Click **Create Helper** in the bottom right.
3. Scroll to the bottom and select **Create via integration**.
4. Search for **Erweiterter Kombinationssensor (+-)**.
