import pandas as pd
import json

# Ruta del archivo Excel
file_path = r"C:\Users\jonathan.lopez\Desktop\REVISION 04-JUNIO\Catalogo_Grupos_Estado_2026B_04_Junio_LGC.xlsx"

# Nombre de la hoja
sheet_name = "Materias_LGC_Web"

# Leer la hoja de Excel
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Convertir DataFrame a lista de diccionarios (JSON)
data_json = df.to_dict(orient="records")

# Ruta de salida del JSON
output_path = r"C:\Users\jonathan.lopez\Desktop\REVISION 04-JUNIO\materias_lgc_2026B.json"

# Guardar JSON con formato legible
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data_json, f, ensure_ascii=False, indent=4)

print("Conversión completada. Archivo guardado en:", output_path)