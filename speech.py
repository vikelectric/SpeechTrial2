import streamlit as st

st.title("Speech to Text Transcription")

st.markdown("""
    <button id="start_button">Speak</button>
    <input type="text" id="speech_to_text" readonly style="width: 100%; margin-top: 10px;">
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        console.log('DOM content loaded');
        var startButton = document.getElementById('start_button');
        if (startButton) {
            console.log('Button found');
            startButton.addEventListener('click', function() {
                console.log('Button clicked. Starting recognition...');
                var recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
                recognition.lang = 'en-US';
                recognition.interimResults = false;
                recognition.maxAlternatives = 1;

                recognition.start();
                console.log('Recognition started.');

                recognition.onresult = function(event) {
                    var speechResult = event.results[0][0].transcript;
                    console.log('Recognition result: ', speechResult);
                    document.getElementById('speech_to_text').value = speechResult;
                    recognition.stop();
                };

                recognition.onerror = function(event) {
                    console.error('Recognition error: ', event.error);
                    recognition.stop();
                };

                recognition.onend = function() {
                    console.log('Recognition ended.');
                };
            });
        } else {
            console.error('Button not found.');
        }
    });
    </script>
""", unsafe_allow_html=True)
