import os

folders = [
    "00_Environment_Setup",
    "01_Python_Basics/Notes",
    "01_Python_Basics/Notebooks",
    "01_Python_Basics/Scripts",
    "01_Python_Basics/Algorithms",
    "01_Python_Basics/Datasets",
    "02_Data_Handling_and_Visualization/Notes",
    "02_Data_Handling_and_Visualization/Notebooks",
    "02_Data_Handling_and_Visualization/Scripts",
    "02_Data_Handling_and_Visualization/Datasets/raw",
    "02_Data_Handling_and_Visualization/Datasets/cleaned",
    "02_Data_Handling_and_Visualization/Utils",
    "03_Machine_Learning/Notes",
    "03_Machine_Learning/Notebooks",
    "03_Machine_Learning/Scripts",
    "03_Machine_Learning/Algorithms",
    "03_Machine_Learning/Datasets/raw",
    "03_Machine_Learning/Datasets/processed",
    "03_Machine_Learning/Models/trained_models",
    "03_Machine_Learning/Models/model_evaluation_reports",
    "03_Machine_Learning/Experiments/logs",
    "03_Machine_Learning/Experiments/confusion_matrices",
    "03_Machine_Learning/Utils",
    "04_Deep_Learning/Notes",
    "04_Deep_Learning/Notebooks",
    "04_Deep_Learning/Scripts",
    "04_Deep_Learning/Datasets/images",
    "04_Deep_Learning/Datasets/text",
    "04_Deep_Learning/Datasets/synthetic",
    "04_Deep_Learning/Models/checkpoints",
    "04_Deep_Learning/Models/final_models",
    "04_Deep_Learning/Experiments/tensorboard_logs",
    "04_Deep_Learning/Experiments/training_curves",
    "04_Deep_Learning/Utils",
    "05_AI_Applications/Notes",
    "05_AI_Applications/Notebooks",
    "05_AI_Applications/Scripts",
    "05_AI_Applications/Datasets/nlp",
    "05_AI_Applications/Datasets/vision",
    "05_AI_Applications/Algorithms",
    "05_AI_Applications/Utils",
    "06_LLMs_and_GenAI/Notes",
    "06_LLMs_and_GenAI/Notebooks",
    "06_LLMs_and_GenAI/Scripts",
    "06_LLMs_and_GenAI/Datasets/text_corpus",
    "06_LLMs_and_GenAI/Datasets/qa_pairs",
    "06_LLMs_and_GenAI/Datasets/embeddings",
    "06_LLMs_and_GenAI/Models/fine_tuned",
    "06_LLMs_and_GenAI/Models/lora_weights",
    "06_LLMs_and_GenAI/Utils",
    "06_LLMs_and_GenAI/Experiments/results",
    "06_LLMs_and_GenAI/Experiments/inference_examples",
    "07_Projects/Project_01_Data_Cleaning",
    "07_Projects/Project_02_ML_Model",
    "07_Projects/Project_03_Image_Classifier",
    "07_Projects/Project_04_Fake_News_NLP",
    "07_Projects/Project_05_GenAI_Assistant",
    "08_Resources",
]

files = ["SYLLABUS.md", "PROGRESS_TRACKER.md", "README.md", ".gitignore"]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    open(file, "a").close()

print("✅ Full Data Science to GenAI folder structure created successfully.")