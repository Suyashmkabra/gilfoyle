from uuid import uuid4

from langchain_core.documents import Document
from rag import my_vector_store

document_1 = Document(
    page_content="""Cognitive issues can be difficult to treat, but there are things you can do to help manage them.
Write it down.
Make to-do lists to keep yourself on task.
Use a planner to keep up with treatment times and doctor’s appointments.
Place sticky notes in places you might need an occasional reminder, such as one by the front door - keys, cellphone, wallet.
Use a timer on your phone for medications. 
Exercise your brain.
Play SODOKU or complete crossword puzzles.
Read a little every day, even if it’s just a magazine or newspaper.
Color - new coloring books for adults are a fun trend! These books contain beautiful and detailed images to give your brain and creativity a workout.  
Download apps on your phone or tablet like QuizUp or 1278.
Avoid alcohol.
Avoid other substances that alter cognition as well.
De-clutter.
Throw away or donate all the things in your house that you don’t need.
Use labels or color coded boxes for storage.
Convert paper files to electronic files.
Sleep well.
Make sure your bedding is comfortable for you.
Use the bathroom right before you go to bed.
Do not watch TV or browse the web at least an hour before bed.
Take a warm bath before bed to relax.
Talk to your healthcare team.
Anemia, shortness of red blood cells, can cause cognitive issues. Ask your healthcare team to check your red blood cell counts if they are not doing so already.""",id=1,
)

document_2 = Document(
    page_content="""Steps to Improve Your Concentration
Concentration is the ability to stay focused on your work without letting people, feelings, thoughts, or activities get in the way. Here are a few strategies for establishing or improving concentration:
Establish concentration
Be aware of external distractions. For example, give yourself permission to let your voicemail pick up calls when you’re in the middle of a task. That way, you’re not distracted by the call
Try to recognize internal distractions, such as thoughts, emotions, physical feelings, and hunger. These things can interrupt your ability to focus. Do something to reduce these internal distractions. For example, if you’re hungry, have a snack before starting a task.
Stop distracting thoughts that pop into your mind as soon as you’re aware of them. You can do this by acknowledging the thought, then consciously bringing your attention back to the task you’re working on.
Keep a notebook or pad of paper handy. If something you need to do pops into your head in the middle of a task, write it down to get it off your mind and schedule time later in the day to do it.
Increase concentration
Set aside time to concentrate. Imagine how you may feel or what you may accomplish after your task is done.
Use a pencil or highlighter when reading. Take notes or highlight important points.
Divide tasks into smaller, more manageable parts.
Plan breaks according to your concentration span. Take a walk or a lunch break to help clear your head.
If you find yourself losing focus, stand up. The physical act of standing brings your attention to the fact that you’re losing focus.
Vary your activities. Change is often as good as taking a break.
Develop your concentration habits. Like any other skill, you must learn, develop, and practice concentration.
Figure out how long your concentration span is. To do this, write down the time you start a task (such as reading). As soon as your mind starts to drift, write down the time again. The length between your start and end times is your concentration span.
Learn when your concentration level is at its best. Find a time during the day when you know you won’t be interrupted and your energy level matches the particular task. Try to plan your tasks accordingly.
Find out if there’s an environment that helps you concentrate better. Remove yourself from distractions for set periods of time to accomplish your work. Figure out what works for you, whether it’s an uncluttered desk, good lighting, or soothing music playing in the background.""",id=2,
)

