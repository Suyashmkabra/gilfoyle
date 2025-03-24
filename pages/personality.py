import streamlit as st

# http://www.lrjj.cn/encrm1.0/public/upload/MBTI-personality-test.pdf

class Question:
    def __init__(self,ques,options):
        self.ques= ques
        self.options= options


def generate_questions(quesdata,startIndex,endIndex):
    selected_option=[]
    for i in range(startIndex, endIndex):
        if i >= len(quesdata):
            break
        question = quesdata[i]
        option_index = st.radio(f"Q {i+1}: ***{question.ques}***", range(len(question.options)), format_func=lambda x: f":rainbow[{question.options[x]}]",index=None)
        selected_option.append(option_index)
    return selected_option

def compute_scores(options):
    E, I, N, S, T, F, J, P=0,0,0,0,0,0,0,0
    for i in range(len(options)):
        option_index=options[i]
        print(option_index)
        if i % 7 == 0:
            if option_index == 0:
                E += 1
            elif(option_index==1):
                I += 1
        elif i % 7 in [1, 2]:
            if option_index == 0:
                S += 1
            elif(option_index==1):
                N += 1
        elif i % 7 in [3, 4]:
            if option_index == 0:
                T += 1
            elif(option_index==1):
                F += 1
        elif i % 7 in [5, 6]:
            if option_index == 0:
                J += 1
            elif(option_index==1):
                P += 1
    return E, I, S, N, T, F, J, P

questionData = [
    Question(ques='At a party do you:', options=['a. Interact with many, including strangers', 'b. Interact with a few, known to you ']),
    Question(ques='Are you more:', options=['a. Realistic than speculative', 'b. Speculative than realistic ']),
    Question(ques='Is it worse to:', options=['a. Have your “head in the clouds”', 'b. Be “in a rut” ']),
    Question(ques='Are you more impressed by:', options=['a. Principles', 'b. Emotions ']),
    Question(ques='Are more drawn toward the:', options=['a. Convincing', 'b. Touching ']),
    Question(ques='Do you prefer to work: ', options=['a. To deadlines', 'b. Just “whenever”']),
    Question(ques='Do you tend to choose', options=['a. Rather carefully', 'b. Somewhat impulsively']),

    Question(ques='At parties do you:', options=['a. Stay late, with increasing energy', 'b. Leave early with decreased energy']),
    Question(ques='Are you more attracted to: ', options=['a. Sensible people', 'b. Imaginative people']),
    Question(ques='Are you more interested in: ', options=['a. What is actual ', 'b. What is possible ']),
    Question(ques='In judging others are you more swayed by:', options=['a. Laws than circumstances ', 'b. Circumstances than laws ']),
    Question(ques='In approaching others is your inclination to be somewhat: ', options=['a. Objective ', 'b. Personal']),
    Question(ques='Are you more:', options=['a. Punctual ', 'b. Leisurely']),
    Question(ques='Does it bother you more having things:', options=['a. Incomplete ', 'b. Completed ']),
 
    Question(ques='In your social groups do you:', options=['a. Keep abreast of other’s happenings ', 'b. Get behind on the news ']),
    Question(ques='In doing ordinary things are you more likely to:', options=['a. Do it the usual way', 'b. Do it your own way']),
    Question(ques='Writers should:', options=['a. “Say what they mean and mean what they say”', 'b. Express things more by use of analogy']),
    Question(ques='Which appeals to you more:', options=['a. Consistency of thought', 'b. Harmonious human relationships']),
    Question(ques='Are you more comfortable in making:', options=['a. Logical judgments ', 'b. Value judgments ']),
    Question(ques='Do you want things: ', options=['a. Settled and decided', 'b. Unsettled and undecided ']),
    Question(ques='Would you say you are more:', options=['a. Serious and determined ', 'b. Easy-going']),
    
    # Question(ques='jshc', options=['csahc', 'mijsdcb']),
    # Question(ques='jshc', options=['csahc', 'mijsdcb']),
    # Question(ques='jshc', options=['csahc', 'mijsdcb']),
    # Question(ques='jshc', options=['csahc', 'mijsdcb']),
    # Question(ques='jshc', options=['csahc', 'mijsdcb']),
    # Question(ques='jshc', options=['csahc', 'mijsdcb']),
    # Question(ques='jshc', options=['csahc', 'mijsdcb']),
]

