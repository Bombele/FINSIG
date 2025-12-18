import csv
import datetime
import os
from typing import Dict, List, Any


class Traceability:
    """
    Moteur de traçabilité institutionnelle.
    Permet d'enregistrer des événements avec horodatage en UTC
    et d'exporter les logs pour audit externe.
    """

    def __init__(self):
        self.logs: List[Dict[str, Any]] = []

    def log_event(self, module: str, action: str, metadata: Dict[str, Any] = None) -> None:
        """
        Enregistre un événement avec horodatage en UTC.
        """
        timestamp = datetime.datetime.utcnow().isoformat() + "Z"  # format ISO 8601 UTC
        entry = {
            "timestamp": timestamp,
            "module": module,
            "action": action,
            "metadata": metadata or {}
        }
        self.logs.append(entry)
        print(f"[TRACE] {timestamp} | {module} | {action} | {entry['metadata']}")

    def export_to_csv(self, filepath: str = "logs/traceability_log.csv") -> None:
        """
        Exporte les logs vers un fichier CSV.
        """
        if not self.logs:
            print("⚠️ Aucun log à exporter.")
            return

        # Crée le répertoire si nécessaire
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, mode="w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["timestamp", "module", "action", "metadata"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for entry in self.logs:
                writer.writerow({
                    "timestamp": entry["timestamp"],
                    "module": entry["module"],
                    "action": entry["action"],
                    "metadata": str(entry["metadata"])
                })

        print(f"✅ Logs exportés vers {filepath}")