document_3 = Document(
    page_content=""" Getting support from your family
As you're coping with chemo brain, you may find it helpful to talk with your family. "If you try to hide what you're experiencing from your loved ones, it can increase your stress and make you more tired. And that can lead to more memory challenges," Joette cautions. "By talking to your family, you can help adjust their expectations of you right now, and they can help to support your new coping strategies."
Joette adds, "Know that you are not alone and you don't have to manage these challenges on your own. Talk with your doctor and your family and ask for the help you need to manage your recovery. Above all, be kind to yourself and use the strategies and routines that work best for you."
To family and friends, Joette suggests, "Don't point out every mistake. Instead, help your loved one set realistic goals after transplant and take breaks."
Managing chemo brain challenges
Here are some tips to help you cope with chemo brain:
Use memory aids
Use calendars, sticky notes, checklists, alarms and alerts on your phone.
Use a calendar or daily planner to schedule your days.
Carry a small notebook or electronic organizer with you to jot down reminders.
Use a bulletin board or dry erase board to post large reminders.
Post small reminders where you need them—on the phone, in the kitchen, on the front door, etc.
Bring someone with you to appointments to help listen, ask questions and take notes.
Record reminders on cell phones and/or use a standalone notetaker (a visual aid device).
Simplify
List things you would like to get done and choose those that are most important to you.
Do your hardest tasks at the time of day you find it easiest to concentrate.
Write yourself simple, step-by-step directions for tasks that are difficult.
Try to focus on one thing at a time. Turn off things that might distract you like the TV or radio.
Ask for help making plans or decisions, even if it's just to review and confirm your plans.
Reduce stress
Stress can make it harder to think clearly. Find ways to relax. Exercise and relaxation techniques like yoga, meditation and guided imagery can help reduce stress.
Keep your normal routines and habits to lower stress on your memory.
Plan your days and weeks. Make sure your plan is realistic, and that you schedule breaks to rest.""",id=3,
)

document_4 = Document(
    page_content="""There are several supplements that may help with chemo brain fog. However, be sure to discuss these supplements with your treatment team to ensure they do not interact with your cancer treatment or decrease its efficacy.
Fish oil (omega-3 fatty acids)
Omega-3 fatty acids, particularly EPA and DHA found in fish oil, are crucial for brain health and cognitive function.

Acetyl-L-Carnitine (ALC)
ALC is an amino acid derivative that may have antioxidant properties and support brain energy metabolism. While studies on ALC for chemo brain are lacking, dementia research shows that ALC may slow cognitive decline.
Probiotics
Probiotics are live bacteria and yeasts beneficial for gut health. They may help alleviate brain fog by modulating gut microbes, influencing brain function through the gut-brain axis.
In a study of 159 breast cancer patients undergoing chemotherapy, probiotics reduced CRCI incidence and improved cognitive functions.
Curcumin
Curcumin is a compound found in turmeric that has strong antioxidant and anti-inflammatory properties.

Antioxidants
Antioxidants, such as vitamins E and C, may help protect the brain from oxidative stress. Research
Trusted Source
 shows that cisplatin, a chemotherapy drug, can cause toxicities in the body due to the production of free radicals, which lead to oxidative damage in organs.
Taking antioxidants, such as E and C, may help counteract the damaging effects of oxidative stress.""",id=4,
)

document_5 = Document(
    page_content=""" Strategies for Recovery: Intellectual Empowerment
The core of the book focuses on practical strategies designed to enhance cognitive function and emotional well-being post-chemotherapy. The author presents a variety of techniques and exercises aimed at improving mental clarity and coping with the challenges of chemo brain.
Mindfulness Practices
Mindfulness practices play a crucial role in managing anxiety and improving cognitive focus. The author introduces several mindfulness techniques, including:
Meditation: Simple meditation exercises can help individuals cultivate awareness and reduce stress. Guided meditations focused on breathing and relaxation techniques can be beneficial for managing anxiety.
Mindful Walking: Engaging in mindful walking encourages individuals to focus on their surroundings and physical sensations, fostering a sense of calm and clarity.
Journaling: Keeping a mindfulness journal allows individuals to reflect on their feelings and experiences, providing an outlet for emotional expression and a tool for fostering self-awareness.""",id=5,
)

