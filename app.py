import streamlit as st
import utils
import plotly.graph_objects as go

def main():
    ########### Sidebar ##############################
    st.sidebar.markdown("# Fitness app 🏋️")
    st.sidebar.markdown("This application is developped using streamlit 💻")
    st.sidebar.markdown("Please enter the following information:\n")
    weight = st.sidebar.slider("Choose your weight (kg): ", min_value=0,   
                       max_value=200, value=73, step=1)
    height = st.sidebar.slider("Choose your height (cm): ", min_value=0,   
                       max_value=200, value=178, step=1)
    age = st.sidebar.slider("Choose your age : ", min_value=0,   
    max_value=100, value=24, step=1)
    gender=st.sidebar.radio("Choose your gender:",("Man", "Woman"))
    activity=st.sidebar.radio("How active are you?",("Sedentary", "Moderately active", "Very active"))
    target=st.sidebar.radio("What are your goals?",("Fat loss and muscle development", "Muscle development"))


    ########### Core ##############################
    ### IMC
    st.markdown("# 💊 Health indicators")
    st.markdown("## BMI")
    
    imc=int(weight/(height/100)**2)
    st.markdown("Your BMI is the following:")
    fig=utils.imc_chart(imc)
    st.write(fig)

    ### Calories
    st.markdown("## Calories")
    
    if gender=="Man":
        bmr=int(10*weight+6.25*height-5*age+5)
    elif gender=="Woman":
        bmr=int(10*weight+6.25*height-5*age-161)
    
    if activity=="Sedentary":
        ded=int(bmr*1.4)
    elif activity=="Moderately active":
        ded=int(bmr*1.6)
    elif activity=="Very active":
        ded=int(bmr*1.8)
    
    if target=="Fat loss and muscle development":
        tded=ded-500
    elif target=="Muscle development":
        tded=ded+500

    fig=utils.calories_chart(bmr, ded, tded)
    st.write(fig)

    ### Nutrition
    st.markdown("# 🍖 Nutrition indicators")
    st.markdown("This section is based on all the information given above")

    prot_needs_g=int(1.6*weight)
    prot_needs_kcal=int(4*prot_needs_g)

    fat_needs_g=int(tded*0.35/9)
    fat_needs_kcal=9*fat_needs_g

    carbs_needs_kcal=tded-prot_needs_kcal-fat_needs_kcal
    carbs_needs_g=int((tded-prot_needs_kcal-fat_needs_kcal)/4)
  
    choice_nut=st.radio("", ("Gramme", "Calorie"))
    fig=utils.nutri_chart(choice_nut, prot_needs_g,fat_needs_g,carbs_needs_g, prot_needs_kcal,fat_needs_kcal, carbs_needs_kcal)
    st.write(fig)

# @st.cache
# def

if __name__ == "__main__":
    main()




