#Correr servidor: uvicorn app:app --reload --host 0.0.0.0 --port 8000

from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# Lista temporal de temas seleccionados
temas_seleccionados = []

# Modelo de entrada
class Tema(BaseModel):
    id: int
    tema: str

# ✅ Endpoint raíz para comprobar que la API está corriendo (usado por navegador o Render)
@app.get("/")
def root():
    return {"status": "ok", "mensaje": "API de temas corriendo correctamente en Render 🎉"}


@app.get("/temas/")
def get_temas():
    return [
    {"id": 1, "tema": "Ventilador"},
    {"id": 2, "tema": "iPhone"},
    {"id": 3, "tema": "Katy Perry"},
    {"id": 4, "tema": "Elon Musk"},
    {"id": 5, "tema": "Artificial Intelligence"},
    {"id": 6, "tema": "Isay"},
    {"id": 7, "tema": "Hector"},
    {"id": 8, "tema": "Daniel"},
    {"id": 9, "tema": "Sistemas computacionales"},
    {"id": 10, "tema": "Matematicas"},
    {"id": 11, "tema": "SpaceX"},
    {"id": 12, "tema": "Machine Learning"},
    {"id": 13, "tema": "Taylor Swift"},
    {"id": 14, "tema": "Blockchain"},
    {"id": 15, "tema": "Robótica"},
    {"id": 16, "tema": "Neurociencia"},
    {"id": 17, "tema": "Ciberseguridad"},
    {"id": 18, "tema": "Python"},
    {"id": 19, "tema": "JavaScript"},
    {"id": 20, "tema": "React"},
    {"id": 21, "tema": "Node.js"},
    {"id": 22, "tema": "Vue.js"},
    {"id": 23, "tema": "PHP"},
    {"id": 24, "tema": "CSS"},
    {"id": 25, "tema": "HTML"},
    {"id": 26, "tema": "Swift"},
    {"id": 27, "tema": "Go"},
    {"id": 28, "tema": "Rust"},
    {"id": 29, "tema": "Kotlin"},
    {"id": 30, "tema": "Dart"},
    {"id": 31, "tema": "Scala"},
    {"id": 32, "tema": "R"},
    {"id": 33, "tema": "Perl"},
    {"id": 34, "tema": "Java"},
    {"id": 35, "tema": "C++"},
    {"id": 36, "tema": "C#"},
    {"id": 37, "tema": "SQL"},
    {"id": 38, "tema": "NoSQL"},
    {"id": 39, "tema": "MongoDB"},
    {"id": 40, "tema": "PostgreSQL"},
    {"id": 41, "tema": "MySQL"},
    {"id": 42, "tema": "SQLite"},
    {"id": 43, "tema": "GraphQL"},
    {"id": 44, "tema": "REST API"},
    {"id": 45, "tema": "WebSockets"},
    {"id": 46, "tema": "Golang"},
    {"id": 47, "tema": "Azure"},
    {"id": 48, "tema": "AWS"},
    {"id": 49, "tema": "Google Cloud"},
    {"id": 50, "tema": "Docker"},
    {"id": 51, "tema": "Kubernetes"},
    {"id": 52, "tema": "Terraform"},
    {"id": 53, "tema": "Jenkins"},
    {"id": 54, "tema": "Ansible"},
    {"id": 55, "tema": "Chef"},
    {"id": 56, "tema": "Puppet"},
    {"id": 57, "tema": "Linux"},
    {"id": 58, "tema": "Windows"},
    {"id": 59, "tema": "MacOS"},
    {"id": 60, "tema": "Ubuntu"},
    {"id": 61, "tema": "Debian"},
    {"id": 62, "tema": "Fedora"},
    {"id": 63, "tema": "CentOS"},
    {"id": 64, "tema": "Red Hat"},
    {"id": 65, "tema": "VMware"},
    {"id": 66, "tema": "Xen"},
    {"id": 67, "tema": "Hyper-V"},
    {"id": 68, "tema": "Proxmox"},
    {"id": 69, "tema": "VirtualBox"},
    {"id": 70, "tema": "Vagrant"},
    {"id": 71, "tema": "AWS EC2"},
    {"id": 72, "tema": "GCP Compute"},
    {"id": 73, "tema": "Google Kubernetes Engine"},
    {"id": 74, "tema": "ECS"},
    {"id": 75, "tema": "Lambda"},
    {"id": 76, "tema": "S3"},
    {"id": 77, "tema": "CloudFormation"},
    {"id": 78, "tema": "CloudWatch"},
    {"id": 79, "tema": "IAM"},
    {"id": 80, "tema": "VPC"},
    {"id": 81, "tema": "DynamoDB"},
    {"id": 82, "tema": "SQS"},
    {"id": 83, "tema": "SNS"},
    {"id": 84, "tema": "RDS"},
    {"id": 85, "tema": "Redshift"},
    {"id": 86, "tema": "CloudFront"},
    {"id": 87, "tema": "Route 53"},
    {"id": 88, "tema": "API Gateway"},
    {"id": 89, "tema": "Cognito"},
    {"id": 90, "tema": "EFS"},
    {"id": 91, "tema": "EBS"},
    {"id": 92, "tema": "Lambda Layers"},
    {"id": 93, "tema": "Elastic Beanstalk"},
    {"id": 94, "tema": "AppSync"},
    {"id": 95, "tema": "CloudTrail"},
    {"id": 96, "tema": "SNS Topics"},
    {"id": 97, "tema": "S3 Buckets"},
    {"id": 98, "tema": "IoT Core"},
    {"id": 99, "tema": "CodeCommit"},
    {"id": 100, "tema": "CodePipeline"}
    ]

# Limpiar la lista de temas seleccionados
@app.post("/temas/limpiar/")
def limpiar_temas():
    temas_seleccionados.clear()
    return {"message": "Lista de temas limpiada"}

# Agregar un tema seleccionado a la lista
@app.post("/temas/seleccionar/")
def seleccionar_tema(tema: Tema):
    temas_seleccionados.append(tema.dict())
    return {"message": "Tema agregado", "temas_seleccionados": temas_seleccionados}

# Obtener temas seleccionados actuales
@app.get("/temas/seleccionados/")
def get_temas_seleccionados():
    return temas_seleccionados

# Generar grafo con pesos simulados
@app.post("/grafo/generar/")
def generar_grafo():
    if not temas_seleccionados:
        return {"message": "No hay temas seleccionados"}

    tema_principal = temas_seleccionados[0]["tema"]
    grafo = {tema_principal: 1.0}

    for tema in temas_seleccionados[1:]:
        grafo[tema["tema"]] = round(random.uniform(0.2, 0.9), 2)

    return {"grafo": grafo}