document_6 = Document(
    page_content=""" Cognitive Enhancements and Brain Training
To combat cognitive impairments, the book offers a plethora of cognitive exercises designed to stimulate brain activity. Some key exercises include:
Memory Games: Engaging in memory-enhancing games, such as card matching or word games, can aid in improving cognitive flexibility and memory.
Puzzles: Completing puzzles like crosswords and Sudoku challenges the brain, supporting mental agility and problem-solving skills.
Learning New Skills: Learning a new language or picking up an instrument fosters neural growth and helps create new cognitive pathways, enhancing overall brain function.
Nutrition and Brain Health""",id=6,
)

document_7 = Document(
    page_content=""" 
 nutrition and cognitive function. The author outlines specific dietary recommendations to support brain health:
Healthy Foods: Incorporating foods rich in antioxidants, omega-3 fatty acids, and vitamins is recommended. Examples of beneficial foods include fatty fish, berries, nuts, leafy greens, and whole grains.
Hydration: Proper hydration is essential, as even mild dehydration can lead to cognitive impairments. The author advises survivors to drink plenty of water and limit caffeine and alcohol intake.""",id=7,
)

document_8 = Document(
    page_content=""" physical activity as a means to promote cognitive recovery. Regular exercise can improve blood flow to the brain, enhance mood, and boost memory function. The author recommends:
Aerobic Exercise: Activities like walking, running, swimming, and dancing not only improve cardiovascular health but also stimulate cognitive function.
Strength Training: Resistance training enhances overall physical capacity, which can positively influence cognitive performance.
Yoga and Tai Chi: Incorporating mind-body exercises such as yoga and Tai Chi can aid in calming the mind, reducing anxiety, and promoting mental clarity.""",id=8,
)

document_9 = Document(
    page_content=""" Quality sleep is vital for cognitive health. The author discusses the importance of establishing good sleep hygiene practices:
Regular Sleep Schedule: Creating a consistent sleep routine can help regulate circadian rhythms, leading to better sleep quality.
Creating a Comfortable Sleep Environment: The importance of a calm sleeping environment is emphasized—cool temperatures, darkness, and minimal noise can greatly improve sleep quality.
Relaxation Techniques: Incorporating relaxation techniques, such as progressive muscle relaxation or deep breathing exercises, can help individuals wind down before bed.""",id=9,
)

document_10 = Document(
    page_content="""  organizational challenges that complicate daily tasks. The book provides advice on enhancing organizational skills:
To-Do Lists: Keeping lists can help individuals remember important tasks and reduce cognitive overload. Breaking down tasks into smaller, more manageable steps can alleviate feelings of being overwhelmed.
Calendar Use: Utilizing calendars or planner apps to track appointments and important dates can promote accountability.
Simplifying Tasks: The author encourages survivors to simplify their daily routines, creating checklists for regular tasks to foster a sense of control.

Tracking Progress and Celebrating Wins
The author stresses the importance of monitoring progress in cognitive recovery:
Self-Assessments: Keeping a journal or using apps to track cognitive symptoms and emotional states can help individuals spot areas of improvement over time.
Celebrating Small Achievements: Acknowledging small victories, whether it’s completing a task or recalling difficult information, fosters motivation and boosts confidence.
Cultivating Resilience and Maintaining Hope
Cultivating resilience is a central message of the book. The author presents several strategies for maintaining hope and a positive outlook during the recovery process:
Positive Affirmations: Utilizing daily affirmations can help individuals counter negative self-talk and cultivate a growth-oriented mindset.
Visualization Techniques: Guided imagery exercises can help survivors envision their cognitive recovery, reinforcing a sense of agency in overcoming challenges.
Focus on Growth: The idea of viewing challenges as opportunities for growth, rather than insurmountable obstacles, helps shift perspectives and foster resilience""",id=10,
)

# doc=Document(
#     page_content="""
#     """
# )

documents = [

    document_1,
    document_2,
    document_3,
    document_4,
    document_5,
    document_6,
    document_7,
    document_8,
    document_9,
    document_10,
]
# uuids = [str(uuid4()) for _ in range(len(documents))]
vcs=my_vector_store()
vcs.add_documents(documents=documents)
print("done")

