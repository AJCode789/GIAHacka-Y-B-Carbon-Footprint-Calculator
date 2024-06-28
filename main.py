
import google.generativeai as genai
import os
#import matplotlib
genai.configure(api_key = "removed(ENTER API KEY)")#ENTER API KEY
#genai.configure(api_key=os.environ["removed"])
"""
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content(["What is a good carbon footprint and how to calculate it from various factors?"])
print(response.text)
"""

location = input('Enter your Country and City. (Eg: Spain, Madrid)')
count = 0
answer =[]
questions = [
    "How many people live in your household?",
    "Do you own or rent your home?",
    "What type of heating do you use at home (e.g., gas, electric, oil)?",
    "What is the fuel efficiency of your vehicle (miles per gallon or km per liter)?",
    "How often do you use public transportation (e.g., bus, train)?",
    "How often do you fly for leisure or business purposes each year?",
    "How many solar panels do you have at home?",
    "How often do you recycle materials like paper, plastic, glass, and metal? (very frequently, somewhat frequenctly, not at all)",
    "Do you compost organic waste (e.g., food scraps, yard trimmings)?",
    "How often do you eat meat (including beef, pork, and poultry)?",
    "How often do you eat dairy products (e.g., milk, cheese, yogurt)?",
    "How often do you buy locally produced food and products?",
    "How often do you buy organic food and products?",
    "How often do you purchase new clothes and goods?",
    "How often do you use energy-efficient appliances and electronics?",
    "How often do you use air conditioning or heating in your home?",
    "How often do you turn off lights and electronics when not in use?",
    "How often do you use single-use plastics (e.g., bags, bottles)?",
    "How often do you participate in community clean-up or environmental initiatives?",
    "How often do you support environmentally conscious businesses or brands?",
    "How many miles do you drive per week?",
    "How often do you plant trees or participate in tree-planting initiatives?",
    "How often do you use energy-efficient modes of transportation (e.g., biking, walking)?",
    "How often do you volunteer or donate to environmental causes?",
    "How often do you educate others about environmental issues and sustainability practices?"
]


for i in questions:
    count += 1 
    print(i)
    userans = input('Enter answer: ')
    AnsF = (str(count) + '. ' +  userans)
    answer.append(AnsF)
    
    


prompt1 = f"Hello Gemini, you are now CarbonAI. You have over 10 years of experience in calculating carbon footprints. Your goal is to assist me in \
    calculating a users carbon footprint based on data i will send at the end of this prompt. After that, you must calculate the users carbon \
        footprint using a basic points system, as in an answer that is carbon friednly will generate from a score from 5-20, and a non-carbon friendly answer will \
            score from -5 to -20 points. After all 5 questions you must total up the users score and output it, you must also tell the user if their \
                score is good or not, compared to what an average score must be(-70 to +70). Your only output must the the final score(formatted as a table (question,answer,score as the collumns)), and how the score compares to average. You must think step by step. After all that, at the end, you have to give an estimate to the actual carbon footprint value of the user using factors and research online in kilograms(kg) of carbon footprint. \
                The data to use: \
                    Questions (1-25): \
                    1. How many people live in your household?  Answer: {answer[0]} \
                    2. Do you own or rent your home? Answer: {answer[1]} \
                    3. What type of heating do you use at home (e.g., gas, electric, oil)? Answer: {answer[2]} \
                    4. What is the fuel efficiency of your vehicle (miles per gallon or km per liter)? Answer: {answer[3]} \
                    5. How often do you use public transportation (e.g., bus, train)? Answer: {answer[4]} \
                    6. How often do you fly for leisure or business purposes each year? Answer: {answer[5]} \
                    7. How many solar panels do you have at home? Answer: {answer[6]} \
                    8. How often do you recycle materials like paper, plastic, glass, and metal? (very frequently, somewhat frequenctly, not at all)? Answer: {answer[7]} \
                    9. Do you compost organic waste (e.g., food scraps, yard trimmings)? Answer: {answer[8]} \
                    10. How often do you eat meat (including beef, pork, and poultry)? Answer: {answer[9]} \
                    11. How often do you eat dairy products (e.g., milk, cheese, yogurt)? Answer: {answer[10]} \
                    12. How often do you buy locally produced food and products? Answer: {answer[11]} \
                    13. How often do you buy organic food and products? Answer: {answer[12]} \
                    14. How often do you purchase new clothes and goods? Answer: {answer[13]} \
                    15. How often do you use energy-efficient appliances and electronics? Answer: {answer[14]} \
                    16. How often do you use air conditioning or heating in your home? Answer: {answer[15]} \
                    17. How often do you turn off lights and electronics when not in use? Answer: {answer[16]} \
                    18. How often do you use single-use plastics (e.g., bags, bottles)? Answer: {answer[17]} \
                    19. How often do you participate in community clean-up or environmental initiatives? Answer: {answer[18]} \
                    20. How many miles do you drive per week? Answer: {answer[19]} \
                    21. How often do you support environmentally conscious businesses or brands? Answer: {answer[20]} \
                    22. How often do you plant trees or participate in tree-planting initiatives? Answer: {answer[21]} \
                    23. How often do you use energy-efficient modes of transportation (e.g., biking, walking)? Answer: {answer[22]} \
                    24. How often do you volunteer or donate to environmental causes? Answer: {answer[23]} \
                    25. How often do you educate others about environmental issues and sustainability practices? Answer: {answer[24]}  "
                                       
                    
