from docx.shared import RGBColor

# Document
HEADER_COLOR = RGBColor(0x4E, 0xAD, 0xEA)
BLACK_COLOR = RGBColor(0x00, 0x00, 0x00)
FONT_ARIAL: str = "Arial"
FONT_TIMES_NEW_ROMAN: str = "Times New Roman"

# System
PARENT_DIR = "../darwin/deploy_document"

# Content
GOOGLE_CLOUD_NAME: str = "tlp-public-api-uservices-prod"
CLUSTER_NAME: str = "prod-public-api-uservices-gke"

# Command list
COMMAND_LIST = [
    "kubectl apply -f configmap-p.yml",
    "kubectl apply -f service-p.yml",
    "kubectl apply -f deployment-p.yml"
]
