from uuid import uuid4

from langchain_core.documents import Document
from rag import my_vector_store

document_1 = Document(
    page_content="""Breast Cancer

Common Cognitive Symptoms:

Memory loss (forgetting names, appointments, or daily tasks)

Difficulty concentrating (trouble focusing on conversations or tasks)

Word-finding difficulties

Slower processing speed

Emotional Impact:

Frustration and embarrassment due to memory lapses

Anxiety about work and social interactions

Fear of long-term cognitive decline

Recommended Actions & Exercises:

Cognitive training: Word recall games, brain puzzles

Physical exercise: Yoga and aerobic workouts for mental clarity

Mindfulness techniques: Meditation to reduce stress and improve focus

Journaling: Writing down thoughts to aid memory retention.""",
    id=1,
)

document_2 = Document(
    page_content="""Lung Cancer

Common Cognitive Symptoms:

Mental fog (feeling disoriented or slow thinking)

Short-term memory issues

Fatigue-related cognitive decline

Difficulty multitasking

Emotional Impact:

Feeling disconnected from surroundings

Increased frustration due to difficulty processing information

Helplessness and depression

Recommended Actions & Exercises:

Breathing exercises: Helps increase oxygen flow to the brain

Brain-stimulating activities: Crossword puzzles, memory games

Social interaction: Engaging in group discussions to enhance cognitive engagement

Regular rest: Managing fatigue through a structured sleep schedule""",
    id=2,
)

document_3 = Document(
    page_content=""" Prostate Cancer

Common Cognitive Symptoms:

Lack of motivation and mental sluggishness

Attention difficulties

Mood instability linked to hormonal therapy

Decision-making difficulties

Emotional Impact:

Irritability due to hormonal changes

Anxiety about personal and professional life

Emotional withdrawal from loved ones

Recommended Actions & Exercises:

Strength training: Resistance exercises to stabilize hormone levels

Music therapy: Helps improve mood and cognitive alertness

Cognitive behavioral therapy (CBT): Managing mood swings effectively

Structured planning: Using digital reminders and planners to aid decision-making""",
    id=3,
)

document_4 = Document(
    page_content="""Leukemia & Lymphoma

Common Cognitive Symptoms:

Confusion and difficulty processing complex information

Frequent forgetfulness

Mental exhaustion

Reduced verbal fluency

Emotional Impact:

Overwhelm from information overload

Loss of confidence in communication skills

Emotional exhaustion leading to social isolation

Recommended Actions & Exercises:

Mind-mapping techniques: Visual charts for organizing thoughts

Nutritional support: Anti-inflammatory diet to reduce cognitive decline

Art therapy: Painting or creative writing to boost cognitive flexibility

Guided meditation: Improves concentration and stress reduction""",
    id=4,
)

document_5 = Document(
    page_content=""" Brain Cancer (Glioblastoma, Astrocytoma, etc.)

Common Cognitive Symptoms:

Severe memory loss

Difficulty recognizing familiar faces or places

Confusion and disorientation

Reduced executive function (problem-solving, planning)

Emotional Impact:

Fear of losing independence

Severe depression due to cognitive decline

Increased reliance on caregivers, leading to frustration

Recommended Actions & Exercises:

Repetitive learning techniques: Repeated exposure to information for better recall

Occupational therapy: Personalized cognitive rehabilitation

Adaptive technology: Use of voice assistants and memory aids

Gentle physical activity: Tai Chi or light stretching for brain-body coordination""",
    id=5,
)

documents = [
    document_1,
    document_2,
    document_3,
    document_4,
    document_5
]
# uuids = [str(uuid4()) for _ in range(len(documents))]
vcs=my_vector_store()
vcs.add_documents(documents=documents)

