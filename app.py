import streamlit as st
from transformers import pipeline
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Ensure required NLTK resources are downloaded
import nltk
nltk.download('punkt_tab')
nltk.download('punkt', quiet=True)
print(nltk.data.path)
nltk.download('stopwords', quiet=True)

# Load chatbot model
@st.cache_resource
def load_chatbot_model():
    return pipeline('question-answering', model='deepset/bert-base-cased-squad2')

# Preprocess input text
def preprocess_input(user_input):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(user_input)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

# Healthcare chatbot logic
def healthcare_chatbot(user_input, chatbot_model):
    user_input = preprocess_input(user_input).lower()
    
    if 'sneeze' in user_input or 'sneezing' in user_input:
        return 'Frequent sneezing may indicate allergies or a cold. Consult a doctor if symptoms persist.'
    elif 'fever' in user_input:
        return 'A fever may indicate an infection. Stay hydrated and consult a doctor if it persists.'
    elif 'headache' in user_input:
        return 'Frequent headaches may be caused by stress or dehydration. Please rest and drink water. Consult a doctor if it continues.'
    elif 'stomach pain' in user_input or 'abdominal pain' in user_input:
        return 'Stomach pain can be caused by indigestion or other issues. If severe, consult a doctor immediately.'
    elif 'cold' in user_input:
        return 'Cold symptoms can be alleviated with rest and hydration. If symptoms persist, consult a doctor.'
    elif 'cough' in user_input:
        return 'Persistent coughing might indicate allergies or respiratory issues. Consult a doctor if it doesn’t improve.'
    elif 'throat pain' in user_input or 'sore throat' in user_input:
        return 'A sore throat could be a sign of a cold or infection. Gargle with warm salt water and stay hydrated.'
    elif 'back pain' in user_input:
        return 'Back pain can be caused by poor posture or strain. Rest and proper posture might help, but consult a doctor if it persists.'
    elif 'chest pain' in user_input:
        return 'Chest pain can be serious. Please consult a doctor immediately.'
    elif 'dizziness' in user_input:
        return 'Dizziness may indicate dehydration or low blood pressure. Rest and hydrate, and consult a doctor if it continues.'
    elif 'allergy' in user_input or 'allergic' in user_input:
        return 'Allergic reactions may require antihistamines. Consult a doctor if symptoms worsen.'
    elif 'skin rash' in user_input or 'rash' in user_input:
        return 'A skin rash could indicate an allergy or infection. Consult a dermatologist for advice.'
    elif 'weight loss' in user_input or 'unintentional weight loss' in user_input:
        return 'Unintentional weight loss should be evaluated by a doctor to rule out underlying conditions.'
    elif 'fatigue' in user_input or 'tiredness' in user_input:
        return 'Fatigue can result from lack of sleep, stress, or other factors. Ensure proper rest and consult a doctor if it persists.'
    elif 'diabetes' in user_input:
        return 'Diabetes management involves a healthy diet, exercise, and regular medication. Consult a doctor for personalized advice.'
    elif 'appointment' in user_input:
        return "Would you like me to schedule an appointment with a doctor?"
    elif 'medication' in user_input:
        return "It's important to take your medicines regularly. Consult a doctor for accurate advice."
    else:
        context = '''
        Common healthcare-related scenarios include symptoms of colds, flu, and allergies,
        along with medication guidance and appointment scheduling.
        '''
        response = chatbot_model(question=user_input, context=context)
        return response['answer']

# Streamlit app
def main():
    st.title("Healthcare Assistant Chatbot")

    chatbot_model = load_chatbot_model()

    user_input = st.text_input("How can I assist you today?", '')
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            response = healthcare_chatbot(user_input, chatbot_model)
            st.write("Healthcare Assistant: ", response)
        else:
            st.write("Please enter a query.")

if __name__ == '__main__':
    main()
