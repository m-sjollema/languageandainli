# Introduction
This is the github page for a project in the course Language and Artificial Intelligence from the Research Master Linguistics at Utrecht University. 
The project analysed whether an LLM is able to reproduce human judgements of inferences. The authors are Naomi Oppeneer and Maike Sjollema.
#

# Contents
This github page contains two RStudio markdown files ("entropy_sentence_selection" and "ModelAnalyses"). The former was used for the sentence selection and the latter for the statistical analyses. The sentence selection was done using the SNLI corpus data ("chaosNLI_snli.jsonl"), which was donwlaoded from the [ChaosNLI Github page](https://github.com/easonnie/ChaosNLI). The Python code is in "NLI_LLM.py". To be able to run this code, [Ollama](https://ollama.com/) is needed. Additionally, it was run in an environment with Python version 3.13.0. The Pyhton code retrieves csv files stored in the input folder (e.g., "persona_prompt.csv" and "Input_SSS_1.csv") and places the output in the output folder. The output folder contains csv files with all the data (i.e., every single output of every single row of the input csv file) in the "Full_Output_Data" folder, and it also contains summarised versions (i.e., adding the output per persona row) of these data in the "Summary_Output_Data" folder. The summary output was combined to create the "Output_Full.csv" file, which was used for the data analyses. 

**NB: The file called "chaosNLI_snli.jsonl" was directly copied from the ChaosNLI database (Yixin et al., 2020) see full reference below**

## Citation of ChaosNLI database
#
	@inproceedings{ynie2020chaosnli,
	Author = {Yixin Nie and Xiang Zhou and Mohit Bansal},
	Booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
	Publisher = {Association for Computational Linguistics},
	Title = {What Can We Learn from Collective Human Opinions on Natural Language Inference Data?},
	Year = {2020}
	}
