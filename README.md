# 🏍️ NoHelmetDetection — Detección y Clasificación de Casco en Motociclistas con YOLO

Este proyecto desarrolla un sistema de **detección de motocicletas y clasificación de ocupantes** para identificar si **llevan casco o no**, utilizando modelos YOLO entrenados sobre datos de Birmania y Medellín.

📌 Se implementa entrenamiento desde cero y fine-tuning sobre un modelo base para adaptar el conocimiento a un nuevo dominio.

---

## 👥 Autores

- Cristian Mauricio Blandón Londoño  
- Harold Nolberto Díaz Giraldo  
- Edgard Iglesias Rubio  

---

## 📁 Estructura del Proyecto

```
dataset/
├── birmania/
│   ├── images/
│   │   ├── train/
│   │   └── val/
│   └── labels/
│       ├── train/
│       └── val/
├── medellin/
│   ├── images/
│   │   ├── train/
│   │   └── val/
│   └── labels/
│       ├── train/
│       └── val/
├── databirmania.yaml
├── datafinetuningmde.yaml

raw/
├── birmania/
│   ├── Bago_highway_1/
│   └── Bago_highway_1.csv
│   └── ...
├── medellin/
│   ├── anotaciones/
│   └── imagenes/
└── medellin2/
    ├── anotaciones/
    ├── imagenes/
    └── videos/
src/                    # Notebooks y Scripts principales
src_extra/              # Notebooks y scripts adicionales
.gitignore
requirements.txt
```

---

## ⚙️ Instalación y Preparación del Entorno

```bash
git clone https://github.com/eiglesiasr/NoHelmetDetection.git NoHelmetDetection
cd NoHelmetDetection
conda create -n no-helmet-detection python=3.10 -y
conda activate no-helmet-detection
pip install -r requirements.txt
```

---

## 🧠 Descripción del Proyecto

### 🏍️ Entrenamiento Inicial — Dataset de Birmania

Se realiza el entrenamiento de un modelo YOLO desde cero utilizando imágenes del dataset de Birmania.

1. `1_yolo_parsing_birmania_dataset.ipynb`:  
   Convierte imágenes a resolución 640x640 y etiquetas al formato YOLO.

2. `2_yolo_training_birmania.ipynb`:  
   Entrena el modelo durante 30 epochs (tras experimentar con distintas configuraciones).

---

### 🔁 Fine-Tuning — Dataset de Medellín

Se reutiliza el modelo entrenado con Birmania para adaptarlo a datos locales de Medellín mediante fine-tuning:

1. `3_yolo_parsing_medellin_dataset.ipynb`:  
   Convierte las imágenes y anotaciones (etiquetadas con Roboflow) al formato YOLO.

2. `4_data_augmentation_medellin_dataset.ipynb`:  
   Aplica técnicas de aumento de datos para mejorar la generalización.

3. `5_yolo_finetuning_medellin.ipynb`:  
   Realiza el fine-tuning sobre el modelo base entrenado con Birmania.

> ❗ La carpeta `medellin2` contiene el dataset final utilizado, mientras que `medellin/` (con imágenes CCTV de la Secretaría de Movilidad de Medellín [https://www.medellin.gov.co/SIMM/camaras-de-circuito-cerrado]) fue descartada por condiciones de imagen no óptimas.

---

### 🎥 Detección en Video

- `6_yolo_detect_video.py`:  
  Permite cargar un video y un modelo entrenado para realizar inferencia cuadro a cuadro y visualizar las predicciones.

---

## 📦 Datos

- Se ha compartido una muestra del dataset de Birmania para facilitar pruebas.
- El dataset completo (~100K imágenes) puede descargarse desde [enlace pendiente](https://www.medellin.gov.co/SIMM/camaras-de-circuito-cerrado) este ya esta en formato YOLO y solo debe ser copiado en la ubicación correspondiente.
- Para entrenar desde cero, colocar las imágenes originales en `raw/birmania/` siguiendo la estructura mostrada.
- El dataset final de medellín etiquetado en Roboflow está en `raw/medellin2/` y fue utilizado para el finetuning del modelo final