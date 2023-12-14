Introduction
=================
1. The motivation behind this project is to address two significant issues in healthcare: 
2.The high cost of doctor consultations 
3. Difficulty in finding timely appointments and inability for consumers to understand their medical reports.

Focused Area: Large Language Models in Medicine	
Fine Tuning/LLM Development/RAG,In Context Learning: Aadit Kapoor
Frontend/Fine Tuning/Data Preprocessing: Pavan Satyam
Video Demo: https://youtu.be/yQ1jTBbn85U

https://umeddemo.streamlit.app/

Source Code
====================
Retrieval Engine: retrieve.py and neighbors.py
Knowledge Index Creation: embed.py
Fine Tuning using LoRA: fine_tune.py
Streamlit application: app.py

If using openai.api_key = os.environ["OPENAI_API_KEY"]
otherwise add OPENAI_API_KEY to:
retrieve.py
neighbors.py
app.py
embed.py


References
=================================================================
[1] C. Li et al., “LLaVA-Med: Training a Large Language-and-Vision
Assistant for Biomedicine in One Day,” arXiv.org, Jun. 01, 2023.
https://arxiv.org/abs/2306.00890 (accessed Jul. 12, 2023)
[2] Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P. C., Mark, R., ... &
Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new
research
[3]  Moody, G. B. & Mark, R. G. A database to support development and
evaluation of intelligent intensive care monitoring. In Computers in Cardiology
1996, 657–660 (IEEE, 1996)
[4] Adams, Robert John. "Improving health outcomes with better patient
understanding and education." Risk management and healthcare policy
(2010): 61-72
[5] https://github.com/streamlit/streamlit
[6] https://qdrant.tech/
[7] https://together.ai/
[8] https://mistral.ai/news/announcing-mistral-7b/
[9]https://huggingface.co/datasets/Mohammed-Altaf/medical-instruction-120k/viewer/default/train
[10]https://learn.microsoft.com/en-us/azure/ai-services/openai/tutorials/embeddings?tabs=python-new%2Ccommand-line&pivots=programming-language-python
[11] https://huggingface.co/docs/transformers/training
[12] https://huggingface.co/docs/transformers/peft
[13] https://www.databricks.com/blog/efficient-fine-tuning-lora-guide-llms
[14] https://huggingface.co/datasets/Mohammed-Altaf/medical-instruction-120k
[15] https://github.com/amazon-science/auto-cot
[16] https://qdrant.tech/
[17] https://cookbook.openai.com/
[18]https://docs.streamlit.io/library/api-reference/chat