prompt2 = f"Hello Gemini, you are now CarbonAI. You have over 10 years of experience in calculating carbon footprints. Your goal is to assist me in \
    helping a user with their carbon footprint. You must keep note of the answers the user \
                has scored poor on(non-carbon friendly answer). You must generate 8 total follow up questions to all the answers answered poorly(high carbon footprint) to find out more. The follow-up questions you generate must \
                be simple to answer. Your only output must the the 8 follow up questions and nothing else. The only output must be the questions. The questions have to be orginal, and cannot be the same or similar to the following questions in \
                    the data provided. You must think step by step, \
                    This is the questions and answers to use: \
                        The data to use: \
                    Questions (1-25): \
                    1. How many people live in your household?  Answer: {answer[0]} \
                    2. Do you own or rent your home? Answer: {answer[1]} \
                    3. What type of heating do you use at home (e.g., gas, electric, oil)? Answer: {answer[2]} \
                    4. What is the fuel efficiency of your vehicle (miles per gallon or km per liter)? Answer: {answer[3]} \
                    5. How often do you use public transportation (e.g., bus, train)? Answer: {answer[4]} \
                    6. How often do you fly for leisure or business purposes each year? Answer: {answer[5]} \
                    7. How many solar panels do you have at home? Answer: {answer[6]} \
                    8. How often do you recycle materials like paper, plastic, glass, and metal? (very frequently, somewhat frequenctly, not at all)? Answer: {answer[7]} \
                    9. Do you compost organic waste (e.g., food scraps, yard trimmings)? Answer: {answer[8]} \
                    10. How often do you eat meat (including beef, pork, and poultry)? Answer: {answer[9]} \
                    11. How often do you eat dairy products (e.g., milk, cheese, yogurt)? Answer: {answer[10]} \
                    12. How often do you buy locally produced food and products? Answer: {answer[11]} \
                    13. How often do you buy organic food and products? Answer: {answer[12]} \
                    14. How often do you purchase new clothes and goods? Answer: {answer[13]} \
                    15. How often do you use energy-efficient appliances and electronics? Answer: {answer[14]} \
                    16. How often do you use air conditioning or heating in your home? Answer: {answer[15]} \
                    17. How often do you turn off lights and electronics when not in use? Answer: {answer[16]} \
                    18. How often do you use single-use plastics (e.g., bags, bottles)? Answer: {answer[17]} \
                    19. How often do you participate in community clean-up or environmental initiatives? Answer: {answer[18]} \
                    20. How many miles do you drive per week? Answer: {answer[19]} \
                    21. How often do you support environmentally conscious businesses or brands? Answer: {answer[20]} \
                    22. How often do you plant trees or participate in tree-planting initiatives? Answer: {answer[21]} \
                    23. How often do you use energy-efficient modes of transportation (e.g., biking, walking)? Answer: {answer[22]} \
                    24. How often do you volunteer or donate to environmental causes? Answer: {answer[23]} \
                    25. How often do you educate others about environmental issues and sustainability practices? Answer: {answer[24]}  "




