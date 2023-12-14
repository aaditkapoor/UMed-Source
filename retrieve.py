# Module to retrieve pubmed ids for a given medical practice
from Bio import Entrez
import pandas as pd
Entrez.email = "data@gmail.com"


def search_pubmed(keyword):
    handle = Entrez.esearch(db="pubmed", term=keyword, retmax=10)
    record = Entrez.read(handle)
    handle.close()
    return record["IdList"]

def fetch_abstract(pubmed_id):
    handle = Entrez.efetch(db="pubmed", id=pubmed_id, retmode="xml")
    records = Entrez.read(handle)
    handle.close()
    try:
        return records['PubmedArticle'][0]['MedlineCitation']['Article'].get('Abstract', {}).get('AbstractText', [None])[0]
    except IndexError:
        return ""

    
general_medical_keywords = [
    "fever", "cough", "headache", "dizziness", "nausea", "fatigue", "abdominal pain",
    "back pain", "joint pain", "skin rash", "sore throat", "shortness of breath",
    "chest pain", "diarrhea", "constipation", "urinary problems", "vision changes",
    "hearing loss", "weight loss", "weight gain", "allergies", "asthma", "diabetes",
    "hypertension", "heart disease", "arthritis", "depression", "anxiety",
    "insomnia", "stress", "cholesterol", "thyroid disorders", "osteoporosis",
    "menstrual irregularities", "pregnancy", "contraception", "sexual health",
    "vaccinations", "preventive health", "nutrition", "exercise", "smoking cessation",
    "alcohol use", "drug use", "mental health", "childhood illnesses", "geriatric health",
    "cancer screening", "HIV/AIDS", "hepatitis", "tuberculosis", "travel medicine"
]

cardiac_keywords = [
    "angina", "myocardial infarction", "heart failure", "arrhythmia", "atrial fibrillation",
    "ventricular tachycardia", "bradycardia", "hypertension", "hypotension", "cardiomyopathy",
    "pericarditis", "endocarditis", "valvular heart disease", "mitral valve prolapse",
    "aortic stenosis", "aortic regurgitation", "mitral regurgitation", "mitral stenosis",
    "tricuspid regurgitation", "pulmonary hypertension", "coronary artery disease",
    "atherosclerosis", "peripheral arterial disease", "aneurysm", "dissection",
    "heart block", "pacemaker", "implantable cardioverter-defibrillator (ICD)",
    "echocardiography", "cardiac catheterization", "angiography", "electrocardiogram (ECG)",
    "stress test", "holter monitor", "cardiac MRI", "cardiac CT", "lipid disorders",
    "cholesterol management", "cardiac rehabilitation", "heart transplant",
    "ventricular assist device", "congestive heart failure", "sudden cardiac arrest",
    "cardiac arrest", "chest pain", "dyspnea", "edema", "palpitations",
    "syncope", "cardiogenic shock", "diuretics", "beta-blockers", "ACE inhibitors",
    "angiotensin II receptor blockers (ARBs)", "calcium channel blockers", "anticoagulants",
    "antiplatelet therapy", "statins", "nitrates", "digitalis", "cardiac risk assessment",
    "preventive cardiology"
]

dietary_keywords = [
    "nutrition", "dietary counseling", "weight loss", "weight gain", "obesity",
    "overweight", "underweight", "balanced diet", "calorie counting", "macronutrients",
    "micronutrients", "vitamins", "minerals", "protein intake", "carbohydrates",
    "fats", "dietary fiber", "hydration", "water intake", "vegetarian diet",
    "vegan diet", "Mediterranean diet", "ketogenic diet", "low-carb diet",
    "high-protein diet", "gluten-free diet", "lactose intolerance", "food allergies",
    "eating disorders", "anorexia", "bulimia", "binge eating disorder", "diabetes management",
    "heart-healthy diet", "hypertension diet", "DASH diet", "renal diet",
    "liver disease diet", "celiac disease", "IBS diet", "inflammatory bowel disease",
    "FODMAP diet", "pregnancy nutrition", "pediatric nutrition", "geriatric nutrition",
    "sports nutrition", "supplements", "probiotics", "antioxidants", "omega-3 fatty acids",
    "meal planning", "portion control", "emotional eating", "mindful eating",
    "intermittent fasting", "detoxification diets", "organic foods", "superfoods",
    "cholesterol management", "plant-based diets", "sustainable eating", "nutritional deficiencies"
]


def get_pubmed_ids_and_summaries(keywords):
    all_summaries = {}
    for keyword in keywords:
        print(f"starting {keyword}")
        pubmed_ids = search_pubmed(keyword)
        pubmed_summaries = {}
        for pid in pubmed_ids:
            abstract = fetch_abstract(pid)
            pubmed_summaries[pid] = abstract
        all_summaries[keyword] = pubmed_summaries
    return all_summaries

def save_to_file(data, keyword_practice, filename="pubmed_summaries.txt"):
    data_df = {}
    with open(filename, "w") as file:
        for keyword, summaries in data.items():
            for pubmed_id, abstract in summaries.items():
                # Write each abstract in a new line
                if abstract:
                    file.write(f"{abstract}\n")
                    data_df[pubmed_id] = abstract.lower()
    df = pd.DataFrame(data=data_df.items(), columns=['pubmed', 'abstract'])
    df.to_csv(f"df_{keyword_practice}_{filename}.csv")
    print(f"Data saved to {filename}")


"""
Add or increase keywords accordingly
data = get_pubmed_ids_and_summaries(dietary_keywords[:])
save_to_file(data, keyword_practice="diet_practice")
#save_to_file(get_pubmed_ids_and_summaries(cardiac_keywords))
#save_to_file(get_pubmed_ids_and_summaries(dietary_keywords))
"""