def main():
    optionSelected = st.session_state.get('optionSelected', [])
    num_ques= len(questionData)
    num_pages= num_ques/7 

    if 'page_index' not in st.session_state:
            st.session_state.page_index = 0
    start_idx = st.session_state.page_index * 7
    end_idx = min((st.session_state.page_index + 1) * 7, 70)

    st.title("Personality Quiz")

    # Generate questions for the current page
    selected_options = generate_questions(quesdata=questionData, startIndex=start_idx, endIndex=end_idx)
    st.session_state.optionSelected = optionSelected

    form = st.form(key='navigation_form')
    col1, col2, col3 = form.columns([1, 8, 1])  
    with col2:
        if st.session_state.page_index > 0:
            if form.form_submit_button("Previous"):
                optionSelected.extend(selected_options)
                print("option selected:"+optionSelected)
                st.session_state.page_index -= 1 

        if st.session_state.page_index < num_pages - 1:
            if form.form_submit_button("Next"):
                optionSelected.extend(selected_options)
                print(f"option selected: {optionSelected}")
                st.session_state.page_index += 1

    if st.button("Submit"):
            optionSelected.extend(selected_options)
            # print(optionSelected)
            st.write("Your personality score is")
            E, I, N, S, T, F, J, P=0,0,0,0,0,0,0,0;
            # print(E, I, N, S, T, F, J, P)
            # print(selected_options)
            E, I, S, N, T, F, J, P= compute_scores(st.session_state.optionSelected )

            E_pcent=(E*100)/(E+I).__round__(2)
            I_pcent=(I*100)/(E+I).__round__(2)
            S_pcent=(S*100)/(S+N).__round__(2)
            N_pcent=(N*100)/(S+N).__round__(2)
            T_pcent=(T*100)/(T+F).__round__(2)
            F_pcent=(F*100)/(T+F).__round__(2)
            J_pcent=(J*100)/(J+P).__round__(2)
            P_pcent=(P*100)/(J+P).__round__(2)

            st.write(f"E : {E_pcent}")
            st.write(f"I : {I_pcent}")
            st.write(f"S : {S_pcent}")
            st.write(f"N : {N_pcent}")
            st.write(f"T : {T_pcent}")
            st.write(f"F : {F_pcent}")
            st.write(f"J : {J_pcent}")
            st.write(f"P : {P_pcent}")

            # st.write(f"E : {E}")
            # st.write(f"I : {I}")
            # st.write(f"S : {S}")
            # st.write(f"N : {N}")
            # st.write(f"T : {T}")
            # st.write(f"F : {F}")
            # st.write(f"J : {J}")
            # st.write(f"P : {P}")
            

if __name__ == '__main__':
    main()
# col1, col2, col3 =st.columns(3)
# with col1:
#     if st.session_state.page_index > 0:
#         if st.button("Previous"):
#             st.session_state['page_index'] -= 1
#             st.session_state.sync()   

# with col2:
#     if st.button("Submit"):
#         st.write("Your personality score is")
#         E, I, S, N, T, F, J, P= compute_scores(selected_options)
#         st.write(f"E : {E}")
#         st.write(f"I : {I}")
#         st.write(f"S : {S}")
#         st.write(f"N : {N}")
#         st.write(f"T : {T}")
#         st.write(f"F : {F}")
#         st.write(f"J : {J}")
#         st.write(f"P : {P}")

# with col3:
#     if st.session_state.page_index < num_pages - 1:
#         if st.button("Next"):
#             st.session_state['page_index'] += 1
#             st.session_state.sync()
            