model = genai.GenerativeModel(model_name="gemini-1.5-flash")
CarbonAnswer = model.generate_content([prompt1])
print(CarbonAnswer.text)


model = genai.GenerativeModel(model_name = 'gemini-1.5-flash')
FollowUp = model.generate_content([prompt2])
print(FollowUp.text)

count2 = 0
ans2 = []
for i in range(8):
    count2 += 1
    UserAns2 = input('Enter the answer to question'+ str(count2)+ ': ' )
    UserAns2 = str(count2), ' ', UserAns2
    ans2.append(UserAns2)
    

ans2str = ' '.join(map(str, ans2))

prompt3 = f"Hello Gemini, you are now CarbonAI. You have over 10 years of experience in calculating carbon footprints. Your goal is to assist me in \
    helping a user with their carbon footprint. Your goal is to give the user a detailed 800 word analysis on how the user can improve their carbon footprint,\
        based on their geographical location() and answers. At the end of the analysis, you must give a 8 bullet point summary on the most important, basic steps, that the user \
            can quickly implementin their livesto reduce their carbon footprint. \
                This is the questions and answers to use: \
                    Questions (1-25): \
                    1. How many people live in your household?  Answer: {answer[0]} \
                    2. Do you own or rent your home? Answer: {answer[1]} \
                    3. What type of heating do you use at home (e.g., gas, electric, oil)? Answer: {answer[2]} \
                    4. What is the fuel efficiency of your vehicle (miles per gallon or km per liter)? Answer: {answer[3]} \
                    5. How often do you use public transportation (e.g., bus, train)? Answer: {answer[4]} \
                    6. How often do you fly for leisure or business purposes each year? Answer: {answer[5]} \
                    7. How many solar panels do you have at home? Answer: {answer[6]} \
                    8. How often do you recycle materials like paper, plastic, glass, and metal? (very frequently, somewhat frequenctly, not at all)? Answer: {answer[7]} \
                    9. Do you compost organic waste (e.g., food scraps, yard trimmings)? Answer: {answer[8]} \
                    10. How often do you eat meat (including beef, pork, and poultry)? Answer: {answer[9]} \
                    11. How often do you eat dairy products (e.g., milk, cheese, yogurt)? Answer: {answer[10]} \
                    12. How often do you buy locally produced food and products? Answer: {answer[11]} \
                    13. How often do you buy organic food and products? Answer: {answer[12]} \
                    14. How often do you purchase new clothes and goods? Answer: {answer[13]} \
                    15. How often do you use energy-efficient appliances and electronics? Answer: {answer[14]} \
                    16. How often do you use air conditioning or heating in your home? Answer: {answer[15]} \
                    17. How often do you turn off lights and electronics when not in use? Answer: {answer[16]} \
                    18. How often do you use single-use plastics (e.g., bags, bottles)? Answer: {answer[17]} \
                    19. How often do you participate in community clean-up or environmental initiatives? Answer: {answer[18]} \
                    20. How many miles do you drive per week? Answer: {answer[19]} \
                    21. How often do you support environmentally conscious businesses or brands? Answer: {answer[20]} \
                    22. How often do you plant trees or participate in tree-planting initiatives? Answer: {answer[21]} \
                    23. How often do you use energy-efficient modes of transportation (e.g., biking, walking)? Answer: {answer[22]} \
                    24. How often do you volunteer or donate to environmental causes? Answer: {answer[23]} \
                    25. How often do you educate others about environmental issues and sustainability practices? Answer: {answer[24]} \
                        and {FollowUp.text} with answers: {ans2str}"

#model = genai.GenerativeModel(model_name = 'gemini-1.5-flash')
SmHelp = model.generate_content([prompt3])
print(SmHelp.text)
